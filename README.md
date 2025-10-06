# Mochi 🎯

**AI-Powered Voice Interview Coach**

Practice thinking out loud during coding interviews with real AI coaching, natural voice synthesis, and instant feedback.

## Quick Start

### 1. Install

```bash
pip install -e .
```

### 2. Start Web Interface

```bash
mochi web
```

### 3. Open Browser

Navigate to **http://127.0.0.1:8000**

### 4. Setup

1. Enter your **OpenAI API key** (required)
2. (Optional) Enter your **Eleven Labs API key** for ultra-realistic voice
3. Click **"💾 Save All Keys"**
4. Paste a coding problem from LeetCode/HackerRank
5. Click **"Start Interview"**

### 5. Practice!

- **Speak your thoughts** out loud
- **Get AI coaching** tailored to your approach
- **Review your code** for feedback
- **Discuss complexity** when done

## Features

### 🤖 Real AI Coaching
- Uses GPT-4o-mini for intelligent, contextual responses
- Remembers your entire conversation
- Analyzes your specific code
- Guides without revealing solutions
- ~$0.001 per interview (1/10 of a penny!)

### 🔊 Natural Voice
- **Eleven Labs TTS** (optional): Ultra-realistic voice
- **Browser TTS** (fallback): Works without API key
- Automatic symbol conversion: `2^n` → "2 to the power of n"
- No markdown spoken (clean, natural speech)

### 📖 Smart Problem Formatting
- AI formats pasted problems into clean markdown
- Professional layout with headings, code blocks, lists
- Always visible in left panel (40% width)

### 💻 Code Editor
- Solution panel on right side (60% width)
- Write code while seeing the problem
- Automatic code review when requested
- Monospace font for comfortable coding

### 🎤 Voice Interaction
- Web Speech API for voice input (Chrome/Edge/Safari)
- Click "Start Speaking" to talk
- Natural commands: "review my code", "give me a hint", "I'm done"
- Automatic transcription

### ⏱️ Interview Simulation
- Timer tracks elapsed time (MM:SS)
- Real-time chat interface
- Coach and user messages tracked
- Complexity discussion when finished

## How It Works

### The Interview Flow

1. **Problem Display**
   - Paste problem from anywhere (LeetCode, HackerRank, etc.)
   - AI formats it into readable markdown
   - Displays in left panel

2. **Problem Reading**
   - Coach reads problem aloud with natural voice
   - Mathematical symbols converted to speech
   - You follow along visually

3. **Think Out Loud**
   - Click "Start Speaking"
   - Explain your approach
   - AI coach responds with guidance

4. **Code Your Solution**
   - Write in right panel editor
   - Problem always visible on left
   - AI remembers your approach

5. **Get Feedback**
   - Click "Review My Code" for analysis
   - Click "Get Hint" if stuck
   - AI provides contextual help

6. **Finish Interview**
   - Click "I'm Done"
   - Discuss time/space complexity
   - Get feedback on your analysis

### AI Coaching

The coach:
- **Asks clarifying questions** about your approach
- **Guides with hints** without revealing solutions
- **Analyzes your code** for bugs and improvements
- **Encourages edge case thinking**
- **Helps with complexity analysis**
- **Stays concise** (2-3 sentences, spoken aloud)

## Configuration

### API Keys (Required/Optional)

**OpenAI API Key (Required):**
- Used for: AI coaching, problem formatting
- Cost: ~$0.001 per interview
- Get key: https://platform.openai.com/api-keys

**Eleven Labs API Key (Optional):**
- Used for: Ultra-realistic voice output
- Cost: Free tier 10,000 chars/month (~20 interviews)
- Get key: https://elevenlabs.io
- Fallback: Browser TTS if not provided

### Security

- ✅ API keys stored in browser localStorage only
- ✅ Never sent to our server
- ✅ Direct browser → OpenAI/Eleven Labs communication
- ✅ No data logged or stored server-side

## Cost Breakdown

### OpenAI (GPT-4o-mini)
- Problem formatting: ~500 tokens = $0.0001
- Coach conversation: ~2,500 tokens = $0.0009
- **Total per interview: ~$0.001** (1/10 of a penny)
- **100 interviews: ~$0.10** (ten cents)

### Eleven Labs (Optional)
- Problem reading: ~500 chars = $0.00009
- Coach responses: ~1,000 chars = $0.00018
- **Total per interview: ~$0.0003** (3/100 of a penny)
- **Free tier: 10,000 chars/month** (~20 interviews)

**Combined cost: ~$0.0013 per interview** (barely over 1/10 of a penny!)

## CLI Mode (Advanced)

For terminal-based interviews with local file watching:

```bash
# Create solution file
touch solution.py

# Start CLI interview
mochi start --voice -f solution.py

# Paste problem when prompted
# Coach speaks, you respond
# File changes detected automatically
```

**CLI Features:**
- Local TTS (pyttsx3) instead of browser
- Whisper STT for voice input
- Live file watching
- Works offline (after setup)

## Documentation

### User Guides
- **QUICKSTART.md** - 2-minute setup guide
- **WEB_INTERFACE.md** - Complete web interface guide
- **SPEAKING_GUIDE.md** - Tips on what to say during interviews

### Feature Documentation
- **docs/AI_COACH_INTEGRATION.md** - How AI coaching works
- **docs/AI_FORMATTING_FEATURE.md** - Problem formatting details
- **docs/ELEVENLABS_TTS.md** - Voice synthesis guide

### Development
- **CLAUDE.md** - Guide for AI assistance
- **docs/development/** - Debug and troubleshooting guides
- **docs/archive/** - Update history and change logs

## Troubleshooting

### Voice Issues

**Test button works but interview is robotic:**
- Eleven Labs key not saved to localStorage
- Click "💾 Save All Keys" after entering key
- Refresh page and check browser console

**No voice at all:**
- Check system volume
- Check browser audio permissions
- Try different browser (Chrome recommended)

**Problem text too long error:**
- Paste shorter problem (just description, not all examples)
- Text > 5,000 chars exceeds Eleven Labs limit
- Will fallback to browser TTS

### API Issues

**OpenAI 401 Unauthorized:**
- Invalid API key
- Re-enter and save key

**Eleven Labs 401:**
- Invalid API key
- Get correct key from elevenlabs.io

**Rate limits:**
- OpenAI free tier: 3 requests/minute
- Eleven Labs free tier: 2 requests/second
- Wait and retry

### Browser Console

Press **F12** to see debug logs:
- API call status
- Voice method used
- Error messages
- Character counts

See `docs/development/WHERE_ARE_LOGS.md` for details.

## Project Structure

```
mochi/
├── mochi/
│   ├── static/
│   │   ├── index.html          # Web interface
│   │   └── app.js              # Client-side logic
│   ├── server.py               # FastAPI web server
│   ├── cli.py                  # CLI interface
│   ├── core/                   # Core orchestration
│   ├── ai/                     # AI coach logic
│   ├── io/                     # Voice I/O (STT/TTS)
│   └── harness/                # Code execution
├── docs/                       # Feature documentation
│   ├── development/            # Debug guides
│   └── archive/                # Change history
├── README.md                   # This file
├── QUICKSTART.md              # Quick setup
├── WEB_INTERFACE.md           # Web guide
└── SPEAKING_GUIDE.md          # Interview tips
```

## Why Mochi?

The hardest part of coding interviews isn't solving problems—it's **explaining your thinking while you code**. Most people:

- ❌ Go silent when they start coding
- ❌ Forget to verbalize their approach
- ❌ Don't explain trade-offs

**Mochi forces you to practice this critical skill!**

After 5-10 sessions, talking while coding becomes natural. You'll be ready for real interviews where communication is key.

## Requirements

- Python 3.10+
- Modern browser (Chrome/Edge recommended for full voice support)
- Internet connection (for API calls)
- OpenAI API key (required)
- Eleven Labs API key (optional, for better voice)

## Installation

```bash
# Clone the repo
git clone <repository-url>
cd mochi

# Install
pip install -e .

# Start web interface
mochi web

# Or start CLI mode
mochi start --voice -f solution.py
```

## Contributing

This is a personal practice tool, but improvements welcome:
- Bug fixes
- Better voice handling
- Multi-language support
- UI improvements

## License

MIT

## Credits

Built to help developers practice the most overlooked interview skill: **thinking out loud**.

---

**Ready to practice?**

```bash
mochi web
```

Then open http://127.0.0.1:8000 and start your first interview! 🎯
