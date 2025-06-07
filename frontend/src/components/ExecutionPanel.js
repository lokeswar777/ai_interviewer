import React from 'react';
import { 
  Box, 
  Typography, 
  Paper, 
  Chip,
  Divider,
  CircularProgress
} from '@mui/material';
import CheckCircleIcon from '@mui/icons-material/CheckCircle';
import ErrorIcon from '@mui/icons-material/Error';
import AccessTimeIcon from '@mui/icons-material/AccessTime';

const ExecutionPanel = ({ result }) => {
  const getStatusColor = (status) => {
    switch (status) {
      case 'success':
        return 'success';
      case 'error':
        return 'error';
      case 'timeout':
        return 'warning';
      default:
        return 'default';
    }
  };

  const getStatusIcon = (status) => {
    switch (status) {
      case 'success':
        return <CheckCircleIcon />;
      case 'error':
        return <ErrorIcon />;
      case 'timeout':
        return <AccessTimeIcon />;
      default:
        return null;
    }
  };

  if (!result) {
    return (
      <Box sx={{ 
        height: '30%', 
        p: 2, 
        bgcolor: 'background.paper',
        borderTop: 1,
        borderColor: 'divider'
      }}>
        <Typography variant="h6" gutterBottom>
          Output
        </Typography>
        <Typography variant="body2" color="text.secondary">
          Click "Run" to execute your code
        </Typography>
      </Box>
    );
  }

  return (
    <Box sx={{ 
      height: '30%', 
      p: 2, 
      bgcolor: 'background.paper',
      borderTop: 1,
      borderColor: 'divider',
      overflow: 'auto'
    }}>
      <Box sx={{ display: 'flex', alignItems: 'center', mb: 2 }}>
        <Typography variant="h6" sx={{ mr: 2 }}>
          Output
        </Typography>
        
        {result.status && (
          <Chip
            icon={getStatusIcon(result.status)}
            label={result.status.toUpperCase()}
            color={getStatusColor(result.status)}
            size="small"
            sx={{ mr: 2 }}
          />
        )}
        
        {result.execution_time !== undefined && (
          <Chip
            label={`${result.execution_time.toFixed(3)}s`}
            size="small"
            variant="outlined"
          />
        )}
      </Box>

      <Divider sx={{ mb: 2 }} />

      {result.output && (
        <Box sx={{ mb: 2 }}>
          <Typography variant="subtitle2" color="success.main" gutterBottom>
            Output:
          </Typography>
          <Paper 
            sx={{ 
              p: 1, 
              bgcolor: 'grey.900', 
              fontFamily: 'monospace',
              fontSize: '0.875rem',
              whiteSpace: 'pre-wrap',
              overflow: 'auto',
              maxHeight: '150px'
            }}
          >
            <Typography 
              component="pre" 
              sx={{ 
                color: 'success.light',
                fontFamily: 'inherit',
                fontSize: 'inherit',
                margin: 0
              }}
            >
              {result.output}
            </Typography>
          </Paper>
        </Box>
      )}

      {result.error && (
        <Box>
          <Typography variant="subtitle2" color="error.main" gutterBottom>
            Error:
          </Typography>
          <Paper 
            sx={{ 
              p: 1, 
              bgcolor: 'grey.900', 
              fontFamily: 'monospace',
              fontSize: '0.875rem',
              whiteSpace: 'pre-wrap',
              overflow: 'auto',
              maxHeight: '150px'
            }}
          >
            <Typography 
              component="pre" 
              sx={{ 
                color: 'error.light',
                fontFamily: 'inherit',
                fontSize: 'inherit',
                margin: 0
              }}
            >
              {result.error}
            </Typography>
          </Paper>
        </Box>
      )}
    </Box>
  );
};

export default ExecutionPanel;
