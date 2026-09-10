import React from 'react';
import './Header.css';

const Header = ({ connectionStatus, totalClients }) => {
  const getStatusColor = () => {
    switch (connectionStatus) {
      case 'connected':
        return '#10b981';
      case 'connecting':
        return '#f59e0b';
      case 'disconnected':
        return '#ef4444';
      default:
        return '#94a3b8';
    }
  };

  const getStatusText = () => {
    switch (connectionStatus) {
      case 'connected':
        return 'Connected';
      case 'connecting':
        return 'Connecting...';
      case 'disconnected':
        return 'Disconnected';
      default:
        return 'Unknown';
    }
  };

  return (
    <header className="header">
      <div className="header-content">
        <div className="header-title">
          <h1>🛡️ Security Threat Monitor</h1>
          <p>Real-time Threat Detection & Response Dashboard</p>
        </div>
        
        <div className="header-status">
          <div className="status-indicator">
            <span 
              className="status-dot" 
              style={{ 
                backgroundColor: getStatusColor(),
                boxShadow: `0 0 10px ${getStatusColor()}`
              }}
            ></span>
            <span className="status-text">{getStatusText()}</span>
          </div>
          
          {connectionStatus === 'connected' && (
            <div className="connected-clients">
              👥 {totalClients} client{totalClients !== 1 ? 's' : ''} connected
            </div>
          )}
        </div>
      </div>
    </header>
  );
};

export default Header;
