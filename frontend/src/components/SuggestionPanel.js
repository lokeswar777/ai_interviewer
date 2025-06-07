import React from 'react';
import { 
  Box, 
  Typography, 
  Paper, 
  List, 
  ListItem, 
  ListItemText,
  ListItemIcon,
  IconButton,
  Tooltip,
  Divider
} from '@mui/material';
import LightbulbIcon from '@mui/icons-material/Lightbulb';
import InfoIcon from '@mui/icons-material/Info';
import ContentCopyIcon from '@mui/icons-material/ContentCopy';
import CheckIcon from '@mui/icons-material/Check';

const SuggestionPanel = ({ suggestions, onSuggestionApply }) => {
  const handleCopy = (suggestion) => {
    if (onSuggestionApply) {
      onSuggestionApply(suggestion);
    }
  };

  const renderSuggestion = (suggestion, index) => {
    const isExplanation = suggestion.type === 'explanation';
    
    return (
      <ListItem
        key={index}
        alignItems="flex-start"
        sx={{
          flexDirection: 'column',
          bgcolor: 'background.paper',
          mb: 1,
          borderRadius: 1,
          '&:hover': {
            bgcolor: 'action.hover',
          },
        }}
      >
        <Box sx={{ 
          display: 'flex', 
          width: '100%', 
          alignItems: 'flex-start',
          mb: 1
        }}>
          <ListItemIcon sx={{ minWidth: 40 }}>
            {isExplanation ? <InfoIcon color="info" /> : <LightbulbIcon color="primary" />}
          </ListItemIcon>
          
          <ListItemText
            primary={
              <Typography variant="subtitle2" color="text.primary">
                {isExplanation ? 'Code Explanation' : 'Suggestion'}
              </Typography>
            }
          />

          {!isExplanation && (
            <Tooltip title="Apply Suggestion">
              <IconButton 
                size="small" 
                onClick={() => handleCopy(suggestion.content)}
                sx={{ ml: 1 }}
              >
                <ContentCopyIcon fontSize="small" />
              </IconButton>
            </Tooltip>
          )}
        </Box>

        <Box sx={{ pl: 5, pr: 2, width: '100%' }}>
          <Paper
            variant="outlined"
            sx={{
              p: 1,
              bgcolor: 'background.default',
              fontFamily: 'monospace',
              fontSize: '0.875rem',
              whiteSpace: 'pre-wrap',
              overflow: 'auto',
              maxHeight: '200px'
            }}
          >
            <Typography
              component="pre"
              sx={{
                fontFamily: 'inherit',
                fontSize: 'inherit',
                margin: 0,
                color: 'text.primary'
              }}
            >
              {suggestion.content}
            </Typography>
          </Paper>
        </Box>
      </ListItem>
    );
  };

  return (
    <Box sx={{ 
      width: '30%', 
      minWidth: 300,
      maxWidth: 500,
      height: '100%',
      bgcolor: 'background.paper',
      display: 'flex',
      flexDirection: 'column'
    }}>
      <Box sx={{ 
        p: 2, 
        borderBottom: 1,
        borderColor: 'divider'
      }}>
        <Typography variant="h6">
          AI Suggestions
        </Typography>
      </Box>

      {suggestions.length === 0 ? (
        <Box sx={{ 
          p: 2, 
          display: 'flex', 
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
          height: '100%',
          color: 'text.secondary'
        }}>
          <LightbulbIcon sx={{ fontSize: 40, mb: 2 }} />
          <Typography variant="body2">
            Start typing to get AI-powered suggestions
          </Typography>
        </Box>
      ) : (
        <List sx={{ 
          flex: 1, 
          overflow: 'auto',
          p: 2
        }}>
          {suggestions.map((suggestion, index) => renderSuggestion(suggestion, index))}
        </List>
      )}
    </Box>
  );
};

export default SuggestionPanel;
