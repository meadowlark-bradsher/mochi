"""Message and session schemas."""

from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel
from enum import Enum


class MessageRole(str, Enum):
    """Message roles in conversation."""
    SYSTEM = "system"
    COACH = "coach"
    CANDIDATE = "candidate"


class Message(BaseModel):
    """A single message in the interview."""
    role: MessageRole
    content: str
    timestamp: datetime = datetime.now()


class InterviewState(str, Enum):
    """States of the interview process."""
    INIT = "init"
    INTRO = "intro"
    UNDERSTANDING = "understanding"
    APPROACH = "approach"
    CODING = "coding"
    TESTING = "testing"
    DEBUGGING = "debugging"
    COMPLEXITY = "complexity"
    REFLECTION = "reflection"
    DONE = "done"


class SessionState(BaseModel):
    """Current state of an interview session."""
    state: InterviewState = InterviewState.INIT
    problem_id: str
    solution_file: str
    messages: List[Message] = []
    hints_given: int = 0
    test_runs: int = 0
    tests_passing: bool = False
    start_time: datetime = datetime.now()
