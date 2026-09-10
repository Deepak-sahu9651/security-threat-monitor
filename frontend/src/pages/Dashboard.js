import React, { useState } from 'react';
import StatCard from '../components/StatCard';
import ThreatCard from '../components/ThreatCard';
import './Dashboard.css';

const Dashboard = ({ threats, stats, selectedThreat, onSelectThreat, filterSeverity, onFilterChange }) => {
  const [sortBy, setSortBy] = useState('timestamp'); // timestamp, severity
  const [viewMode, setViewMode] = useState('list'); // list, grid

  // Sort threats
  const sortedThreats = [...threats].sort((a, b) => {
    if (sortBy === 'severity') {
      const severityOrder = { CRITICAL: 0, HIGH: 1, MEDIUM: 2, LOW: 3, INFO: 4 };
      return severityOrder[a.severity] - severityOrder[b.severity];
    }
    return new Date(b.timestamp) - new Date(a.timestamp);
  });

  return (
    <div className="dashboard">
      {/* Statistics Section */}
      <section className="stats-section">
        <h2>Threat Overview</h2>
        <div className="stats-grid">
          <StatCard
            title="Total Threats"
            value={stats.total_threats}
            icon="🎯"
            color="#3b82f6"
          />
          <StatCard
            title="Critical"
            value={stats.critical}
            icon="🚨"
            color="#dc2626"
          />
          <StatCard
            title="High"
            value={stats.high}
            icon="⚠️"
            color="#ea580c"
          />
          <StatCard
            title="Medium"
            value={stats.medium}
            icon="⚡"
            color="#eab308"
          />
          <StatCard
            title="Low"
            value={stats.low}
            icon="ℹ️"
            color="#3b82f6"
          />
          <StatCard
            title="Avg Response"
            value={`${stats.avg_response_time}ms`}
            icon="⏱️"
            color="#10b981"
          />
        </div>
      </section>

      {/* Threats Section */}
      <section className="threats-section">
        <div className="threats-header">
          <h2>Detected Threats ({sortedThreats.length})</h2>
          
          <div className="threats-controls">
            {/* Filter by Severity */}
            <div className="filter-group">
              <label>Filter by Severity:</label>
              <div className="filter-buttons">
                <button
                  className={`filter-btn ${!filterSeverity ? 'active' : ''}`}
                  onClick={() => onFilterChange(null)}
                >
                  All
                </button>
                <button
                  className={`filter-btn critical ${filterSeverity === 'CRITICAL' ? 'active' : ''}`}
                  onClick={() => onFilterChange('CRITICAL')}
                >
                  🚨 Critical
                </button>
                <button
                  className={`filter-btn high ${filterSeverity === 'HIGH' ? 'active' : ''}`}
                  onClick={() => onFilterChange('HIGH')}
                >
                  ⚠️ High
                </button>
                <button
                  className={`filter-btn medium ${filterSeverity === 'MEDIUM' ? 'active' : ''}`}
                  onClick={() => onFilterChange('MEDIUM')}
                >
                  ⚡ Medium
                </button>
                <button
                  className={`filter-btn low ${filterSeverity === 'LOW' ? 'active' : ''}`}
                  onClick={() => onFilterChange('LOW')}
                >
                  ℹ️ Low
                </button>
              </div>
            </div>

            {/* Sort & View Options */}
            <div className="view-controls">
              <select value={sortBy} onChange={(e) => setSortBy(e.target.value)} className="sort-select">
                <option value="timestamp">Latest First</option>
                <option value="severity">By Severity</option>
              </select>
              
              <div className="view-mode-buttons">
                <button
                  className={`view-btn ${viewMode === 'list' ? 'active' : ''}`}
                  onClick={() => setViewMode('list')}
                  title="List View"
                >
                  ☰
                </button>
                <button
                  className={`view-btn ${viewMode === 'grid' ? 'active' : ''}`}
                  onClick={() => setViewMode('grid')}
                  title="Grid View"
                >
                  ⊞
                </button>
              </div>
            </div>
          </div>
        </div>

        {/* Threats List */}
        {sortedThreats.length === 0 ? (
          <div className="no-threats">
            <p>✅ No threats detected</p>
            <span>System is secure</span>
          </div>
        ) : (
          <div className={`threats-${viewMode}`}>
            {sortedThreats.map(threat => (
              <ThreatCard
                key={threat.id}
                threat={threat}
                onSelect={onSelectThreat}
              />
            ))}
          </div>
        )}
      </section>

      {/* Real-time Updates Indicator */}
      <div className="update-indicator">
        <span className="update-dot"></span>
        Updates in real-time
      </div>
    </div>
  );
};

export default Dashboard;
