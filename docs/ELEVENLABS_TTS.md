# Eleven Labs TTS Integration 🔊

## What's New

Mochi now supports **Eleven Labs text-to-speech** for ultra-realistic voice output! This is optional - you can still use the browser's built-in TTS.

## Why Eleven Labs?

### Browser TTS (Default)
- ✅ Free
- ✅ No API key needed
- ✅ Works offline
- ❌ Robotic voice
- ❌ Limited expressiveness

### Eleven Labs TTS (Optional)
- ✅ **Ultra-realistic voice**
- ✅ Natural intonation and pacing
- ✅ Professional quality
- ✅ Multiple voice options
- ❌ Requires API key
- ❌ Costs per character (~$0.18 per 1,000 characters)

## How to Use

### Step 1: Get Your Eleven Labs API Key

1. Go to [elevenlabs.io](https://elevenlabs.io/)
2. Sign up (free tier includes 10,000 characters/month)
3. Go to your profile → API Key
4. Copy your API key

### Step 2: Add to Mochi

```bash
# 1. Start Mochi
mochi web

# 2. Open http://127.0.0.1:8000

# 3. Enter BOTH keys:
#    - OpenAI API key (required)
#    - Eleven Labs API key (optional)

# 4. Click "Save Keys"
```

### Step 3: Enjoy Natural Voice!

When you start an interview:
- If Eleven Labs key is provided → Uses Eleven Labs
- If not provided → Falls back to browser TTS
- If Eleven Labs fails → Auto-fallback to browser TTS

## Voice Configuration

### Default Voice
- **Voice ID**: `EXAVITQu4vr4xnSDxMaL` (Rachel)
- **Model**: `eleven_monolingual_v1`
- **Stability**: 0.5
- **Similarity Boost**: 0.75

### Want a Different Voice?

Edit `mochi/static/app.js`:

```javascript
// Find this line (around line 319):
const voiceId = 'EXAVITQu4vr4xnSDxMaL'; // Default voice (Rachel)

// Replace with your preferred voice ID from:
// https://api.elevenlabs.io/v1/voices
```

**Popular Voice IDs:**
- **Rachel** (Default): `EXAVITQu4vr4xnSDxMaL` - Warm, professional
- **Adam**: `pNInz6obpgDQGcFmaJgB` - Deep, authoritative
- **Bella**: `EXAVITQu4vr4xnSDxMaL` - Friendly, energetic
- **Antoni**: `ErXwobaYiN019PkySvjV` - Smooth, narrative

## Panel Proportions

The interview view now has adjusted proportions:
- **Problem Panel**: 40% (left side)
- **Solution Panel**: 60% (right side)

This matches typical coding environments like LeetCode where you spend more time in the editor.

## Cost Breakdown

### Eleven Labs Pricing
- **Free Tier**: 10,000 characters/month
- **Starter**: $5/month - 30,000 characters
- **Creator**: $22/month - 100,000 characters

### Typical Usage
- Average problem statement: ~500 characters
- Average coach response: ~100 characters
- **20 interviews ≈ 12,000 characters** (within free tier!)

## Technical Details

### How It Works

1. **Text Input** → Clean text (no markdown)
2. **API Call** → Eleven Labs text-to-speech endpoint
3. **Audio Blob** → MP3 audio returned
4. **Audio Playback** → Browser plays audio
5. **Cleanup** → Blob URL revoked after playback

### API Endpoint

```javascript
POST https://api.elevenlabs.io/v1/text-to-speech/{voice_id}

Headers:
  - Accept: audio/mpeg
  - Content-Type: application/json
  - xi-api-key: YOUR_KEY

Body:
{
  "text": "Your text here",
  "model_id": "eleven_monolingual_v1",
  "voice_settings": {
    "stability": 0.5,
    "similarity_boost": 0.75
  }
}
```

### Fallback Logic

```javascript
if (elevenLabsKey) {
    try {
        await speakWithElevenLabs(text);
    } catch (error) {
        // Fallback to browser TTS
        speakWithBrowserTTS(text);
    }
} else {
    speakWithBrowserTTS(text);
}
```

## Security

✅ **API key stored in browser localStorage**
✅ **Never sent to our server**
✅ **Direct browser → Eleven Labs communication**
✅ **No data logged or stored**

## Troubleshooting

### "Eleven Labs TTS failed"
- Check API key is valid
- Check you have credits remaining
- Check browser console for errors
- System will auto-fallback to browser TTS

### No audio playing
- Check system volume
- Check browser audio permissions
- Try refreshing the page

### Voice sounds robotic (using browser TTS)
- Verify Eleven Labs key is entered
- Click "Save Keys" again
- Check browser console for errors

### Rate limit errors
- Free tier: 2 requests/second
- Upgrade plan for higher limits
- System will queue requests automatically

## Files Modified

### mochi/static/index.html
- Added Eleven Labs API key input field
- Updated panel proportions (40% / 60%)
- Updated security note for multiple keys

### mochi/static/app.js
- Added `elevenLabsKey` variable
- Updated `saveApiKeys()` to handle both keys
- Added `speakWithElevenLabs()` function
- Added `speakWithBrowserTTS()` function
- Updated `speakText()` with fallback logic

## Comparison

### Before
```
User: "Start Interview"
→ Browser TTS: "Here is the problem..." (robotic)
```

### After (with Eleven Labs)
```
User: "Start Interview"
→ Eleven Labs: "Here is the problem..." (natural, human-like)
```

## Next Steps

Future enhancements:
- [ ] Voice selection UI (choose from dropdown)
- [ ] Voice settings UI (adjust stability, similarity)
- [ ] Multi-lingual voice support
- [ ] Custom voice cloning (Eleven Labs feature)
- [ ] Audio speed control

---

**Enjoy ultra-realistic voice coaching with Eleven Labs!** 🎯

Get your API key: https://elevenlabs.io/
