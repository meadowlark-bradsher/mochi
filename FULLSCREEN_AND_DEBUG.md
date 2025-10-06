# Full Screen Layout & Eleven Labs Debug Guide

## Changes Made

### 1. ✅ Full Screen Layout (No More Mobile View!)

**Before:** Constrained to 900px max-width with rounded container
```
┌────────────────────────────────────────────────┐
│                                                │
│     ┌──────────────────────────┐              │
│     │  Content (max 900px)     │              │
│     │  Wasted space on sides   │              │
│     └──────────────────────────┘              │
│                                                │
└────────────────────────────────────────────────┘
```

**After:** Full screen width, professional layout
```
┌────────────────────────────────────────────────┐
│  Content spans full width with proper padding │
│  Maximum readability and workspace            │
│  No wasted screen real estate                 │
└────────────────────────────────────────────────┘
```

### Changes to CSS:
```css
/* Removed */
max-width: 900px;
border-radius: 20px;
box-shadow: 0 20px 60px rgba(0,0,0,0.3);
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

/* Added */
width: 100%;
min-height: 100vh;
padding: 40px 60px;
background: white;
```

### 2. ✅ Eleven Labs Debugging Tools Added

Added comprehensive logging to debug TTS issues:

**Console Logs:**
- ✅ Key save confirmation with partial key display
- ✅ Which TTS method is being used (Eleven Labs vs Browser)
- ✅ API call status and response
- ✅ Audio blob size
- ✅ Playback status (started/completed/error)

## How to Debug Eleven Labs TTS

### Step 1: Check Browser Console

Open Developer Tools (F12 or Right-click → Inspect) and go to the Console tab.

### Step 2: Save Your Keys

When you click "Save Keys", you should see:
```
Eleven Labs key saved: abc123def4...
```

OR if no Eleven Labs key:
```
No Eleven Labs key provided
```

### Step 3: Start Interview

When the coach speaks, check console:

**If Using Eleven Labs:**
```
Using Eleven Labs TTS
Eleven Labs: Making API call...
Eleven Labs API response status: 200
Eleven Labs: Received audio blob, size: 45231 bytes
Eleven Labs: Audio playback started
Eleven Labs: Audio playback completed
```

**If Using Browser TTS:**
```
No Eleven Labs key, using browser TTS
```

**If Eleven Labs Failed:**
```
Using Eleven Labs TTS
Eleven Labs: Making API call...
Eleven Labs API response status: 401
Eleven Labs API error: {"detail":"Unauthorized"}
Eleven Labs TTS failed, falling back to browser TTS: Error: Eleven Labs API error: 401
```

### Common Issues & Solutions

#### Issue 1: "No Eleven Labs key, using browser TTS"
**Cause:** Key not saved or empty
**Solution:**
1. Make sure you entered the key
2. Click "Save Keys" button
3. Refresh the page
4. Check localStorage in console: `localStorage.getItem('mochi_elevenlabs_key')`

#### Issue 2: "Eleven Labs API error: 401"
**Cause:** Invalid API key
**Solution:**
1. Verify your key at elevenlabs.io
2. Copy the correct key
3. Paste and save again
4. Refresh the page

#### Issue 3: "Eleven Labs API error: 429"
**Cause:** Rate limit exceeded
**Solution:**
- Free tier: 2 requests/second
- Wait a few seconds
- Upgrade plan if needed

#### Issue 4: Audio blob size is 0 bytes
**Cause:** API returned empty response
**Solution:**
1. Check network tab for the actual API response
2. Verify account has credits remaining
3. Check API key permissions

#### Issue 5: Hearing browser TTS instead of Eleven Labs
**Cause:** Fallback activated due to error
**Solution:**
1. Check console for error messages
2. Look for "failed, falling back" message
3. Fix the underlying error from logs

## Manual Verification

### Check localStorage
```javascript
// In browser console:
localStorage.getItem('mochi_elevenlabs_key')
// Should show your key
```

### Test Eleven Labs API Directly
```javascript
// In browser console:
const key = localStorage.getItem('mochi_elevenlabs_key');
fetch('https://api.elevenlabs.io/v1/text-to-speech/EXAVITQu4vr4xnSDxMaL', {
    method: 'POST',
    headers: {
        'Accept': 'audio/mpeg',
        'Content-Type': 'application/json',
        'xi-api-key': key
    },
    body: JSON.stringify({
        text: 'Test message',
        model_id: 'eleven_monolingual_v1',
        voice_settings: {
            stability: 0.5,
            similarity_boost: 0.75
        }
    })
}).then(r => console.log('Response:', r.status));
```

Expected: `Response: 200`

### Clear and Retry
```javascript
// Clear all stored data
localStorage.clear();
// Refresh page and re-enter keys
```

## Eleven Labs API Key Format

Valid key format:
- Usually starts with alphanumeric characters
- About 32 characters long
- Example: `abc123def456ghi789jkl012mno345pq`

**NOT** like OpenAI (doesn't start with `sk-`)

## Full Screen Layout

The app now uses the full screen width:

**Desktop Layout:**
- Full width with 60px padding on sides
- No max-width constraint
- Problem panel: 40% of screen
- Solution panel: 60% of screen

**Mobile Layout (< 768px):**
- Stacked panels (vertical)
- Full width
- Responsive padding

## Files Modified

### mochi/static/index.html
```css
/* Full screen layout */
body {
    background: white;
    margin: 0;
    padding: 0;
}

.container {
    width: 100%;
    min-height: 100vh;
    padding: 40px 60px;
}
```

### mochi/static/app.js
- Added detailed console logging
- Key validation in saveApiKeys()
- API response logging in speakWithElevenLabs()
- Playback status tracking

## Testing Checklist

- [ ] Full screen layout (no constrained container)
- [ ] Console shows "Eleven Labs key saved" when saving
- [ ] Console shows "Using Eleven Labs TTS" when speaking
- [ ] Console shows 200 response status
- [ ] Console shows audio blob size > 0
- [ ] Hear realistic voice (not browser TTS)
- [ ] Check for any error messages in console

## Next Steps

If you're still experiencing issues:

1. **Copy all console output** from when you:
   - Save keys
   - Start interview
   - Hear the voice

2. **Check Network tab** (F12 → Network):
   - Look for request to `elevenlabs.io`
   - Check request headers (should have xi-api-key)
   - Check response (should be audio/mpeg)

3. **Verify your Eleven Labs account:**
   - Go to elevenlabs.io
   - Check credits remaining
   - Verify API key is active

---

**You should now have:**
- ✅ Full screen layout (no mobile view)
- ✅ Comprehensive debugging logs
- ✅ Clear error messages
- ✅ Easy troubleshooting

**Open browser console (F12) and watch the logs!** 🐛
