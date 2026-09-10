import React from 'react';
import './StatCard.css';

const StatCard = ({ title, value, icon, color, trend }) => {
  return (
    <div className="stat-card" style={{ borderTopColor: color }}>
      <div className="stat-header">
        <span className="stat-icon" style={{ color: color }}>{icon}</span>
        <h3>{title}</h3>
      </div>
      
      <div className="stat-value" style={{ color: color }}>
        {value}
      </div>
      
      {trend && (
        <div className="stat-trend">
          {trend > 0 ? '📈' : '📉'} {Math.abs(trend)}% from last hour
        </div>
      )}
    </div>
  );
};

export default StatCard;
