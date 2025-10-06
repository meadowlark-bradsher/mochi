# Split View Implementation Summary

## Changes Made

I've updated the web interface with the following improvements:

### 1. ✅ Coach Reads Problem Aloud with Symbol Conversion

The coach now reads the problem statement out loud when you start an interview, with intelligent symbol-to-speech conversion:

**Symbol Conversions:**
- `^` → "to the power of"
- `*` → "times"
- `/` → "divided by"
- `+` → "plus"
- `<=` → "less than or equal to"
- `>=` → "greater than or equal to"
- `!=` → "not equal to"
- `==` → "equals"
- `<` → "less than"
- `>` → "greater than"
- `%` → "percent"
- `[` → "open bracket"
- `]` → "close bracket"
- `{` → "open brace"
- `}` → "close brace"

**Example:**
- Input: "Given array nums where nums[i] <= 2^31 - 1"
- Spoken: "Given array nums where nums open bracket i close bracket less than or equal to 2 to the power of 31 minus 1"

### 2. ✅ Problem Statement Always Visible

The problem is now displayed in a dedicated **Problem Statement** panel on the left side that remains visible throughout the interview. This matches real interview conditions where you can always reference the problem.

### 3. ✅ Solution Editor Panel

Added a **Your Solution** panel on the right side where you can write your code in real-time:

- **Monospace font** (Monaco, Menlo, Courier New)
- **Always visible** alongside problem
- **Auto-used for reviews** - Click "Review My Code" to analyze
- **Syntax-ready** for future highlighting

### 4. ✅ Split View Layout

The interview screen now shows:

```
┌─────────────────────────────────────────────────────────┐
│  Timer: 00:00                      Status: Connected    │
├────────────────────┬────────────────────────────────────┤
│  Problem Statement │  Your Solution                     │
│  ─────────────────│  ──────────────────────────────    │
│                    │                                    │
│  [Problem text]    │  def twoSum(nums, target):         │
│                    │      # Your code here              │
│                    │      pass                          │
│                    │                                    │
├────────────────────┴────────────────────────────────────┤
│  Chat Box (Coach & User Messages)                       │
├─────────────────────────────────────────────────────────┤
│  [🎤 Start Speaking] [Review Code] [Get Hint] [Done]   │
└─────────────────────────────────────────────────────────┘
```

### 5. Mobile Responsive

On mobile/tablet (< 768px width), the split view becomes vertical:
```
Problem Statement
─────────────────
Your Solution
─────────────────
Chat Box
Controls
```

## New User Flow

1. **Enter API key** and paste problem → Click "Start Interview"
2. **Coach reads problem aloud** with symbol conversion
3. **Follow along** in Problem Statement panel (left)
4. **Write solution** in Your Solution panel (right)
5. **Think out loud** while coding (click "Start Speaking")
6. **Review code** automatically uses solution editor
7. **Finish** when done for complexity discussion

## Files Modified

### mochi/static/app.js
- Added `symbolsToSpeech()` function for mathematical symbol conversion
- Updated `startInterview()` to display problem and read it aloud
- Modified `reviewCode()` to use solution editor instead of prompt

### mochi/static/index.html
- Added split-container with problem-panel and solution-panel
- Added CSS for grid layout (50/50 split)
- Added responsive design for mobile
- Added problem-display div and solution-editor textarea

### WEB_INTERFACE.md
- Updated documentation with new workflow
- Added symbol conversion examples
- Updated feature list

## Testing

You can test this by:

```bash
# 1. Start server
mochi web

# 2. Open http://127.0.0.1:8000

# 3. Enter API key and paste:
Given an array of integers nums and an integer target,
return indices of two numbers such that they add up to target.

Example: nums = [2,7,11,15], target = 9
Output: [0,1] because nums[0] + nums[1] == 9

# 4. Click "Start Interview"
# 5. Listen to coach read it (with symbols converted)
# 6. See problem on left, write solution on right
```

## Benefits

✅ **Hear problems like a real interviewer** - Symbol conversion makes it natural
✅ **No context switching** - Problem and solution side-by-side
✅ **More realistic** - Mimics actual interview setup
✅ **Better workflow** - Write code while seeing problem
✅ **Automatic reviews** - Uses your solution editor directly

## Next Steps (Future)

- [ ] Add syntax highlighting to solution editor
- [ ] Add auto-save for solution (localStorage)
- [ ] Add "copy to clipboard" for solution
- [ ] Support multiple programming languages
- [ ] Add keyboard shortcuts (Cmd+Enter to review)
