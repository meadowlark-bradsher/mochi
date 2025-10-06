"""Problem schema definitions."""

from typing import List, Optional, Any
from pydantic import BaseModel


class TestCase(BaseModel):
    """A single test case for a problem."""
    name: str
    function: str
    input: dict
    expected: Any


class Problem(BaseModel):
    """A coding interview problem."""
    id: str
    title: str
    description: str
    difficulty: str  # "easy" | "medium" | "hard"
    signature_file: str  # Path to starter code
    test_file: str  # Path to test cases
    hints_file: Optional[str] = None  # Path to progressive hints
    time_complexity_expected: Optional[str] = None
    space_complexity_expected: Optional[str] = None


class Hint(BaseModel):
    """Progressive hint structure."""
    level: int
    hints: List[str]
    never_say: List[str] = []
