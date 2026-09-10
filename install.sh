#!/bin/bash

echo "🛡️  Security Threat Monitor - Installation Script"
echo "================================================="
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8+"
    exit 1
fi
echo "✅ Python 3 found: $(python3 --version)"

# Check Node
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js 14+"
    exit 1
fi
echo "✅ Node.js found: $(node --version)"

echo ""
echo "📦 Setting up Backend..."
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
cd ..
echo "✅ Backend setup complete"

echo ""
echo "📦 Setting up Frontend..."
cd frontend
npm install
cp .env.example .env
cd ..
echo "✅ Frontend setup complete"

echo ""
echo "================================================="
echo "✅ Installation Complete!"
echo ""
echo "🚀 To start the application:"
echo ""
echo "Terminal 1 - Backend:"
echo "  cd backend"
echo "  source venv/bin/activate  # On Windows: venv\\Scripts\\activate"
echo "  python app.py"
echo ""
echo "Terminal 2 - Frontend:"
echo "  cd frontend"
echo "  npm start"
echo ""
echo "Then open: http://localhost:3000"
echo "================================================="
