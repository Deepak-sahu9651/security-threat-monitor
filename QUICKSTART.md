# Security Threat Monitor - Quick Start Guide

## 🚀 Get Started in 5 Minutes

### Prerequisites
- Python 3.8+
- Node.js 14+
- git

### Step 1: Clone Repository

```bash
git clone https://github.com/Deepak-sahu9651/security-threat-monitor.git
cd security-threat-monitor
```

### Step 2: Start Backend (Terminal 1)

```bash
cd backend
python -m venv venv

# Linux/Mac
source venv/bin/activate
# Windows
venv\Scripts\activate

pip install -r requirements.txt
python app.py
```

✅ Backend running on `http://localhost:5000`

### Step 3: Start Frontend (Terminal 2)

```bash
cd frontend
npm install
npm start
```

✅ Frontend running on `http://localhost:3000`

### Step 4: Open Dashboard

Visit: **http://localhost:3000** 🎉

## 📊 Dashboard Features

✅ **Real-time Threat Detection**
- Live threat feed with WebSocket updates
- Threats appear instantly as they're detected

✅ **Statistics Dashboard**
- Total threats count
- Severity breakdown (Critical, High, Medium, Low)
- Average response time

✅ **Threat Filtering**
- Filter by severity level
- Sort by timestamp or severity
- Switch between list and grid view

✅ **Detailed Threat Analysis**
- Click any threat for detailed information
- View threat source and timestamp
- Get recommended actions
- See technical details

## 🎯 Demo Threats

The system simulates various threats:
- 🚨 **Failed Login Attempts** - Multiple auth failures
- 🚨 **Port Scanning** - Suspicious port access
- 🚨 **Privilege Escalation** - Unauthorized sudo attempts
- 🚨 **Suspicious Processes** - Malware-like process execution
- 🚨 **Unauthorized File Access** - System file tampering
- 🚨 **Anomalous Network Traffic** - Unusual data flows

## 📱 User Interface

### Header
- Connection status indicator
- Connected clients counter
- Real-time status updates

### Statistics Cards
- Color-coded by severity
- Quick overview metrics
- Trending indicators

### Threat Cards
- Threat type and source
- Severity badge
- Time since detection
- Click to view details

### Threat Modal
- Detailed threat information
- Technical specifications
- Recommended actions
- Easy-to-read format

## 🔧 Configuration

### Backend Config (backend/.env)

```
FLASK_ENV=development
DEBUG=True
THREAT_CHECK_INTERVAL=5
FAILED_LOGIN_THRESHOLD=5
```

### Frontend Config (frontend/.env)

```
REACT_APP_API_URL=http://localhost:5000
REACT_APP_WS_URL=ws://localhost:5000
REACT_APP_ENV=development
```

## 📈 Architecture

```
┌─────────────────────────────────────────────┐
│         React Dashboard (Frontend)          │
│  - Real-time threat visualization          │
│  - Interactive filtering & sorting          │
│  - Responsive design                       │
└────────────────┬────────────────────────────┘
                 │ WebSocket + REST API
                 │
┌────────────────┴────────────────────────────┐
│      Flask Backend with SocketIO            │
│  - Threat detection engine                  │
│  - Real-time event broadcasting             │
│  - Threat analysis & statistics             │
└─────────────────────────────────────────────┘
```

## 🎮 Try These Actions

1. **Monitor Real-time Threats**
   - Watch threats appear automatically
   - See statistics update in real-time

2. **Filter by Severity**
   - Click severity buttons to filter
   - See how many threats in each level

3. **View Threat Details**
   - Click any threat card
   - Read recommended actions
   - View technical details

4. **Switch View Modes**
   - Toggle between list and grid view
   - Sort by severity or timestamp

## 🚀 Hackathon Tips

✅ **Impress with:**
- Real-time threat detection
- Beautiful, modern UI
- Detailed threat analysis
- Professional dashboard
- Clean code structure

✅ **Demo Script:**
1. Show connection status
2. Point out statistics cards
3. Click on high/critical threats
4. Show threat details modal
5. Explain severity levels
6. Mention filter capabilities

## 🔮 Future Enhancements

- [ ] Machine learning for anomaly detection
- [ ] Database integration for persistence
- [ ] User authentication & roles
- [ ] Alert notifications (email/Slack)
- [ ] Threat response automation
- [ ] Advanced analytics & reporting
- [ ] Mobile app
- [ ] Cloud deployment

## 📚 Documentation

- **Backend Setup**: See `backend/SETUP.md`
- **Frontend Setup**: See `frontend/SETUP.md`
- **Full README**: See `README.md`

## 💡 Troubleshooting

### Backend won't start
```bash
# Check if port 5000 is free
lsof -i :5000
# Install dependencies
pip install -r requirements.txt
```

### Frontend won't connect
```bash
# Check .env file
cat frontend/.env
# Ensure backend is running
curl http://localhost:5000/api/health
```

### No threats showing
- Wait 5-10 seconds for demo threats to generate
- Check browser console for errors
- Verify WebSocket connection in DevTools

## 🎯 Project Stats

- **Languages**: Python, JavaScript, CSS
- **Components**: 6 React components
- **Real-time**: WebSocket-powered
- **Responsive**: Mobile, Tablet, Desktop
- **Build Time**: ~2 days (hackathon)
- **LOC**: ~2000+ lines

## 📞 Support

For issues or questions:
1. Check the troubleshooting section
2. Review component documentation
3. Check browser console for errors
4. Verify environment configuration

---

**Happy Hacking! 🎉** 🛡️ 🔐 💻
