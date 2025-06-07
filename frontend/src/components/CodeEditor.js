import React from 'react';
import Editor from '@monaco-editor/react';
import { Box, Button, AppBar, Toolbar, IconButton, Tooltip } from '@mui/material';
import PlayArrowIcon from '@mui/icons-material/PlayArrow';
import HelpOutlineIcon from '@mui/icons-material/HelpOutline';
import LightbulbIcon from '@mui/icons-material/Lightbulb';

const CodeEditor = ({ code, onChange, onExecute, onExplain }) => {
  const handleEditorChange = (value) => {
    onChange(value);
  };

  const editorOptions = {
    minimap: { enabled: false },
    fontSize: 14,
    lineNumbers: 'on',
    rulers: [80],
    wordWrap: 'on',
    wrappingIndent: 'indent',
    automaticLayout: true,
    suggestOnTriggerCharacters: true,
    acceptSuggestionOnEnter: 'on',
    tabSize: 4,
    fontFamily: "'Roboto Mono', monospace",
    scrollBeyondLastLine: false,
  };

  return (
    <Box sx={{ 
      display: 'flex', 
      flexDirection: 'column', 
      height: '70%',
      borderBottom: 1,
      borderColor: 'divider'
    }}>
      <AppBar 
        position="static" 
        color="default" 
        sx={{ 
          borderBottom: 1,
          borderColor: 'divider'
        }}
      >
        <Toolbar variant="dense">
          <Tooltip title="Run Code (Ctrl+Enter)">
            <Button
              variant="contained"
              color="primary"
              startIcon={<PlayArrowIcon />}
              onClick={onExecute}
              sx={{ mr: 1 }}
            >
              Run
            </Button>
          </Tooltip>
          
          <Box sx={{ flexGrow: 1 }} />
          
          <Tooltip title="Get Code Explanation">
            <IconButton 
              color="primary"
              onClick={onExplain}
              size="small"
              sx={{ mr: 1 }}
            >
              <HelpOutlineIcon />
            </IconButton>
          </Tooltip>

          <Tooltip title="Get Suggestions">
            <IconButton
              color="primary"
              size="small"
            >
              <LightbulbIcon />
            </IconButton>
          </Tooltip>
        </Toolbar>
      </AppBar>
      
      <Box sx={{ flex: 1, overflow: 'hidden' }}>
        <Editor
          height="100%"
          defaultLanguage="python"
          theme="vs-dark"
          value={code}
          onChange={handleEditorChange}
          options={editorOptions}
          onMount={(editor) => {
            // Add keyboard shortcut for code execution
            editor.addCommand(
              monaco.KeyMod.CtrlCmd | monaco.KeyCode.Enter,
              onExecute
            );
          }}
        />
      </Box>
    </Box>
  );
};

export default CodeEditor;
