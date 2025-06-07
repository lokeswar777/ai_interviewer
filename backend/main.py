from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import uvicorn
import json

# Import our services and routes
from app.api.code_routes import router as code_router
from app.services.code_executor import code_executor
from app.services.llm_service import llm_service

app = FastAPI(title="AI Coding Platform API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(code_router, prefix="/api", tags=["code"])

# WebSocket connection manager
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_suggestion(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

manager = ConnectionManager()

@app.on_event("startup")
async def startup_event():
    """Initialize services on startup"""
    print("Initializing AI Coding Platform...")
    # Initialize LLM service (this might take some time)
    await llm_service.initialize()
    print("Platform ready!")

@app.get("/")
async def root():
    """Root endpoint to verify API is running"""
    return {"message": "AI Coding Platform API is running"}

@app.post("/execute")
async def execute_code_endpoint(request: dict):
    """Execute Python code"""
    code = request.get("code", "")
    timeout = request.get("timeout", 30)
    
    result = await code_executor.execute_python_code(code, timeout)
    return result

@app.post("/explain")
async def explain_code_endpoint(request: dict):
    """Get code explanation from LLM"""
    code = request.get("code", "")
    detail_level = request.get("detail_level", "medium")
    
    result = await llm_service.explain_code(code, detail_level)
    return result

@app.websocket("/ws/code-suggestions")
async def websocket_endpoint(websocket: WebSocket):
    """WebSocket endpoint for real-time code suggestions"""
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            try:
                message = json.loads(data)
                if message.get("type") == "code_update":
                    code = message.get("content", "")
                    # Generate suggestions using LLM
                    suggestions = await llm_service.generate_suggestions(code)
                    response = {
                        "type": "suggestions",
                        "content": suggestions
                    }
                    await manager.send_suggestion(json.dumps(response), websocket)
            except json.JSONDecodeError:
                # Handle plain text messages
                suggestions = await llm_service.generate_suggestions(data)
                response = {
                    "type": "suggestions", 
                    "content": suggestions
                }
                await manager.send_suggestion(json.dumps(response), websocket)
    except WebSocketDisconnect:
        manager.disconnect(websocket)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
