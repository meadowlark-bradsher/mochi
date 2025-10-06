// Mochi Interview Coach - Client-side JavaScript

let ws = null;
let apiKey = null;
let elevenLabsKey = null;
let timerInterval = null;
let startTime = null;
let isListening = false;
let recognition = null;
let problemText = '';

// Convert mathematical symbols to spoken text
function symbolsToSpeech(text) {
    let spoken = text;

    // Mathematical operators
    spoken = spoken.replace(/\^/g, ' to the power of ');
    spoken = spoken.replace(/\*/g, ' times ');
    spoken = spoken.replace(/\//g, ' divided by ');
    spoken = spoken.replace(/\+/g, ' plus ');
    spoken = spoken.replace(/->/g, ' arrow ');
    spoken = spoken.replace(/<=/g, ' less than or equal to ');
    spoken = spoken.replace(/>=/g, ' greater than or equal to ');
    spoken = spoken.replace(/!=/g, ' not equal to ');
    spoken = spoken.replace(/==/g, ' equals ');
    spoken = spoken.replace(/=/g, ' equals ');
    spoken = spoken.replace(/</g, ' less than ');
    spoken = spoken.replace(/>/g, ' greater than ');

    // Common symbols
    spoken = spoken.replace(/%/g, ' percent ');
    spoken = spoken.replace(/&/g, ' and ');
    spoken = spoken.replace(/\|/g, ' or ');
    spoken = spoken.replace(/#/g, ' number ');
    spoken = spoken.replace(/@/g, ' at ');

    // Array/bracket notation
    spoken = spoken.replace(/\[/g, ' open bracket ');
    spoken = spoken.replace(/\]/g, ' close bracket ');
    spoken = spoken.replace(/\{/g, ' open brace ');
    spoken = spoken.replace(/\}/g, ' close brace ');

    // Clean up extra spaces
    spoken = spoken.replace(/\s+/g, ' ').trim();

    return spoken;
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    // Load API keys from localStorage
    apiKey = localStorage.getItem('mochi_api_key');
    elevenLabsKey = localStorage.getItem('mochi_elevenlabs_key');

    console.log('Page loaded. API keys check:');
    console.log('  OpenAI key exists:', !!apiKey);
    console.log('  Eleven Labs key exists:', !!elevenLabsKey);
    if (elevenLabsKey) {
        console.log('  Eleven Labs key preview:', elevenLabsKey.substring(0, 10) + '...');
    }

    if (apiKey) {
        document.getElementById('api-key-input').value = apiKey;
        enableStartButton();
    }

    if (elevenLabsKey) {
        document.getElementById('elevenlabs-key-input').value = elevenLabsKey;
    }

    // Initialize Web Speech API if available
    if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        recognition = new SpeechRecognition();
        recognition.continuous = false;
        recognition.interimResults = false;
        recognition.lang = 'en-US';

        recognition.onresult = (event) => {
            const transcript = event.results[0][0].transcript;
            handleUserSpeech(transcript);
        };

        recognition.onerror = (event) => {
            console.error('Speech recognition error:', event.error);
            stopListening();
        };

        recognition.onend = () => {
            stopListening();
        };
    }
});

async function testElevenLabs() {
    const elevenLabsInput = document.getElementById('elevenlabs-key-input');
    const testKey = elevenLabsInput.value.trim();
    const resultDiv = document.getElementById('elevenlabs-test-result');

    if (!testKey) {
        resultDiv.innerHTML = '<span style="color: red;">❌ Please enter an Eleven Labs API key first</span>';
        return;
    }

    resultDiv.innerHTML = '<span style="color: blue;">🔄 Testing API key...</span>';
    console.log('Testing Eleven Labs API with key:', testKey.substring(0, 10) + '...');

    try {
        const voiceId = 'EXAVITQu4vr4xnSDxMaL';
        const url = `https://api.elevenlabs.io/v1/text-to-speech/${voiceId}`;

        console.log('Making test API call to:', url);

        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Accept': 'audio/mpeg',
                'Content-Type': 'application/json',
                'xi-api-key': testKey
            },
            body: JSON.stringify({
                text: 'Hello! This is a test of Eleven Labs text to speech.',
                model_id: 'eleven_monolingual_v1',
                voice_settings: {
                    stability: 0.5,
                    similarity_boost: 0.75
                }
            })
        });

        console.log('Test API response status:', response.status);

        if (!response.ok) {
            const errorText = await response.text();
            console.error('Test API error response:', errorText);
            resultDiv.innerHTML = `<span style="color: red;">❌ API Error ${response.status}: ${errorText}</span>`;
            return;
        }

        const audioBlob = await response.blob();
        console.log('Test API success! Audio blob size:', audioBlob.size);

        resultDiv.innerHTML = '<span style="color: green;">✅ API key works! Playing test audio...</span>';

        const audioUrl = URL.createObjectURL(audioBlob);
        const audio = new Audio(audioUrl);

        audio.onended = () => {
            URL.revokeObjectURL(audioUrl);
            resultDiv.innerHTML = '<span style="color: green;">✅ Eleven Labs working! You should have heard a test message.</span>';
        };

        audio.onerror = (error) => {
            console.error('Audio playback error:', error);
            resultDiv.innerHTML = '<span style="color: red;">❌ Audio playback failed. Check browser console.</span>';
        };

        await audio.play();
        console.log('Test audio playing...');

    } catch (error) {
        console.error('Test failed:', error);
        resultDiv.innerHTML = `<span style="color: red;">❌ Test failed: ${error.message}</span>`;
    }
}

function saveApiKeys() {
    const openaiInput = document.getElementById('api-key-input');
    const elevenLabsInput = document.getElementById('elevenlabs-key-input');

    apiKey = openaiInput.value.trim();
    elevenLabsKey = elevenLabsInput.value.trim();

    if (!apiKey.startsWith('sk-')) {
        alert('Please enter a valid OpenAI API key (starts with sk-)');
        return;
    }

    // Store in localStorage
    localStorage.setItem('mochi_api_key', apiKey);

    if (elevenLabsKey) {
        localStorage.setItem('mochi_elevenlabs_key', elevenLabsKey);
        console.log('Eleven Labs key saved:', elevenLabsKey.substring(0, 10) + '...');
    } else {
        console.log('No Eleven Labs key provided');
    }

    // Enable start button
    enableStartButton();

    const message = elevenLabsKey
        ? 'API keys saved securely in your browser! Eleven Labs TTS enabled.'
        : 'OpenAI API key saved! Using browser TTS (add Eleven Labs key for better voice).';

    alert(message);
}

function enableStartButton() {
    const problemInput = document.getElementById('problem-input');
    const startBtn = document.getElementById('start-btn');

    if (apiKey && problemInput.value.trim()) {
        startBtn.disabled = false;
    } else {
        startBtn.disabled = true;
    }
}

// Update start button state when problem is typed
document.getElementById('problem-input')?.addEventListener('input', enableStartButton);

async function formatProblemWithAI(problemText) {
    try {
        const response = await fetch('https://api.openai.com/v1/chat/completions', {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${apiKey}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                model: 'gpt-4o-mini',
                messages: [
                    {
                        role: 'system',
                        content: `You are a formatting assistant. Convert the given coding problem into clean, readable markdown format.

Rules:
- Use headings (##) for sections like "Problem", "Examples", "Constraints"
- Use **bold** for important terms
- Use code blocks (\`\`\`) for code examples
- Use inline code (\`) for variable names, arrays, etc.
- Use lists for constraints and examples
- Make it easy to read and well-structured
- DO NOT solve the problem or add explanations
- Only format what's given`
                    },
                    {
                        role: 'user',
                        content: problemText
                    }
                ],
                temperature: 0.3,
                max_tokens: 1000
            })
        });

        const data = await response.json();
        return data.choices[0].message.content;
    } catch (error) {
        console.error('Error formatting problem:', error);
        return problemText; // Fallback to original text
    }
}

async function startInterview() {
    const problemInput = document.getElementById('problem-input');
    const problem = problemInput.value.trim();

    if (!apiKey) {
        alert('Please save your API key first!');
        return;
    }

    if (!problem) {
        alert('Please paste a coding problem!');
        return;
    }

    // Store problem text
    problemText = problem;

    // Hide setup, show interview
    document.getElementById('setup-section').style.display = 'none';
    document.getElementById('interview-section').classList.add('active');

    // Show loading message
    const problemDisplay = document.getElementById('problem-display');
    problemDisplay.innerHTML = '<p style="color: #666; font-style: italic;">Formatting problem with AI...</p>';

    // Format problem with AI and render as markdown
    const formattedProblem = await formatProblemWithAI(problem);
    problemDisplay.innerHTML = marked.parse(formattedProblem);

    // Connect WebSocket
    connectWebSocket();

    // Start timer
    startTimer();

    // Initialize conversation with system prompt
    conversationHistory = [
        {
            role: 'system',
            content: `You are a helpful coding interview coach. The candidate is working on this problem:

${problem}

Your role:
- Ask clarifying questions about their approach
- Encourage them to think out loud
- Guide them with hints, but NEVER give away the solution
- Help them consider edge cases and complexity
- Be encouraging and supportive
- Keep responses concise (2-3 sentences max)
- Don't use markdown formatting in responses (it will be spoken aloud)

The candidate will explain their thinking. Coach them through the problem-solving process.`
        }
    ];

    // Send problem to server and trigger coach to read it
    ws.onopen = () => {
        updateStatus('connected');
        ws.send(JSON.stringify({
            type: 'start',
            problem: problem
        }));

        // Coach reads the problem aloud with symbol conversion
        // Use ORIGINAL problem text (not markdown) for speech
        setTimeout(async () => {
            const spokenProblem = symbolsToSpeech(problem);
            const intro = "Here is the problem. " + spokenProblem + ". Take a moment to read through it, then start thinking out loud about your approach.";

            displayCoachMessage("Reading the problem aloud...");
            console.log('Reading problem, text length:', intro.length, 'chars');
            console.log('Using Eleven Labs:', !!elevenLabsKey);
            await speakText(intro);
        }, 500);
    };
}

function connectWebSocket() {
    const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
    const wsUrl = `${protocol}//${window.location.host}/ws/interview`;

    ws = new WebSocket(wsUrl);

    ws.onmessage = (event) => {
        const data = JSON.parse(event.data);

        if (data.type === 'coach') {
            console.log('Received coach message:', data.message);
            displayCoachMessage(data.message);
            console.log('Calling speakText with Eleven Labs key:', !!elevenLabsKey);
            speakText(data.message);
        }
    };

    ws.onerror = (error) => {
        console.error('WebSocket error:', error);
        updateStatus('disconnected');
    };

    ws.onclose = () => {
        updateStatus('disconnected');
    };
}

function updateStatus(status) {
    const statusEl = document.getElementById('status');
    if (status === 'connected') {
        statusEl.className = 'status connected';
        statusEl.innerHTML = '<span>●</span> Connected';
    } else {
        statusEl.className = 'status disconnected';
        statusEl.innerHTML = '<span>●</span> Disconnected';
    }
}

function startTimer() {
    startTime = Date.now();
    timerInterval = setInterval(updateTimer, 1000);
}

function updateTimer() {
    const elapsed = Math.floor((Date.now() - startTime) / 1000);
    const minutes = Math.floor(elapsed / 60);
    const seconds = elapsed % 60;

    document.getElementById('timer').textContent =
        `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
}

function displayCoachMessage(text) {
    const chatBox = document.getElementById('chat-box');
    const messageDiv = document.createElement('div');
    messageDiv.className = 'message coach';
    messageDiv.innerHTML = `
        <div class="label">Coach</div>
        <div>${text}</div>
    `;
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function displayUserMessage(text) {
    const chatBox = document.getElementById('chat-box');
    const messageDiv = document.createElement('div');
    messageDiv.className = 'message user';
    messageDiv.innerHTML = `
        <div class="label">You</div>
        <div>${text}</div>
    `;
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}

async function speakText(text) {
    // Use Eleven Labs if key is available, otherwise use browser TTS
    if (elevenLabsKey) {
        console.log('Using Eleven Labs TTS');
        try {
            await speakWithElevenLabs(text);
        } catch (error) {
            console.error('Eleven Labs TTS failed, falling back to browser TTS:', error);
            speakWithBrowserTTS(text);
        }
    } else {
        console.log('No Eleven Labs key, using browser TTS');
        speakWithBrowserTTS(text);
    }
}

async function speakWithElevenLabs(text) {
    console.log('Eleven Labs: Making API call for text length:', text.length, 'characters');

    // Check text length - Eleven Labs has limits
    if (text.length > 5000) {
        console.warn('Text too long for Eleven Labs (5000 char limit), using browser TTS');
        throw new Error('Text too long for Eleven Labs');
    }

    // Eleven Labs API endpoint
    const voiceId = 'EXAVITQu4vr4xnSDxMaL'; // Default voice (Rachel)
    const url = `https://api.elevenlabs.io/v1/text-to-speech/${voiceId}`;

    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Accept': 'audio/mpeg',
            'Content-Type': 'application/json',
            'xi-api-key': elevenLabsKey
        },
        body: JSON.stringify({
            text: text,
            model_id: 'eleven_monolingual_v1',
            voice_settings: {
                stability: 0.5,
                similarity_boost: 0.75
            }
        })
    });

    console.log('Eleven Labs API response status:', response.status);

    if (!response.ok) {
        const errorText = await response.text();
        console.error('Eleven Labs API error:', errorText);
        throw new Error(`Eleven Labs API error: ${response.status}`);
    }

    const audioBlob = await response.blob();
    console.log('Eleven Labs: Received audio blob, size:', audioBlob.size, 'bytes');

    const audioUrl = URL.createObjectURL(audioBlob);
    const audio = new Audio(audioUrl);

    return new Promise((resolve, reject) => {
        audio.onended = () => {
            console.log('Eleven Labs: Audio playback completed');
            URL.revokeObjectURL(audioUrl);
            resolve();
        };
        audio.onerror = (error) => {
            console.error('Eleven Labs: Audio playback error:', error);
            reject(error);
        };
        audio.play().then(() => {
            console.log('Eleven Labs: Audio playback started');
        }).catch(reject);
    });
}

function speakWithBrowserTTS(text) {
    if ('speechSynthesis' in window) {
        const utterance = new SpeechSynthesisUtterance(text);
        utterance.rate = 0.9;
        utterance.pitch = 1;
        window.speechSynthesis.speak(utterance);
    }
}

function startListening() {
    if (!recognition) {
        alert('Speech recognition not supported in this browser. Please use Chrome or Edge.');
        return;
    }

    if (isListening) return;

    isListening = true;
    const listenBtn = document.getElementById('listen-btn');
    listenBtn.innerHTML = '🎤 Listening... <span class="mic-indicator"></span>';
    listenBtn.disabled = true;

    recognition.start();
}

function stopListening() {
    isListening = false;
    const listenBtn = document.getElementById('listen-btn');
    listenBtn.innerHTML = '🎤 Start Speaking';
    listenBtn.disabled = false;
}

function handleUserSpeech(transcript) {
    console.log('User said:', transcript);
    displayUserMessage(transcript);

    // Check for special commands
    const lowerTranscript = transcript.toLowerCase();

    if (lowerTranscript.includes('review') || lowerTranscript.includes('check my code')) {
        reviewCode();
    } else if (lowerTranscript.includes('hint') || lowerTranscript.includes('stuck')) {
        getHint();
    } else if (lowerTranscript.includes("i'm done") || lowerTranscript.includes('finished')) {
        finishInterview();
    } else {
        // Send to coach via OpenAI
        sendToCoach(transcript);
    }
}

let conversationHistory = [];

async function sendToCoach(userMessage) {
    // Add user message to conversation history
    conversationHistory.push({
        role: 'user',
        content: userMessage
    });

    try {
        // Call OpenAI API directly from browser
        const response = await fetch('https://api.openai.com/v1/chat/completions', {
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
        });

        if (!response.ok) {
            throw new Error(`OpenAI API error: ${response.status}`);
        }

        const data = await response.json();
        const coachResponse = data.choices[0].message.content;

        // Add coach response to history
        conversationHistory.push({
            role: 'assistant',
            content: coachResponse
        });

        // Display and speak the response
        displayCoachMessage(coachResponse);
        await speakText(coachResponse);

    } catch (error) {
        console.error('Error getting coach response:', error);
        displayCoachMessage("I'm having trouble responding right now. Please continue with your approach.");
    }
}

async function reviewCode() {
    const solutionEditor = document.getElementById('solution-editor');
    const code = solutionEditor.value.trim();

    if (!code) {
        alert('Please write some code in the solution editor first!');
        return;
    }

    displayUserMessage('Review my code');

    const reviewPrompt = `Here's my current code:\n\n${code}\n\nCan you review it and give me feedback?`;
    await sendToCoach(reviewPrompt);
}

async function getHint() {
    displayUserMessage('Give me a hint');
    await sendToCoach("I'm stuck. Can you give me a hint without revealing the solution?");
}

async function finishInterview() {
    displayUserMessage("I'm done");

    await sendToCoach("I've finished my solution. Can you ask me about the time and space complexity?");

    // Stop timer
    if (timerInterval) {
        clearInterval(timerInterval);
    }
}
