# Panel Proportions & Eleven Labs TTS Update 🎨🔊

## Changes Made

### 1. ✅ Adjusted Panel Proportions (40% / 60%)

The interview view now matches typical coding environments:

**Before:** 50% / 50% split
```
┌──────────────┬──────────────┐
│   Problem    │   Solution   │
│     50%      │     50%      │
└──────────────┴──────────────┘
```

**After:** 40% / 60% split (like LeetCode!)
```
┌─────────┬──────────────────┐
│ Problem │    Solution      │
│   40%   │      60%         │
└─────────┴──────────────────┘
```

**Why?** You spend more time in the code editor, so it gets more space!

### 2. ✅ Added Eleven Labs TTS Integration

Now you can choose between two TTS options:

#### Browser TTS (Default)
- ✅ Free
- ✅ No API key needed
- ✅ Works offline
- ❌ Robotic voice

#### Eleven Labs (Optional)
- ✅ **Ultra-realistic voice**
- ✅ Natural intonation
- ✅ Professional quality
- ✅ Free tier: 10,000 characters/month
- ✅ Auto-fallback if it fails

## How to Use Eleven Labs

### Get API Key
1. Go to [elevenlabs.io](https://elevenlabs.io/)
2. Sign up (free tier available)
3. Go to Profile → API Key
4. Copy your key

### Add to Mochi
```bash
mochi web
# Open http://127.0.0.1:8000

# Enter both keys:
# - OpenAI API key (required)
# - Eleven Labs API key (optional)

# Click "Save Keys"
```

### That's It!
- Coach will use Eleven Labs voice automatically
- If Eleven Labs fails → Auto-fallback to browser TTS
- No Eleven Labs key → Uses browser TTS

## Example Comparison

### Browser TTS
> "Given an array of integers nums and an integer target..."
>
> 🤖 *Robotic, flat intonation*

### Eleven Labs
> "Given an array of integers nums and an integer target..."
>
> 👤 *Natural, human-like, clear pronunciation*

## Cost Breakdown

### Free Tier (Eleven Labs)
- 10,000 characters/month
- ~20 full interview sessions
- Plenty for practice!

### Paid Plans
- **Starter**: $5/month - 30,000 chars
- **Creator**: $22/month - 100,000 chars

### Typical Usage Per Interview
- Problem reading: ~500 characters
- Coach responses: ~1,000 characters
- **Total per session: ~1,500 characters**

## Files Modified

### mochi/static/index.html
- Adjusted grid: `grid-template-columns: 40% 60%`
- Added Eleven Labs API key input
- Updated "Step 1" to "API Keys Setup"
- Added helper text for optional TTS
- Updated security note

### mochi/static/app.js
- Added `elevenLabsKey` variable
- Updated `saveApiKeys()` to store both keys
- Added `speakWithElevenLabs()` function
- Added `speakWithBrowserTTS()` function
- Updated `speakText()` with smart fallback logic

### Documentation
- **ELEVENLABS_TTS.md** - Complete guide
- **WEB_INTERFACE.md** - Updated features
- **PANEL_AND_TTS_UPDATE.md** - This summary

## Technical Details

### Eleven Labs API Call
```javascript
POST https://api.elevenlabs.io/v1/text-to-speech/{voice_id}

Headers:
  xi-api-key: YOUR_KEY
  Content-Type: application/json
  Accept: audio/mpeg

Body:
{
  "text": "Your text here",
  "model_id": "eleven_monolingual_v1",
  "voice_settings": {
    "stability": 0.5,
    "similarity_boost": 0.75
  }
}

Response: MP3 audio blob
```

### Fallback Logic
```javascript
async function speakText(text) {
    if (elevenLabsKey) {
        try {
            await speakWithElevenLabs(text);
        } catch (error) {
            // Auto-fallback to browser
            speakWithBrowserTTS(text);
        }
    } else {
        speakWithBrowserTTS(text);
    }
}
```

### Default Voice
- **Name**: Rachel
- **Voice ID**: `EXAVITQu4vr4xnSDxMaL`
- **Type**: Warm, professional female voice

Want a different voice? Edit the `voiceId` in `app.js` line 319!

## Panel Proportions Details

### CSS Change
```css
/* Before */
.split-container {
    grid-template-columns: 1fr 1fr;  /* 50/50 */
}

/* After */
.split-container {
    grid-template-columns: 40% 60%;  /* 40/60 */
}
```

### Responsive Behavior
- **Desktop (> 768px)**: 40% problem / 60% solution
- **Mobile (< 768px)**: Stacked vertically

## Benefits

### Better Proportions
✅ More editor space (like LeetCode/HackerRank)
✅ Still see full problem statement
✅ Better coding ergonomics
✅ Mobile responsive

### Eleven Labs TTS
✅ Natural, human-like voice
✅ Clear pronunciation
✅ Professional quality
✅ Optional - use browser TTS if you prefer
✅ Auto-fallback if it fails
✅ Free tier for practice

## Try It Now!

```bash
# 1. Start server
mochi web

# 2. Open http://127.0.0.1:8000

# 3. Enter keys:
#    - OpenAI: sk-...
#    - Eleven Labs: (optional)

# 4. Paste a problem and start!

# 5. Listen to the natural voice read it! 🎧
```

## What's Next?

Future enhancements:
- [ ] Voice selection UI (choose from dropdown)
- [ ] Adjustable panel proportions (drag to resize)
- [ ] Voice speed control
- [ ] Multi-lingual voices
- [ ] Custom voice cloning

---

**Enjoy the improved layout and ultra-realistic voice!** 🎯

Panel proportions: ✅ 40% / 60%
Eleven Labs TTS: ✅ Integrated with fallback
