import React, { useState, useEffect } from 'react';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import Box from '@mui/material/Box';
import CodeEditor from './components/CodeEditor';
import SuggestionPanel from './components/SuggestionPanel';
import ExecutionPanel from './components/ExecutionPanel';
import { connectWebSocket } from './services/websocket';

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
    primary: {
      main: '#90caf9',
    },
    background: {
      default: '#1e1e1e',
      paper: '#252526',
    },
  },
  typography: {
    fontFamily: "'Roboto Mono', monospace",
  },
});

function App() {
  const [code, setCode] = useState('# Start coding here\n');
  const [suggestions, setSuggestions] = useState([]);
  const [executionResult, setExecutionResult] = useState(null);
  const [ws, setWs] = useState(null);

  useEffect(() => {
    // Initialize WebSocket connection
    const socket = connectWebSocket();
    setWs(socket);

    return () => {
      if (socket) {
        socket.close();
      }
    };
  }, []);

  const handleCodeChange = async (newCode) => {
    setCode(newCode);
    
    // Send code to WebSocket for real-time suggestions
    if (ws && ws.readyState === WebSocket.OPEN) {
      ws.send(JSON.stringify({
        type: 'code_update',
        content: newCode
      }));
    }
  };

  const handleCodeExecution = async () => {
    try {
      const response = await fetch('http://localhost:8000/execute', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ code }),
      });
      const result = await response.json();
      setExecutionResult(result);
    } catch (error) {
      setExecutionResult({
        status: 'error',
        error: 'Failed to execute code',
        output: null
      });
    }
  };

  const handleExplanationRequest = async () => {
    try {
      const response = await fetch('http://localhost:8000/explain', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 
          code,
          detail_level: 'medium'
        }),
      });
      const result = await response.json();
      setSuggestions(prev => [...prev, {
        type: 'explanation',
        content: result.explanation
      }]);
    } catch (error) {
      setSuggestions(prev => [...prev, {
        type: 'error',
        content: 'Failed to get explanation'
      }]);
    }
  };

  return (
    <ThemeProvider theme={darkTheme}>
      <CssBaseline />
      <Box sx={{ 
        display: 'flex', 
        height: '100vh', 
        bgcolor: 'background.default',
        overflow: 'hidden'
      }}>
        <Box sx={{ 
          flex: 1, 
          display: 'flex', 
          flexDirection: 'column',
          borderRight: 1,
          borderColor: 'divider'
        }}>
          <CodeEditor
            code={code}
            onChange={handleCodeChange}
            onExecute={handleCodeExecution}
            onExplain={handleExplanationRequest}
          />
          <ExecutionPanel result={executionResult} />
        </Box>
        <SuggestionPanel 
          suggestions={suggestions}
          onSuggestionApply={(suggestion) => setCode(suggestion)}
        />
      </Box>
    </ThemeProvider>
  );
}

export default App;
