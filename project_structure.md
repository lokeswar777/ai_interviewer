ai_coding_platform/
├── frontend/                 # React.js application
│   ├── src/
│   │   ├── components/       # React components
│   │   ├── services/         # API communication
│   │   └── utils/           # Utility functions
│   ├── public/
│   └── package.json
├── backend/                  # FastAPI application
│   ├── app/
│   │   ├── api/             # API routes
│   │   ├── core/            # Core functionality
│   │   ├── models/          # Data models
│   │   ├── services/        # Business logic
│   │   └── utils/           # Utility functions
│   ├── requirements.txt
│   └── main.py
├── llm_service/             # LLM integration service
│   ├── model_handler.py     # Llama model management
│   ├── code_analyzer.py     # Code analysis logic
│   └── suggestion_engine.py # Suggestion generation
└── docker-compose.yml       # Container orchestration
