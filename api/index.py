from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Enable CORS so your mobile web app can talk to the Vercel backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Temporary in-memory state (Note: For persistent production use, pair with a database like Supabase)
latest_command = {"action": "none", "dx": 0, "dy": 0}

class MouseCommand(BaseModel):
    action: str  # 'move', 'click', 'right-click'
    dx: Optional[float] = 0.0
    dy: Optional[float] = 0.0

@app.post("/api/mouse")
def receive_command(cmd: MouseCommand):
    global latest_command
    latest_command = cmd.dict()
    return {"status": "success", "received": latest_command}

@app.get("/api/mouse")
def get_command():
    return latest_command