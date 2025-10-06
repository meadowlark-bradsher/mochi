"""LLM-based interview coach."""

from typing import List, Optional
from mochi.core.config import Config
from mochi.schemas import Message, MessageRole, InterviewState
from mochi.ai.safeguards import CoachSafeguards
from mochi.core.prompts import get_system_prompt


class Coach:
    """AI interview coach that provides guidance without revealing solutions."""

    def __init__(self, config: Config):
        self.config = config
        self.safeguards = CoachSafeguards()
        self.client = None
        self._init_client()

    def _init_client(self):
        """Initialize the LLM client based on configuration."""
        engine = self.config.llm_engine

        if engine == "openai":
            from openai import OpenAI
            self.client = OpenAI()
            self.engine = "openai"
        elif engine == "anthropic":
            from anthropic import Anthropic
            self.client = Anthropic()
            self.engine = "anthropic"
        else:
            raise ValueError(f"Unsupported LLM engine: {engine}")

    def get_response(
        self,
        user_message: str,
        message_history: List[Message],
        problem_title: str,
        state: InterviewState,
        elapsed_min: float = 0,
        helpfulness: str = None,
    ) -> str:
        """Get a coaching response, applying safeguards."""

        # Check for fishing attempts
        redirect = self.safeguards.detect_fishing(user_message)
        if redirect:
            return redirect

        # Build conversation history
        system_prompt = get_system_prompt(
            problem_title=problem_title,
            state=state,
            helpfulness=helpfulness or self.config.coach_helpfulness,
            elapsed_min=elapsed_min,
        )

        # Get LLM response
        if self.engine == "openai":
            response = self._get_openai_response(system_prompt, message_history, user_message)
        else:
            response = self._get_anthropic_response(system_prompt, message_history, user_message)

        # Apply safeguards
        filtered_response = self.safeguards.filter_coach_response(response)
        return filtered_response

    def _get_openai_response(
        self, system_prompt: str, message_history: List[Message], user_message: str
    ) -> str:
        """Get response from OpenAI API."""
        messages = [{"role": "system", "content": system_prompt}]

        # Add message history
        for msg in message_history[-10:]:  # Keep last 10 messages for context
            role = "assistant" if msg.role == MessageRole.COACH else "user"
            messages.append({"role": role, "content": msg.content})

        # Add current message
        messages.append({"role": "user", "content": user_message})

        response = self.client.chat.completions.create(
            model=self.config.llm_model,
            messages=messages,
            temperature=self.config.llm_temperature,
            max_tokens=self.config.llm_max_tokens,
        )

        return response.choices[0].message.content

    def _get_anthropic_response(
        self, system_prompt: str, message_history: List[Message], user_message: str
    ) -> str:
        """Get response from Anthropic API."""
        messages = []

        # Add message history
        for msg in message_history[-10:]:
            role = "assistant" if msg.role == MessageRole.COACH else "user"
            messages.append({"role": role, "content": msg.content})

        # Add current message
        messages.append({"role": "user", "content": user_message})

        response = self.client.messages.create(
            model=self.config.llm_model,
            system=system_prompt,
            messages=messages,
            temperature=self.config.llm_temperature,
            max_tokens=self.config.llm_max_tokens,
        )

        return response.content[0].text
