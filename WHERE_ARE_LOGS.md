# Where to Find Debug Logs 🔍

## ⚠️ Important: Logs Are In Your BROWSER, Not Server Terminal!

The debug logs I added are **JavaScript console logs** that appear in your **browser developer tools**, NOT in the terminal where the server is running.

## How to See the Logs

### Step 1: Open Browser Developer Tools

**Method 1: Keyboard Shortcut**
- **Windows/Linux**: Press `F12` or `Ctrl+Shift+I`
- **Mac**: Press `Cmd+Option+I`

**Method 2: Right-click Menu**
- Right-click anywhere on the page
- Select **"Inspect"** or **"Inspect Element"**

**Method 3: Browser Menu**
- Chrome: Menu (⋮) → More Tools → Developer Tools
- Firefox: Menu (≡) → More Tools → Web Developer Tools
- Safari: Develop → Show Web Inspector (enable Develop menu in preferences first)

### Step 2: Go to Console Tab

In the developer tools panel, click the **"Console"** tab at the top.

### Step 3: Clear Old Logs (Optional)

Click the 🚫 clear icon or press `Ctrl+L` to clear old messages.

### Step 4: Start Your Interview

Now when you:
1. Click "Save Keys"
2. Click "Test Voice"
3. Start Interview

You'll see all the debug logs appear in the Console tab!

## What You Should See

### When Saving Keys:
```javascript
Eleven Labs key saved: abc123def4...
```

### When Testing Voice:
```javascript
Testing Eleven Labs API with key: abc123def4...
Making test API call to: https://api.elevenlabs.io/...
Test API response status: 200
Test API success! Audio blob size: 48432
Test audio playing...
```

### When Starting Interview:
```javascript
Reading problem, text length: 1523 chars
Using Eleven Labs: true
Eleven Labs: Making API call for text length: 1523 characters
Eleven Labs API response status: 200
Eleven Labs: Received audio blob, size: 67234 bytes
Eleven Labs: Audio playback started
Eleven Labs: Audio playback completed
```

### When Coach Speaks (WebSocket):
```javascript
Received coach message: Let's begin. I see your problem...
Calling speakText with Eleven Labs key: true
Using Eleven Labs TTS
Eleven Labs: Making API call for text length: 89 characters
...
```

## Server Logs vs Browser Logs

### Server Terminal (What You Showed)
```
INFO:     Started server process [62068]
INFO:     127.0.0.1:58243 - "GET / HTTP/1.1" 200 OK
INFO:     ('127.0.0.1', 58245) - "WebSocket /ws/interview" [accepted]
Client 4381327536 disconnected
```
→ This shows HTTP requests and WebSocket connections
→ **No JavaScript logs here!**

### Browser Console (What You Need)
```javascript
Eleven Labs key saved: abc123def4...
Using Eleven Labs: true
Eleven Labs: Making API call...
Eleven Labs API response status: 200
Audio playback started
```
→ This shows what's happening with Eleven Labs
→ **This is where all the debug info is!**

## Quick Test

1. **Open http://127.0.0.1:8000**
2. **Press F12** (opens developer tools)
3. **Click "Console" tab**
4. **Type in console:** `console.log('Hello from browser!')`
5. **Press Enter**

You should see:
```
Hello from browser!
```

If you see that, you're in the right place! Now try saving keys or starting an interview.

## Screenshots Guide

### Chrome Developer Tools:
```
┌─────────────────────────────────────────┐
│  Address Bar: http://127.0.0.1:8000     │
├─────────────────────────────────────────┤
│                                         │
│  Your Mochi Web Interface               │
│                                         │
├─────────────────────────────────────────┤
│  Developer Tools Panel (F12)            │
│  ┌────────────────────────────────────┐ │
│  │ Elements  Console  Sources  Network│ │
│  ├────────────────────────────────────┤ │
│  │ > Eleven Labs key saved: abc...    │ │
│  │ > Using Eleven Labs: true          │ │
│  │ > Eleven Labs: Making API call...  │ │
│  │ > Status: 200                      │ │
│  └────────────────────────────────────┘ │
└─────────────────────────────────────────┘
```

## Common Issues

### Issue: "I don't see Console tab"
**Solution:**
- Make sure developer tools are open (F12)
- Look for tabs at the top: Elements, Console, Network, etc.
- Click "Console"

### Issue: "Console is empty"
**Solution:**
- Make sure you're on the right page (http://127.0.0.1:8000)
- Try clicking "Save Keys" - you should see a log
- If nothing appears, try refreshing the page

### Issue: "I see errors in red"
**Good!** That's what we want to see - errors tell us what's wrong

### Issue: "Console keeps disappearing"
**Solution:**
- Click the dock icon (⋮) in dev tools
- Select "Dock to bottom" or "Dock to right"
- This keeps it open

## Mobile/Tablet

If you're on mobile:
- **Chrome on Android**: Menu → More tools → Developer tools (not available on all devices)
- **Safari on iOS**: Connect to Mac and use Safari's Web Inspector
- **Best option**: Use desktop browser for debugging

## Alternative: Network Tab

If you want to see Eleven Labs API calls:

1. **F12** → **Network** tab
2. **Start interview**
3. Look for request to: `api.elevenlabs.io`
4. Click on it to see request/response details

This shows:
- Request URL
- Headers (including API key)
- Response status
- Audio data size

## Summary

**Server Terminal:**
- Shows HTTP requests, WebSocket connections
- Does NOT show JavaScript logs
- ❌ Not where you look for debugging

**Browser Console (F12):**
- Shows all JavaScript console.log() output
- Shows Eleven Labs API calls
- Shows errors and warnings
- ✅ This is where all the debug info is!

---

**Press F12 right now and go to the Console tab!** 🔍

Then start an interview and watch the logs appear in real-time.
