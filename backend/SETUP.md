# Backend Setup Guide

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## Installation

### 1. Navigate to Backend Directory

```bash
cd backend
```

### 2. Create Virtual Environment (Optional but Recommended)

```bash
# On Linux/Mac
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

```bash
cp .env.example .env
# Edit .env with your configuration
```

### 5. Run the Backend Server

```bash
python app.py
```

The backend will start on `http://localhost:5000`

## API Endpoints

### REST API

- `GET /api/health` - Health check
- `GET /api/threats` - Get all threats
- `GET /api/threats/<id>` - Get threat details
- `GET /api/stats` - Get threat statistics
- `GET /api/config` - Get configuration

### WebSocket Events

- `connect` - Client connects
- `disconnect` - Client disconnects
- `subscribe_threats` - Subscribe to threat updates
- `unsubscribe_threats` - Unsubscribe from threats
- `new_threat` - New threat detected (broadcast)
- `stats_update` - Statistics updated (broadcast)

## Architecture

### Files

- **app.py** - Main Flask application with SocketIO
- **threat_detector.py** - Threat detection engine
- **config.py** - Configuration management
- **requirements.txt** - Python dependencies

### Threat Detection

The system detects:
- Failed login attempts
- Port scanning activity
- Privilege escalation attempts
- Suspicious processes
- Anomalous network traffic
- Unauthorized file access

## Development

### Adding New Threat Detectors

Edit `threat_detector.py` and add new detection methods:

```python
def _detect_your_threat(self):
    """Detect your custom threat"""
    threats = []
    # Your detection logic
    return threats
```

Then call it in `detect_threats()` method.

## Troubleshooting

### Port Already in Use

```bash
lsof -i :5000  # Find process
kill -9 <PID>  # Kill process
```

### Module Not Found

Ensure virtual environment is activated and dependencies installed:

```bash
pip install -r requirements.txt
```

### Connection Issues

Make sure CORS is enabled and frontend is configured with correct backend URL.
