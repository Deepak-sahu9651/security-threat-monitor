# Security Threat Monitor - Makefile

.PHONY: help install setup-backend setup-frontend start-backend start-frontend start-all docker-build docker-up docker-down clean

help:
	@echo "Security Threat Monitor - Available Commands"
	@echo ""
	@echo "Development:"
	@echo "  make setup-backend      - Setup Python backend"
	@echo "  make setup-frontend     - Setup Node.js frontend"
	@echo "  make start-backend      - Start Flask backend"
	@echo "  make start-frontend     - Start React frontend"
	@echo "  make start-all          - Start both backend and frontend"
	@echo ""
	@echo "Docker:"
	@echo "  make docker-build       - Build Docker images"
	@echo "  make docker-up          - Start with Docker Compose"
	@echo "  make docker-down        - Stop Docker containers"
	@echo ""
	@echo "Maintenance:"
	@echo "  make clean              - Clean up generated files"

setup-backend:
	cd backend && python -m venv venv && . venv/bin/activate && pip install -r requirements.txt && cp .env.example .env

setup-frontend:
	cd frontend && npm install && cp .env.example .env

start-backend:
	cd backend && . venv/bin/activate && python app.py

start-frontend:
	cd frontend && npm start

start-all:
	@echo "Starting both frontend and backend..."
	@echo "Open two terminal windows and run:"
	@echo "Terminal 1: make start-backend"
	@echo "Terminal 2: make start-frontend"

docker-build:
	docker-compose build

docker-up:
	docker-compose up

docker-down:
	docker-compose down

clean:
	rm -rf backend/venv frontend/node_modules frontend/build
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name '*.pyc' -delete
