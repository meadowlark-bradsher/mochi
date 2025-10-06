# AI Problem Formatting Feature 🎨

## What's New

The web interface now uses your OpenAI API key to **automatically format pasted problems** into beautiful, readable markdown - while keeping the speech output clean and natural.

## How It Works

### 1. You Paste Raw Problem Text

Example raw paste from LeetCode:
```
Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Constraints:
2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Only one valid answer exists.
```

### 2. AI Formats It Beautifully

The problem is sent to OpenAI (using your API key) with instructions to format it as clean markdown:

```markdown
## Two Sum

Given an array of integers `nums` and an integer `target`, return **indices** of the two numbers such that they add up to `target`.

You may assume that each input would have **exactly one solution**, and you may not use the same element twice.

You can return the answer in any order.

### Example 1

**Input:** `nums = [2,7,11,15]`, `target = 9`
**Output:** `[0,1]`
**Explanation:** Because `nums[0] + nums[1] == 9`, we return `[0, 1]`.

### Constraints

- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Only one valid answer exists
```

### 3. Rendered in Your Browser

The markdown is rendered with proper styling:
- **Headings** for sections
- **Bold text** for important terms
- `Code formatting` for variables and arrays
- **Lists** for constraints
- **Code blocks** for examples

### 4. TTS Reads Original Text

The **text-to-speech still uses the original pasted text** with symbol conversion:
- "2 to the power of 4" (not "2^4")
- "nums open bracket i close bracket" (not "nums[i]")
- "less than or equal to" (not "<=")

**No markdown syntax is spoken!** (No "asterisk asterisk" or "backtick")

## Benefits

### 👁️ Visual: Beautiful Markdown
- Professional formatting
- Easy to read sections
- Clear examples and constraints
- Code-styled variables

### 👂 Audio: Natural Speech
- Clean spoken problem statement
- Mathematical symbols converted properly
- No markdown artifacts in speech

### 🎯 Best of Both Worlds
- **See:** Well-formatted problem with markdown
- **Hear:** Natural spoken problem with symbol conversion

## Technical Details

### AI Formatting Prompt

```javascript
You are a formatting assistant. Convert the given coding problem
into clean, readable markdown format.

Rules:
- Use headings (##) for sections like "Problem", "Examples", "Constraints"
- Use **bold** for important terms
- Use code blocks (```) for code examples
- Use inline code (`) for variable names, arrays, etc.
- Use lists for constraints and examples
- Make it easy to read and well-structured
- DO NOT solve the problem or add explanations
- Only format what's given
```

### Model Used
- **gpt-4o-mini** for cost-effective formatting
- Temperature: 0.3 (consistent formatting)
- Max tokens: 1000 (sufficient for most problems)

### Cost
- Typical problem: ~500 tokens input + output
- Cost: ~$0.0003 per problem (less than a penny!)
- Uses your personal API key

### Fallback
If the API call fails:
- Falls back to displaying original text
- Still works, just without markdown formatting
- Error logged to console

## Example Comparison

### Before (Plain Text)
```
Two Sum
Given array nums and integer target, return indices...
Example: Input nums = [2,7] target = 9 Output [0,1]
Constraints: 2 <= nums.length <= 10^4
```

### After (AI-Formatted Markdown)
```markdown
## Two Sum

Given an array `nums` and an integer `target`, return **indices**...

### Example

**Input:** `nums = [2,7]`, `target = 9`
**Output:** `[0,1]`

### Constraints

- `2 <= nums.length <= 10^4`
```

**Much easier to read!**

## Usage

Just paste your problem as usual:

```bash
# 1. Start server
mochi web

# 2. Open http://127.0.0.1:8000

# 3. Enter API key

# 4. Paste problem (raw text is fine!)

# 5. Click "Start Interview"

# 6. Watch it format beautifully ✨
```

The formatting happens automatically - you don't need to do anything!

## Files Modified

### mochi/static/index.html
- Added `marked.js` library for markdown rendering
- Added CSS for markdown elements (h1, h2, code, lists, etc.)

### mochi/static/app.js
- Added `formatProblemWithAI()` function
- OpenAI API call with formatting prompt
- Renders markdown with `marked.parse()`
- TTS still uses original text (no markdown)

### WEB_INTERFACE.md
- Updated documentation with AI formatting feature
- Explained visual vs audio separation

## Privacy & Security

✅ **Your API key stays in your browser**
✅ **Problem sent only to OpenAI, not our server**
✅ **No data stored or logged**
✅ **Standard OpenAI API call from browser**

## Future Enhancements

Possible improvements:
- [ ] Syntax highlighting in code blocks
- [ ] Custom formatting preferences
- [ ] Cache formatted problems (localStorage)
- [ ] Support for different markdown renderers
- [ ] Dark mode for problem display

---

**Enjoy beautifully formatted problems while hearing natural speech!** 🎯
