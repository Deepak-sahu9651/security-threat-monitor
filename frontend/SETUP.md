# Frontend Setup Guide

## Prerequisites

- Node.js 14+ or higher
- npm or yarn package manager

## Installation

### 1. Navigate to Frontend Directory

```bash
cd frontend
```

### 2. Install Dependencies

```bash
npm install
```

Or with yarn:

```bash
yarn install
```

### 3. Configure Environment Variables

```bash
cp .env.example .env
# Edit .env with your configuration
```

Example `.env`:

```
REACT_APP_API_URL=http://localhost:5000
REACT_APP_WS_URL=ws://localhost:5000
REACT_APP_ENV=development
```

### 4. Start Development Server

```bash
npm start
```

The frontend will open at `http://localhost:3000`

## Build for Production

```bash
npm run build
```

This creates an optimized production build in the `build/` directory.

## Available Scripts

- `npm start` - Start development server
- `npm build` - Build for production
- `npm test` - Run tests
- `npm eject` - Eject from Create React App (irreversible)

## Project Structure

```
frontend/
├── public/
│   └── index.html          # Main HTML file
├── src/
│   ├── components/         # Reusable React components
│   │   ├── Header.js
│   │   ├── ThreatDetail.js
│   │   ├── ThreatCard.js
│   │   └── StatCard.js
│   ├── pages/              # Page components
│   │   └── Dashboard.js
│   ├── App.js              # Main App component
│   ├── App.css             # App styles
│   ├── index.js            # Entry point
│   └── index.css           # Global styles
├── package.json            # Dependencies
├── .env.example            # Environment template
└── .gitignore              # Git ignore rules
```

## Components

### Header
- Displays title and connection status
- Shows connected clients count

### Dashboard
- Statistics overview with stat cards
- Threat list with filtering and sorting
- Multiple view modes (list/grid)

### ThreatCard
- Individual threat display
- Severity indicators
- Click for detailed view

### ThreatDetail
- Detailed threat information
- Recommended actions based on severity
- Technical details modal

## WebSocket Integration

The app connects to the backend via Socket.IO for real-time threat updates:

```javascript
const socket = io('http://localhost:5000');

// Subscribe to threats
socket.emit('subscribe_threats');

// Listen for new threats
socket.on('new_threat', (threat) => {
  // Handle new threat
});
```

## Styling

- **CSS Variables** for theming
- **Responsive Design** for mobile/tablet/desktop
- **Dark Theme** by default
- **Gradient Backgrounds** for modern look
- **Smooth Animations** for better UX

## Browser Support

- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Mobile browsers (iOS Safari, Chrome Mobile)

## Deployment

### Netlify

```bash
npm run build
# Deploy build/ folder to Netlify
```

### Vercel

```bash
npm run build
# Deploy to Vercel
```

### Docker

```dockerfile
FROM node:16-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
EXPOSE 3000
CMD ["npm", "start"]
```

## Troubleshooting

### Port Already in Use

```bash
PORT=3001 npm start  # Use different port
```

### Module Not Found

```bash
rm -rf node_modules package-lock.json
npm install
```

### WebSocket Connection Issues

Make sure backend is running and `.env` has correct URL.
