"""Core session orchestrator."""

import yaml
from pathlib import Path
from datetime import datetime
from typing import Optional, List, Dict, Any
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown

from mochi.core.config import Config
from mochi.core.prompts import get_intro_message
from mochi.core.file_watcher import FileWatcher
from mochi.ai.coach import Coach
from mochi.harness.python_harness import PythonHarness, TestResult
from mochi.schemas import (
    Problem,
    Message,
    MessageRole,
    InterviewState,
    SessionState,
)


class Orchestrator:
    """Orchestrate the interview session."""

    def __init__(
        self,
        problem_statement: str,
        solution_file: Path,
        config: Config,
        voice_mode: bool = True,
        tts_mode: str = "local",
        helpfulness_override: Optional[str] = None
    ):
        self.config = config
        self.console = Console()
        self.problem_statement = problem_statement
        self.solution_file = solution_file
        self.coach = Coach(config)
        self.tts_mode = tts_mode
        self.helpfulness = helpfulness_override or config.coach_helpfulness

        # Timer
        self.start_time = None

        self.voice_mode = voice_mode
        self.stt = None
        self.tts = None

        if voice_mode:
            from mochi.io.stt import SpeechToText
            from mochi.io.tts import TextToSpeech
            self.stt = SpeechToText(model_size="base")
            if tts_mode == "local":
                self.tts = TextToSpeech(rate=180)
            # API TTS mode will use LLM audio capabilities

        self.state = SessionState(
            problem_id="custom",  # No predefined ID for pasted problems
            solution_file=str(solution_file),
            state=InterviewState.INIT,
        )

        self.watcher: Optional[FileWatcher] = None

    def start(self):
        """Start the interview session."""
        self.console.print("\n[bold cyan]🎯 Mochi Mock Interview[/bold cyan]\n")

        # Display problem for user to read
        self.console.print(Panel(
            Markdown(self.problem_statement),
            title="[bold blue]Problem Statement[/bold blue]",
            border_style="blue"
        ))
        self.console.print(f"\n[dim]Solution file: {self.solution_file}[/dim]\n")

        # Start file watcher
        self.watcher = FileWatcher(self.solution_file, self._on_file_change)
        self.watcher.start()

        # Start timer
        self.start_time = datetime.now()

        # Start interview with brief intro
        self.state.state = InterviewState.INTRO
        intro = "Let's begin the interview. I can see your problem statement on the screen. Take a moment to read through it, and when you're ready, feel free to ask any clarifying questions."

        # Optionally read the problem aloud
        if self.voice_mode:
            problem_intro = f"The problem is: {self.problem_statement[:500]}"  # First 500 chars
            self._display_coach_message(problem_intro)
            self._add_message(MessageRole.COACH, problem_intro)

        self._display_coach_message(intro)
        self._add_message(MessageRole.COACH, intro)

        # Main interaction loop
        try:
            self._interaction_loop()
        finally:
            if self.watcher:
                self.watcher.stop()

    def _get_elapsed_time(self) -> str:
        """Get formatted elapsed time."""
        elapsed = (datetime.now() - self.start_time).total_seconds()
        minutes = int(elapsed // 60)
        seconds = int(elapsed % 60)
        return f"{minutes:02d}:{seconds:02d}"

    def _interaction_loop(self):
        """Main interaction loop."""
        if self.voice_mode:
            self.console.print("\n[dim]Voice mode active - speak your responses[/dim]")
            self.console.print("[dim]Say 'run tests', 'give me a hint', or 'quit' for commands[/dim]")
        else:
            self.console.print("\n[dim]Commands: 'test' to run tests, 'hint' for a hint, 'quit' to exit[/dim]")

        self.console.print(f"[dim]Timer started at {self.start_time.strftime('%H:%M:%S')}[/dim]\n")

        while self.state.state != InterviewState.DONE:
            try:
                # Show elapsed time
                elapsed_display = f"[dim][{self._get_elapsed_time()}][/dim]"

                # Get user input (voice or text)
                if self.voice_mode:
                    self.console.print(f"{elapsed_display}")
                    user_input = self.stt.quick_listen(max_silence_sec=2.0)
                else:
                    user_input = self.console.input(f"{elapsed_display} [bold green]You:[/bold green] ").strip()

                if not user_input:
                    continue

                # Check for commands
                lower_input = user_input.lower()

                if any(word in lower_input for word in ["quit", "exit", "stop", "end interview", "i'm done"]):
                    elapsed = self._get_elapsed_time()
                    self.console.print(f"\n[yellow]Interview ended. Total time: {elapsed}[/yellow]")

                    # Ask for Big-O analysis if they finished
                    if any(word in lower_input for word in ["done", "finished", "complete"]):
                        self.state.state = InterviewState.COMPLEXITY
                        final_question = "Great! Before we wrap up, can you analyze the time and space complexity of your solution?"
                        self._add_message(MessageRole.COACH, final_question)
                        self._display_coach_message(final_question)
                        continue
                    break

                if any(word in lower_input for word in ["review", "check", "test", "run test", "look at my code"]):
                    self._run_tests()
                    continue

                if any(word in lower_input for word in ["hint", "give me a hint", "i'm stuck", "help", "stuck"]):
                    user_input = "I'm stuck. Can you give me a hint?"

                # Get coach response
                self._handle_user_message(user_input)

            except KeyboardInterrupt:
                self.console.print("\n\n[yellow]Interview interrupted.[/yellow]")
                break
            except EOFError:
                break

    def _handle_user_message(self, user_input: str):
        """Process user message and get coach response."""
        self._add_message(MessageRole.CANDIDATE, user_input)

        elapsed = (datetime.now() - self.start_time).total_seconds() / 60

        # Include problem context in first exchange
        context = f"Problem: {self.problem_statement}\n\n" if len(self.state.messages) < 3 else ""

        response = self.coach.get_response(
            user_message=context + user_input,
            message_history=self.state.messages,
            problem_title="Interview Problem",
            state=self.state.state,
            elapsed_min=elapsed,
            helpfulness=self.helpfulness
        )

        self._add_message(MessageRole.COACH, response)
        self._display_coach_message(response)

        # Update state based on conversation
        self._update_state(user_input)

    def _run_tests(self):
        """Ask coach to review the current solution."""
        self.console.print("\n[cyan]Reviewing your solution...[/cyan]")

        # Read the current solution
        try:
            with open(self.solution_file, 'r') as f:
                solution_code = f.read()
        except Exception as e:
            self.console.print(f"[red]Error reading solution file: {e}[/red]\n")
            return

        self.state.test_runs += 1

        # Ask coach to review
        review_request = f"Here's my current solution:\n\n```\n{solution_code}\n```\n\nCan you review it and tell me if there are any issues?"

        self._handle_user_message(review_request)

    def _display_failure(self, failure: Dict[str, Any]):
        """Display a test failure."""
        if "error" in failure:
            self.console.print(f"  [red]{failure['name']}:[/red] {failure['error']}")
        else:
            self.console.print(
                f"  [red]{failure['name']}:[/red] "
                f"Expected {failure['expected']}, got {failure['got']}"
            )

    def _get_test_feedback(self, result: TestResult):
        """Get coach feedback on test results."""
        if result.all_passing:
            feedback_msg = "All tests are passing! Let's discuss the time and space complexity of your solution."
        else:
            failures_summary = "; ".join([
                f.get("name", "unknown") for f in result.failures[:2]
            ])
            feedback_msg = f"Some tests are failing: {failures_summary}. Can you trace through your logic?"

        elapsed = (datetime.now() - self.state.start_time).total_seconds() / 60
        response = self.coach.get_response(
            user_message=feedback_msg,
            message_history=self.state.messages,
            problem_title=self.problem.title,
            state=self.state.state,
            elapsed_min=elapsed,
        )

        self._add_message(MessageRole.COACH, response)
        self._display_coach_message(response)

    def _on_file_change(self):
        """Handle solution file changes."""
        self.console.print("\n[dim]📝 Solution file updated[/dim]\n")

    def _update_state(self, user_input: str):
        """Update interview state based on conversation."""
        lower_input = user_input.lower()

        if self.state.state == InterviewState.INTRO:
            self.state.state = InterviewState.UNDERSTANDING

        elif self.state.state == InterviewState.UNDERSTANDING:
            if any(word in lower_input for word in ["approach", "strategy", "plan", "use"]):
                self.state.state = InterviewState.APPROACH

        elif self.state.state == InterviewState.APPROACH:
            if any(word in lower_input for word in ["code", "implement", "write"]):
                self.state.state = InterviewState.CODING

    def _add_message(self, role: MessageRole, content: str):
        """Add message to history."""
        message = Message(role=role, content=content, timestamp=datetime.now())
        self.state.messages.append(message)

    def _display_coach_message(self, message: str):
        """Display coach message with formatting."""
        self.console.print(Panel(
            Markdown(message),
            title="[bold blue]Coach[/bold blue]",
            border_style="blue"
        ))
        self.console.print()

        # Speak the message in voice mode
        if self.voice_mode and self.tts:
            self.tts.speak(message)
