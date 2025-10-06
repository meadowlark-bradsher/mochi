"""Utilities for voice I/O."""

import re


def strip_markdown(text: str) -> str:
    """
    Remove markdown formatting for clean TTS output.

    Args:
        text: Text with potential markdown formatting

    Returns:
        Plain text suitable for speech
    """
    # Remove bold/italic (**text**, *text*, __text__, _text_)
    text = re.sub(r'\*\*([^\*]+)\*\*', r'\1', text)  # **bold**
    text = re.sub(r'\*([^\*]+)\*', r'\1', text)      # *italic*
    text = re.sub(r'__([^_]+)__', r'\1', text)       # __bold__
    text = re.sub(r'_([^_]+)_', r'\1', text)         # _italic_

    # Remove code blocks (```code```)
    text = re.sub(r'```[^\n]*\n.*?```', '[code block]', text, flags=re.DOTALL)

    # Remove inline code (`code`)
    text = re.sub(r'`([^`]+)`', r'\1', text)

    # Remove links [text](url)
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)

    # Remove headers (##, ###, etc.)
    text = re.sub(r'^#{1,6}\s+', '', text, flags=re.MULTILINE)

    # Remove special symbols
    text = text.replace('✅', '')
    text = text.replace('❌', '')
    text = text.replace('🎯', '')
    text = text.replace('🔊', '')
    text = text.replace('🎤', '')
    text = text.replace('⌨️', '')
    text = text.replace('🔄', '')

    # Clean up extra whitespace
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()

    return text
