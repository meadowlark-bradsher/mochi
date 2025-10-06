"""Speech-to-text using Whisper."""

import whisper
import sounddevice as sd
import numpy as np
from pathlib import Path
import tempfile
import wave
from rich.console import Console


class SpeechToText:
    """Convert speech to text using OpenAI Whisper."""

    def __init__(self, model_size: str = "base"):
        """
        Initialize Whisper model.

        Args:
            model_size: Model size - "tiny", "base", "small", "medium", "large"
                       "base" is good balance of speed/accuracy
        """
        self.console = Console()
        self.console.print(f"[dim]Loading Whisper {model_size} model...[/dim]")
        self.model = whisper.load_model(model_size)
        self.sample_rate = 16000
        self.console.print("[dim]✓ Whisper ready[/dim]")

    def listen(self, duration: float = 10.0, silence_threshold: float = 0.02) -> str:
        """
        Listen for speech and convert to text.

        Args:
            duration: Maximum recording duration in seconds
            silence_threshold: Audio level below which is considered silence

        Returns:
            Transcribed text
        """
        self.console.print("\n[bold cyan]🎤 Listening... (press Ctrl+C when done speaking)[/bold cyan]")

        try:
            # Record audio
            recording = sd.rec(
                int(duration * self.sample_rate),
                samplerate=self.sample_rate,
                channels=1,
                dtype=np.float32
            )

            # Wait for recording (but allow interrupt)
            sd.wait()

            # Detect actual speech end (simple energy-based)
            recording = self._trim_silence(recording, silence_threshold)

            # Save to temporary file
            with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
                temp_path = Path(f.name)
                self._save_wav(temp_path, recording)

            # Transcribe
            self.console.print("[dim]Transcribing...[/dim]")
            result = self.model.transcribe(str(temp_path), fp16=False)
            text = result["text"].strip()

            # Cleanup
            temp_path.unlink()

            if text:
                self.console.print(f"[dim]You said:[/dim] {text}")
                return text
            else:
                self.console.print("[yellow]No speech detected[/yellow]")
                return ""

        except KeyboardInterrupt:
            # Stop recording on Ctrl+C
            sd.stop()

            # Get what was recorded so far
            recording = recording[:sd.get_stream().write_available]

            if len(recording) > 0:
                recording = self._trim_silence(recording, silence_threshold)
                with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
                    temp_path = Path(f.name)
                    self._save_wav(temp_path, recording)

                self.console.print("[dim]Transcribing...[/dim]")
                result = self.model.transcribe(str(temp_path), fp16=False)
                text = result["text"].strip()
                temp_path.unlink()

                if text:
                    self.console.print(f"[dim]You said:[/dim] {text}")
                    return text

            return ""

    def _trim_silence(self, audio: np.ndarray, threshold: float) -> np.ndarray:
        """Trim silence from end of audio."""
        # Find where audio drops below threshold for extended period
        energy = np.abs(audio).flatten()

        # Find last point above threshold
        for i in range(len(energy) - 1, 0, -1):
            if energy[i] > threshold:
                return audio[:i + self.sample_rate]  # Keep 1 second after last sound

        return audio

    def _save_wav(self, path: Path, audio: np.ndarray):
        """Save audio as WAV file."""
        # Convert to int16
        audio_int16 = (audio * 32767).astype(np.int16)

        with wave.open(str(path), 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)  # 2 bytes for int16
            wf.setframerate(self.sample_rate)
            wf.writeframes(audio_int16.tobytes())

    def quick_listen(self, max_silence_sec: float = 2.0) -> str:
        """
        Listen and auto-stop after silence.

        Args:
            max_silence_sec: Stop after this many seconds of silence

        Returns:
            Transcribed text
        """
        self.console.print("\n[bold cyan]🎤 Listening... (speak now)[/bold cyan]")

        silence_threshold = 0.02
        chunk_duration = 0.5  # Check for silence every 0.5 seconds
        max_duration = 30.0  # Absolute maximum

        chunks = []
        silence_chunks = 0
        max_silence_chunks = int(max_silence_sec / chunk_duration)

        try:
            for _ in range(int(max_duration / chunk_duration)):
                chunk = sd.rec(
                    int(chunk_duration * self.sample_rate),
                    samplerate=self.sample_rate,
                    channels=1,
                    dtype=np.float32
                )
                sd.wait()

                chunks.append(chunk)

                # Check if chunk is silence
                if np.max(np.abs(chunk)) < silence_threshold:
                    silence_chunks += 1
                    if silence_chunks >= max_silence_chunks:
                        self.console.print("[dim]Silence detected, processing...[/dim]")
                        break
                else:
                    silence_chunks = 0

            # Combine all chunks
            if chunks:
                recording = np.concatenate(chunks)
                recording = self._trim_silence(recording, silence_threshold)

                # Transcribe
                with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
                    temp_path = Path(f.name)
                    self._save_wav(temp_path, recording)

                result = self.model.transcribe(str(temp_path), fp16=False)
                text = result["text"].strip()
                temp_path.unlink()

                if text:
                    self.console.print(f"[dim]You said:[/dim] {text}")
                    return text

            return ""

        except KeyboardInterrupt:
            sd.stop()
            return ""
