"""Python code execution harness with sandboxing."""

import subprocess
import json
import tempfile
import sys
from pathlib import Path
from typing import Dict, Any, List
from dataclasses import dataclass


@dataclass
class TestResult:
    """Result of running tests."""
    passed: int
    failed: int
    total: int
    failures: List[Dict[str, Any]]
    error: str = ""

    @property
    def all_passing(self) -> bool:
        return self.failed == 0 and self.passed > 0


class PythonHarness:
    """Execute Python code with resource limits."""

    def __init__(self, timeout_ms: int = 4000, memory_mb: int = 512):
        self.timeout_ms = timeout_ms
        self.memory_mb = memory_mb

    def run_tests(self, solution_path: Path, test_cases: List[Dict[str, Any]]) -> TestResult:
        """Execute solution against test cases in isolated subprocess."""

        with tempfile.TemporaryDirectory() as tmpdir:
            # Create test runner script
            runner_script = self._create_runner_script(solution_path, test_cases)
            runner_path = Path(tmpdir) / "runner.py"
            runner_path.write_text(runner_script)

            # Execute with restrictions
            result = self._execute_sandboxed(runner_path)

        return self._parse_result(result)

    def _create_runner_script(self, solution_path: Path, test_cases: List[Dict[str, Any]]) -> str:
        """Generate test runner script."""
        test_cases_json = json.dumps(test_cases)

        return f'''
import sys
import json
import traceback
import signal
import resource

# Set resource limits
try:
    resource.setrlimit(resource.RLIMIT_AS, ({self.memory_mb} * 1024 * 1024, -1))
    resource.setrlimit(resource.RLIMIT_CPU, (10, 10))
except Exception:
    pass  # Skip on systems that don't support resource limits

# Timeout handler
def timeout_handler(signum, frame):
    print(json.dumps({{"error": "Timeout exceeded", "passed": 0, "failed": -1}}))
    sys.exit(1)

signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm({self.timeout_ms // 1000 + 1})

# Load solution
sys.path.insert(0, "{solution_path.parent}")
try:
    exec(open("{solution_path}").read(), globals())
except Exception as e:
    print(json.dumps({{"error": f"Failed to load solution: {{e}}", "passed": 0, "failed": -1}}))
    sys.exit(1)

# Load tests
test_cases = {test_cases_json}

results = {{"passed": 0, "failed": 0, "failures": []}}

for test in test_cases:
    try:
        func = globals()[test["function"]]
        result = func(**test["input"])

        if result == test["expected"]:
            results["passed"] += 1
        else:
            results["failed"] += 1
            results["failures"].append({{
                "name": test["name"],
                "input": test["input"],
                "expected": test["expected"],
                "got": result
            }})
    except Exception as e:
        results["failed"] += 1
        results["failures"].append({{
            "name": test["name"],
            "error": str(e),
            "traceback": traceback.format_exc()
        }})

print(json.dumps(results))
'''

    def _execute_sandboxed(self, runner_path: Path) -> Dict:
        """Run with subprocess isolation."""
        try:
            result = subprocess.run(
                [sys.executable, "-u", str(runner_path)],
                capture_output=True,
                text=True,
                timeout=self.timeout_ms / 1000 + 2,
                cwd=tempfile.gettempdir(),
                env={
                    "PATH": "/usr/bin:/bin",
                    "PYTHONPATH": "",
                    "HOME": tempfile.gettempdir(),
                },
            )

            if result.stdout:
                return json.loads(result.stdout.strip().split('\n')[-1])
            else:
                return {"error": result.stderr or "No output", "passed": 0, "failed": -1}

        except subprocess.TimeoutExpired:
            return {"error": "Timeout", "passed": 0, "failed": -1}
        except json.JSONDecodeError as e:
            return {"error": f"JSON decode error: {e}", "passed": 0, "failed": -1}
        except Exception as e:
            return {"error": str(e), "passed": 0, "failed": -1}

    def _parse_result(self, result: Dict) -> TestResult:
        """Parse execution result into TestResult."""
        if "error" in result and result.get("failed") == -1:
            return TestResult(
                passed=0,
                failed=0,
                total=0,
                failures=[],
                error=result["error"]
            )

        passed = result.get("passed", 0)
        failed = result.get("failed", 0)
        failures = result.get("failures", [])

        return TestResult(
            passed=passed,
            failed=failed,
            total=passed + failed,
            failures=failures
        )
