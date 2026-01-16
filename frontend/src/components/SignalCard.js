import React from 'react';

const SignalCard = ({ title, data }) => {
  const getRiskColor = (risk) => {
    if (risk < 0.3) return 'var(--success)';
    if (risk < 0.6) return 'var(--warning)';
    return 'var(--danger)';
  };

  const formatKey = (key) => key.replace(/_/g, ' ');

  return (
    <div className="card signal-card">
      <h4>{title}</h4>
      <div style={{ marginBottom: '1rem' }}>
        {Object.entries(data).map(([key, val]) => (
          key !== 'risk' && (
            <div key={key} style={{ fontSize: '0.9rem' }}>
              <strong>{formatKey(key)}:</strong> {val.toString()}
            </div>
          )
        ))}
      </div>
      <div 
        className="risk-tag" 
        style={{ 
          backgroundColor: getRiskColor(data.risk),
          color: 'white'
        }}
      >
        Risk: {(data.risk * 100).toFixed(0)}%
      </div>
    </div>
  );
};

export default SignalCard;