# Troubleshooting Voice Issues 🔊

## Problem: Test Works, But Interview Uses Robo-Voice

If the "Test Voice" button works (you hear natural Eleven Labs voice), but during the interview you hear robotic browser TTS, here's what's happening:

## Most Likely Cause: Text Too Long

**Eleven Labs has a 5,000 character limit per request.**

When you read a LeetCode problem with examples and constraints, the text can easily exceed this:

```
"Here is the problem. Given an integer x, return true if x is a palindrome...
Example 1: Input x equals 121, Output true, Explanation 121 reads as 121...
Example 2: Input x equals negative 121, Output false...
Constraints: negative 2 to the power of 31 less than or equal to x..."

= Easily 2,000+ characters with symbol conversion!
```

### Check the Console

**When interview starts, look for:**

✅ **If Using Eleven Labs:**
```
Reading problem, text length: 1523 chars
Using Eleven Labs: true
Eleven Labs: Making API call for text length: 1523 characters
Eleven Labs API response status: 200
Eleven Labs: Audio playback started
```

❌ **If Text Too Long (Falls Back to Browser):**
```
Reading problem, text length: 5847 chars
Using Eleven Labs: true
Eleven Labs: Making API call for text length: 5847 characters
Text too long for Eleven Labs (5000 char limit), using browser TTS
Eleven Labs TTS failed, falling back to browser TTS: Error: Text too long
```

## Solutions

### Solution 1: Use Shorter Problem Statements

When pasting from LeetCode:
- ❌ Don't paste all examples and constraints
- ✅ Paste just the core problem description
- ✅ You can still see the full problem in the left panel

**Before (Too Long):**
```
9. Palindrome Number

Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right...

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121...

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left...

Constraints:
-2^31 <= x <= 2^31 - 1
```

**After (Shorter):**
```
Palindrome Number

Given an integer x, return true if x is a palindrome, and false otherwise.
```

### Solution 2: Remove Symbol Conversion for Long Text

The `symbolsToSpeech()` function expands symbols, making text longer:
- `2^31` → `2 to the power of 31` (19 chars → 23 chars)
- `nums[i]` → `nums open bracket i close bracket` (7 chars → 37 chars!)

This can DOUBLE the text length!

### Solution 3: Skip Problem Reading

If problem is very long, don't have the coach read it:

**Current:**
- Coach reads entire problem (may be too long)
- Falls back to browser TTS

**Alternative:**
- Skip the problem reading
- Just say "Let's begin. What's your approach?"
- You read it yourself from the left panel

## How to Check What's Happening

### Step 1: Open Console (F12)

### Step 2: Start Interview

### Step 3: Look for These Messages

**Scenario A: Working (Eleven Labs)**
```
✅ Using Eleven Labs: true
✅ text length: 1523 chars
✅ Eleven Labs API response status: 200
✅ Audio playback started
```
→ You'll hear natural voice

**Scenario B: Text Too Long (Browser Fallback)**
```
✅ Using Eleven Labs: true
❌ text length: 5847 chars
❌ Text too long for Eleven Labs (5000 char limit)
❌ failed, falling back to browser TTS
```
→ You'll hear robo-voice

**Scenario C: API Key Not Loaded**
```
❌ Using Eleven Labs: false
❌ No Eleven Labs key, using browser TTS
```
→ Key wasn't saved, click "Save Keys" and refresh

## Character Limit Details

### Eleven Labs Limits:
- **Free tier**: 10,000 chars/month total
- **Per request**: 5,000 chars max
- **Our check**: Throws error if > 5,000 chars

### Typical Lengths:
- Short problem: 200-500 chars
- Medium problem: 500-1,500 chars
- Long problem with examples: 2,000-5,000 chars
- **With symbol conversion**: Add 50-100%!

### Example:
```javascript
// Original text
"nums[i] <= 2^31 - 1"  // 19 chars

// After symbolsToSpeech()
"nums open bracket i close bracket less than or equal to 2 to the power of 31 minus 1"  // 86 chars!

// 4.5x longer!
```

## Quick Fixes

### Fix 1: Paste Shorter Problems
```
# Just the problem statement
"Given an integer x, return true if x is a palindrome."
```

### Fix 2: Check Text Length Before Interview
```javascript
// In browser console:
const problem = document.getElementById('problem-input').value;
const symbols = symbolsToSpeech(problem);
const full = "Here is the problem. " + symbols + ". Take a moment...";
console.log('Will speak:', full.length, 'characters');
```

If > 5,000 → Edit your problem paste to be shorter

### Fix 3: Disable Problem Reading (Code Change)

Edit `app.js` around line 294:
```javascript
// Comment out the problem reading
// setTimeout(async () => {
//     const spokenProblem = symbolsToSpeech(problem);
//     const intro = "Here is the problem. " + spokenProblem + "...";
//     await speakText(intro);
// }, 500);

// Just start without reading
displayCoachMessage("Interview started. Read the problem and begin!");
```

## Future Enhancement

We could split long text into chunks:

```javascript
async function speakLongText(text) {
    const maxChars = 4500; // Leave buffer

    if (text.length <= maxChars) {
        await speakText(text);
    } else {
        // Split at sentence boundaries
        const sentences = text.match(/[^.!?]+[.!?]+/g);
        let chunk = '';

        for (const sentence of sentences) {
            if ((chunk + sentence).length > maxChars) {
                await speakText(chunk);
                chunk = sentence;
            } else {
                chunk += sentence;
            }
        }

        if (chunk) await speakText(chunk);
    }
}
```

## Summary

**Why robo-voice during interview:**
1. Problem text (with symbol conversion) > 5,000 chars
2. Eleven Labs throws error
3. Auto-falls back to browser TTS
4. You hear robotic voice

**Solution:**
- Paste shorter problems
- Or disable problem reading
- Or check char count first

**Test button works because:**
- Test message is only 50 chars
- Well under the 5,000 limit
- Always succeeds with Eleven Labs

---

**Check console for "text length" to see if this is your issue!** 📊
