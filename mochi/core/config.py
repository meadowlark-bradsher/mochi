"""Configuration management."""

import tomli
from pathlib import Path
from typing import Dict, Any


class Config:
    """Application configuration."""

    def __init__(self, config_path: str = "settings.toml"):
        self.config_path = Path(config_path)
        self._config: Dict[str, Any] = {}
        self.load()

    def load(self) -> None:
        """Load configuration from TOML file."""
        if self.config_path.exists():
            with open(self.config_path, "rb") as f:
                self._config = tomli.load(f)
        else:
            raise FileNotFoundError(f"Configuration file not found: {self.config_path}")

    def get(self, section: str, key: str, default: Any = None) -> Any:
        """Get a configuration value."""
        return self._config.get(section, {}).get(key, default)

    @property
    def llm_engine(self) -> str:
        return self.get("llm", "engine", "openai")

    @property
    def llm_model(self) -> str:
        return self.get("llm", "model", "gpt-4o-mini")

    @property
    def llm_temperature(self) -> float:
        return self.get("llm", "temperature", 0.3)

    @property
    def llm_max_tokens(self) -> int:
        return self.get("llm", "max_tokens", 600)

    @property
    def coach_helpfulness(self) -> str:
        return self.get("coach", "helpfulness", "balanced")

    @property
    def harness_timeout_ms(self) -> int:
        return self.get("harness", "timeout_ms", 4000)

    @property
    def harness_memory_mb(self) -> int:
        return self.get("harness", "memory_mb", 512)
