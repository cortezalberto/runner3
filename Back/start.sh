#!/bin/bash
# Python Playground - Backend Only Startup Script

echo "========================================"
echo "Python Playground - Backend Only"
echo "========================================"
echo ""

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "ERROR: Docker is not running!"
    echo "Please start Docker and try again."
    exit 1
fi

echo "[1/3] Building runner image..."
if ! docker build -t py-playground-runner:latest ./runner; then
    echo "ERROR: Failed to build runner image!"
    exit 1
fi

echo ""
echo "[2/3] Starting backend services (postgres, redis, backend, worker)..."
if ! docker compose up -d; then
    echo "ERROR: Failed to start services!"
    exit 1
fi

echo ""
echo "[3/3] Waiting for services to be healthy..."
sleep 10

echo ""
echo "========================================"
echo "Backend Started Successfully!"
echo "========================================"
echo ""
echo "API Endpoint: http://localhost:49000"
echo "Swagger Docs: http://localhost:49000/docs"
echo "Health Check: http://localhost:49000/api/health"
echo ""
echo "To view logs:    docker compose logs -f"
echo "To stop:         docker compose down"
echo ""
echo "Testing the backend..."
if curl -s http://localhost:49000/api/health > /dev/null 2>&1; then
    echo ""
    echo "✅ Backend is healthy and ready to accept connections!"
else
    echo ""
    echo "⚠️  Note: Backend may still be starting up. Wait a few seconds and try:"
    echo "   curl http://localhost:49000/api/health"
fi

echo ""
