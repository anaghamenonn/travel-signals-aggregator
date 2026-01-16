const BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

export const fetchTravelSignal = async (params) => {
  const query = new URLSearchParams({
    destination: params.destination,
    start_date: params.startDate,
    end_date: params.endDate,
    ...(params.budget && { budget: params.budget }),
  });

  const response = await fetch(`${BASE_URL}/travel-signal?${query.toString()}`);
  
  if (!response.ok) {
    const errorData = await response.json().catch(() => ({}));
    throw new Error(errorData.message || 'Failed to fetch travel signals');
  }

  return response.json();
};