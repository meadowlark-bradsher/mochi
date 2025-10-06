# 🎤 START HERE - Mochi Interview Coach

**Practice thinking out loud during coding interviews!**

## What is Mochi?

Mochi is an **AI interview coach** that helps you practice the hardest part of technical interviews: **explaining your thinking while you code**.

Most people go silent when they start coding. Real interviewers want to hear your thought process! Mochi uses voice to force you to speak out loud.

## Getting Started in 3 Steps

### 1. Install

```bash
pip install -e .
```

### 2. Set API Key

```bash
export OPENAI_API_KEY='your-key-here'
```

### 3. Start an Interview

```bash
# Create a file for your solution
touch solution.py

# Start Mochi
mochi start --voice -f solution.py
```

**When prompted, paste a problem from LeetCode/HackerRank/etc.**

Put on headphones and start speaking!

## What to Expect

1. **Paste the problem** - Copy from LeetCode and paste when prompted
2. **🔊 Coach reads it** - Hear the problem statement (first 500 chars)
3. **🎤 Ask questions** - "Can the array be empty?"
4. **🎤 Explain approach** - "I'm thinking of using a hash map..."
5. **⌨️ Code in your file** while continuing to speak
6. **🎤 Say "review my code"** - Coach analyzes your solution
7. **🎤 Say "I'm done"** - Coach asks about Big-O complexity

## Voice Commands (Just Speak Naturally)

- **"Review my code"** - Get feedback on your solution
- **"Give me a hint"** - Get guidance (won't spoil!)
- **"I'm done"** - Triggers complexity discussion
- **"Quit"** - End interview

## Important Tips

✅ **Use headphones** - Prevents feedback
✅ **Speak from the start** - Don't go silent!
✅ **Explain while coding** - This is the whole point
✅ **Say "review my code"** periodically

## The New Workflow

No pre-made problem files needed! Just:
1. Find any LeetCode problem
2. Copy the description
3. Paste it into Mochi
4. Start coding and speaking!

## Example Session

```
$ mochi start --voice -f solution.py

Paste your problem statement:
[You paste: "Given an array of integers nums and an integer..."]

🔊 Coach: "The problem is: Given an array of integers nums..."
🔊 Coach: "Take a moment to read through it. Any questions?"

🎤 You: "Can I modify the input array?"

🔊 Coach: "Good question. Typically you can, unless specified otherwise."

🎤 You: "Okay, I'm thinking of sorting the array first..."

[You start coding while explaining]

🎤 You: "Review my code"

🔊 Coach: "I see you're iterating through... one issue I notice is..."

🎤 You: "I'm done"

🔊 Coach: "Great! What's the time and space complexity?"
```

## Timer

A timer starts automatically when the interview begins. Your elapsed time shows with each interaction:

```
[05:23] You: "I think I have a solution..."
```

---

Questions? Check `SPEAKING_GUIDE.md` for detailed tips on what to say during interviews.
