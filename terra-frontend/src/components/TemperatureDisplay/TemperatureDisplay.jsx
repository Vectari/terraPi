import React, { useEffect, useState } from 'react';

export function TemperatureDisplay() {
  const [temperatures, setTemperatures] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchTemperatures = () => {
      fetch('http://localhost:5000/api/temperature')
        .then(response => response.json())
        .then(data => {
          setTemperatures(data.temperatures);
          setLoading(false);
        })
        .catch(error => {
          console.error('Error fetching temperatures:', error);
          setLoading(false);
        });
    };

    // Fetch immediately on mount
    fetchTemperatures();

    // Set interval to fetch every 5 seconds
    const intervalId = setInterval(fetchTemperatures, 5000);

    // Clean up on unmount
    return () => clearInterval(intervalId);
  }, []);

  if (loading) return <div>Loading...</div>;

  return (
    <div>
      <h2>Temperatures</h2>
      <ul>
        {temperatures.map((temp, idx) => (
          <li key={idx}>{temp} °C</li>
        ))}
      </ul>
    </div>
  );
}
