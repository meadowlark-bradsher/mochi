# Mochi Web Interface Guide 🌐

**Browser-based interview practice with voice interaction**

## Quick Start

```bash
# 1. Install Mochi
pip install -e .

# 2. Start the web server
mochi web

# 3. Open your browser to http://127.0.0.1:8000
```

## Features

### 🔒 Secure API Key Storage
- Your OpenAI API key is stored in your browser's localStorage
- **Optional:** Add Eleven Labs API key for ultra-realistic TTS
- **Never sent to our server**
- API calls go directly from your browser to the respective services
- Keys persist across browser sessions

### 📖 AI-Formatted Problem Statement Panel
- Always visible on the left side
- **AI formats your pasted problem into clean markdown**
  - Adds headings for sections (Problem, Examples, Constraints)
  - Bold text for important terms
  - Code blocks for examples
  - Lists for constraints
  - Professional, readable layout
- Scrollable for long problems
- Uses your OpenAI API key for formatting

### 💻 Solution Editor Panel
- Always visible on the right side
- Monospace code font
- Write solution as you think out loud
- Automatically used for code reviews

### 🔊 Problem Read Aloud
- Coach reads problem with symbol conversion
  - `^` → "to the power of"
  - `<=` → "less than or equal to"
  - `[i]` → "open bracket i close bracket"
  - And many more!
- Helps you hear the problem as an interviewer would say it

### 🔊 Text-to-Speech Options
- **Browser TTS** (default) - Free, works offline
- **Eleven Labs** (optional) - Ultra-realistic voice with natural intonation
  - Requires API key from elevenlabs.io
  - Free tier: 10,000 characters/month
  - Auto-fallback to browser TTS if fails

### 🎤 Browser-Based Voice Input
- Uses Web Speech API (built into Chrome/Edge)
- No installation of Whisper or pyttsx3 needed
- Click "Start Speaking" to begin voice input
- Automatic speech-to-text transcription

### ⏱️ Real-Time Timer
- Automatic interview timing
- Displays elapsed time in MM:SS format
- Starts when interview begins

### 💬 Chat Interface
- Visual conversation history
- Coach messages in blue
- Your messages in green
- Auto-scrolls to latest message

## How to Use

### Step 1: Setup API Keys
1. Enter your OpenAI API key (starts with `sk-`) - **Required**
2. (Optional) Enter your Eleven Labs API key for better TTS
3. Click "Save Keys"
4. Keys are stored locally in browser

### Step 2: Paste Problem
1. Copy a coding problem from LeetCode/HackerRank
2. Paste into the textarea
3. Problem can be any length or format

### Step 3: Start Interview
1. Click "Start Interview"
2. Setup section disappears
3. Interview interface appears
4. Timer starts automatically

### Step 4: AI Formats Problem
1. **AI automatically formats** the pasted problem into beautiful markdown
   - Wait 1-2 seconds while it formats
   - See structured sections, code blocks, and formatted text
   - Professional, readable layout

### Step 5: Listen to Problem
1. Coach reads the **original** problem aloud with symbol conversion
   - "2^n" → "2 to the power of n"
   - "nums[i] <= target" → "nums open bracket i close bracket less than or equal to target"
   - **Reads plain text, not markdown syntax**
2. Follow along in the **Problem Statement** panel (left side)

### Step 6: Write Your Solution
1. Use the **Your Solution** panel (right side)
2. Code editor with monospace font
3. Syntax highlighting ready
4. Visible at all times alongside problem

### Step 7: Practice Speaking
1. Click "🎤 Start Speaking"
2. Allow microphone access when prompted
3. Speak your thoughts out loud
4. System transcribes and sends to coach

### Step 8: Get Feedback
- **Review My Code**: Analyzes code from solution editor
- **Get Hint**: Click for guidance (won't spoil solution)
- **I'm Done**: Triggers complexity discussion

## Voice Commands

The system recognizes these commands when you speak:

- **"Review my code"** / **"Check my solution"** → Code review
- **"Give me a hint"** / **"I'm stuck"** → Get guidance
- **"I'm done"** / **"I'm finished"** → End interview

## Browser Compatibility

### ✅ Fully Supported
- **Chrome** (desktop & mobile)
- **Edge** (desktop)
- **Safari** (desktop, limited mobile support)

### ⚠️ Limited Support
- **Firefox** (no Web Speech API, use keyboard only)
- **Opera** (may work, not tested)

### 📱 Mobile
- Chrome on Android works well
- Safari on iOS has limited voice support

## Troubleshooting

### "Speech recognition not supported"
- **Solution**: Use Chrome or Edge browser
- Firefox doesn't support Web Speech API

### Microphone not working
- Check browser permissions (click lock icon in address bar)
- Allow microphone access for localhost
- Try refreshing the page

### API key not saving
- Check browser console for errors (F12)
- Ensure localStorage is enabled
- Try incognito/private mode to test

### No audio from coach
- Check system volume
- Ensure browser TTS is working (test on other sites)
- Try different browser

### WebSocket connection fails
- Server must be running (`mochi web`)
- Check console for errors
- Firewall may be blocking connection

## Advanced Usage

### Custom Port
```bash
mochi web --port 3000
```
Then visit: http://127.0.0.1:3000

### Custom Host (Network Access)
```bash
mochi web --host 0.0.0.0 --port 8000
```
Then visit from other devices: http://YOUR_IP:8000

**⚠️ Warning**: Only do this on trusted networks!

### Development Mode
```bash
# Run with auto-reload
uvicorn mochi.server:app --reload --host 127.0.0.1 --port 8000
```

## Architecture

### Client-Side (Browser)
- `index.html` - UI structure and styling
- `app.js` - WebSocket, voice I/O, API key management
- Web Speech API - Speech recognition
- Web Speech Synthesis API - Text-to-speech

### Server-Side (Python)
- `server.py` - FastAPI app with WebSocket
- Session management for active interviews
- Conversation history tracking

### Data Flow
1. User speaks → Browser STT → WebSocket → Server
2. Server processes → Generates response → WebSocket → Browser
3. Browser TTS → User hears response

## Security Notes

### ✅ What's Secure
- API keys stored in browser localStorage only
- Keys never transmitted to our server
- OpenAI API calls go directly from browser
- WebSocket uses secure connection (wss://) on HTTPS

### ⚠️ What to Watch
- localStorage is accessible to any script on localhost
- Don't share your screen with API key visible
- Clear localStorage when done: `localStorage.clear()`

### 🔐 Best Practices
- Use API keys with spending limits
- Monitor OpenAI usage dashboard
- Don't commit API keys to version control
- Use environment variables for server secrets

## Differences from CLI Mode

| Feature | Web Interface | CLI Mode |
|---------|---------------|----------|
| Voice Input | Web Speech API | Whisper |
| Voice Output | Browser TTS | pyttsx3 |
| API Key | localStorage | Environment variable |
| Code Editing | Paste in dialog | Live file watching |
| Setup | Just browser | Install dependencies |
| Offline | Requires server | Works offline* |

*CLI requires internet for LLM API calls

## Next Steps

- Try the CLI mode: `mochi start --voice -f solution.py`
- Read `SPEAKING_GUIDE.md` for tips on what to say
- Customize coaching in `settings.toml`
- Practice with different problem types

## Feedback

Found a bug or have a suggestion? Open an issue on GitHub!

Happy interviewing! 🎯
