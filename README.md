# AI-Powered Coding Platform

An intelligent coding platform that provides real-time AI-powered suggestions, code explanations, and secure code execution capabilities for Python development.

## 🚀 Features

- **Smart Code Editor**
  - Monaco Editor (VS Code-like experience)
  - Syntax highlighting and IntelliSense
  - Real-time error detection
  - Custom themes and keyboard shortcuts

- **AI-Powered Assistance**
  - Real-time code suggestions using Llama model
  - Context-aware completions
  - Code optimization recommendations
  - Best practices guidance

- **Code Explanations**
  - On-demand code explanations
  - Algorithm approach breakdowns
  - Best practices recommendations
  - Performance insights

- **Secure Code Execution**
  - Isolated Python execution environment
  - Output and error handling
  - Execution time limits
  - Memory usage restrictions

- **Real-time Communication**
  - WebSocket-based live suggestions
  - Instant feedback
  - Low-latency updates

## 🛠️ Technology Stack

- **Frontend**
  - React.js
  - Monaco Editor
  - Material-UI
  - WebSocket client

- **Backend**
  - FastAPI
  - WebSockets
  - Hugging Face Transformers
  - Docker

- **AI/ML**
  - Llama model (local deployment)
  - Hugging Face Transformers
  - PyTorch

## 📦 Installation

### Prerequisites

- Python 3.8+
- Node.js 16+
- Docker and Docker Compose (optional)

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ai-coding-platform.git
   cd ai-coding-platform
   ```

2. **Run the setup script**
   ```bash
   python setup.py
   ```
   This will:
   - Create necessary directories
   - Set up Python virtual environment
   - Install backend dependencies
   - Install frontend dependencies
   - Configure initial settings

3. **Start the application**

   Using Docker:
   ```bash
   docker-compose up
   ```

   Manual start:
   ```bash
   # Terminal 1 - Backend
   cd backend
   python main.py

   # Terminal 2 - Frontend
   cd frontend
   npm start
   ```

4. Open your browser to `http://localhost:3000`

## 🏗️ Project Structure

```
ai_coding_platform/
├── frontend/                 # React.js application
│   ├── src/
│   │   ├── components/      # React components
│   │   ├── services/        # API communication
│   │   └── utils/          # Utility functions
│   └── public/
├── backend/                  # FastAPI application
│   ├── app/
│   │   ├── api/            # API routes
│   │   ├── services/       # Business logic
│   │   └── utils/         # Utility functions
│   └── main.py
├── models/                   # LLM model storage
├── docker-compose.yml        # Container orchestration
├── setup.py                 # Setup script
└── .env                     # Environment configuration
```

## 🔧 Configuration

The platform can be configured using environment variables in the `.env` file:

```ini
# Backend Configuration
BACKEND_HOST=localhost
BACKEND_PORT=8000

# Frontend Configuration
FRONTEND_HOST=localhost
FRONTEND_PORT=3000

# LLM Configuration
MODEL_NAME=meta-llama/Llama-2-7b-hf
MODEL_CACHE_DIR=./models
```

## 💻 Development

### Backend Development

1. Activate the virtual environment:
   ```bash
   cd backend
   source venv/bin/activate  # Unix
   # or
   venv\Scripts\activate     # Windows
   ```

2. Start the backend server:
   ```bash
   python main.py
   ```

### Frontend Development

1. Install dependencies:
   ```bash
   cd frontend
   npm install
   ```

2. Start the development server:
   ```bash
   npm start
   ```

## 🔒 Security

- Code execution is performed in isolated environments
- Memory and execution time limits are enforced
- Network access is restricted in code execution
- Input validation and sanitization
- CORS configuration for API security

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/)
- [React](https://reactjs.org/)
- [Monaco Editor](https://microsoft.github.io/monaco-editor/)
- [Hugging Face](https://huggingface.co/)
- [Material-UI](https://mui.com/)
