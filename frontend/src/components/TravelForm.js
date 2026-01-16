import React, { useState } from 'react';

const TravelForm = ({ onSubmit, isLoading }) => {
  const [formData, setFormData] = useState({
    destination: '',
    startDate: '',
    endDate: '',
    budget: ''
  });

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(formData);
  };

  return (
    <form className="card" onSubmit={handleSubmit}>
      <div className="form-grid">
        <div className="input-group">
          <label>Destination</label>
          <input
            required
            placeholder="e.g. Paris"
            value={formData.destination}
            onChange={(e) => setFormData({...formData, destination: e.target.value})}
          />
        </div>
        <div className="input-group">
          <label>Start Date</label>
          <input
            type="date"
            required
            value={formData.startDate}
            onChange={(e) => setFormData({...formData, startDate: e.target.value})}
          />
        </div>
        <div className="input-group">
          <label>End Date</label>
          <input
            type="date"
            required
            value={formData.endDate}
            onChange={(e) => setFormData({...formData, endDate: e.target.value})}
          />
        </div>
        <div className="input-group">
          <label>Budget (Optional)</label>
          <input
            type="number"
            placeholder="USD"
            value={formData.budget}
            onChange={(e) => setFormData({...formData, budget: e.target.value})}
          />
        </div>
      </div>
      <button type="submit" disabled={isLoading}>
        {isLoading ? 'Analyzing Signals...' : 'Get Travel Signal'}
      </button>
    </form>
  );
};

export default TravelForm;