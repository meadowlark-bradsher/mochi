"""Web server for Mochi interview coach."""

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pathlib import Path
import json
import asyncio
from typing import Optional

app = FastAPI(title="Mochi Interview Coach")

# Serve static files (HTML, JS, CSS)
static_dir = Path(__file__).parent / "static"
static_dir.mkdir(exist_ok=True)

app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")


@app.get("/")
async def home():
    """Serve the main interview interface."""
    html_file = static_dir / "index.html"
    if html_file.exists():
        return HTMLResponse(content=html_file.read_text())
    return HTMLResponse(content="""
<!DOCTYPE html>
<html>
<head>
    <title>Mochi - Interview Coach</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>Mochi Interview Coach</h1>
    <p>Static files not yet created. Run: mochi web --setup</p>
</body>
</html>
    """)


# Session storage for active interviews
active_sessions = {}

@app.websocket("/ws/interview")
async def interview_websocket(websocket: WebSocket):
    """WebSocket endpoint for real-time interview interaction."""
    await websocket.accept()

    session_id = id(websocket)
    session_data = {
        "problem": None,
        "conversation": [],
        "code": None
    }
    active_sessions[session_id] = session_data

    try:
        while True:
            # Receive message from client
            data = await websocket.receive_json()

            message_type = data.get("type")

            if message_type == "start":
                # Interview started
                problem = data.get("problem", "")
                session_data["problem"] = problem

                # Store problem in conversation context
                session_data["conversation"].append({
                    "role": "system",
                    "content": f"The user is working on this problem:\n\n{problem}\n\nCoach them without revealing the solution."
                })

                await websocket.send_json({
                    "type": "coach",
                    "message": "Let's begin. I see your problem. Take a moment to read it, then start thinking out loud. What's your initial approach?"
                })

            elif message_type == "user_message":
                # User spoke or typed
                user_text = data.get("text", "")

                # Add to conversation
                session_data["conversation"].append({
                    "role": "user",
                    "content": user_text
                })

                # Get coach response (client will call OpenAI directly)
                # For now, send back a placeholder
                await websocket.send_json({
                    "type": "coach",
                    "message": "I understand. Can you explain your reasoning for that approach? What trade-offs are you considering?"
                })

            elif message_type == "review_code":
                # User wants code reviewed
                code = data.get("code", "")
                session_data["code"] = code

                await websocket.send_json({
                    "type": "coach",
                    "message": "I see your code. Let me analyze it... One thing to consider: have you thought about edge cases like empty inputs?"
                })

            elif message_type == "hint":
                # User requested a hint
                await websocket.send_json({
                    "type": "coach",
                    "message": "Think about what data structure would help you track elements you've already seen. How could you avoid checking the same pairs repeatedly?"
                })

            elif message_type == "finish":
                # User finished the problem
                await websocket.send_json({
                    "type": "coach",
                    "message": "Great work! Let's discuss complexity. What's the time complexity of your solution? And what about space complexity?"
                })

    except WebSocketDisconnect:
        print(f"Client {session_id} disconnected")
        if session_id in active_sessions:
            del active_sessions[session_id]


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "ok"}


def run_server(host: str = "127.0.0.1", port: int = 8000):
    """Run the web server."""
    import uvicorn
    uvicorn.run(app, host=host, port=port)
