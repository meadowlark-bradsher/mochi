# Quick Debug: Is Eleven Labs Working? 🔍

## 1-Minute Check

### Step 1: Open Browser Console
Press **F12** or **Right-click → Inspect** → **Console** tab

### Step 2: Check When You Save Keys
After clicking "Save Keys", you should see:
```
✅ Eleven Labs key saved: abc123def4...
```

If you see:
```
❌ No Eleven Labs key provided
```
→ You didn't enter a key in the field!

### Step 3: Check When Coach Speaks
When interview starts and coach speaks, you should see:
```
✅ Using Eleven Labs TTS
✅ Eleven Labs: Making API call...
✅ Eleven Labs API response status: 200
✅ Eleven Labs: Received audio blob, size: 45231 bytes
✅ Eleven Labs: Audio playback started
```

If you see:
```
❌ No Eleven Labs key, using browser TTS
```
→ Key wasn't saved properly. Refresh and try again.

If you see:
```
❌ Eleven Labs API error: 401
```
→ Invalid API key. Check your key at elevenlabs.io

## Quick Fixes

### Problem: Browser TTS voice (robotic), not Eleven Labs
1. Open console (F12)
2. Type: `localStorage.getItem('mochi_elevenlabs_key')`
3. If it shows `null` → Key not saved
4. Re-enter key and click "Save Keys"
5. Refresh page

### Problem: Key is saved but still using browser TTS
1. Check console for errors
2. Look for "401" or "403" → Invalid key
3. Look for "429" → Rate limit (wait 1 minute)
4. Look for "fallback" → Check the error above it

### Problem: Hearing nothing at all
1. Check system volume
2. Check browser console for errors
3. Check Network tab for blocked requests
4. Try browser TTS first (remove Eleven Labs key temporarily)

## Test Your API Key Directly

Paste this in browser console:
```javascript
const key = localStorage.getItem('mochi_elevenlabs_key');
console.log('Key exists:', !!key);
console.log('Key preview:', key ? key.substring(0, 10) + '...' : 'NONE');

// Test API call
fetch('https://api.elevenlabs.io/v1/text-to-speech/EXAVITQu4vr4xnSDxMaL', {
    method: 'POST',
    headers: {
        'Accept': 'audio/mpeg',
        'Content-Type': 'application/json',
        'xi-api-key': key
    },
    body: JSON.stringify({
        text: 'Testing Eleven Labs',
        model_id: 'eleven_monolingual_v1',
        voice_settings: { stability: 0.5, similarity_boost: 0.75 }
    })
})
.then(r => {
    console.log('Status:', r.status);
    if (r.ok) {
        console.log('✅ Eleven Labs API working!');
    } else {
        r.text().then(t => console.log('Error:', t));
    }
})
.catch(e => console.log('Network error:', e));
```

**Expected output:**
```
Key exists: true
Key preview: abc123def4...
Status: 200
✅ Eleven Labs API working!
```

## Common Console Messages

| Message | Meaning | Action |
|---------|---------|--------|
| `Using Eleven Labs TTS` | ✅ Key found, attempting to use Eleven Labs | None - working! |
| `No Eleven Labs key, using browser TTS` | ❌ No key in localStorage | Enter and save key |
| `API response status: 200` | ✅ Eleven Labs responded successfully | None - working! |
| `API response status: 401` | ❌ Unauthorized (bad key) | Check key is correct |
| `API response status: 429` | ❌ Too many requests | Wait 1 minute |
| `Audio blob size: 0 bytes` | ❌ Empty response | Check account credits |
| `Audio playback started` | ✅ Playing Eleven Labs voice | None - working! |
| `failed, falling back to browser TTS` | ⚠️ Error occurred, using backup | Check error above it |

## Still Not Working?

### Check Your Eleven Labs Account
1. Go to https://elevenlabs.io
2. Log in
3. Check "Usage" - do you have credits?
4. Check "Profile" → "API Key" - is it correct?
5. Try generating a new API key

### Check Browser
1. Try incognito/private mode
2. Try different browser (Chrome works best)
3. Clear site data: F12 → Application → Clear storage
4. Refresh and re-enter keys

### Check Network
1. F12 → Network tab
2. Start interview
3. Look for request to `elevenlabs.io`
4. Click it → Check response
5. If blocked/failed → Check firewall/VPN

## Success Indicators

You know it's working when:
- ✅ Console shows "Using Eleven Labs TTS"
- ✅ Console shows status 200
- ✅ Console shows blob size > 0
- ✅ Voice sounds natural (not robotic)
- ✅ Clear pronunciation and intonation

## Comparison

### Browser TTS (What you DON'T want)
- Robotic, flat voice
- Console: "No Eleven Labs key, using browser TTS"
- Fast response
- Works offline

### Eleven Labs TTS (What you WANT)
- Natural, human-like voice
- Console: "Using Eleven Labs TTS" → 200 → "Audio playback started"
- 1-2 second delay (normal)
- Requires internet

---

**If you see "Using Eleven Labs TTS" and status 200 in console, it IS working!**

The voice quality difference should be immediately obvious. 🎧
