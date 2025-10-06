# Mochi 🎯

**AI-powered voice interview coach - Practice thinking out loud!**

The hardest part of coding interviews isn't solving problems - it's explaining your thinking while you code. Mochi helps you practice this critical skill by forcing you to speak out loud during mock interviews.

## Quick Start

### Option 1: Web Interface (Easiest)

```bash
# 1. Install
pip install -e .

# 2. Start web server
mochi web

# 3. Open browser to http://127.0.0.1:8000
```

Then in your browser:
- Enter your OpenAI API key (stored locally, never sent to our server)
- Paste a coding problem from LeetCode/HackerRank
- Click "Start Interview" and start speaking!

**Your browser will handle voice input/output using Web Speech API.**

### Option 2: CLI Mode

```bash
# 1. Install
pip install -e .

# 2. Set Your API Key
export OPENAI_API_KEY='your-key-here'

# 3. Start an Interview
touch solution.py
mochi start --voice -f solution.py
```

**Paste any LeetCode/HackerRank problem when prompted.**

**Use headphones!** Then speak naturally:
- "Can the array be empty?"
- "I'm thinking of using a hash map..."
- "Review my code"
- "I'm done"

## How It Works

**The Simple Workflow:**

1. **Copy/paste a problem** from LeetCode or anywhere - no pre-made problem database needed
2. **AI reads it aloud** - Hear the problem statement (optional)
3. **Timer starts** - Track your progress
4. **You speak your thoughts** - Explain your approach out loud
5. **Code in your editor** - Work in any editor you like
6. **Say "review my code"** - AI analyzes your solution and gives feedback
7. **Say "I'm done"** - AI asks about Big-O complexity

**Note**: You can use `--no-voice` for keyboard mode, but speaking is the whole point!

## Configuration

Edit `settings.toml` to customize:

```toml
[llm]
engine = "openai"           # or "anthropic"
model = "gpt-4o-mini"       # or "claude-3-5-sonnet-20241022"

[coach]
helpfulness = "balanced"    # "gentle" | "balanced" | "insistent"
```

Or override per session:
```bash
mochi start --voice -f solution.py --helpfulness insistent
```

## Example Session

```
$ mochi start --voice -f solution.py

Paste your problem statement:
[Paste: "Given an array of integers nums and an integer target..."]

┌─ Problem Statement ─────────────────────┐
│ Given an array of integers nums...     │
└─────────────────────────────────────────┘

🔊 Coach: "The problem is: Given an array..."
🔊 Coach: "Take a moment to read it. Any questions?"

[00:15] 🎤 You: "Can I use the same element twice?"

🔊 Coach: "No, you can't use the same element twice."

[01:23] 🎤 You: "I'm thinking of using a hash map..."

[You code while explaining]

[05:47] 🎤 You: "Review my code"

🔊 Coach: "I see a hash map. One edge case to consider..."

[08:15] 🎤 You: "I'm done"

🔊 Coach: "What's the time and space complexity?"
```

## What to Say During Interviews

Not sure what to say? **Read `SPEAKING_GUIDE.md`** for:
- Specific phrases and patterns to practice
- Example dialogues
- How to explain your approach out loud
- How to debug verbally
- Common mistakes to avoid

## Features

✅ **Paste any problem** - LeetCode, HackerRank, or anywhere. No database needed!
✅ **Voice-driven** - Speak out loud to practice thinking during interviews
✅ **Coach speaks back** - Real interview feel with spoken feedback
✅ **Timer** - Track elapsed time automatically
✅ **Code review** - AI analyzes your solution and provides feedback
✅ **Anti-solution safeguards** - Coach guides without revealing answers
✅ **Live file watching** - Edit in any editor
✅ **Natural commands** - Say "review my code", "hint", or "I'm done"
✅ **Auto-silence detection** - Stops listening when you pause
✅ **Big-O discussion** - Automatic complexity analysis at the end
✅ **Configurable helpfulness** - Gentle, balanced, or insistent coaching

## Advanced Options

### Web Interface

```bash
# Run on a different port
mochi web --port 3000

# Bind to all interfaces (not just localhost)
mochi web --host 0.0.0.0 --port 8000
```

### CLI Mode

```bash
# Override helpfulness for one session
mochi start --voice -f solution.py --helpfulness gentle

# Use API-based TTS (if available)
mochi start --voice -f solution.py --tts-mode api

# Keyboard-only mode
mochi start --no-voice -f solution.py
```

## Project Status

**v0.1.0 - Ready to use!**

✅ **Web interface** - Browser-based with local API key storage
✅ **CLI mode** - Terminal-based for advanced users
✅ Paste-based workflow (any LeetCode problem)
✅ Voice interaction (Web Speech API for web, Whisper STT + pyttsx3 TTS for CLI)
✅ AI code review and feedback
✅ Timer tracking
✅ Anti-solution coaching
✅ Big-O complexity discussion

Future enhancements:
- Real AI coaching integration in web UI (currently uses placeholder responses)
- Session persistence and replay
- Performance analytics
- Multi-language support (Java, JavaScript, etc.)
- Voice calibration wizard

## Why This Matters

Real interviewers want to hear:
- Your thought process
- How you break down problems
- Trade-offs you consider
- How you debug
- Your communication skills

**Mochi forces you to develop these habits** in a low-pressure environment.

After 5-10 sessions, talking while coding will feel natural!

## License

MIT
