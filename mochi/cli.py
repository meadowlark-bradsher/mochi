"""CLI interface for Mochi."""

import click
from pathlib import Path
from rich.console import Console

from mochi.core.config import Config
from mochi.core.orchestrator import Orchestrator


console = Console()


@click.group()
@click.version_option(version="0.1.0")
def cli():
    """🎯 Mochi - AI-powered mock technical interview coach"""
    pass


@cli.command()
@click.option(
    "--file",
    "-f",
    required=True,
    type=click.Path(),
    help="Path to your solution file",
)
@click.option(
    "--problem",
    "-p",
    type=str,
    help="Problem statement (or paste when prompted)",
)
@click.option(
    "--config",
    "-c",
    default="settings.toml",
    type=click.Path(),
    help="Path to configuration file",
)
@click.option(
    "--voice/--no-voice",
    default=True,
    help="Enable/disable voice mode (default: enabled)",
)
@click.option(
    "--tts-mode",
    type=click.Choice(["local", "api"], case_sensitive=False),
    default="local",
    help="TTS mode: 'local' for pyttsx3, 'api' for LLM audio",
)
@click.option(
    "--helpfulness",
    type=click.Choice(["gentle", "balanced", "insistent"], case_sensitive=False),
    help="Override coach helpfulness level for this session",
)
def start(file: str, problem: str, config: str, voice: bool, tts_mode: str, helpfulness: str):
    """Start a new mock interview session.

    Copy the problem statement from LeetCode/etc and paste it when prompted,
    or provide it via --problem flag.
    """

    # Validate inputs
    solution_file = Path(file)
    config_path = Path(config)

    if not config_path.exists():
        console.print(f"[red]Error: Config file not found: {config}[/red]")
        console.print("[yellow]Tip: Copy settings.toml to your desired location[/yellow]")
        return

    # Ensure solution file exists
    if not solution_file.exists():
        console.print(f"[yellow]Solution file doesn't exist. Creating: {solution_file}[/yellow]")
        solution_file.parent.mkdir(parents=True, exist_ok=True)
        solution_file.touch()

    try:
        # Load config
        cfg = Config(str(config_path))

        # Check for API keys
        import os
        if cfg.llm_engine == "openai" and not os.getenv("OPENAI_API_KEY"):
            console.print("[red]Error: OPENAI_API_KEY environment variable not set[/red]")
            console.print("[yellow]Set it with: export OPENAI_API_KEY='your-key'[/yellow]")
            return
        elif cfg.llm_engine == "anthropic" and not os.getenv("ANTHROPIC_API_KEY"):
            console.print("[red]Error: ANTHROPIC_API_KEY environment variable not set[/red]")
            console.print("[yellow]Set it with: export ANTHROPIC_API_KEY='your-key'[/yellow]")
            return

        # Get problem statement if not provided
        if not problem:
            console.print("\n[bold cyan]Paste your problem statement[/bold cyan]")
            console.print("[dim](Press Enter, paste, then Ctrl+D or Ctrl+Z when done)[/dim]\n")

            lines = []
            try:
                while True:
                    line = input()
                    lines.append(line)
            except EOFError:
                pass

            problem = "\n".join(lines).strip()

            if not problem:
                console.print("[red]Error: No problem statement provided[/red]")
                return

        # Start orchestrator
        if voice:
            console.print("[bold cyan]🎤 Voice mode enabled - you'll speak your responses![/bold cyan]")
        else:
            console.print("[yellow]Voice mode disabled - you'll type your responses[/yellow]")

        console.print(f"[dim]TTS mode: {tts_mode}[/dim]\n")

        orchestrator = Orchestrator(
            problem_statement=problem,
            solution_file=solution_file,
            config=cfg,
            voice_mode=voice,
            tts_mode=tts_mode,
            helpfulness_override=helpfulness
        )
        orchestrator.start()

    except FileNotFoundError as e:
        console.print(f"[red]Error: {e}[/red]")
    except Exception as e:
        console.print(f"[red]Unexpected error: {e}[/red]")
        import traceback
        console.print(f"[dim]{traceback.format_exc()}[/dim]")


@cli.command()
@click.option(
    "--host",
    default="127.0.0.1",
    help="Host to bind the web server to (default: 127.0.0.1)",
)
@click.option(
    "--port",
    default=8000,
    type=int,
    help="Port to run the web server on (default: 8000)",
)
def web(host: str, port: int):
    """Start the web-based interview interface.

    This starts a local web server where you can:
    - Paste coding problems from LeetCode/HackerRank
    - Provide your OpenAI API key (stored locally in browser)
    - Practice speaking out loud using your browser's microphone
    - Get real-time AI coaching feedback
    """
    from mochi.server import run_server

    console.print(f"[bold cyan]🌐 Starting Mochi web server...[/bold cyan]")
    console.print(f"[green]✓[/green] Server running at: [bold]http://{host}:{port}[/bold]")
    console.print(f"[dim]Press Ctrl+C to stop[/dim]\n")

    try:
        run_server(host=host, port=port)
    except KeyboardInterrupt:
        console.print("\n[yellow]Server stopped[/yellow]")


@cli.command()
def config_example():
    """Show example configuration."""
    example = """
[app]
workspace_dir = "~/mochi_practice"

[coach]
helpfulness = "balanced"
personality = "supportive"

[llm]
engine = "openai"           # or "anthropic"
model = "gpt-4o-mini"       # or "claude-3-5-sonnet-20241022"
temperature = 0.3
max_tokens = 600

[harness]
timeout_ms = 4000
memory_mb = 512
"""
    console.print("[cyan]Example settings.toml:[/cyan]")
    console.print(example)


if __name__ == "__main__":
    cli()
