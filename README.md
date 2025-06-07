# AI-Powered Coding Platform

A web-based coding platform that provides AI-powered suggestions, explanations, and code execution capabilities for Python development.

## Features

- **Smart Code Editor**: Monaco Editor with syntax highlighting and IntelliSense
- **AI Suggestions**: Real-time code suggestions using local Llama model
- **Code Explanations**: On-demand explanations of code logic and approaches
- **Code Execution**: Secure Python code execution environment
- **Real-time Communication**: WebSocket-based live suggestions

## Architecture

- **Frontend**: React.js with Monaco Editor
- **Backend**: FastAPI with WebSocket support
- **AI Engine**: Local Llama model via Hugging Face Transformers
- **Code Execution**: Secure Python sandbox environment

## Project Structure

```
ai_coding_platform/
├── frontend/                 # React.js application
├── backend/                  # FastAPI application
├── llm_service/             # LLM integration service
└── docker-compose.yml       # Container orchestration
```

## Getting Started

### Prerequisites

- Python 3.8+
- Node.js 16+
- Docker (optional)

### Installation

1. Clone the repository
2. Set up backend dependencies: `cd backend && pip install -r requirements.txt`
3. Set up frontend dependencies: `cd frontend && npm install`
4. Download and configure the Llama model
5. Start the development servers

### Usage

1. Start the backend server: `cd backend && python main.py`
2. Start the frontend server: `cd frontend && npm start`
3. Open your browser to `http://localhost:3000`

## Development

This platform is designed to help developers write better Python code with AI assistance. The system provides:

- Context-aware code completions
- Real-time syntax and logic suggestions
- Code explanation and documentation
- Secure code execution and testing

## License

MIT License
"# ai_interviewer" 
