"""Text-to-speech for coach responses."""

import pyttsx3
from rich.console import Console
from mochi.io.utils import strip_markdown


class TextToSpeech:
    """Convert text to speech."""

    def __init__(self, rate: int = 180, voice_id: int = 0):
        """
        Initialize TTS engine.

        Args:
            rate: Speaking rate in words per minute (default 180)
            voice_id: Voice index (0 for first available voice)
        """
        self.console = Console()
        self.engine = pyttsx3.init()

        # Set properties
        self.engine.setProperty('rate', rate)

        # Set voice
        voices = self.engine.getProperty('voices')
        if voices and voice_id < len(voices):
            self.engine.setProperty('voice', voices[voice_id].id)

    def speak(self, text: str):
        """
        Speak the given text.

        Args:
            text: Text to speak (will be cleaned of markdown)
        """
        if not text:
            return

        # Strip markdown formatting for clean speech
        clean_text = strip_markdown(text)

        self.console.print(f"[dim]🔊 Coach speaking...[/dim]")

        try:
            self.engine.say(clean_text)
            self.engine.runAndWait()
        except Exception as e:
            self.console.print(f"[yellow]TTS error: {e}[/yellow]")
            # Fall back to just showing text
            pass

    def set_rate(self, rate: int):
        """Set speaking rate."""
        self.engine.setProperty('rate', rate)

    def set_voice(self, voice_id: int):
        """Set voice by index."""
        voices = self.engine.getProperty('voices')
        if voices and voice_id < len(voices):
            self.engine.setProperty('voice', voices[voice_id].id)
