# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Mochi** is a voice-driven mock interview coach that helps developers practice **thinking out loud** during coding interviews. The core insight: the hardest part of interviews isn't solving problems - it's explaining your thinking while you code.

## Project Status

- **Current State**: MVP complete and functional
- **Voice interaction**: ✅ Working (Whisper STT + pyttsx3 TTS)
- **Keyboard fallback**: ✅ Available (but voice is the point)
- **Test Harness**: ✅ Working (sandboxed Python execution)
- **Anti-solution coaching**: ✅ Working (Socratic guidance only)
- **Documentation**: Complete specification in `docs/MOCHI-SPEC.md`
- **Language**: Python 3.10+

## Architecture (Planned)

The system follows a modular architecture with these core components:

### Core Components
- **Core Orchestrator** (`core/orchestrator.py`) - Session state, timers, transcripts, and coach coordination
- **STT/TTS Adapters** (`io/`) - Abstract local and cloud speech engines (Whisper, Vosk, pyttsx3, edge-tts)
- **LLM Adapter** (`ai/`) - Abstract local (llama.cpp) or API models (OpenAI, Anthropic)
- **Execution Harness** (`harness/`) - Safely runs candidate code and tests in sandboxed environments
- **Code Analyzer** (`harness/analyzers.py`) - AST-based analysis for intelligent hints without revealing solutions
- **Session Store** (`core/store.py`) - SQLite + JSON blobs for transcripts, prompts, config, metrics
- **Difficulty Calibrator** (`core/calibrator.py`) - Adjusts coaching based on performance

### Planned Directory Structure
```
mock_interviewer/
  pyproject.toml
  settings.toml           # User configuration
  mock_interviewer/
    cli.py                # Main entry point
    core/                 # Session orchestration
    io/                   # Speech input/output
    ai/                   # LLM integration
    harness/              # Code execution
    ui/                   # Terminal/web UI
    schemas/              # Data models
  tests/
  examples/problems/      # Interview problems
```

## Key Design Principles

### Anti-Solution-Leak Safeguards
The coach must **never** provide direct solutions or code. See `docs/MOCHI-SPEC.md:229-315` for:
- Forbidden patterns (e.g., "use a hashmap", "the solution is...")
- Socratic questioning approach
- Progressive hint system that guides without revealing

### Interview Realism
- Natural timing (8s silence before nudging)
- Voice calibration for natural interaction
- State machine for interview phases (INTRO → UNDERSTANDING → APPROACH → CODING → TESTING → COMPLEXITY → REFLECTION)

### Safety & Isolation
- Code execution in sandboxed subprocess with resource limits
- No network access during execution
- Memory and CPU limits enforced

## Development Guidelines

### When Implementing Components

1. **Follow the spec closely**: `docs/MOCHI-SPEC.md` contains detailed implementation guidance for each component
2. **Start with MVP features** (see spec lines 820-828):
   - Basic STT → LLM → TTS pipeline
   - Single problem support (two_sum)
   - Simple subprocess harness
   - File watching for code changes
3. **Testing is critical**: Every harness must be thoroughly tested for sandbox escapes
4. **Privacy by default**: No audio recording unless explicitly enabled, local-only operation

### Configuration

User configuration will be in `settings.toml` in the project root. Key sections:
- `[coach]` - Helpfulness level, personality, timing
- `[stt]` / `[tts]` - Speech engine selection
- `[llm]` - Model provider and parameters
- `[harness]` - Execution sandbox settings
- `[privacy]` - Recording and cloud preferences

See spec lines 108-179 for complete configuration schema.

### Anti-Patterns to Avoid

❌ **Never** let the LLM coach:
- Write code for the candidate
- Name specific data structures ("use a hashmap")
- Provide algorithmic solutions directly
- Fix bugs instead of pointing to them

✅ **Always** ensure the coach:
- Asks Socratic questions
- Requests candidates explain their approach
- Points to issues without solving them
- Guides through progressive hints

## Implementation Status

✅ **MVP Complete**:
- Voice interaction (Whisper STT + pyttsx3 TTS)
- Keyboard fallback (for when mic doesn't work)
- LLM coaching with anti-solution safeguards
- Test execution with sandboxing
- File watching
- State transitions

🚧 **Next Priorities**:
1. Session persistence and replay
2. Voice calibration wizard
3. Performance analytics
4. Difficulty adjustment
5. More example problems

## CLI Commands (Current MVP)

```bash
# Start an interview (use --voice to speak)
mochi start --voice --problem <path> --file <path>

# Keyboard-only fallback (omit --voice)
mochi start --problem <path> --file <path>

# Show example configuration
mochi config-example
```

**Note**: The `--voice` flag enables speaking. Without it, you type instead. But the whole point of Mochi is practicing speaking out loud!

### Planned Commands (Future)

```bash
# Resume existing session
mochi resume --session <id>

# Voice setup wizard
mochi calibrate

# View session history and analytics
mochi list-sessions [--last n]
mochi stats [--session id|--all]
```

## Dependencies (When Setting Up)

Expected core dependencies:
- **Speech**: `whisper`, `vosk-api`, `pyttsx3`, `edge-tts`, `sounddevice`
- **LLM**: `openai`, `anthropic`, or local inference (llama-cpp-python)
- **Execution**: Standard library `subprocess`, `resource`, `ast`
- **Storage**: `sqlite3`, `pydantic` (for schemas)
- **CLI/TUI**: `click`, `rich` or `textual`

## Testing Strategy

When implementing:
- Unit tests for each component in isolation
- Integration tests for STT→LLM→TTS pipeline
- **Security tests** for sandbox escapes in harness
- End-to-end tests with mock problems
- Voice calibration tests with synthetic audio

## References

- Full specification: `docs/MOCHI-SPEC.md`
- State machine diagram: spec lines 207-225
- Architecture diagram: spec lines 9-28
- Progressive hints structure: spec lines 322-346
- Code analyzer examples: spec lines 349-393
