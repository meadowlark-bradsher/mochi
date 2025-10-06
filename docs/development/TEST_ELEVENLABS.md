# Test Eleven Labs Integration 🧪

## New "Test Voice" Button Added!

I've added a **Test Voice** button next to the Eleven Labs API key input. This will immediately test if your API key works and play a sample audio.

## How to Use

### Step 1: Enter Your Eleven Labs Key
1. Go to http://127.0.0.1:8000
2. Paste your Eleven Labs API key in the "Eleven Labs API Key" field
3. **DON'T click "Save Keys" yet**

### Step 2: Click "Test Voice" Button
1. Click the green **"Test Voice"** button
2. Watch the message below the input field

### Step 3: Check Results

#### ✅ Success (You'll see):
```
✅ API key works! Playing test audio...
```

Then you'll hear:
> "Hello! This is a test of Eleven Labs text to speech."

After it finishes:
```
✅ Eleven Labs working! You should have heard a test message.
```

**This means:**
- ✅ Your API key is valid
- ✅ Eleven Labs API is working
- ✅ Audio playback works in your browser
- ✅ You're using Eleven Labs credits (check your account)

#### ❌ Common Errors:

**Error: "Please enter an Eleven Labs API key first"**
→ You didn't enter anything in the field

**Error: "API Error 401"**
```
❌ API Error 401: Unauthorized
```
→ **Your API key is invalid**
- Double-check the key at elevenlabs.io
- Make sure you copied the entire key
- Try generating a new key

**Error: "API Error 403"**
```
❌ API Error 403: Forbidden
```
→ **API key doesn't have permission**
- Check if key is active
- Verify account status

**Error: "API Error 429"**
```
❌ API Error 429: Too many requests
```
→ **Rate limit exceeded**
- Wait 1 minute and try again
- Free tier: 2 requests/second

**Error: "Test failed: Failed to fetch"**
```
❌ Test failed: Failed to fetch
```
→ **Network/CORS issue**
- Check internet connection
- Check if VPN/firewall is blocking
- Try disabling browser extensions

**Error: "Audio playback failed"**
```
✅ API key works! Playing test audio...
❌ Audio playback failed. Check browser console.
```
→ **API worked, but audio won't play**
- Check browser audio permissions
- Check system volume
- Try a different browser

## What This Tests

The test button:
1. ✅ Makes a real API call to Eleven Labs
2. ✅ Uses your actual API key
3. ✅ **WILL use credits from your account** (about 50 characters = ~$0.0001)
4. ✅ Plays actual audio in your browser
5. ✅ Shows exact error if something fails

## After Test Succeeds

Once you see:
```
✅ Eleven Labs working! You should have heard a test message.
```

**Then:**
1. Click "Save Keys" button (top)
2. Now your key is saved for interviews
3. Start an interview to use it automatically

## Troubleshooting with Console

### Open Console (F12)

When you click "Test Voice", you should see:

**Success:**
```
Testing Eleven Labs API with key: abc123def4...
Making test API call to: https://api.elevenlabs.io/v1/text-to-speech/...
Test API response status: 200
Test API success! Audio blob size: 48432
Test audio playing...
```

**Failure (401):**
```
Testing Eleven Labs API with key: abc123def4...
Making test API call to: https://api.elevenlabs.io/v1/text-to-speech/...
Test API response status: 401
Test API error response: {"detail":"Unauthorized"}
```

## Quick Diagnosis

| What You See | What It Means | What To Do |
|--------------|---------------|------------|
| ✅ Playing test audio | Working perfectly | Click "Save Keys" |
| ❌ API Error 401 | Bad key | Get correct key from elevenlabs.io |
| ❌ API Error 429 | Too many tests | Wait 1 minute |
| ❌ Failed to fetch | Network issue | Check internet/firewall |
| ❌ Audio playback failed | Browser issue | Check volume/permissions |

## Verify Credits Are Being Used

After a successful test:

1. Go to https://elevenlabs.io
2. Log into your account
3. Check **Usage** or **Credits**
4. You should see:
   - Character count increased by ~50
   - One API request logged
   - Recent timestamp

**If credits aren't decreasing:**
- You saw ✅ but weren't actually calling the API
- Check browser Network tab (F12 → Network)
- Look for request to `api.elevenlabs.io`
- If missing → JavaScript error (check Console)

## Network Tab Verification

To be 100% sure the API is being called:

1. F12 → **Network** tab
2. Clear network log
3. Click **"Test Voice"** button
4. Look for request to: `text-to-speech/EXAVITQu4vr4xnSDxMaL`

**You should see:**
- **Request URL**: `https://api.elevenlabs.io/v1/text-to-speech/EXAVITQu4vr4xnSDxMaL`
- **Method**: POST
- **Status**: 200
- **Type**: audio/mpeg
- **Size**: ~50 KB

Click on it to see:
- **Headers** → Request Headers → `xi-api-key: YOUR_KEY`
- **Response** → Audio data (binary)

## Still Not Working?

### Copy All Diagnostic Info:

1. **Console output** (F12 → Console)
2. **Network request details** (F12 → Network → Click the API call)
3. **Error message** from the page
4. **Your Eleven Labs account status** (credits remaining?)

### Common Issues:

**Issue: Key is correct but always 401**
- Copy key again (might have invisible characters)
- Try generating a brand new key
- Check account isn't suspended

**Issue: Works in test but not in interview**
- Key not saved to localStorage
- Click "Save Keys" after successful test
- Refresh page and check console logs

**Issue: Hear browser TTS not Eleven Labs**
- Test passed but key wasn't saved
- Click "Save Keys" button
- Verify in console: `localStorage.getItem('mochi_elevenlabs_key')`

## Summary

The **Test Voice** button:
- ✅ Immediately tests your API key
- ✅ Uses real Eleven Labs API
- ✅ Shows exact errors
- ✅ Plays sample audio
- ✅ Verifies everything works

**If test succeeds → Your setup is correct!**
**If test fails → You'll see exactly why!**

No more guessing! 🎯
