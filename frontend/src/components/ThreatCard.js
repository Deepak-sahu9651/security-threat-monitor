import React from 'react';
import './ThreatCard.css';

const ThreatCard = ({ threat, onSelect }) => {
  const getSeverityColor = (severity) => {
    switch (severity) {
      case 'CRITICAL':
        return '#dc2626';
      case 'HIGH':
        return '#ea580c';
      case 'MEDIUM':
        return '#eab308';
      case 'LOW':
        return '#3b82f6';
      default:
        return '#10b981';
    }
  };

  const getSeverityIcon = (severity) => {
    switch (severity) {
      case 'CRITICAL':
        return '🚨';
      case 'HIGH':
        return '⚠️';
      case 'MEDIUM':
        return '⚡';
      case 'LOW':
        return 'ℹ️';
      default:
        return '✓';
    }
  };

  const formatDate = (isoString) => {
    const date = new Date(isoString);
    const now = new Date();
    const diffMs = now - date;
    const diffSecs = Math.floor(diffMs / 1000);
    const diffMins = Math.floor(diffSecs / 60);
    const diffHours = Math.floor(diffMins / 60);

    if (diffSecs < 60) return `${diffSecs}s ago`;
    if (diffMins < 60) return `${diffMins}m ago`;
    if (diffHours < 24) return `${diffHours}h ago`;
    return date.toLocaleDateString();
  };

  return (
    <div 
      className="threat-card"
      onClick={() => onSelect(threat)}
      style={{
        borderLeftColor: getSeverityColor(threat.severity)
      }}
    >
      <div className="threat-card-header">
        <div className="threat-icon-title">
          <span className="threat-icon">{getSeverityIcon(threat.severity)}</span>
          <div className="threat-title-info">
            <h3>{threat.type}</h3>
            <p className="threat-source">Source: {threat.source}</p>
          </div>
        </div>
        <span 
          className="threat-badge" 
          style={{ backgroundColor: getSeverityColor(threat.severity) }}
        >
          {threat.severity}
        </span>
      </div>

      <p className="threat-description">{threat.description}</p>

      <div className="threat-footer">
        <span className="threat-time">{formatDate(threat.timestamp)}</span>
        <span className="threat-click">Click for details →</span>
      </div>
    </div>
  );
};

export default ThreatCard;
