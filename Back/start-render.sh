#!/bin/bash
# Startup script for Render deployment
# This script initializes the database and starts Gunicorn with Uvicorn workers

set -e  # Exit on error

echo "========================================"
echo "Python Playground Backend - Render"
echo "========================================"

# Set Python path
export PYTHONPATH=/opt/render/project/src/Back:$PYTHONPATH

# Wait for database to be ready
echo "Waiting for database to be ready..."
python -c "
import time
import sys
from sqlalchemy import create_engine
from common.config import settings

max_retries = 30
for i in range(max_retries):
    try:
        engine = create_engine(settings.DATABASE_URL)
        connection = engine.connect()
        connection.close()
        print('Database is ready!')
        sys.exit(0)
    except Exception as e:
        if i < max_retries - 1:
            print(f'Waiting for database... ({i+1}/{max_retries})')
            time.sleep(2)
        else:
            print(f'Failed to connect to database: {e}')
            sys.exit(1)
"

# Initialize database tables
echo "Initializing database tables..."
python -c "
from common.database import Base, engine
from common.models import Submission, TestResult

print('Creating tables...')
Base.metadata.create_all(bind=engine)
print('Database initialized successfully!')
"

echo "========================================"
echo "Starting Gunicorn with Uvicorn workers..."
echo "========================================"

# Start Gunicorn with Uvicorn workers for ASGI support
exec gunicorn backend.app:app \
  --workers 4 \
  --worker-class uvicorn.workers.UvicornWorker \
  --bind 0.0.0.0:${PORT:-8000} \
  --access-logfile - \
  --error-logfile - \
  --log-level info
