#!/bin/bash

echo "🛡️  Security Threat Monitor - Docker Setup"
echo "=========================================="
echo ""

# Check Docker
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed"
    echo "Please install Docker from: https://docs.docker.com/get-docker/"
    exit 1
fi
echo "✅ Docker found: $(docker --version)"

# Check Docker Compose
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed"
    echo "Please install Docker Compose from: https://docs.docker.com/compose/install/"
    exit 1
fi
echo "✅ Docker Compose found: $(docker-compose --version)"

echo ""
echo "🏗️  Building Docker images..."
docker-compose build

echo ""
echo "✅ Build Complete!"
echo ""
echo "🚀 To start the application:"
echo "  docker-compose up"
echo ""
echo "Then open: http://localhost:3000"
echo "=========================================="
