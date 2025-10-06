# Mochi Quick Start Guide 🎤

**Practice thinking out loud during coding interviews!**

Get your first voice-based mock interview running in 2 minutes.

## Web Interface (Recommended)

### Step 1: Install

```bash
pip install -e .
```

### Step 2: Start Web Server

```bash
mochi web
```

### Step 3: Open Browser

Navigate to **http://127.0.0.1:8000**

### Step 4: Start Interview

1. Enter your OpenAI API key (sk-...)
   - 🔒 Stored locally in your browser only
   - Never sent to our server
2. Paste a coding problem from LeetCode/HackerRank
3. Click "Start Interview"
4. Allow microphone access when prompted
5. Start speaking!

**Pro tip:** Use headphones to avoid feedback!

---

## CLI Mode (Advanced)

### Step 1: Install

```bash
pip install -e .
```

### Step 2: Set API Key

```bash
# If you have an OpenAI API key (recommended)
export OPENAI_API_KEY='sk-...'

# OR if you prefer Anthropic
export ANTHROPIC_API_KEY='sk-ant-...'
# and edit settings.toml to set engine="anthropic"
```

### Step 3: Start an Interview

```bash
# Create a solution file
touch solution.py

# Start Mochi (voice mode is default)
mochi start --voice -f solution.py
```

**When prompted, paste a problem from LeetCode, HackerRank, or anywhere!**

## What Happens Next (Web Interface)

1. **Problem displayed** - Read the problem you pasted
2. **🔊 Coach greets you** - Hear welcome message via browser TTS
3. **🎤 Click "Start Speaking"** - Browser asks for mic permission
4. **🎤 You speak your thoughts** - "I'm thinking of using a hash map because..."
5. **Click "Review My Code"** - Paste your code and get AI feedback
6. **🎤 Say "I'm done"** - Triggers complexity discussion

## What Happens Next (CLI Mode)

1. **Paste the problem** - Copy from LeetCode and paste when prompted
2. **🔊 Coach reads it** - Hear the problem statement
3. **🎤 You speak your clarifying questions** - "Can the array be empty?"
4. **🎤 Discuss your approach out loud** - "I'm thinking of using a hash map because..."
5. **⌨️ Edit your solution file** - Code while continuing to explain
6. **🎤 Say "review my code"** - Get AI feedback
7. **🎤 Say "I'm done"** - Triggers complexity discussion

## Voice Commands

Just speak naturally - the system recognizes:

- **"Review my code"** or **"Check my solution"** - AI reviews your code
- **"Give me a hint"** or **"I'm stuck"** - Get guidance (won't spoil!)
- **"I'm done"** - Triggers Big-O complexity questions
- **"Quit"** - End interview

## Why Voice?

The hardest part of coding interviews isn't solving problems - it's **explaining your thinking while you code**. Most people:

- Go silent when they start coding ❌
- Forget to verbalize their approach ❌
- Don't explain trade-offs ❌

**Mochi forces you to practice this critical skill!**

## Tips for Success

✅ **Use headphones** - Prevents echo and feedback
✅ **Think out loud from the start** - "Okay, so I need to find two numbers..."
✅ **Explain while you type** - "I'm creating a hash map here to store..."
✅ **Ask for reviews** - Say "review my code" periodically
✅ **Verbalize trade-offs** - "This is O(n²) but I could optimize with..."

## Keyboard-Only Mode

If your mic isn't working or you want to ease into it:

```bash
# Omit --voice to type instead of speak
mochi start --no-voice -f solution.py
```

But remember: **the whole point is practicing speaking out loud!**

## Advanced Options

```bash
# Override helpfulness for this session
mochi start --voice -f solution.py --helpfulness gentle
# Options: gentle, balanced, insistent

# Use API-based TTS instead of local
mochi start --voice -f solution.py --tts-mode api
# Options: local, api
```

## Next Steps

- **Read `SPEAKING_GUIDE.md`** for detailed tips on what to say during interviews
- Adjust coach personality in `settings.toml`
- Try different helpfulness levels to match your skill

## Troubleshooting

**"OPENAI_API_KEY not set"**
- Run `export OPENAI_API_KEY='your-key'` in your terminal

**Mic not working?**
- Check system microphone permissions
- Speak clearly at normal volume
- Use a quiet environment

**Coach speaks too fast?**
- Edit `mochi/io/tts.py` line 20: change `rate=180` to `rate=150`

**Want to use Anthropic instead?**
- Edit `settings.toml`, set `engine = "anthropic"`
- Set `export ANTHROPIC_API_KEY='your-key'`

## Example Session (Web Interface)

1. Open http://127.0.0.1:8000 in your browser
2. Enter your OpenAI API key and save it
3. Paste the Two Sum problem from LeetCode
4. Click "Start Interview"
5. Timer starts: 00:00
6. Coach says: "Let's begin. I see your problem. Take a moment to read it, then start thinking out loud."
7. Click "Start Speaking" and say: "I'm thinking of using a hash map..."
8. Coach responds: "I understand. Can you explain your reasoning for that approach?"
9. Click "Review My Code", paste your solution
10. Coach analyzes: "I see your code. Let me analyze it..."
11. Say "I'm done"
12. Coach asks: "Great work! Let's discuss complexity. What's the time complexity?"

## Example Session (CLI Mode)

```
$ mochi start --voice -f solution.py

🎯 Mochi Mock Interview

Paste your problem statement:
[You paste the Two Sum problem from LeetCode]

┌─ Problem Statement ─────────────────────────────────────┐
│ Given an array of integers nums and an integer target...│
└─────────────────────────────────────────────────────────┘

🔊 Coach: "The problem is: Given an array of integers nums..."
🔊 Coach: "Take a moment to read it. Any questions?"

[00:15] 🎤 You: "Can I use the same element twice?"

🔊 Coach: "Good question! No, you can't use the same element twice."

[01:23] 🎤 You: "I'm thinking of using a hash map approach..."

[You start coding in solution.py while explaining]

[05:47] 🎤 You: "Review my code"

🔊 Coach: "I see you're using a hash map. One thing to consider..."

[08:15] 🎤 You: "I'm done"

🔊 Coach: "Great! What's the time and space complexity?"
```

---

**Ready to practice speaking out loud?**

```bash
mochi start --voice -f solution.py
```

Happy interviewing! 🎯
