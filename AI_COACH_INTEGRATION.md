# AI Coach Integration ✨

## What Changed

The coach now uses **real OpenAI GPT-4o-mini** to respond intelligently instead of canned responses!

## Before (Canned Responses)

**User:** "I'm thinking of using a hash map"
**Coach:** "I understand. Can you explain your reasoning for that approach? What trade-offs are you considering?" *(same every time)*

**User:** "Review my code"
**Coach:** "I see your code. Let me analyze it... One thing to consider: have you thought about edge cases like empty inputs?" *(generic)*

## After (Real AI)

**User:** "I'm thinking of using a hash map"
**Coach:** *(Analyzes your specific problem and context)* "That's a good approach for this problem! How will you handle the case where you need to check if an element already exists? Walk me through your logic."

**User:** "Review my code"
**Coach:** *(Actually reads and analyzes your code)* "I see you're iterating through the array. One issue - your solution has O(n²) time complexity. Can you think of a way to reduce that using the hash map you mentioned?"

## How It Works

### 1. System Prompt (Interview Start)
When you start an interview, the conversation is initialized with:

```
You are a helpful coding interview coach. The candidate is working on this problem:

[YOUR PROBLEM]

Your role:
- Ask clarifying questions about their approach
- Encourage them to think out loud
- Guide them with hints, but NEVER give away the solution
- Help them consider edge cases and complexity
- Be encouraging and supportive
- Keep responses concise (2-3 sentences max)
- Don't use markdown formatting (it will be spoken aloud)
```

### 2. Conversation History
Every interaction is tracked:
- Your spoken/typed messages
- Coach responses
- Code reviews
- Everything builds context

### 3. Direct OpenAI API Calls
**From your browser:**
- Uses your OpenAI API key (already stored)
- Calls GPT-4o-mini for cost-effectiveness
- Temperature: 0.7 (balanced creativity)
- Max tokens: 300 (concise responses)

## Features

### ✅ Contextual Responses
The coach remembers:
- The problem you're solving
- Your previous statements
- Your approach
- Your code (when you ask for review)

### ✅ Natural Coaching
- Asks probing questions
- Guides without revealing answers
- Encourages edge case thinking
- Helps with complexity analysis

### ✅ Code Review
When you click "Review My Code":
1. Sends your actual code to GPT-4o-mini
2. Gets specific feedback on YOUR code
3. Points out bugs, inefficiencies, edge cases
4. Suggests improvements

### ✅ Hints
When you click "Get Hint":
1. Analyzes where you're stuck
2. Gives gentle nudges
3. Doesn't reveal the solution
4. Tailored to your current approach

### ✅ Complexity Discussion
When you click "I'm Done":
1. Automatically asks about Big-O
2. Listens to your answer
3. Provides feedback on your analysis
4. Helps you understand trade-offs

## API Costs

### GPT-4o-mini Pricing
- **Input**: $0.150 per 1M tokens (~$0.00015 per 1K)
- **Output**: $0.600 per 1M tokens (~$0.0006 per 1K)

### Typical Interview Session
- Problem: ~500 tokens
- 10 exchanges: ~3,000 tokens total
- **Cost: ~$0.001 per interview** (about 1/10 of a penny!)

### Example Calculation
```
Problem setup: 500 tokens = $0.00008
User messages (10): 1,000 tokens = $0.00015
Coach responses (10): 1,500 tokens = $0.0009
Total: ~$0.0011 per interview
```

**100 practice interviews = ~$0.11** (eleven cents!)

## Configuration

### Model: gpt-4o-mini
- Fast responses
- Cost-effective
- Great for coaching
- Concise output

### Temperature: 0.7
- Balanced between consistency and creativity
- Not too robotic, not too random
- Good for conversational coaching

### Max Tokens: 300
- Keeps responses concise
- Perfect for spoken output
- ~2-3 sentences typically
- Reduces cost

## How to Use

### 1. Speak Your Thoughts
- Click "Start Speaking"
- Say: "I'm thinking of using a two-pointer approach"
- Coach responds with context-aware guidance

### 2. Review Code
- Write code in solution editor
- Click "Review My Code"
- Coach analyzes YOUR specific code
- Points out issues and improvements

### 3. Get Hints
- Click "Get Hint"
- Coach gives tailored hint based on:
  - The problem
  - Your previous statements
  - Where you seem stuck

### 4. Finish Interview
- Click "I'm Done"
- Coach asks about complexity
- You explain Big-O
- Coach provides feedback

## Technical Details

### Conversation Flow
```javascript
conversationHistory = [
    { role: 'system', content: 'Coaching instructions + problem' },
    { role: 'user', content: 'I think I should use a hash map' },
    { role: 'assistant', content: 'Good idea! How will you...' },
    { role: 'user', content: 'I would iterate once and...' },
    { role: 'assistant', content: 'That works! Consider...' },
    ...
]
```

### API Call Structure
```javascript
fetch('https://api.openai.com/v1/chat/completions', {
    method: 'POST',
    headers: {
        'Authorization': `Bearer ${apiKey}`,
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        model: 'gpt-4o-mini',
        messages: conversationHistory,
        temperature: 0.7,
        max_tokens: 300
    })
})
```

### Response Handling
1. Get AI response
2. Add to conversation history
3. Display in chat
4. Speak using Eleven Labs/browser TTS

## Error Handling

### If OpenAI API Fails
```javascript
catch (error) {
    console.error('Error getting coach response:', error);
    displayCoachMessage("I'm having trouble responding right now.
                         Please continue with your approach.");
}
```

- Shows fallback message
- You can continue practicing
- Check console for error details

### Common Issues

**401 Unauthorized**
- Invalid OpenAI API key
- Re-enter and save key

**429 Rate Limit**
- Too many requests
- Free tier: 3 requests/minute
- Wait a moment, try again

**Network Error**
- Check internet connection
- Check firewall/VPN
- Try again

## Files Modified

### mochi/static/app.js
- Added `conversationHistory` array
- Added system prompt initialization
- Replaced `sendToCoach()` with real OpenAI API call
- Updated `reviewCode()` to send actual code
- Updated `getHint()` for contextual hints
- Updated `finishInterview()` to ask about complexity

## Coaching Philosophy

The AI coach is designed to:

1. **Never give the solution** - System prompt enforces this
2. **Guide with questions** - Socratic method
3. **Encourage thinking out loud** - Core skill being practiced
4. **Consider edge cases** - Interview best practice
5. **Analyze complexity** - Essential interview skill
6. **Be supportive** - Reduce anxiety, build confidence

## Example Session

**Coach:** *"Here is the problem..."* (reads problem)

**You:** "Okay, I'm thinking this is a two-sum problem, so I could use a hash map"

**Coach:** "That's a solid approach! Can you walk me through how you'd use the hash map? What would you store as keys and values?"

**You:** "I'd store the number as the key and the index as the value"

**Coach:** "Good thinking! And as you iterate, what would you check for in the hash map?"

**You:** "I'd check if target minus current number exists in the map"

**Coach:** "Exactly! That's the key insight. Have you considered what happens if there's no valid pair?"

**You:** *(writes code)* "Review my code"

**Coach:** "I see your solution. You're iterating through the array and checking the hash map - that's correct! One thing: you should check if the complement exists before accessing it to avoid errors. Otherwise, looks good!"

**You:** "I'm done"

**Coach:** "Great work! Now let's discuss complexity. What's the time complexity of your solution, and why?"

## Summary

✅ **Real AI coaching** - Not canned responses
✅ **Contextual feedback** - Remembers everything
✅ **Code-specific reviews** - Analyzes YOUR code
✅ **Cost-effective** - ~$0.001 per interview
✅ **Conversational** - Natural back-and-forth
✅ **Educational** - Guides without revealing

**The coach is now a real AI tutor!** 🎯
