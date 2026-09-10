import React from 'react';
import './ThreatDetail.css';

const ThreatDetail = ({ threat, onClose }) => {
  if (!threat) return null;

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

  const formatDate = (isoString) => {
    return new Date(isoString).toLocaleString();
  };

  return (
    <div className="threat-detail-overlay" onClick={onClose}>
      <div className="threat-detail-modal" onClick={(e) => e.stopPropagation()}>
        <div className="detail-header">
          <div className="detail-title-section">
            <h2>{threat.type}</h2>
            <span 
              className="detail-severity" 
              style={{ backgroundColor: getSeverityColor(threat.severity) }}
            >
              {threat.severity}
            </span>
          </div>
          <button className="close-btn" onClick={onClose}>✕</button>
        </div>

        <div className="detail-content">
          <div className="detail-section">
            <h3>Description</h3>
            <p>{threat.description}</p>
          </div>

          <div className="detail-grid">
            <div className="detail-item">
              <label>Threat ID</label>
              <code>{threat.id}</code>
            </div>
            <div className="detail-item">
              <label>Source</label>
              <p>{threat.source}</p>
            </div>
            <div className="detail-item">
              <label>Detection Time</label>
              <p>{formatDate(threat.timestamp)}</p>
            </div>
            <div className="detail-item">
              <label>Severity Level</label>
              <p style={{ color: getSeverityColor(threat.severity) }}>
                {threat.severity}
              </p>
            </div>
          </div>

          {threat.details && (
            <div className="detail-section">
              <h3>Details</h3>
              <div className="details-table">
                {Object.entries(threat.details).map(([key, value]) => (
                  <div key={key} className="detail-row">
                    <span className="detail-key">{key}:</span>
                    <span className="detail-value">
                      {typeof value === 'object' ? JSON.stringify(value) : String(value)}
                    </span>
                  </div>
                ))}
              </div>
            </div>
          )}

          <div className="detail-section">
            <h3>Recommended Actions</h3>
            <ul className="action-list">
              {threat.severity === 'CRITICAL' && (
                <>
                  <li>🚨 Immediately isolate affected systems</li>
                  <li>📞 Contact security team immediately</li>
                  <li>🔒 Change all related credentials</li>
                  <li>📊 Collect forensic evidence</li>
                </>
              )}
              {threat.severity === 'HIGH' && (
                <>
                  <li>⚠️ Investigate threat immediately</li>
                  <li>🔍 Review access logs</li>
                  <li>🛡️ Strengthen access controls</li>
                </>
              )}
              {threat.severity === 'MEDIUM' && (
                <>
                  <li>📋 Monitor system for similar activity</li>
                  <li>🔧 Apply security patches</li>
                  <li>📊 Update security policies</li>
                </>
              )}
              {threat.severity === 'LOW' && (
                <>
                  <li>ℹ️ Log and track for future reference</li>
                  <li>📈 Review trends over time</li>
                </>
              )}
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ThreatDetail;
