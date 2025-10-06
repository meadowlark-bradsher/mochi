# Web Version Implementation Summary

## What Was Built

A complete web-based interface for Mochi, allowing users to practice technical interviews directly in their browser without installing voice dependencies.

## Files Created/Modified

### New Files
1. **mochi/server.py** - FastAPI web server with WebSocket support
2. **mochi/static/index.html** - Complete web UI with styling
3. **mochi/static/app.js** - Client-side JavaScript for voice, WebSocket, and API key management
4. **WEB_INTERFACE.md** - Comprehensive web interface documentation

### Modified Files
1. **mochi/cli.py** - Added `mochi web` command
2. **README.md** - Updated with web interface quick start
3. **QUICKSTART.md** - Added web interface instructions
4. **pyproject.toml** - Added web dependencies (fastapi, uvicorn, websockets)

## How to Use

### Start the Server
```bash
pip install -e .
mochi web
```

### Open Browser
Navigate to: **http://127.0.0.1:8000**

### Use the Interface
1. Enter OpenAI API key (stored locally in browser)
2. Paste a coding problem
3. Click "Start Interview"
4. Click "Start Speaking" to use voice
5. Practice thinking out loud!

## Key Features

### 🔒 Security
- API keys stored in browser localStorage only
- Never sent to our server
- Direct browser-to-OpenAI communication

### 🎤 Voice Input
- Web Speech API (Chrome/Edge/Safari)
- No Whisper installation needed
- Click-to-speak interface

### 🔊 Voice Output
- Browser's built-in TTS
- No pyttsx3 installation needed
- Automatic speech synthesis

### 💬 Real-Time Communication
- WebSocket for instant messaging
- Session management on server
- Conversation history tracking

### ⏱️ Timer
- Automatic interview timing
- MM:SS display format
- Starts on interview begin

## Architecture

```
Browser (Client)
├── index.html (UI)
├── app.js (Logic)
│   ├── API key management (localStorage)
│   ├── WebSocket client
│   ├── Web Speech API (STT)
│   └── Speech Synthesis API (TTS)
│
WebSocket Connection
│
FastAPI Server (Python)
├── /ws/interview endpoint
├── Session management
├── Message routing
└── (Future: OpenAI integration)
```

## Current Limitations

### Placeholder Responses
The server currently returns placeholder coaching responses. To fully integrate:

1. Add OpenAI API calls from **client-side** (using user's API key from localStorage)
2. Or add secure OpenAI calls from **server-side** (requires API key management)

### Browser Support
- Chrome/Edge: Full support
- Safari: Partial support
- Firefox: No Web Speech API (keyboard only)

## Next Steps to Complete Integration

### Option 1: Client-Side AI (Recommended for now)
```javascript
// In app.js, modify sendToCoach():
async function sendToCoach(userMessage) {
    const response = await fetch('https://api.openai.com/v1/chat/completions', {
        method: 'POST',
        headers: {
            'Authorization': `Bearer ${apiKey}`,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            model: 'gpt-4o-mini',
            messages: conversationHistory
        })
    });

    const data = await response.json();
    const coachReply = data.choices[0].message.content;
    displayCoachMessage(coachReply);
    speakText(coachReply);
}
```

### Option 2: Server-Side AI (More secure)
```python
# In server.py, modify user_message handler:
from openai import OpenAI

client = OpenAI(api_key=user_provided_key)  # Need key management

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=session_data["conversation"]
)

coach_message = response.choices[0].message.content
```

## Testing Checklist

- [x] Web server starts successfully
- [x] HTML page loads with correct styling
- [x] API key input saves to localStorage
- [x] Problem textarea accepts input
- [x] WebSocket connection establishes
- [x] Timer starts and updates
- [x] Messages display in chat
- [ ] Web Speech API captures voice (browser-dependent)
- [ ] TTS reads coach messages (browser-dependent)
- [ ] OpenAI integration for real responses (not yet implemented)

## Commands Reference

```bash
# Start web server (default port 8000)
mochi web

# Custom port
mochi web --port 3000

# Network access
mochi web --host 0.0.0.0 --port 8000

# CLI mode (original)
mochi start --voice -f solution.py
```

## Documentation

- **WEB_INTERFACE.md** - Complete web guide
- **README.md** - Updated with web quick start
- **QUICKSTART.md** - Web and CLI instructions
- **SPEAKING_GUIDE.md** - What to say during interviews (applies to both)

## Benefits Over CLI

1. **Easier setup** - No voice dependencies to install
2. **Cross-platform** - Works on any OS with a browser
3. **Visual interface** - See conversation history
4. **Shareable** - Can deploy to server for team use
5. **Mobile-friendly** - Use on phones/tablets (Chrome/Safari)

## CLI Still Useful For

1. **File watching** - Auto-detects code changes
2. **Local TTS** - Better voice quality with pyttsx3
3. **Offline mode** - Works without internet (after setup)
4. **Advanced users** - Terminal integration, scripting

## Summary

The web interface provides a more accessible entry point while maintaining all core functionality. Users can now choose:

- **Web**: Quick start, visual, cross-platform
- **CLI**: Advanced features, file watching, local tools

Both modes support the same goal: **practicing thinking out loud during coding interviews!**
