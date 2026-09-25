from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Shared in-memory store for mouse state
mouse_state = {
    "x": 0.0,
    "y": 0.0,
    "action": "idle"
}

class MouseData(BaseModel):
    x: float
    y: float
    action: str

@app.post("/api/update")
async def update_mouse(data: MouseData):
    global mouse_state
    mouse_state = {
        "x": data.x,
        "y": data.y,
        "action": data.action
    }
    return {"status": "success", "data": mouse_state}

@app.get("/api/get")
async def get_mouse():
    return mouse_state