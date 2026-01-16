import React, { useState } from 'react';
import './styles/App.css';
import { fetchTravelSignal } from './api/travelApi';
import TravelForm from './components/TravelForm';
import SignalCard from './components/SignalCard';

function App() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSearch = async (params) => {
    setLoading(true);
    setError(null);
    try {
      const result = await fetchTravelSignal(params);
      setData(result);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <header>
        <h1>Travel Signal Aggregator</h1>
        <p>Get real-time insights before you book your trip.</p>
      </header>

      <TravelForm onSubmit={handleSearch} isLoading={loading} />

      {error && (
        <div className="card" style={{ borderLeft: '4px solid var(--danger)', color: 'var(--danger)' }}>
          <strong>Error:</strong> {error}
        </div>
      )}

      {data && (
        <div className="results-area">
          <div className="card" style={{ textAlign: 'center' }}>
            <h2>{data.destination}</h2>
            <p>{data.date_range}</p>
            <div className="score-badge">{data.score}</div>
            <p>Overall Readiness Score</p>
          </div>

          <div className="signals-grid">
            {Object.entries(data.explanation).map(([key, signal]) => (
              <SignalCard key={key} title={key} data={signal} />
            ))}
          </div>

          {data.missing_signals.length > 0 && (
            <div className="missing-signals">
              <strong>Notice:</strong> Missing data for: {data.missing_signals.join(', ')}
            </div>
          )}
        </div>
      )}
    </div>
  );
}

export default App;