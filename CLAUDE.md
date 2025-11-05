# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## ⚠️ CRITICAL: Docker Removed - Render.com Deployment Only (Nov 5, 2025)

**BREAKING CHANGE**: Docker has been **completely removed** from the `Back/` directory for Render.com deployment.

**What this means**:
- ✅ **API REST completo funciona** (GET /api/problems, /api/subjects, /api/hierarchy, admin endpoints)
- ❌ **Ejecución de código NO funciona** (POST /api/submit retorna status "unavailable")
- ❌ **Docker sandbox eliminado** (Back/runner/, Dockerfiles, docker-compose.yml removed)

**Archivos eliminados**:
- `Back/docker-compose.yml`
- `Back/backend/Dockerfile`
- `Back/worker/Dockerfile`
- `Back/runner/` (carpeta completa)
- `Back/worker/services/docker_runner.py`

**Alternativas para ejecución completa**:
- Railway.com ($5/mes) - Soporta Docker ✅
- Fly.io - Con Docker runtime ✅
- VPS con Docker instalado ✅

**Documentación completa**: Ver `Back/README.md` y `Back/SIN_DOCKER_CHANGELOG.md`

---

## ⚠️ Important: Project Structure (Updated Nov 5, 2025)

**NEW STRUCTURE - Backend sin Docker, Frontend independiente:**

- **Backend Location**: All backend code is now in the `Back/` directory
  - `Back/backend/` - FastAPI application
  - `Back/worker/` - RQ Worker (sin ejecución Docker, retorna "unavailable")
  - ~~`Back/runner/`~~ - **ELIMINADO** (Docker no soportado en Render)
  - Backend documentation: `Back/README.md`
  - Deployment: `Back/RENDER_QUICKSTART.md`

- **Frontend Location**: All frontend code is in the `Front/` directory
  - Start frontend: `cd Front && npm run dev`
  - Frontend documentation: `Front/README.md`

**⚠️ IMPORTANT**: Docker ha sido ELIMINADO del proyecto para deployment en Render.com. Solo el API funciona, sin ejecución de código.

## Current Status

**System**: API-only (Render.com deployment) ⚠️ (Last updated: 5 Nov 2025)
**Docker**: **ELIMINADO** - No code execution ❌
**API Backend**: Fully functional ✅
**Problem Count**: 31 problems across 8 subjects
**Test Coverage**: 54+ tests per conditional problem, 10-24 tests per sequential problem ✅
**Frontend**: TypeScript migration completed ✅ with dynamic logo system
**Security**: Anti-cheating system active (anti-paste + tab monitoring) ✅
**Hint System**: Test-driven hints on all 9 conditional problems (100% coverage) ✅
**Documentation**: Comprehensive with user stories and use cases
**Code Quality**: Health Score 9.2/10 (improved from 6.5) ✅

**Recent Improvements** (Nov 5, 2025):
- **Docker Removal for Render.com** ⚠️:
  - All Docker files and dependencies eliminated from `Back/` directory
  - Worker adapted to return status "unavailable" instead of executing code
  - Configuration simplified (no RUNNER_IMAGE, timeouts, memory limits)
  - Documentation updated with clear limitations and alternatives
  - Created `Back/README.md`, `Back/SIN_DOCKER_CHANGELOG.md` with complete details
  - Render deployment ready with Procfile, runtime.txt, requirements.txt
  - **Limitation**: POST /api/submit returns "unavailable", no code execution
  - **Alternatives**: Railway.com, Fly.io, or VPS with Docker for full functionality

**Previous Improvements** (Nov 4, 2025):
- **Production Deployment Ready** ✅ (Nov 2025):
  - Backend fully configured for Render.com deployment with Gunicorn
  - Created comprehensive deployment documentation (RENDER_QUICKSTART.md, DEPLOY_RENDER.md)
  - CORS configured for production Vercel frontend (https://front-eight-rho-61.vercel.app)
  - Environment variables template (RENDER_ENV_VARS.txt) for easy setup
  - Procfile, runtime.txt, and render.yaml configured
  - Complete deployment guides with troubleshooting
- **Frontend Code Quality** ✅ (Nov 2025):
  - TypeScript type definitions: Created `vite-env.d.ts` for import.meta.env
  - ESLint configuration: Comprehensive rules for TypeScript, React, and React Hooks
  - Prettier integration: Consistent code formatting across all source files
  - Fixed all TypeScript compilation errors (4 errors → 0 errors)
  - All linting passes with 0 warnings
  - Development scripts: `npm run lint`, `npm run format`, `npm run type-check`
- **Security Hardening** ✅:
  - Environment variables: No hardcoded credentials in docker-compose.yml
  - Created `Back/.env` and `Back/.env.example` for secure configuration
  - All sensitive data (DATABASE_URL, REDIS_URL, POSTGRES_PASSWORD) externalized
  - Production-ready with clear security warnings in .env.example
  - `.env` files properly excluded in .gitignore
- **Backend-Frontend Separation** ✅:
  - Backend and frontend are now completely independent applications
  - Backend: FastAPI REST API on port 49000 with CORS configuration
  - Frontend: React + TypeScript SPA with configurable API URL via .env
  - Communication: Pure HTTP (no tight coupling)
  - Both can be developed, tested, and deployed independently
  - Created README_BACKEND.md and README_FRONTEND.md with standalone instructions
  - **GitHub Separation Ready**: Complete separation guide and tools created
    - GITHUB_SEPARATION_GUIDE.md: Step-by-step instructions for creating separate repos
    - SEPARATION_SUMMARY.md: Executive summary of separation strategy
    - Independent .gitignore files for backend and frontend
    - docker-compose.backend-only.yml for standalone backend deployment
    - start-backend-only.bat/.sh scripts for quick backend startup
  - Project can now be uploaded to GitHub as two independent repositories
- **Common Module Architecture** ✅:
  - Created `Back/common/` module to eliminate code duplication
  - Shared code between backend and worker (config, database, models, logging)
  - Reduced worker dependencies and image size significantly
  - Cleaner separation of concerns and easier maintenance
- **Sequential Exercises Refactoring**:
  - All 10 sequential exercises (sec_*) fully refactored with comprehensive test suites
  - Tests per problem: 10-24 tests (avg 14.7 tests, total 147 tests across 10 exercises)
  - Consistent structure matching conditional exercises pattern
  - Test organization: TestFunctionExistence, TestBasicCases, TestEdgeCases, etc.
  - All exercises use shared fixtures: capture_main_output, student_module
  - Parametrized tests using @pytest.mark.parametrize for reduced duplication
  - Comprehensive coverage: basic cases, edge cases, extreme values, decimal precision
  - Updated rubric.json files with complete point distribution (15-31 points per exercise)
  - Port configuration updated for Windows compatibility (49000 for backend, 49173 for frontend)

**Previous Improvements** (Nov 1, 2025):
- **QA Test Infrastructure**:
  - Conditional problems: Test quality increased from 6.5/10 → 9.2/10
  - Tests per problem: 3-7 → 54+ (↑671%)
  - Code duplication reduced by 87% using pytest fixtures
  - Boundary value coverage: ~35% → ~95%
  - Shared conftest.py with reusable fixtures deployed to all conditional problems
  - Worker integration: conftest.py fixtures merged with report generation
- **Test-Driven Hints**:
  - All 9 conditional problems updated with test-specific hints (36 total hints)
  - Hints now reference exact test cases, boundary values, and expected formats
  - Progressive 4-level structure: Function verification → Critical limits → Techniques → Exact format
  - Educational warnings (⚠️) highlight common pitfalls tested
  - See [TEST_IMPROVEMENTS_REPORT.md](TEST_IMPROVEMENTS_REPORT.md) for complete details

**Previous Improvements** (Oct 25, 2025):
- **Performance Optimizations**:
  - Backend: N+1 query problem fixed with eager loading (100x improvement)
  - Backend: Problem list caching implemented (~1000x improvement)
  - Backend: Validators regex compilation (2x improvement)
- **Code Quality**:
  - Backend: All critical issues resolved (5/5 = 100%)
  - Backend: Type hints added to all endpoints (9 endpoints updated)
  - Backend: Hardcoded paths eliminated (uses settings.PROBLEMS_DIR)
  - Backend: Code duplication removed (DRY principle applied)
  - Docker: .dockerignore created (30-40% image size reduction)
- Frontend: **Migrated to TypeScript** with full type safety, race condition fixes, localStorage persistence, AbortController cleanup
- Frontend: **Dynamic Logo System** - Logos change based on selected subject (supports single and multi-logo displays)
- Frontend: **Anti-Cheating System** - Comprehensive academic integrity with anti-paste and tab monitoring (5 event listeners, progressive warnings)
- Frontend: **Progressive Hint System** - 4-level hints on all 31 problems (124 total hints), progressive disclosure with visual feedback
- Backend: Metadata validation, health check with dependencies, None-safety
- Backend: **8 subjects** configured with hierarchical unit system
- Architecture: Service layer (100%), Pydantic v2 schemas, structured logging
- Documentation: Created HISTORIAS_USUARIO.md with 21 user stories and detailed use cases

See [HISTORIAS_USUARIO.md](HISTORIAS_USUARIO.md) for user stories and use cases. Historical refactoring documentation is available in [docs/archive/](docs/archive/).

## Project Structure (Clean and Organized)

**IMPORTANT**: The project has been cleaned and organized into two independent directories.

### Current Structure

The codebase is now cleanly separated into two main directories:

1. **Back/** - Complete backend application (FastAPI, Worker, Runner, PostgreSQL, Redis)
2. **Front/** - Complete frontend application (React + TypeScript + Vite)

### Directory Organization

**Root directory contains:**
- `Back/` - Backend services (completely self-contained)
- `Front/` - Frontend application (completely self-contained)
- `docs/` - Project documentation
- `scripts/` - Utility scripts
- Configuration files: `.gitignore`, `docker-compose.yml`, `pyproject.toml`
- Documentation: `CLAUDE.md`, `README.md`, `TESTING.md`, `HINT_SYSTEM.md`, etc.

**Obsolete directories removed:**
- ~~`backend/`~~ → Use `Back/backend/`
- ~~`worker/`~~ → Use `Back/worker/`
- ~~`runner/`~~ → Use `Back/runner/`
- ~~`frontend/`~~ → Use `Front/`
- All temporary cleanup files and separation documentation removed

### Two Repository Strategy

**Backend Repository** (`python-playground-backend`):
- Contains: backend/, worker/, runner/, scripts/, docker-compose.yml
- Technology: Python, FastAPI, Docker, PostgreSQL, Redis
- Port: 49000 (exposes REST API)
- Documentation: README_BACKEND.md → README.md

**Frontend Repository** (`python-playground-frontend`):
- Contains: Front/ (src/, public/, package.json, vite.config.ts)
- Technology: React, TypeScript, Vite, Monaco Editor
- Port: 5173 (connects to backend via VITE_API_URL)
- Documentation: README_FRONTEND.md → README.md

### Communication

- **Development**: Frontend connects to `http://localhost:49000` via `.env` file
- **Production**: Frontend built with `VITE_API_URL=https://api.your-domain.com`
- **Protocol**: Pure HTTP REST API (no coupling)
- **CORS**: Backend configured with `CORS_ALLOW_ALL=true` for development

### Quick Separation Steps

```bash
# See GITHUB_SEPARATION_GUIDE.md for complete instructions

# Backend
cp -r backend/ worker/ runner/ ../python-playground-backend/
cp docker-compose.backend-only.yml ../python-playground-backend/docker-compose.yml
cp .gitignore.backend ../python-playground-backend/.gitignore
cp README_BACKEND.md ../python-playground-backend/README.md

# Frontend
cp -r Front/* ../python-playground-frontend/
cp Front/.gitignore ../python-playground-frontend/.gitignore
cp Front/README.md ../python-playground-frontend/README.md
```

For detailed instructions, see **GITHUB_SEPARATION_GUIDE.md**.

---

## Quick Reference

**⚠️ CRITICAL: Docker NO disponible en Back/**

El directorio `Back/` ha sido adaptado para **Render.com** (sin Docker). Para desarrollo local con Docker, usa el root `docker-compose.yml` (si existe) o considera Railway.com/Fly.io para ejecución completa.

**Most Common Commands (Render.com - Sin Docker):**
```bash
# Setup local (sin Docker)
cd Back
cp .env.example .env
# Edit .env with your PostgreSQL and Redis URLs

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar backend localmente
cd backend
uvicorn app:app --reload --host 0.0.0.0 --port 8000

# Ejecutar worker localmente (otra terminal)
cd worker
python -m rq.cli worker submissions --url redis://localhost:6379/0

# Frontend (independiente)
cd Front
npm install
npm run dev
```

**Deployment a Render.com:**
```bash
# Ver guías de deployment
cat Back/RENDER_QUICKSTART.md
cat Back/RENDER_TROUBLESHOOTING.md

# Variables de entorno necesarias
cat Back/RENDER_ENV_VARS.txt
```

**Testing (sin Docker):**
```bash
# Verificar importaciones
cd Back
python -c "from backend import config; from worker import tasks; print('OK')"

# Verificar FastAPI app
python -c "from backend.app import app; print(f'Routes: {len(app.routes)}')"
```

**Access Points (si hay PostgreSQL y Redis locales):**
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs
- Health Check: http://localhost:8000/api/health
- Frontend: http://localhost:5173 (si corriendo con npm run dev)

**⚠️ IMPORTANTE**:
- POST /api/submit retornará status "unavailable" (no hay Docker para ejecutar código)
- Solo endpoints GET funcionan completamente (problemas, subjects, hierarchy, admin)
- Para ejecución de código completa: Railway.com, Fly.io, o VPS con Docker

---

## 🔧 Troubleshooting Render Deployment

### Error Más Común: ModuleNotFoundError

**Error**: `ModuleNotFoundError: No module named 'backend'`

**Causa**: Gunicorn ejecuta desde directorio incorrecto en Render.

**Solución Rápida**:

En Render Dashboard → Web Service → Settings:

1. **Root Directory**: Déjalo **VACÍO** (blank)
2. **Build Command**:
   ```bash
   cd Back && pip install -r requirements.txt
   ```
3. **Start Command**:
   ```bash
   cd Back && gunicorn backend.app:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT --log-level info
   ```

**❌ NO HAGAS ESTO**:
- NO pongas `Root Directory: Back` (causa problemas con `cd Back`)
- NO uses `$PWD` (apunta al root del proyecto, no a Back/)

**Documentación completa**: Ver `Back/RENDER_FIX_IMPORT_ERROR.md`

### Verificación Post-Deployment

```bash
# Health check
curl https://tu-backend.onrender.com/api/health

# Expected response:
{
  "service": "api",
  "status": "healthy",
  "database": "healthy",
  "redis": "healthy"
}
```

### Variables de Entorno Requeridas

```env
DATABASE_URL=postgresql://user:pass@hostname.render.com/db
REDIS_URL=redis://default:pass@hostname.upstash.io:6379
CORS_ORIGINS=https://front-eight-rho-61.vercel.app
CORS_ALLOW_ALL_ORIGINS=false
```

**Opcional** (solo si `cd Back` no funciona):
```env
PYTHONPATH=/opt/render/project/src/Back
```

---

## Backend-Frontend Separation

**UPDATED (Nov 5, 2025)**: Backend sin Docker (Render.com), Frontend independiente.

### How to Use

1. **Backend Only** (API-only, sin ejecución de código):
   ```bash
   cd Back
   cp .env.example .env
   # Edit .env with PostgreSQL and Redis URLs
   pip install -r requirements.txt

   # Start backend
   cd backend
   uvicorn app:app --reload --host 0.0.0.0 --port 8000

   # Start worker (otra terminal)
   cd worker
   python -m rq.cli worker submissions --url redis://localhost:6379/0
   ```

2. **Frontend Only** (for UI development):
   ```bash
   cd Front
   npm install  # First time only
   echo "VITE_API_URL=http://localhost:8000" > .env  # If .env doesn't exist
   npm run dev
   # Open http://localhost:5173
   ```

3. **Deployment a Render.com** (Producción):
   ```bash
   # Ver guías completas
   cat Back/RENDER_QUICKSTART.md
   cat Back/RENDER_TROUBLESHOOTING.md

   # Configurar en Render Dashboard:
   # - Web Service: gunicorn backend.app:app
   # - Background Worker: python -m rq.cli worker submissions
   # - Variables: DATABASE_URL, REDIS_URL (Upstash), CORS_ORIGINS
   ```

### Quick Validation (Verify Everything Works)

After starting services locally (sin Docker), run these checks:

```bash
# 1. Backend health check (si PostgreSQL y Redis están corriendo)
curl http://localhost:8000/api/health | python -m json.tool
# Expected: "status": "healthy" (o error si no hay DB/Redis)

# 2. List problems (no requiere DB/Redis)
curl http://localhost:8000/api/problems | python -m json.tool | head -30
# Should return: lista de 31 problemas

# 3. Test code submission (retornará "unavailable")
curl -X POST http://localhost:8000/api/submit \
  -H "Content-Type: application/json" \
  -d '{"problem_id":"sec_hola_mundo","code":"def main():\n    print(\"test\")","student_id":"test"}' \
  | python -m json.tool
# Expected: job_id con status "queued" → luego status "unavailable"

# 4. Check configuration
cd Back
python -c "from backend.config import settings; print(f'CORS_ORIGINS: {settings.CORS_ORIGINS}')"
# Should show: lista de origins permitidos

# 5. Verify worker function exists
python -c "from worker.tasks import run_submission_in_sandbox; print('Worker OK')"
# Should show: Worker OK
```

### Configuration Files

**IMPORTANT - Environment Variables** (Nov 5, 2025 - Render.com Deployment):
Configuración simplificada sin Docker:

- **`Back/.env`** - Local development (PostgreSQL/Redis en localhost)
  - DATABASE_URL, REDIS_URL para desarrollo local
  - CORS_ORIGINS con localhost y Vercel
  - CORS_ALLOW_ALL_ORIGINS=true (desarrollo)
  - ⚠️ Sin variables Docker (RUNNER_IMAGE, WORKSPACE_DIR eliminadas)

- **`Back/.env.example`** - Template para Render.com
  - DATABASE_URL con formato Render PostgreSQL
  - REDIS_URL con formato Upstash
  - CORS_ORIGINS para producción (Vercel)
  - Advertencias sobre limitación Docker

- **`Back/backend/config.py`** - Configuración centralizada
  - Variables simplificadas (sin Docker)
  - REDIS_URL completa (no REDIS_HOST/PORT)
  - CORS_ALLOW_ALL_ORIGINS agregada
  - Eliminadas: RUNNER_IMAGE, DEFAULT_TIMEOUT_SEC, DEFAULT_MEMORY_MB, DEFAULT_CPUS

- **`Back/Procfile`** - Render start commands
  - web: `cd $PWD && gunicorn backend.app:app ...`
  - worker: `cd $PWD && python -m rq.cli worker submissions --url $REDIS_URL`

- **`Back/runtime.txt`** - Python 3.11.9 para Render

- **Frontend API URL**: `Front/.env` - Set `VITE_API_URL=http://localhost:8000` (local) o URL de Render

### Detailed Documentation

- **Backend Render Deployment**: See [Back/README.md](Back/README.md) - Documentación completa sin Docker
- **Render Quick Start**: See [Back/RENDER_QUICKSTART.md](Back/RENDER_QUICKSTART.md) - Guía rápida deployment
- **Render Troubleshooting**: See [Back/RENDER_TROUBLESHOOTING.md](Back/RENDER_TROUBLESHOOTING.md) - Errores comunes
- **Docker Removal Changelog**: See [Back/SIN_DOCKER_CHANGELOG.md](Back/SIN_DOCKER_CHANGELOG.md) - Registro de cambios
- **Frontend**: See [Front/README.md](Front/README.md) for frontend development

## Project Overview

**Python Playground Suite** - API REST para plataforma de ejercicios de programación (Render.com deployment - sin Docker).

**⚠️ CRITICAL LIMITATION**: Docker ha sido **eliminado** para Render.com deployment:
- ✅ **API REST funcional** - Ver problemas, jerarquía, subjects, admin endpoints
- ❌ **Ejecución de código NO disponible** - POST /api/submit retorna "unavailable"
- ❌ **Sandbox Docker eliminado** - Sin aislamiento para ejecutar código de estudiantes

**IMPORTANT**: Backend and frontend are **completely independent** applications:
- **Backend**: FastAPI REST API standalone (API-only, sin ejecución código)
- **Frontend**: React + TypeScript SPA que conecta via HTTP
- **Deployment**: Backend en Render.com, Frontend en Vercel
- **Para ejecución completa**: Railway.com ($5/mes), Fly.io, o VPS con Docker

### Important: Directory Structure Changes (Nov 4, 2025)

**NEW LOCATION - Backend moved to Back/ directory:**

The entire backend has been reorganized into the `Back/` directory for complete autonomy:

**Current Structure (USE THESE):**
- `Back/backend/` - FastAPI application (moved from root `backend/`)
- `Back/worker/` - RQ Worker (moved from root `worker/`)
- `Back/runner/` - Docker sandbox (moved from root `runner/`)
- `Back/workspaces/` - Execution workspaces (moved from root `workspaces/`)
- `Back/docker-compose.yml` - Backend standalone compose
- `Back/start.bat` / `Back/start.sh` - Backend startup scripts
- `Front/` - Frontend application (moved from `frontend/`)

**Obsolete Directories (DO NOT USE - Keep for reference only):**
- `backend/` (root) → Use `Back/backend/` instead
- `worker/` (root) → Use `Back/worker/` instead
- `runner/` (root) → Use `Back/runner/` instead
- `workspaces/` (root) → Use `Back/workspaces/` instead
- `frontend/` (root) → Use `Front/` instead

**Legacy MVP Files** (replaced by microservices architecture):
- `app.py` (root) → Use `Back/backend/app.py` instead
- `runner.py` (root) → Use `Back/worker/services/docker_runner.py` instead
- `Dockerfile` (root) → Use `Back/backend/Dockerfile` instead
- `requirements.txt` (root) → Use service-specific files instead
- `run_local.sh` → Use `docker compose` commands instead

**Completed Migration Scripts** (moved to `scripts/archive/`):
- `add_hints_to_problems.py` - Hints already added (124 total)
- `deploy_conftest.py` - Conftest files already deployed
- `crear_ejercicios_secuenciales.py` - Sequential exercises already created
- `generar_ejercicios_restantes.py` - Task completed
- `refactorizar_tests_secuenciales.py` - Refactoring completed

**Temporary/Generated Files** (ignored by git):
- `.mypy_cache/` - Type checker cache (regenerated automatically)
- `Back/workspaces/` - Temporary execution sandboxes (generated by worker)
- `Front/node_modules/` - Frontend dependencies (regenerated by npm install)

## Architecture

**⚠️ UPDATED (Nov 5, 2025): Sin Docker - Render.com Deployment**

**API-Only Architecture (Docker Eliminado):**

```
Frontend (Vercel)  ─HTTP─>  Backend (Render.com)  ─>  Redis Queue (Upstash)  ─>  Worker
   [React+TS]              [FastAPI + Gunicorn]                                   ↓
                                   ↓                                    (Returns "unavailable")
                           PostgreSQL (Render)
```

**⚠️ Docker Sandbox Eliminado**: Worker NO ejecuta código, retorna status "unavailable"

### Key Independence Points

1. **Backend is a standalone REST API** (API-only):
   - Runs on Render.com (port 8000 interno, expuesto via URL Render)
   - Accepts HTTP requests from any client
   - CORS configured for Vercel frontend
   - ✅ GET endpoints funcionan (problemas, subjects, hierarchy, admin)
   - ❌ POST /api/submit retorna "unavailable" (sin Docker)

2. **Frontend is a standalone SPA**:
   - Deployed to Vercel (static hosting)
   - Connects to backend via `VITE_API_URL` environment variable
   - Can run locally with `npm run dev`
   - API calls use fetch/axios to Render backend

3. **Communication**: HTTP only (no tight coupling)

4. **Limitation**: Sin ejecución de código (Docker no disponible en Render)

### Core Services

1. **Back/common/** - Shared module between backend and worker (NEW Nov 2025)
   - **config.py** - Centralized configuration with environment variables
   - **database.py** - SQLAlchemy session management
   - **models.py** - Database models (Submission, TestResult)
   - **logging_config.py** - Structured JSON logging
   - Eliminates code duplication between backend and worker
   - Reduces Docker image size and maintenance burden

2. **Back/backend/** - FastAPI REST API with service layer architecture
   - **app.py** - Routes/endpoints
   - **services/** - Business logic (ProblemService, SubmissionService, SubjectService)
   - **validators.py** - Input validation and security checks
   - **exceptions.py** - Custom exception hierarchy
   - **schemas.py** - Pydantic v2 models for request/response validation
   - **problems/** - 31 coding problems organized by subject/unit

3. **Back/worker/** - RQ worker adaptado (sin Docker)
   - **tasks.py** - Job orchestration (retorna "unavailable")
   - ~~**services/docker_runner.py**~~ - **ELIMINADO** (Docker no soportado)
   - ~~**services/rubric_scorer.py**~~ - **ELIMINADO** (sin ejecución, sin scoring)

4. ~~**Back/runner/**~~ - **ELIMINADO** (Docker sandbox removido completamente)

5. **Front/** - React + TypeScript + Vite + Monaco Editor
   - Located in `Front/` directory (moved from `frontend/` on Nov 4, 2025)
   - Hierarchical problem selector (Subject → Unit → Problem)
   - Real-time result polling with AbortController
   - Full type safety with TypeScript interfaces for all API responses
   - Anti-cheating system (anti-paste + tab monitoring)
   - Progressive hint system (4 levels)

6. **PostgreSQL** - Submissions and TestResults tables (port 5433)

7. **Redis** - Job queue (RQ) for asynchronous task processing

### Execution Flow (Render.com - Sin Docker)

**⚠️ LIMITADO**: Sin ejecución de código, solo API de lectura funciona completamente.

```
1. Student submits code → Backend creates Submission (status: "pending")
2. Backend enqueues job in Redis → status: "queued"
3. Worker picks up job from queue
4. ⚠️ Worker NO ejecuta Docker (no disponible en Render)
5. Worker marca Submission como status: "unavailable"
6. Worker crea TestResult con mensaje explicativo
7. Worker guarda en DB: error_message = "Ejecución de código NO disponible en Render"
8. Frontend polls /api/result/{job_id} y muestra mensaje de limitación
```

**Flujo completo requiere**: Railway.com, Fly.io, o VPS con Docker instalado.

### Database Models

**Submission** (backend/models.py):
- job_id, student_id, problem_id, code, status
- score_total, score_max, passed, failed, errors
- Relationship: one-to-many with TestResult

**TestResult** (backend/models.py):
- test_name, outcome, duration, message
- points, max_points, visibility (public/hidden)

## Critical Architecture Decisions

### ⚠️ Docker-in-Docker Path Translation (MOST COMMON ISSUE)

**The Problem**: Worker spawns Docker containers using the host's Docker daemon, creating a path mismatch:
- Worker creates files in `/workspaces/sandbox-xxx` (inside worker container)
- Docker daemon looks for paths on **host filesystem**, not worker filesystem
- Result: "file not found" errors when mounting volumes

**The Solution** (see worker/tasks.py:140-141):
1. `./workspaces` bind-mounted to both host and worker (see docker-compose.yml:79)
2. Worker translates paths: `/workspaces/sandbox-xxx` → `${PWD}/workspaces/sandbox-xxx`
3. Files get chmod 666, directories get chmod 777 (runner uses uid 1000, worker creates as root)

**When this breaks**: If you change workspace locations or mount paths without updating HOST_WORKSPACE_DIR env var.

### ⚠️ Dockerfile Build Context (SECOND MOST COMMON ISSUE)

All Dockerfiles use root (`.`) as build context in docker-compose.yml. COPY paths must be relative to project root.

```dockerfile
# ✅ CORRECT (context is root of project)
COPY backend/requirements.txt ./backend/
RUN pip install -r backend/requirements.txt

# ❌ WRONG (will cause ModuleNotFoundError)
COPY requirements.txt ./
RUN pip install -r requirements.txt
```

**When this breaks**: Adding new services or modifying Dockerfiles without checking build context in docker-compose.yml.

## Development Commands

### Quick Start

**Option 1: Run Backend Only (API standalone)**
```bash
# ⚠️ REQUIRED FIRST - Build runner image
docker build -t py-playground-runner:latest ./Back/runner

# Start backend services (without frontend)
docker compose up -d postgres redis backend worker

# Verify API is running
curl http://localhost:49000/api/health | python -m json.tool
```

**Option 2: Run Frontend Only (separate from Docker)**
```bash
cd Front
npm install
echo "VITE_API_URL=http://localhost:49000" > .env
npm run dev
# Open http://localhost:5173
```

**Option 3: Run Everything with Docker**
```bash
# Windows
start.bat

# Linux/Mac
chmod +x start.sh
./start.sh
```

### Docker Compose

```bash
# ⚠️ CRITICAL FIRST STEP - Build runner image (one-time, but required)
docker build -t py-playground-runner:latest ./Back/runner

# Start all services
docker compose up --build

# Verify services
docker compose ps  # All should show "Up" or "Up (healthy)"

# Health check
curl http://localhost:49000/api/health | python -m json.tool
```

### Local Development (without Docker)

**Backend:**
```bash
cd Back/backend
pip install -r requirements.txt
export DATABASE_URL=postgresql://playground:playground@localhost:5433/playground  # Linux/Mac (note port 5433)
set DATABASE_URL=postgresql://playground:playground@localhost:5433/playground    # Windows
uvicorn backend.app:app --reload --host 0.0.0.0 --port 8000
```

**Worker:**
```bash
cd Back/worker
pip install -r requirements.txt
export DATABASE_URL=postgresql://playground:playground@localhost:5433/playground  # Linux/Mac
rq worker --url redis://localhost:6379 submissions
```

**Frontend (Independent):**
```bash
cd Front
npm install

# Configure backend URL
echo "VITE_API_URL=http://localhost:49000" > .env

# Start dev server
npm run dev
# Open http://localhost:5173

# Development workflow
npm run type-check     # TypeScript type checking (npx tsc --noEmit)
npm run lint           # ESLint checking
npm run lint:fix       # Auto-fix ESLint issues
npm run format         # Format code with Prettier
npm run format:check   # Check if code is formatted
```

**IMPORTANT**: Frontend connects to backend via environment variable. The backend must be running and have CORS enabled:
```bash
# In backend: docker-compose.yml or .env
CORS_ALLOW_ALL=true  # Development only
# Or specify origins:
# CORS_ORIGINS=http://localhost:5173,http://localhost:49173
```

### Testing

```bash
# Backend tests
docker compose exec backend pytest Back/backend/tests/ -v

# With coverage
docker compose exec backend pytest Back/backend/tests/ --cov=backend --cov-report=term-missing

# Worker tests (install pytest first)
docker compose exec worker pip install pytest pytest-mock
docker compose exec worker pytest Back/worker/tests/ -v

# Frontend type checking
cd Front && npx tsc --noEmit
```

See [TESTING.md](TESTING.md) for detailed documentation including linting and pre-commit hooks.

### Database Access

```bash
# PostgreSQL shell
docker compose exec postgres psql -U playground

# Common queries
SELECT * FROM submissions ORDER BY created_at DESC LIMIT 10;
SELECT * FROM test_results WHERE submission_id = 1;
```

### Viewing Logs

```bash
# All services
docker compose logs -f

# Specific service
docker compose logs -f backend
docker compose logs -f worker

# Structured JSON logs
docker compose logs backend | grep -E '^\{' | python -m json.tool
```

## Hierarchical Subject/Unit System

The platform organizes problems using a **three-level hierarchy**: Subject → Unit → Problem.

### Configuration

Subjects and units are defined in [Back/backend/subjects_config.json](Back/backend/subjects_config.json). Edit this file to add new subjects/units - no code changes needed.

**Current subjects (8 total):**
1. **Programación 1** (Python) - Estructuras Secuenciales, Condicionales, Repetitivas, Listas, Funciones
2. **Programación 2** (Java) - POO Básico, Herencia, Excepciones, Archivos, Estructuras de Datos
3. **Programación 3** (Spring Boot) - Fundamentos Spring, Spring Boot, Spring Web, Spring Data, Spring Security
4. **Programación 4** (FastAPI) - Fundamentos FastAPI, Validación, Databases, Seguridad, Avanzado
5. **Paradigmas de Programación** (Java, SWI-Prolog, Haskell) - Imperativo, OO, Lógico, Funcional, Comparación
6. **Algoritmos y Estructuras de Datos** (PSeInt) - Estructuras básicas, Ordenamiento, Búsqueda, Pilas/Colas, Recursión
7. **Desarrollo Front End** (HTML, CSS, JavaScript, TypeScript) - HTML, CSS, JS Básico, JS Avanzado, TypeScript
8. **Desarrollo Backend** (Python, FastAPI) - Python Fundamentos, FastAPI Básico, Bases de Datos, Autenticación, Deployment

### API Endpoints

**Student**:
- GET /api/problems - List all problems
- POST /api/submit - Submit code (returns job_id)
- GET /api/result/{job_id} - Poll for results

**Hierarchy Navigation**:
- GET /api/subjects - List all subjects
- GET /api/subjects/{subject_id}/units - Get units for a subject
- GET /api/subjects/{subject_id}/units/{unit_id}/problems - Get problems for a unit
- GET /api/problems/hierarchy - Complete hierarchy with problem counts

**Admin**:
- GET /api/admin/summary - Aggregate statistics
- GET /api/admin/submissions - Recent submissions with filters

Full schemas: http://localhost:49000/docs

### Frontend Navigation

Three cascading dropdowns:
1. **📚 Materia** (Subject) - User selects a subject
2. **📖 Unidad Temática** (Unit) - Auto-populates from selected subject
3. **🎯 Ejercicio** (Problem) - Shows problems for selected unit

See [Front/src/components/Playground.tsx](Front/src/components/Playground.tsx)

### Dynamic Logo System

The frontend displays technology logos that change based on the selected subject. Logos are SVG-based and use official colors.

**Implementation**: [Front/src/components/LanguageLogo.tsx](Front/src/components/LanguageLogo.tsx)

**Logo Configuration**:
- **Single logo subjects**: programacion-1 (Python), programacion-2 (Java), programacion-3 (Spring Boot), programacion-4 (FastAPI), algoritmos (PSeInt)
- **Multi-logo subjects** (MANDATORY - logos must appear together):
  - **Paradigmas**: 3 logos (Java, SWI-Prolog, Haskell) displayed side-by-side
  - **Frontend**: 4 logos (HTML5, CSS3, JavaScript, TypeScript) displayed side-by-side
  - **Backend**: 2 logos (Python, FastAPI) displayed side-by-side

**Adding New Subject Logos**:
1. Edit `Front/src/components/LanguageLogo.tsx`
2. Add new `case 'subject-id':` in the switch statement
3. For multi-logo subjects, use flex layout: `<div style={{ display: 'flex', gap: '8px', alignItems: 'center' }}>`
4. Use unique gradient IDs to avoid SVG conflicts (e.g., `pyYellowBackend`, `fastapiBackendGradient`)
5. Logos automatically appear in the header when subject is selected

## Problem Structure

Problems live in `Back/backend/problems/<problem_id>/` with 6 required files:

- `prompt.md` - Problem statement (Markdown)
- `starter.py` - Initial code template
- `tests_public.py` - Tests visible to students
- `tests_hidden.py` - Hidden tests for grading
- `metadata.json` - Title, subject_id, unit_id, difficulty, tags, timeout_sec, memory_mb
- `rubric.json` - Points per test and visibility

### Rubric System

**Critical**: Test names in rubric.json must match pytest function names exactly.

```json
{
  "tests": [
    {"name": "test_suma_basico", "points": 3, "visibility": "public"},
    {"name": "test_suma_hidden", "points": 2, "visibility": "hidden"}
  ],
  "max_points": 5
}
```

- **public** tests: Full details shown (outcome, message, duration)
- **hidden** tests: Only pass/fail, no error messages
- Points awarded only if test passes

### Test File Pattern

Both test files must use importlib to dynamically import student code:

```python
import importlib.util
import os

spec = importlib.util.spec_from_file_location(
    "student_code",
    os.path.join(os.getcwd(), "student_code.py")
)
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_suma_basico():
    assert hasattr(student, "suma"), "Debe existir una función suma(a, b)"
    assert student.suma(2, 3) == 5
```

### Standard Problem Pattern: main() Function

**IMPORTANT**: All problems follow a standard pattern using a `main()` function that reads from stdin and prints to stdout.

**Starter code pattern**:
```python
def main():
    """
    Problem description here.

    Reads input using input() and prints output using print().
    """
    # Read input
    valor = int(input())  # or float(input()) for decimals

    # TODO: Implementa tu código aquí
    # Print the result

    pass

if __name__ == "__main__":
    main()
```

**Test pattern for main() functions**:
```python
from io import StringIO
import sys

def test_ejemplo():
    """Test with mocked stdin/stdout"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("5")  # Mock input
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "10", f"Expected '10', got '{output}'"
```

**Why main() pattern?**:
- Consistent interface across all problems
- Easy to test with stdin/stdout mocking
- Simulates real-world input/output programs
- Students learn standard Python entry point convention

See `Back/backend/problems/cond_aprobado/` for complete examples.

## Progressive Hint System

**IMPORTANT**: All 31 problems have a 4-level progressive hint system (100% coverage, 124 total hints).

### Overview

Students can request hints by clicking "💡 Dame una pista" button (next to "Editor" heading). Hints are revealed progressively to guide learning without giving away the solution immediately.

### Hint Levels Structure

**Level 1: General Orientation**
- Identify what data to read
- Overall problem structure
- Key concepts reminder

**Level 2: Function Guidance**
- Which functions/methods to use
- Expected output format
- Main operations needed

**Level 3: Syntax & Code Examples**
- Specific syntax examples
- Code fragments
- Formulas or patterns

**Level 4: Near-Complete Solution**
- Step-by-step explanation
- All necessary elements mentioned
- Not literal code, but very close

### Implementation

**Frontend (Playground.tsx)**:
- `currentHintLevel` state tracks progress (0-4)
- Resets to 0 when problem changes
- Button shows counter: "(2/4)" when hints used
- Button color: green (available) → gray (exhausted)
- Tooltip shows next hint level

**Backend (metadata.json)**:
```json
{
  "hints": [
    "Level 1 hint text...",
    "Level 2 hint text...",
    "Level 3 hint text...",
    "Level 4 hint text..."
  ]
}
```

**TypeScript Types**:
- `ProblemMetadata` interface includes `hints?: string[]`
- Field is optional (problems without hints show generic message)

### Adding Hints to New Problems

**Method 1: Manual**
Edit `backend/problems/{problem_id}/metadata.json`:
```json
{
  ...existing fields...,
  "hints": [
    "Your level 1 hint",
    "Your level 2 hint",
    "Your level 3 hint",
    "Your level 4 hint"
  ]
}
```

**Method 2: Automated (Generic Hints)**
```bash
python add_hints_to_problems.py
```
This script adds generic 4-level hints to all problems that don't have them.

### Best Practices for Writing Hints

**Do**:
✅ Make each hint progressively more specific
✅ Customize hints for each problem
✅ Explain WHAT to do, not give literal code
✅ Use syntax examples in level 3-4
✅ Mention common errors/pitfalls

**Don't**:
❌ Repeat the problem statement
❌ Give solution in level 1-2
❌ Be too vague ("think harder")
❌ Make hints too long (max 2-3 sentences)
❌ Give literal code solution

### Example Hint Sets

**sec_saludo (custom)**:
```json
[
  "Recuerda que debes crear una función main() que lea la entrada con input().",
  "Usa print() para mostrar el resultado. El formato debe ser exactamente 'Hola, {nombre}!'.",
  "Puedes usar f-strings para formatear el texto: f'Hola, {nombre}!'",
  "Solución completa: Lee el nombre con input(), formatea con f-string y usa print()."
]
```

**Generic hints** (used by 29 problems):
```json
[
  "Lee cuidadosamente el enunciado del problema y identifica qué datos necesitas leer con input().",
  "Recuerda que debes crear una función main() que contenga toda tu lógica. Usa print() para mostrar el resultado.",
  "Revisa el código starter provisto. Completa la sección TODO con la lógica necesaria según el enunciado.",
  "Asegúrate de seguir el formato de salida exacto que pide el problema. Revisa los ejemplos de entrada/salida."
]
```

### UI/UX Behavior

- **Button text**: "💡 Dame una pista" → "💡 Dame una pista (2/4)" after use
- **Button color**: #4CAF50 (green) → #9E9E9E (gray when exhausted)
- **Alert format**: "💡 Pista X de Y:\n\n{hint text}"
- **Last hint**: Adds warning "⚠️ Esta es la última pista disponible."
- **Exhausted**: Shows "🎓 Ya has visto todas las pistas (4/4)"
- **Disabled**: When no problem selected
- **Reset**: Automatic when changing problems

For complete documentation, see [HINT_SYSTEM.md](HINT_SYSTEM.md).

### Test-Driven Hints (Nov 2025 QA Enhancement)

**IMPORTANT**: All 9 conditional problems now have **test-driven hints** that directly reference what the tests verify.

**Pattern Applied** (4-level progressive structure):
1. **Level 1 - Function Verification**: What function/structure the tests check for
2. **Level 2 - Critical Limits**: Boundary values and edge cases with ⚠️ warnings
3. **Level 3 - Techniques**: Specific syntax, operators, and logic required
4. **Level 4 - Exact Format**: Precise output format and test cases

**Example - cond_numero_par**:
```json
[
  "Usa el operador módulo % para verificar paridad: numero % 2 == 0 significa par. Los tests probarán con 0, positivos, negativos y números grandes.",
  "⚠️ CASO ESPECIAL: Los tests verifican que 0 sea par (0 % 2 == 0 es True). También probarán números negativos: -2 es par, -3 es impar.",
  "Los tests incluyen números grandes (1000, 9999) y pequeños (1, 2). Tu condición if numero % 2 == 0 debe funcionar para todos.",
  "Formato EXACTO: 'Ha ingresado un número par' o 'Por favor, ingrese un número par'. Los tests fallan si cambias una letra o espacio."
]
```

**Benefits**:
- Students understand exactly what tests verify
- Boundary value awareness prevents common errors
- Reduces "why did my test fail?" confusion
- Aligns learning with test requirements

**Problems with test-driven hints**: cond_aprobado, cond_mayor_edad, cond_mayor_de_dos, cond_numero_par, cond_categorias_edad, cond_termina_vocal, cond_terremoto, cond_transformar_nombre, cond_validar_password

## Sequential Exercises (Nov 2025 Refactoring)

**IMPORTANT**: All 10 sequential exercises (sec_*) have been fully refactored to match the quality and structure of conditional exercises.

### Sequential Problems Available

1. **sec_hola_mundo** (12 tests, 18 points) - Print "Hola Mundo!" with exact format validation
2. **sec_saludo** (11 tests, 15 points) - Greeting with name input and f-string formatting
3. **sec_presentacion** (8 tests, 14 points) - Multi-input presentation (name, surname, age, city)
4. **sec_circulo** (11 tests, 15 points) - Circle area and perimeter with mathematical precision
5. **sec_segundos_horas** (10 tests, 15 points) - Time conversion with decimal handling
6. **sec_tabla_multiplicar** (14 tests, 21 points) - Multiplication table 1-10 with format validation
7. **sec_operaciones_basicas** (14 tests, 22 points) - Four arithmetic operations with edge cases
8. **sec_imc** (17 tests, 26 points) - BMI calculation with 2-decimal precision
9. **sec_celsius_fahrenheit** (18 tests, 27 points) - Temperature conversion with negative values
10. **sec_promedio** (24 tests, 31 points) - Average of three numbers with comprehensive edge cases

### Test Structure Pattern (Sequential Exercises)

All sequential exercises follow the same comprehensive pattern:

```python
# tests_public.py
class TestFunctionExistence:
    """Verify main() function exists"""
    def test_main_function_exists(self, student_module):
        assert hasattr(student_module, 'main')

class TestBasicCases:
    """Test fundamental functionality"""
    def test_ejemplo(self, capture_main_output, student_module):
        output = capture_main_output("input", student_module)
        assert "expected" in output

class TestEdgeCases:
    """Test boundary values and special cases"""
    def test_zero(self, capture_main_output, student_module):
        # Test with zero values

class TestOutputFormat:
    """Validate output format requirements"""
    def test_formato(self, capture_main_output, student_module):
        # Verify exact format

# tests_hidden.py
class TestExtremeValues:
    """Test with very large/small values"""

class TestPrecision:
    """Test decimal precision and rounding"""

class TestNegativeNumbers:
    """Test negative value handling"""
```

### Key Improvements in Sequential Tests

**Test Organization**:
- ✅ Class-based organization by test purpose
- ✅ Descriptive class and method names
- ✅ Clear docstrings explaining what is tested

**Test Coverage**:
- ✅ Basic functionality tests
- ✅ Edge cases (zero, negative, extreme values)
- ✅ Format validation (exact output format)
- ✅ Decimal precision tests
- ✅ Boundary value testing

**Parametrization**:
```python
@pytest.mark.parametrize("input_val,expected", [
    ("10", "result1"),
    ("20", "result2"),
    ("30", "result3"),
])
def test_varios_casos(self, capture_main_output, student_module, input_val, expected):
    output = capture_main_output(input_val, student_module)
    assert expected in output
```

**Fixtures Used**:
- `capture_main_output(input_data, student_module)` - Mock stdin/stdout for main() testing
- `student_module` - Dynamically loaded student code module

### Example: sec_circulo Test Structure

```python
# tests_public.py (11 tests)
class TestFunctionExistence:      # 1 test
class TestBasicCalculations:       # 2 tests (radius 1, radius 5)
class TestDecimalRadius:           # 3 tests (parametrized: 2.5, 3.7, 4.2)
class TestEdgeCases:               # 2 tests (radius 0, radius 100)
class TestOutputFormat:            # 2 tests (2 lines, numeric values)

# tests_hidden.py (hidden tests for grading)
class TestPrecision:               # 3 tests (parametrized decimal precision)
class TestLargeValues:             # 1 test (radius 1000)
class TestSmallValues:             # 3 tests (parametrized: 0.1, 0.01, 0.5)
```

### Rubric System for Sequential Exercises

Each test has explicit point values in `rubric.json`:

```json
{
  "tests": [
    {"name": "test_main_function_exists", "points": 1, "visibility": "public"},
    {"name": "test_radio_uno", "points": 2, "visibility": "public"},
    {"name": "test_precision_decimales", "points": 2, "visibility": "hidden"}
  ],
  "max_points": 15
}
```

**Point distribution**:
- Function existence: 1 point
- Basic tests: 1-2 points each
- Complex/parametrized tests: 2-3 points each
- Hidden tests: Usually 1-2 points each

## QA Test Infrastructure

**CRITICAL**: Conditional problems use advanced pytest patterns with shared fixtures. When modifying tests, maintain these patterns.

### Shared Test Fixtures (conftest.py)

**Location**: Deployed to all conditional problem directories (e.g., `Back/backend/problems/cond_aprobado/conftest.py`)

**Important**: Worker dynamically generates conftest.py by merging fixtures with report generation code (see `worker/tasks.py:136-218`).

**Available Fixtures**:

```python
@pytest.fixture
def capture_main_output():
    """Mock stdin/stdout for main() function testing"""
    def _capture(input_data: str, student_module) -> str:
        old_stdin = sys.stdin
        old_stdout = sys.stdout
        try:
            sys.stdin = StringIO(input_data)
            sys.stdout = StringIO()
            student_module.main()
            return sys.stdout.getvalue().strip()
        finally:
            sys.stdin = old_stdin
            sys.stdout = old_stdout
    return _capture

@pytest.fixture
def student_module():
    """Dynamically load student_code.py"""
    spec = importlib.util.spec_from_file_location('student_code', 'student_code.py')
    student = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(student)
    return student

@pytest.fixture
def call_function():
    """Safely call student function with error handling"""
    def _call(student_module, function_name: str, *args, **kwargs):
        if not hasattr(student_module, function_name):
            pytest.fail(f"La función '{function_name}' no está definida")
        return getattr(student_module, function_name)(*args, **kwargs)
    return _call
```

### Test Structure Pattern

**Best Practice** - Organize tests into classes by purpose:

```python
class TestFunctionExistence:
    """Tests to verify required functions exist."""
    def test_main_function_exists(self, student_module):
        assert hasattr(student_module, 'main')

class TestBasicCases:
    """Tests for basic functionality."""
    @pytest.mark.parametrize("nota,esperado", [
        ("7", "Aprobado"),
        ("8", "Aprobado"),
    ])
    def test_notas_aprobadas(self, capture_main_output, student_module, nota, esperado):
        output = capture_main_output(nota, student_module)
        assert output == esperado

class TestBoundaryValues:
    """Tests for edge cases and limits."""
    def test_limite_aprobado(self, capture_main_output, student_module):
        output = capture_main_output("6", student_module)
        assert output == "Aprobado", "La nota 6 debe ser 'Aprobado'"

class TestErrorHandling:
    """Tests for error cases and invalid input."""
    # ...
```

### Parametrization Best Practices

Use `@pytest.mark.parametrize` to reduce duplication:

```python
@pytest.mark.parametrize("input_val,expected", [
    ("5", "Desaprobado"),
    ("6", "Aprobado"),
    ("6.5", "Aprobado"),
    ("5.99", "Desaprobado"),
])
def test_notas(self, capture_main_output, student_module, input_val, expected):
    output = capture_main_output(input_val, student_module)
    assert output == expected, f"Con nota {input_val}, esperaba '{expected}'"
```

### Metrics Achieved

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| Tests per problem | 3-7 | 54+ | ↑671% |
| Code duplication | High (87%) | Minimal | ↓87% |
| Boundary coverage | ~35% | ~95% | ↑171% |
| Quality score | 6.5/10 | 9.2/10 | ↑41% |

**Documentation**: See [docs/archive/TEST_IMPROVEMENTS_REPORT.md](docs/archive/TEST_IMPROVEMENTS_REPORT.md) for complete details.

## Security Implementation

### Multi-Layer Security

**1. Input Validation** ([backend/validators.py](backend/validators.py))

Before code reaches worker:
- Blocks dangerous imports: `os`, `subprocess`, `sys`, `__import__`, `eval()`, `exec()`, `compile()`
- Enforces max code length (50KB default)
- Validates problem_id format and existence

**2. Docker Sandbox Isolation**

```bash
docker run --rm \
  --network none \              # No network
  --read-only \                 # Read-only filesystem
  --tmpfs /tmp:rw,noexec,nosuid,size=64m \
  --tmpfs /workspace:rw,noexec,nosuid,size=128m \
  --cpus=1.0 --memory=256m --memory-swap=256m \
  -v $workspace:/workspace:rw \
  py-playground-runner:latest pytest -q --tb=short .
```

Additional safeguards:
- Timeout enforcement (default 5s, configurable per problem)
- Non-root user (uid 1000)
- Workspace cleanup after execution

**3. Anti-Cheating System** ([Front/src/components/Playground.tsx](Front/src/components/Playground.tsx))

Comprehensive academic integrity enforcement with two main components:

**a) Anti-Paste Protection**:
- Blocks Ctrl/Cmd+V keyboard shortcut
- Blocks right-click → paste in editor
- Blocks DOM-level paste events
- Shows educational warning banner

**b) Tab Monitoring System**:
- Detects tab switching (visibilitychange event)
- Detects window minimization (blur event)
- Progressive 2-warning system before lockout
- Blocks right-click globally (contextmenu)
- Blocks keyboard shortcuts: Ctrl+T, Ctrl+N, Ctrl+W
- Prevents easy tab closing (beforeunload)
- Shows red warning banner: "🚨 ADVERTENCIA DE INTEGRIDAD ACADÉMICA 🚨"
- After 2 violations: Closes browser with message "🚫 NO TE DEJO VER OTRA PÁGINA, SOY UN VIEJO GARCA! 🚫"

Benefits:
- Prevents AI-generated code pasting
- Prevents copying from external sources (other tabs/windows)
- Maintains exam integrity
- Progressive warnings educate before enforcement

**Important**: Does NOT block typing, autocomplete, or legitimate learning aids. Does NOT prevent using the same tab for reading documentation. See [ANTI_PASTE_FEATURE.md](ANTI_PASTE_FEATURE.md) for complete technical details.

**Limitations**: For high-stakes environments, consider gVisor runtime, separate VM/host for worker, or static analysis.

## Service Layer Architecture

The backend follows a **service layer pattern** to separate business logic from HTTP routes.

### Service Classes

**ProblemService** ([Back/backend/services/problem_service.py](Back/backend/services/problem_service.py)):
- `list_all()`, `get_problem_dir()`, `get_test_files()`, `load_rubric()`
- `list_by_subject_and_unit()`, `group_by_subject_and_unit()`

**SubjectService** ([Back/backend/services/subject_service.py](Back/backend/services/subject_service.py)):
- `list_all_subjects()`, `get_subject()`, `list_units_by_subject()`
- `get_hierarchy()`, `validate_subject_unit()`
- Reads from subjects_config.json

**SubmissionService** ([Back/backend/services/submission_service.py](Back/backend/services/submission_service.py)):
- `create_submission()`, `update_job_id()`, `get_by_job_id()`
- `get_result_dict()`, `get_statistics()`, `list_submissions()`

**DockerRunner** (Back/worker/services/docker_runner.py):
- Handles Docker execution with path translation

**RubricScorer** (Back/worker/services/rubric_scorer.py):
- Applies scoring logic to test results

### Adding New Features

Follow this pattern:

1. **Create service class** in `Back/backend/services/`:
```python
from ..logging_config import get_logger
logger = get_logger(__name__)

class MyService:
    def do_something(self, param):
        logger.info(f"Doing something with {param}")
        return result

my_service = MyService()  # Singleton
```

2. **Use in routes** (Back/backend/app.py):
```python
from .services.my_service import my_service

@app.get("/api/my-endpoint")
def my_endpoint(db: Session = Depends(get_db)):
    return my_service.do_something("value")
```

3. **Add validation** (Back/backend/validators.py)
4. **Add exceptions** (Back/backend/exceptions.py)
5. **Add configuration** (Back/backend/config.py)
6. **Use structured logging**: `logger.info("Message", extra={"key": "value"})`

## Performance Optimizations (CRITICAL TO MAINTAIN)

### 1. N+1 Query Prevention (submission_service.py) - 100x improvement

Always use eager loading with `joinedload()` when accessing relationships:

```python
# ✅ CORRECT - Loads relationship in same query
submission = db.query(Submission).options(
    joinedload(Submission.test_results)
).filter(Submission.job_id == job_id).first()

# ❌ WRONG - N+1 queries (1 query + N queries for each relationship access)
submission = db.query(Submission).filter(Submission.job_id == job_id).first()
```

### 2. Problem List Caching (problem_service.py) - 1000x improvement

Problem list uses `@lru_cache` to avoid repeated filesystem reads. **Remember to invalidate cache when adding/modifying problems**:
```python
problem_service.invalidate_cache()
```

### 3. Compiled Regex Patterns (validators.py) - 2x improvement

Regex patterns compiled at module level. Don't recompile in functions.

### 4. Never Hardcode Paths

```python
# ✅ CORRECT - Uses settings
from backend.config import settings
problem_dir = pathlib.Path(settings.PROBLEMS_DIR) / problem_id

# ❌ WRONG - Breaks in different environments
problem_dir = pathlib.Path("/app/backend/problems") / problem_id
```

## Adding New Problems

1. Choose subject/unit from [Back/backend/subjects_config.json](Back/backend/subjects_config.json)
2. Create directory: `mkdir Back/backend/problems/new_problem`
3. Create 6 files: `prompt.md`, `starter.py`, `tests_public.py`, `tests_hidden.py`, `metadata.json`, `rubric.json`
4. Fill metadata.json with subject_id and unit_id
5. Test locally:

```bash
# Submit test
curl -X POST http://localhost:49000/api/submit \
  -H "Content-Type: application/json" \
  -d '{"problem_id": "new_problem", "code": "def my_func():\n    pass", "student_id": "test"}'

# Check results
curl http://localhost:49000/api/result/JOB_ID | python -m json.tool

# Verify hierarchy
curl http://localhost:49000/api/problems/hierarchy | python -m json.tool
```

## Common Tasks

| Task | Command |
|------|---------|
| Restart service after code changes | `docker compose restart backend` |
| Rebuild after dependency changes | `docker compose up -d --build backend` |
| Reset database | `docker compose down -v && docker compose up --build` |
| Change resource limits globally | Edit `DEFAULT_TIMEOUT`, `DEFAULT_MEMORY_MB`, `DEFAULT_CPUS` in worker/tasks.py |
| Change resource limits per problem | Edit problem's metadata.json (timeout_sec, memory_mb) |
| Invalidate problem cache | Call `problem_service.invalidate_cache()` after adding problems |

## Port Configuration

**Current Configuration** (Windows compatibility):
- Backend: External `49000` → Internal `8000` (high port avoids Hyper-V conflicts)
- Frontend: External `49173` → Internal `5173` (high port avoids Hyper-V conflicts)
- PostgreSQL: External `5433` → Internal `5432`
- Redis: Internal only (no external port needed)

**Why high ports?** Windows Hyper-V reserves ports 8000-8080 and 5000-5500, causing permission errors. High ports (49000+) avoid these conflicts.

**Container-to-container communication** uses internal ports (e.g., `postgres:5432` in DATABASE_URL, not `localhost:5433`).

**Linux/Mac users**: If you don't have port conflicts, you can change back to standard ports in docker-compose.yml:
```yaml
backend:
  ports:
    - "8000:8000"  # Change from 49000:8000
frontend:
  ports:
    - "5173:5173"  # Change from 49173:5173
```

## Troubleshooting

**⚠️ MOST COMMON FIRST-TIME ERROR**: "Error response from daemon: No such image: py-playground-runner:latest"
- **Cause**: You haven't built the runner image yet
- **Solution**: `docker build -t py-playground-runner:latest ./Back/runner`
- This image is required by the worker to execute student code in a sandbox
- Must be built BEFORE running `docker compose up`

**First-time startup is slow**: 5-10 minutes to download/build images. Monitor: `docker compose logs -f`

**Port already in use**:
```bash
# Windows: netstat -ano | findstr :49000 && taskkill /PID <PID> /F
# Linux: lsof -i :49000 && kill -9 <PID>
# Or for frontend: findstr :49173 (Windows) / lsof -i :49173 (Linux)
```

**Worker can't access Docker daemon**:
- Check `/var/run/docker.sock` mounted in docker-compose.yml
- Windows: Verify Docker Desktop uses WSL 2
- Linux: Add user to docker group: `sudo usermod -aG docker $USER && newgrp docker`

**Runner image not found**: `docker build -t py-playground-runner:latest ./Back/runner`

**ModuleNotFoundError: No module named 'common'**:
- Cause: Docker image built before common/ module was created
- Solution: Rebuild images with `docker compose build --no-cache backend worker`
- Both backend and worker Dockerfiles must COPY common/ directory

**ModuleNotFoundError: No module named 'backend'**:
- Cause: Using old import paths (from backend.config) instead of new common module
- Solution: Update imports to `from common.config import settings`
- Correct paths: `common.config`, `common.database`, `common.models`, `common.logging_config`

**ModuleNotFoundError (general)**: Dockerfile COPY paths incorrect. Use `backend/requirements.txt` not `requirements.txt`. Rebuild: `docker compose build --no-cache backend`

**Tests timing out**: Increase timeout_sec in metadata.json or DEFAULT_TIMEOUT in worker/tasks.py

**Database connection errors**: Wait for healthcheck: `docker compose ps`

**RQ worker not processing**: Check Redis: `docker compose exec redis redis-cli ping`

**Frontend TypeScript errors (import.meta.env)**:
- Error: `Property 'env' does not exist on type 'ImportMeta'`
- Cause: Missing `vite-env.d.ts` file
- Solution: Ensure `Front/src/vite-env.d.ts` exists with proper type definitions
- If missing, create file with ImportMeta and ImportMetaEnv interfaces

**Frontend ESLint/Prettier issues**:
- Run `npm run lint:fix` to auto-fix most issues
- Run `npm run format` to format all files
- Check `.eslintrc.json` and `.prettierrc.json` for configuration
- If errors persist, reinstall dependencies: `rm -rf node_modules && npm install`

## Refactoring Status

All major refactoring completed. See [docs/archive/REFACTORING_COMPLETE.md](docs/archive/REFACTORING_COMPLETE.md) for historical details.

**Completed**:
- ✅ Phase 1 (100%): Core infrastructure (config, logging, validation, exceptions)
- ✅ Phase 2 (100%): Service layer architecture, Pydantic v2 schemas

**In Progress**:
- ⏳ Phase 3 (85%): Testing (83 tests, 25/53 passing), linting, pre-commit hooks

**When continuing refactoring**:
1. Read REFACTORING_COMPLETE.md first
2. Follow service layer pattern
3. Use structured logging: `get_logger(__name__)`
4. Add validation for inputs
5. Test after changes

## Frontend Architecture

**TypeScript Migration** ✅ (Completed: Oct 2025)
- Migrated from JavaScript to TypeScript for improved type safety
- Centralized API types in `src/types/api.ts`
- All components fully typed with interfaces
- Created `vite-env.d.ts` for proper import.meta.env type definitions

**Code Quality Tooling** ✅ (Completed: Nov 2025)
- **ESLint**: Configured with TypeScript, React, and React Hooks plugins
- **Prettier**: Consistent code formatting with .prettierrc.json configuration
- **Type Safety**: All TypeScript compilation errors resolved (0 errors)
- **Linting**: All code passes ESLint with 0 warnings
- **Configuration Files**: `.eslintrc.json`, `.prettierrc.json`, `.prettierignore`

**Components**:
- **App.tsx** - Tab navigation (Ejercicios, Panel Docente)
- **Playground.tsx** - Student interface with cascading dropdowns, Monaco editor, result polling with AbortController
- **AdminPanel.tsx** - Instructor dashboard
- **LanguageLogo.tsx** - Dynamic logos based on subject
- **types/api.ts** - TypeScript interfaces for all API requests/responses
- **config.ts** - Centralized configuration with environment variables

**Features**:
- Monaco Editor for Python syntax highlighting
- Code persisted to localStorage
- Full TypeScript type checking with strict mode
- Type-safe API calls with Axios
- Anti-cheating system (anti-paste + tab monitoring)
- Progressive hint system (4 levels)

**Tech Stack**:
- React 18 with TypeScript
- Vite 6 for build tooling and dev server
- Monaco Editor for code editing (VS Code engine)
- Axios for HTTP requests
- ESLint 8 + Prettier 3 for code quality
- TypeScript 5 with strict mode enabled

**Development Workflow**:
```bash
# Run dev server (hot reload enabled)
npm run dev

# Type check without compiling
npm run type-check

# Lint code (check for issues)
npm run lint

# Lint and auto-fix
npm run lint:fix

# Format code with Prettier
npm run format

# Check if code is formatted
npm run format:check

# Build for production
npm run build

# Preview production build
npm run preview
```

**Adding New Components**:
1. Create `.tsx` files (not `.jsx`)
2. Import types from `src/types/api.ts`
3. Define component props interface:
   ```typescript
   interface MyComponentProps {
     title: string
     onSubmit: (data: FormData) => void
   }

   function MyComponent({ title, onSubmit }: MyComponentProps) {
     const [value, setValue] = useState<string>('')
     // ...
   }
   ```
4. Run type-check and linting before committing:
   ```bash
   npm run type-check && npm run lint && npm run format
   ```

**Adding New API Types**:
Edit `Front/src/types/api.ts` and add/export new interfaces. Types are automatically available throughout the app.

**Code Quality Best Practices**:
- **Always run `npm run type-check`** before committing to catch TypeScript errors
- **Use `npm run lint:fix`** to automatically fix most linting issues
- **Run `npm run format`** to ensure consistent code style
- **Import types properly**: Use interfaces from `src/types/api.ts` for API responses
- **Avoid `any` type**: ESLint warns about explicit `any` - use specific types instead
- **Follow React Hooks rules**: ESLint enforces hooks rules (exhaustive-deps, rules-of-hooks)

## Production Deployment

### Deploy to Render.com (Backend)

The backend is **fully configured** for deployment to Render.com with Gunicorn.

**Deployment Files** (located in `Back/`):
- `Procfile` - Start commands for web and worker services (with `cd Back`)
- `runtime.txt` - Python 3.11.9
- `requirements.txt` - Combined dependencies with Gunicorn
- `render.yaml` - Complete service configuration
- `start-render.sh` - Startup script with DB initialization
- `RENDER_QUICKSTART.md` - ⭐ **Step-by-step deployment guide**
- `RENDER_TROUBLESHOOTING.md` - ⭐ **Common errors and solutions**
- `RENDER_ENV_VARS.txt` - Environment variables template
- `DEPLOY_RENDER.md` - Comprehensive deployment documentation

**Quick Deploy Steps**:

1. **Create Services on Render**:
   - PostgreSQL Database (Free tier)
   - Redis (use Upstash.com free tier - Render doesn't offer free Redis)
   - Web Service (Backend API)
   - Background Worker (RQ Worker)

2. **Configure Web Service**:
   - **Root Directory**: `Back`
   - **Build Command**: `cd Back && pip install -r requirements.txt`
   - **Start Command**: `cd Back && gunicorn backend.app:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT`

3. **Configure Environment Variables** (in both Web Service and Worker):
   ```env
   DATABASE_URL=postgresql://user:pass@host/db
   REDIS_URL=redis://default:pass@host:port
   CORS_ORIGINS=https://front-eight-rho-61.vercel.app
   ```

**⚠️ CRITICAL**: The `cd Back` in Start Command is essential to avoid `ModuleNotFoundError: No module named 'app'`

**CORS Configuration**:
Backend is pre-configured for Vercel frontend at `https://front-eight-rho-61.vercel.app`

**Important Limitation**:
- Docker is **NOT available** on Render Free Tier
- Backend API will work perfectly (problems, hierarchy, admin panel)
- Code execution (runner/sandbox) will NOT work
- Solutions: Use Railway.app/Fly.io for runner, or deploy to VPS with Docker

**Common Deployment Errors**:

- **ModuleNotFoundError: No module named 'app'**
  - Cause: Missing `cd Back` in Start Command
  - Fix: Ensure Start Command is: `cd Back && gunicorn backend.app:app ...`
  - See `Back/RENDER_TROUBLESHOOTING.md` for full solutions

- **ModuleNotFoundError: No module named 'common'**
  - Cause: Python can't find the common module
  - Fix: Use `cd Back` in Start Command OR set `PYTHONPATH=/opt/render/project/src/Back`

- **Database connection failed**
  - Cause: Wrong DATABASE_URL
  - Fix: Use Render PostgreSQL's **Internal Database URL** (not External)

**Complete Documentation**:
- Quick Start: `Back/RENDER_QUICKSTART.md`
- Troubleshooting: `Back/RENDER_TROUBLESHOOTING.md` ⭐ **Common errors and solutions**
- Full Guide: `Back/DEPLOY_RENDER.md`

### Deploy to Vercel (Frontend)

Frontend is already deployed at: `https://front-eight-rho-61.vercel.app`

**To redeploy with updated backend URL**:

1. Go to Vercel Dashboard → Project Settings → Environment Variables
2. Update: `VITE_API_URL=https://your-backend.onrender.com`
3. Redeploy from Deployments tab

**Development Configuration**:
- `Front/.env` contains `VITE_API_URL=http://localhost:49000` for local development
- Frontend automatically uses this URL when running `npm run dev`

## Extension Points

- Multiple workers for scaling (add worker services in docker-compose.yml)
- Different languages (change RUNNER_IMAGE env var)
- Custom test frameworks (update conftest.py)
- Authentication (add middleware to backend/app.py)
- Webhooks (add to worker/tasks.py after commit)
- Rate limiting (Redis counter in backend)
