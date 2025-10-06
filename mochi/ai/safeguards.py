"""Anti-solution-leak safeguards for coaching."""

import re
from typing import Optional


class CoachSafeguards:
    """Prevent the coach from revealing solutions."""

    FORBIDDEN_PATTERNS = [
        r"(here's|this is|the) (the )?solution",
        r"you (should|need to|must) use (a |an )?(hash|map|dict|set|heap|tree|stack|queue)",
        r"the (answer|solution|trick|key) is",
        r"copy this code",
        r"let me write it for you",
        r"the optimal approach is (to )?use",
        r"use (a |an )?(hashmap|hashtable|hash table|dictionary|heap|tree)",
    ]

    FISHING_ATTEMPTS = {
        "what's the solution": "Let's work through your approach. What have you tried?",
        "just tell me": "I'm here to guide, not solve. What's blocking you?",
        "is it a hashmap": "What makes you consider that data structure?",
        "should i use": "What patterns in the problem suggest that approach?",
        "can you write": "I'll help guide you, but you should write it. Where are you stuck?",
        "what data structure": "What operations do you need? What are the time requirements?",
        "give me the answer": "Let's break down the problem. What have you understood so far?",
        "i give up": "Let's try a simpler version first. What if the array had only 2 elements?",
    }

    def filter_coach_response(self, response: str) -> str:
        """Check if response contains forbidden patterns."""
        for pattern in self.FORBIDDEN_PATTERNS:
            if re.search(pattern, response, re.IGNORECASE):
                return (
                    "Let me rephrase that more carefully - I want to guide you "
                    "without giving away the solution. What specific part are you stuck on?"
                )
        return response

    def detect_fishing(self, user_text: str) -> Optional[str]:
        """Detect attempts to extract the solution."""
        lower_text = user_text.lower()
        for pattern, redirect in self.FISHING_ATTEMPTS.items():
            if pattern in lower_text:
                return redirect
        return None
