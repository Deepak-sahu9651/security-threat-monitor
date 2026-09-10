import React, { useState, useEffect } from 'react';
import io from 'socket.io-client';
import axios from 'axios';
import './App.css';
import Header from './components/Header';
import ThreatDashboard from './pages/Dashboard';
import ThreatDetail from './components/ThreatDetail';

const App = () => {
  const [socket, setSocket] = useState(null);
  const [threats, setThreats] = useState([]);
  const [stats, setStats] = useState({
    total_threats: 0,
    critical: 0,
    high: 0,
    medium: 0,
    low: 0,
    connected_clients: 0,
    avg_response_time: 0
  });
  const [selectedThreat, setSelectedThreat] = useState(null);
  const [connectionStatus, setConnectionStatus] = useState('connecting');
  const [filterSeverity, setFilterSeverity] = useState(null);
  const [loading, setLoading] = useState(true);

  // Initialize WebSocket connection
  useEffect(() => {
    const apiUrl = process.env.REACT_APP_API_URL || 'http://localhost:5000';
    const socketUrl = process.env.REACT_APP_WS_URL || 'ws://localhost:5000';

    const newSocket = io(apiUrl, {
      reconnection: true,
      reconnectionDelay: 1000,
      reconnectionDelayMax: 5000,
      reconnectionAttempts: 5,
      transports: ['websocket', 'polling']
    });

    // Connection events
    newSocket.on('connect', () => {
      console.log('Connected to threat monitor');
      setConnectionStatus('connected');
      newSocket.emit('subscribe_threats');
      setLoading(false);
    });

    newSocket.on('disconnect', () => {
      console.log('Disconnected from threat monitor');
      setConnectionStatus('disconnected');
    });

    newSocket.on('connection_response', (data) => {
      console.log('Connection response:', data);
    });

    // Threat events
    newSocket.on('new_threat', (threat) => {
      console.log('New threat detected:', threat);
      setThreats(prevThreats => [threat, ...prevThreats].slice(0, 100)); // Keep last 100
    });

    newSocket.on('stats_update', (newStats) => {
      setStats(newStats);
    });

    setSocket(newSocket);

    // Fetch initial data
    fetchThreats();
    fetchStats();

    return () => {
      if (newSocket) {
        newSocket.disconnect();
      }
    };
  }, []);

  // Fetch threats from API
  const fetchThreats = async () => {
    try {
      const apiUrl = process.env.REACT_APP_API_URL || 'http://localhost:5000';
      const response = await axios.get(`${apiUrl}/api/threats`);
      setThreats(response.data.threats);
    } catch (error) {
      console.error('Error fetching threats:', error);
    }
  };

  // Fetch stats from API
  const fetchStats = async () => {
    try {
      const apiUrl = process.env.REACT_APP_API_URL || 'http://localhost:5000';
      const response = await axios.get(`${apiUrl}/api/stats`);
      setStats(response.data);
    } catch (error) {
      console.error('Error fetching stats:', error);
    }
  };

  // Filter threats by severity
  const filteredThreats = filterSeverity
    ? threats.filter(t => t.severity === filterSeverity)
    : threats;

  return (
    <div className="app">
      <Header 
        connectionStatus={connectionStatus} 
        totalClients={stats.connected_clients}
      />
      
      <div className="app-container">
        {loading ? (
          <div className="loading">
            <div className="spinner"></div>
            <p>Initializing Threat Monitor...</p>
          </div>
        ) : (
          <>
            <ThreatDashboard
              threats={filteredThreats}
              stats={stats}
              selectedThreat={selectedThreat}
              onSelectThreat={setSelectedThreat}
              filterSeverity={filterSeverity}
              onFilterChange={setFilterSeverity}
            />
            
            {selectedThreat && (
              <ThreatDetail
                threat={selectedThreat}
                onClose={() => setSelectedThreat(null)}
              />
            )}
          </>
        )}
      </div>
    </div>
  );
};

export default App;
