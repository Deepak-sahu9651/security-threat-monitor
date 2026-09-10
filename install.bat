#!/bin/bash

echo "🛡️  Security Threat Monitor - Windows Setup"
echo "==========================================="
echo ""

REM Check Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python is not installed. Please install Python 3.8+
    exit /b 1
)
echo ✅ Python found

REM Check Node
node --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Node.js is not installed. Please install Node.js 14+
    exit /b 1
)
echo ✅ Node.js found

echo.
echo 📦 Setting up Backend...
cd backend
python -m venv venv
call venv\Scripts\activate.bat
pip install -r requirements.txt
copy .env.example .env
cd ..
echo ✅ Backend setup complete

echo.
echo 📦 Setting up Frontend...
cd frontend
call npm install
copy .env.example .env
cd ..
echo ✅ Frontend setup complete

echo.
echo ==========================================
echo ✅ Installation Complete!
echo.
echo 🚀 To start the application:
echo.
echo Terminal 1 - Backend:
echo   cd backend
echo   venv\Scripts\activate
echo   python app.py
echo.
echo Terminal 2 - Frontend:
echo   cd frontend
echo   npm start
echo.
echo Then open: http://localhost:3000
echo ==========================================
