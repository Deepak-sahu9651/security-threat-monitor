# Deployment Guide

## Local Development

See QUICKSTART.md for quick setup.

## Docker Deployment

### Build Docker Images

```bash
# Backend
cd backend
docker build -t threat-monitor-backend .
cd ..

# Frontend
cd frontend
docker build -t threat-monitor-frontend .
cd ..
```

### Run with Docker Compose

```bash
docker-compose up
```

## Cloud Deployment

### Heroku (Backend)

```bash
# Install Heroku CLI
heroku login
heroku create threat-monitor-api

# Deploy backend
cd backend
git push heroku main
```

### Vercel (Frontend)

```bash
npm i -g vercel
vercel --prod
```

### AWS EC2

1. Launch EC2 instance (Ubuntu)
2. Install dependencies: `sudo apt-get install python3 nodejs npm`
3. Clone repository
4. Run setup scripts
5. Use PM2 for process management

## Production Configuration

### Backend (.env)

```
FLASK_ENV=production
DEBUG=False
SECRET_KEY=your-secret-key-here
THREAT_CHECK_INTERVAL=10
```

### Frontend (.env)

```
REACT_APP_API_URL=https://api.yourdomain.com
REACT_APP_WS_URL=wss://api.yourdomain.com
REACT_APP_ENV=production
```

## Security Considerations

- Use HTTPS/WSS for all connections
- Implement authentication
- Validate all inputs
- Use environment variables for secrets
- Enable CORS only for trusted domains
- Implement rate limiting
- Add DDoS protection
