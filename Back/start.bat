@echo off
REM Python Playground - Backend Only Startup Script

echo ========================================
echo Python Playground - Backend Only
echo ========================================
echo.

REM Check if Docker is running
docker info >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Docker is not running!
    echo Please start Docker Desktop and try again.
    pause
    exit /b 1
)

echo [1/3] Building runner image...
docker build -t py-playground-runner:latest ./runner
if %errorlevel% neq 0 (
    echo ERROR: Failed to build runner image!
    pause
    exit /b 1
)

echo.
echo [2/3] Starting backend services (postgres, redis, backend, worker)...
docker compose up -d
if %errorlevel% neq 0 (
    echo ERROR: Failed to start services!
    pause
    exit /b 1
)

echo.
echo [3/3] Waiting for services to be healthy...
timeout /t 10 /nobreak >nul

echo.
echo ========================================
echo Backend Started Successfully!
echo ========================================
echo.
echo API Endpoint: http://localhost:49000
echo Swagger Docs: http://localhost:49000/docs
echo Health Check: http://localhost:49000/api/health
echo.
echo To view logs:    docker compose logs -f
echo To stop:         docker compose down
echo.
echo Testing the backend...
curl http://localhost:49000/api/health 2>nul
if %errorlevel% equ 0 (
    echo.
    echo Backend is healthy and ready to accept connections!
) else (
    echo.
    echo Note: Backend may still be starting up. Wait a few seconds and try:
    echo   curl http://localhost:49000/api/health
)

echo.
pause
