# Mochi Documentation 📚

## Quick Links

### Getting Started
- **[../README.md](../README.md)** - Main documentation and quick start
- **[../QUICKSTART.md](../QUICKSTART.md)** - 2-minute setup guide
- **[../WEB_INTERFACE.md](../WEB_INTERFACE.md)** - Complete web interface guide
- **[../SPEAKING_GUIDE.md](../SPEAKING_GUIDE.md)** - Tips on what to say during interviews

### Features

#### AI Coaching
- **[AI_COACH_INTEGRATION.md](AI_COACH_INTEGRATION.md)** - How real AI coaching works
  - System prompts
  - Conversation history
  - Cost breakdown
  - Example sessions

#### Voice & Audio
- **[ELEVENLABS_TTS.md](ELEVENLABS_TTS.md)** - Eleven Labs text-to-speech integration
  - Setup guide
  - Voice options
  - Cost analysis
  - Troubleshooting

#### Problem Formatting
- **[AI_FORMATTING_FEATURE.md](AI_FORMATTING_FEATURE.md)** - AI-powered problem formatting
  - How it works
  - Markdown rendering
  - Symbol conversion
  - Examples

### Development

#### Debugging & Troubleshooting
- **[development/WHERE_ARE_LOGS.md](development/WHERE_ARE_LOGS.md)** - How to find debug logs
- **[development/DEBUG_ELEVENLABS.md](development/DEBUG_ELEVENLABS.md)** - Eleven Labs troubleshooting
- **[development/TEST_ELEVENLABS.md](development/TEST_ELEVENLABS.md)** - Testing Eleven Labs integration
- **[development/TROUBLESHOOT_VOICE.md](development/TROUBLESHOOT_VOICE.md)** - Voice issues diagnosis
- **[development/COMMIT_SAFETY_CHECK.md](development/COMMIT_SAFETY_CHECK.md)** - Security checklist

#### Change History
- **[archive/](archive/)** - Historical updates and changes
  - CHANGES_SPLIT_VIEW.md
  - PANEL_AND_TTS_UPDATE.md
  - FULLSCREEN_AND_DEBUG.md
  - WEB_VERSION_SUMMARY.md
  - LATEST_UPDATES.md

### For AI Assistants
- **[../CLAUDE.md](../CLAUDE.md)** - Guide for Claude Code and other AI assistants

## Documentation Structure

```
mochi/
├── README.md                    # Main documentation
├── QUICKSTART.md               # Quick start guide
├── WEB_INTERFACE.md            # Web interface guide
├── SPEAKING_GUIDE.md           # Interview tips
├── CLAUDE.md                   # AI assistant guide
│
├── docs/
│   ├── README.md               # This file
│   │
│   ├── AI_COACH_INTEGRATION.md      # AI coaching
│   ├── AI_FORMATTING_FEATURE.md     # Problem formatting
│   ├── ELEVENLABS_TTS.md            # Voice synthesis
│   │
│   ├── development/            # Debug & troubleshooting
│   │   ├── WHERE_ARE_LOGS.md
│   │   ├── DEBUG_ELEVENLABS.md
│   │   ├── TEST_ELEVENLABS.md
│   │   ├── TROUBLESHOOT_VOICE.md
│   │   └── COMMIT_SAFETY_CHECK.md
│   │
│   └── archive/                # Historical changes
│       ├── CHANGES_SPLIT_VIEW.md
│       ├── PANEL_AND_TTS_UPDATE.md
│       ├── FULLSCREEN_AND_DEBUG.md
│       ├── WEB_VERSION_SUMMARY.md
│       └── LATEST_UPDATES.md
```

## Common Tasks

### Setup & Installation
→ See [../README.md](../README.md) or [../QUICKSTART.md](../QUICKSTART.md)

### Using the Web Interface
→ See [../WEB_INTERFACE.md](../WEB_INTERFACE.md)

### Understanding AI Coaching
→ See [AI_COACH_INTEGRATION.md](AI_COACH_INTEGRATION.md)

### Setting up Eleven Labs
→ See [ELEVENLABS_TTS.md](ELEVENLABS_TTS.md)

### Debugging Voice Issues
→ See [development/TROUBLESHOOT_VOICE.md](development/TROUBLESHOOT_VOICE.md)

### Finding Console Logs
→ See [development/WHERE_ARE_LOGS.md](development/WHERE_ARE_LOGS.md)

### Testing Eleven Labs
→ See [development/TEST_ELEVENLABS.md](development/TEST_ELEVENLABS.md)

## Quick Reference

### Costs
- **OpenAI (GPT-4o-mini):** ~$0.001 per interview
- **Eleven Labs:** ~$0.0003 per interview (free tier: 10K chars/month)
- **Combined:** ~$0.0013 per interview

### API Keys
- **OpenAI:** Required - Get at https://platform.openai.com/api-keys
- **Eleven Labs:** Optional - Get at https://elevenlabs.io

### Browser Support
- **Chrome/Edge:** Full support (voice input + output)
- **Safari:** Partial support (limited voice input)
- **Firefox:** No Web Speech API (use CLI mode)

### Commands
```bash
# Web interface
mochi web

# CLI mode
mochi start --voice -f solution.py

# Custom port
mochi web --port 3000
```

### Troubleshooting Quick Links

**Voice not working?**
- [development/TROUBLESHOOT_VOICE.md](development/TROUBLESHOOT_VOICE.md)
- [development/DEBUG_ELEVENLABS.md](development/DEBUG_ELEVENLABS.md)

**No logs visible?**
- [development/WHERE_ARE_LOGS.md](development/WHERE_ARE_LOGS.md)

**API errors?**
- Check [../README.md#troubleshooting](../README.md#troubleshooting)

**Safe to commit?**
- [development/COMMIT_SAFETY_CHECK.md](development/COMMIT_SAFETY_CHECK.md)

---

**Need help?** Start with [../README.md](../README.md) or [../QUICKSTART.md](../QUICKSTART.md)
