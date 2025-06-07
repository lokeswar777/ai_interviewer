const WS_URL = 'ws://localhost:8000/ws/code-suggestions';

export const connectWebSocket = () => {
  const ws = new WebSocket(WS_URL);

  ws.onopen = () => {
    console.log('WebSocket connection established');
  };

  ws.onclose = () => {
    console.log('WebSocket connection closed');
    // Implement reconnection logic if needed
    setTimeout(() => {
      console.log('Attempting to reconnect...');
      connectWebSocket();
    }, 5000);
  };

  ws.onerror = (error) => {
    console.error('WebSocket error:', error);
  };

  return ws;
};

// Utility function to ensure message is sent only when connection is open
export const sendMessage = (ws, message) => {
  if (ws && ws.readyState === WebSocket.OPEN) {
    ws.send(JSON.stringify(message));
    return true;
  }
  console.warn('WebSocket is not connected');
  return false;
};

// Debounce function to limit the rate of messages sent
export const debounce = (func, wait) => {
  let timeout;
  return function executedFunction(...args) {
    const later = () => {
      clearTimeout(timeout);
      func(...args);
    };
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
  };
};

// Example usage of debounced message sending:
// const debouncedSend = debounce((ws, message) => {
//   sendMessage(ws, message);
// }, 500);
