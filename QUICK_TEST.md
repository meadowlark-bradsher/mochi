# Quick Test Guide 🧪

## Test the New Split View Interface

### 1. Start the Server
```bash
mochi web
```

### 2. Open Browser
Navigate to: **http://127.0.0.1:8000**

### 3. Setup
1. **API Key**: Enter your OpenAI key (sk-...)
2. Click "Save"

### 4. Test Problem with Symbols
Paste this problem to test symbol conversion:

```
Two Sum Problem

Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- nums[i] != nums[j] when i != j
- Only one valid answer exists

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: nums[0] + nums[1] == 9, so we return [0, 1].
```

### 5. Start Interview
Click "Start Interview"

### 6. What to Expect

**✅ AI Formats Problem (1-2 seconds):**
Watch the problem transform into beautiful markdown:
- Headings for sections (Problem, Examples, Constraints)
- Bold text for important terms
- Code formatting for variables like `nums[i]`
- Lists for constraints
- Professional layout

**✅ Coach Reads Problem Aloud:**
Listen for symbol conversions (reads ORIGINAL text, not markdown):
- "10 to the power of 4" (not "10^4")
- "nums open bracket i close bracket" (not "nums[i]")
- "not equal to" (not "!=")
- "equals" (not "==")
- **No markdown syntax spoken!** (no "asterisk asterisk")

**✅ Split View Appears:**
- **Left Panel**: Problem Statement (beautifully formatted with markdown!)
- **Right Panel**: Your Solution (empty editor with placeholder)

**✅ Timer Starts:**
Top left shows: 00:00 (and counting)

### 7. Test the Workflow

**A. Write Some Code:**
In the right panel (Your Solution), type:
```python
def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
```

**B. Click "Review My Code":**
- Should send your code to coach
- Coach analyzes it (currently placeholder response)

**C. Click "Start Speaking" (if Chrome/Edge):**
- Allow microphone
- Say: "I'm using a hash map approach"
- Should transcribe and display

**D. Click "I'm Done":**
- Should trigger complexity questions

### 8. Verify Features

| Feature | Test | Expected Result |
|---------|------|-----------------|
| AI formatting | Start interview | Problem transforms to markdown (1-2s) |
| Problem visible | Start interview | Left panel shows formatted problem |
| Solution editor | Type code | Right panel accepts input |
| Symbol reading | Listen to coach | Hears "to the power of" not "caret" |
| No markdown in speech | Listen to coach | No "asterisk asterisk" spoken |
| Code review | Click button | Uses editor content, no prompt |
| Split view | Resize window | Panels stay side-by-side (or stack on mobile) |
| Timer | Wait 1 minute | Shows 01:00 |

### 9. Mobile Test (Optional)

Open on phone (Chrome on Android works best):
1. Should see stacked layout (vertical)
2. Problem on top, solution below
3. Voice should work with "Start Speaking"

### 10. Symbol Conversion Test

To specifically test symbol conversion, paste:
```
Power of Two

Given n, return true if n == 2^x where x >= 0

Constraints: -2^31 <= n <= 2^31 - 1
```

Listen for:
- "2 to the power of x"
- "2 to the power of 31 minus 1"

## Troubleshooting

**Problem not reading aloud?**
- Check browser console (F12)
- Ensure browser supports Speech Synthesis
- Check system volume

**Split view not showing?**
- Refresh page (Ctrl+R)
- Check browser width (needs > 768px for side-by-side)

**Code review not working?**
- Make sure you have code in solution editor
- Check WebSocket connection (status indicator)

**Symbols not converting?**
- This is a speech feature only
- Text display shows original symbols
- Listen to audio for converted speech

## Success Criteria

✅ **AI formats problem** into beautiful markdown (1-2 seconds)
✅ Coach reads **original text** aloud with symbol conversion
✅ **No markdown spoken** (no "asterisk asterisk")
✅ Problem statement visible on left at all times with formatting
✅ Solution editor visible on right at all times
✅ Can write code while seeing problem
✅ Review button uses solution editor content
✅ Timer tracks elapsed time
✅ Chat shows conversation history

---

**Everything working?** You're ready to practice! 🎯

Try a few LeetCode problems:
1. Two Sum (Easy)
2. Valid Parentheses (Easy)
3. Longest Substring Without Repeating Characters (Medium)

Practice thinking out loud while you code!
