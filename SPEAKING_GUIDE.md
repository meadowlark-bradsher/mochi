# Speaking During Interviews 🎤

**How to Think Out Loud - Patterns, Tips, and Examples**

## What This Guide Is

This guide teaches you **what to say and how to say it** during coding interviews. 

**Topics covered:**
- Specific phrases and patterns to practice
- Example dialogues showing good communication  
- Common mistakes to avoid
- Tips for verbalizing your thought process

**Prerequisite**: You should already have Mochi installed. If not, see `QUICKSTART.md` first.

---

## Why Speaking Matters

The **hardest part of coding interviews isn't solving the problem** - it's explaining your thinking out loud while you code. 

Most people:
- Get quiet when they start coding
- Forget to explain their approach
- Don't verbalize trade-offs
- Struggle to think and talk simultaneously

**This guide helps you practice speaking patterns that real interviewers want to hear.**

---

## How It Works

1. **Coach speaks the problem** - Listen carefully
2. **You speak your thoughts** - The mic listens automatically
3. **Coach responds verbally** - Just like a real interviewer
4. **You code in your editor** - Keep talking as you code!
5. **Say "run tests"** - Hear the results spoken

## Voice Commands

Just speak naturally. The system recognizes:

- **"run tests"** or **"run the test"** - Execute your solution
- **"give me a hint"** or **"I'm stuck"** - Request guidance
- **"quit"** or **"stop"** - End the interview

## Tips for Success

### Before You Start

- **Use headphones** - Prevents echo/feedback
- **Find a quiet space** - Background noise can interfere
- **Test your mic** - Say a few words to verify it works

### During the Interview

✅ **Think out loud from the start**
```
"Okay, so I need to find two numbers that add to target...
Let me think about the constraints first..."
```

✅ **Explain while you type**
```
"I'm going to create a hash map to store values I've seen.
As I iterate through the array..."
```

✅ **Verbalize trade-offs**
```
"This approach is O(n²) but I could optimize it to O(n)
if I use extra space for a hash table..."
```

✅ **Walk through test cases aloud**
```
"Let me trace through with [2,7,11,15], target 9.
First iteration: i=0, nums[0]=2, I need 7..."
```

❌ **Don't go silent** while coding
❌ **Don't just say "testing"** - explain what you're testing
❌ **Don't skip explaining your approach**

## The Interview Loop

```
1. Listen to problem
   ↓
2. Ask clarifying questions (speak)
   ↓
3. Explain your approach (speak)
   "I'm thinking of using a hash map because..."
   ↓
4. Code while narrating (speak + type)
   "Now I'm checking if the complement exists..."
   ↓
5. Say "run tests"
   ↓
6. Explain failures (speak)
   "The test is failing because I didn't handle..."
   ↓
7. Fix and repeat
```

## Common Patterns to Practice

### Clarifying Questions
```
"Can the array be empty?"
"Can I use the same element twice?"
"What should I return if no solution exists?"
```

### Explaining Approach
```
"The brute force would be O(n²) with nested loops.
But I can optimize by storing complements in a hash map.
This gives me O(1) lookup time..."
```

### Debugging Out Loud
```
"The test failed on [3,3] with target 6.
Let me trace through... oh, I see - I'm comparing
the element with itself. I need to check the index..."
```

### Complexity Analysis
```
"Time complexity is O(n) because I iterate once.
Space complexity is O(n) for the hash map in worst case..."
```

## Troubleshooting

**Mic not picking up voice?**
- Check system preferences → microphone permissions
- Speak clearly and at normal volume
- Try: `python -c "import sounddevice; print(sounddevice.query_devices())"`

**Coach speaks too fast?**
- Edit `mochi/io/tts.py` line 20: change `rate=180` to `rate=150`

**Transcription is wrong?**
- Speak more slowly and clearly
- Pause briefly between thoughts
- The model improves with clearer audio

**Too much echo?**
- Use headphones
- Lower speaker volume
- Move mic away from speakers

## Model Size Options

The default is `base` (fast, good accuracy). You can change in `mochi/io/stt.py` line 21:

- `tiny` - Fastest, less accurate
- `base` - Good balance (default)
- `small` - Better accuracy, slower
- `medium` - Even better, much slower
- `large` - Best accuracy, very slow

## Example Session

```
🎤 COACH: "Let's begin the interview. The problem is Two Sum..."

🎤 YOU: "Okay, let me make sure I understand. I have an array
        and a target, and I need to find two indices where the
        values add up to target. Can I assume there's always a
        valid answer?"

🎤 COACH: "Yes, you can assume exactly one solution exists."

🎤 YOU: "Great. So my first thought is nested loops - check
        every pair. That would be O(n²) time. But I think I
        can do better with a hash map..."

[You start coding in your editor]

🎤 YOU: "I'm creating a dictionary to store values I've seen.
        As I iterate, for each number, I'll check if target minus
        that number exists in my dictionary..."

[You continue coding]

🎤 YOU: "Alright, let me run tests"

🎤 COACH: "All tests passed! Let's discuss complexity..."
```

## Why This Matters

Real interviewers want to hear:
- Your thought process
- How you break down problems
- Trade-offs you consider
- How you debug
- Your communication skills

**Voice mode forces you to develop this habit.**

After 5-10 sessions, talking while coding will feel natural!

---

Ready to practice? Start with:
```bash
mochi start --voice -p examples/problems/two_sum/problem.yaml -f solution.py
```
