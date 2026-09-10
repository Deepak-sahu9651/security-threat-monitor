# Real-Time Security Threat Monitor 🛡️

A real-time security threat detection dashboard that monitors system and network activities, identifies suspicious patterns, and displays security alerts.

## Features 🚀

- **Real-time Monitoring**: Live detection of security threats
- **Threat Detection**: 
  - Failed login attempts
  - Unusual network traffic patterns
  - Privilege escalation attempts
  - Suspicious file access
  - Port scanning activity
- **Interactive Dashboard**: Beautiful React-based UI with real-time updates
- **Alert System**: Instant notifications for detected threats
- **Threat Severity Levels**: Critical, High, Medium, Low
- **Historical Data**: View and analyze past threats
- **WebSocket Integration**: Real-time data streaming

## Project Structure

```
security-threat-monitor/
├── backend/                 # Python Flask API
│   ├── app.py              # Main Flask application
│   ├── threat_detector.py  # Threat detection logic
│   ├── log_parser.py       # System log parser
│   ├── requirements.txt    # Python dependencies
│   └── config.py           # Configuration settings
├── frontend/               # React Dashboard
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── App.js
│   │   └── index.js
│   ├── package.json
│   └── .env
└── README.md
```

## Tech Stack 🛠️

### Backend
- **Python 3.8+**
- **Flask** - Web framework
- **Flask-SocketIO** - WebSocket support
- **PyYAML** - Config management
- **psutil** - System monitoring

### Frontend
- **React 18**
- **WebSocket** - Real-time communication
- **Chart.js/React-Chartjs-2** - Threat visualization
- **Tailwind CSS** - Styling
- **Axios** - HTTP client

## Installation & Setup

### Prerequisites
- Python 3.8+
- Node.js 14+
- npm/yarn

### Backend Setup

```bash
cd backend
pip install -r requirements.txt
python app.py
```

The backend runs on `http://localhost:5000`

### Frontend Setup

```bash
cd frontend
npm install
npm start
```

The frontend runs on `http://localhost:3000`

## How It Works 🔍

1. **Backend** monitors system logs and network activity
2. **Threat Detection Engine** analyzes patterns for suspicious behavior
3. **WebSocket Server** sends real-time alerts to frontend
4. **Dashboard** visualizes threats with severity levels
5. **Alert System** notifies users of critical threats

## Threat Detection Patterns

- ❌ Multiple failed login attempts (>5 in 5 minutes)
- ❌ Unusual port access patterns
- ❌ Privilege escalation attempts
- ❌ Suspicious file modifications
- ❌ Abnormal network traffic
- ❌ Unauthorized access attempts

## Usage

1. Start both backend and frontend servers
2. Open dashboard at `http://localhost:3000`
3. Monitor threats in real-time
4. Click on threats for detailed information
5. Filter by severity level
6. View threat history

## API Endpoints

### WebSocket
- `ws://localhost:5000/socket.io` - Real-time threat stream

### REST API
- `GET /api/threats` - Get all threats
- `GET /api/threats/<id>` - Get threat details
- `GET /api/stats` - Get threat statistics
- `GET /api/health` - Check backend health

## Demo Data

The application includes mock threat data for demonstration. In production, connect to real system logs.

## Team 👥

Built for hackathon by a 2-person team

## License

MIT License

## Next Steps

- [ ] Integrate real system log parsing
- [ ] Add machine learning for anomaly detection
- [ ] Implement threat response automation
- [ ] Add database for persistent storage
- [ ] Deploy to cloud
- [ ] Add authentication system