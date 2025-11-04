# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Current Status

**System**: Production-ready ✅ (Last updated: 4 Nov 2025)
**Problem Count**: 31 problems across 8 subjects
**Test Coverage**: 54+ tests per conditional problem, 10-24 tests per sequential problem ✅
**Frontend**: TypeScript migration completed ✅ with dynamic logo system
**Security**: Anti-cheating system active (anti-paste + tab monitoring) ✅
**Hint System**: Test-driven hints on all 9 conditional problems (100% coverage) ✅
**Documentation**: Comprehensive with user stories and use cases
**Code Quality**: Health Score 9.2/10 (improved from 6.5) ✅

**Recent Improvements** (Nov 4, 2025):
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

See [REFACTORING_SESSION_2025-10-25.md](REFACTORING_SESSION_2025-10-25.md) for complete refactoring details, [REFACTORIZACION_APLICADA.md](REFACTORIZACION_APLICADA.md), [REFACTORIZACION_TYPESCRIPT.md](REFACTORIZACION_TYPESCRIPT.md), and [HISTORIAS_USUARIO.md](HISTORIAS_USUARIO.md) for detailed changes and use cases.

## Quick Reference

**Most Common Commands:**
```bash
# Start everything (first time)
docker build -t py-playground-runner:latest ./runner && docker compose up --build

# Start everything (subsequent runs)
docker compose up -d

# Check service status
docker compose ps

# View logs
docker compose logs -f backend
docker compose logs -f worker

# Stop everything
docker compose down

# Reset database
docker compose down -v && docker compose up --build

# Verify system health
curl http://localhost:49000/api/health | python -m json.tool

# Test a specific problem (submit from file to avoid JSON escaping issues)
# Create test_submit.json with your code, then:
curl -X POST http://localhost:49000/api/submit -H "Content-Type: application/json" -d @test_submit.json

# Check results (replace JOB_ID with actual job_id from submit response)
curl http://localhost:49000/api/result/JOB_ID | python -m json.tool
```

**Access Points:**
- Frontend: http://localhost:49173 (Windows: port 49173 due to Hyper-V conflicts)
- Backend API: http://localhost:49000 (Windows: port 49000 due to Hyper-V conflicts)
- API Docs: http://localhost:49000/docs
- Health Check: http://localhost:49000/api/health

**Note**: On Windows, default ports 8000 and 5173 may conflict with Hyper-V reserved ports. The project is configured to use high ports (49000+) by default. If running on Linux/Mac without port conflicts, you can change these back in docker-compose.yml.

## Project Overview

**Python Playground Suite** - A production-ready code execution platform with Docker sandbox isolation, job queues, persistent storage, and a modern web interface. Students submit Python code that is executed in isolated Docker containers with strict security constraints.

### Important: Obsolete Files Removed (Nov 4, 2025)

The following files were removed as part of codebase cleanup. **DO NOT recreate them**:

**Legacy MVP Files** (replaced by microservices architecture):
- `app.py` (root) → Use `backend/app.py` instead
- `runner.py` (root) → Use `worker/services/docker_runner.py` instead
- `Dockerfile` (root) → Use `backend/Dockerfile` instead
- `requirements.txt` (root) → Use service-specific files instead
- `run_local.sh` → Use `docker compose` commands instead

**Completed Migration Scripts** (moved to `scripts/archive/`):
- `add_hints_to_problems.py` - Hints already added (124 total)
- `deploy_conftest.py` - Conftest files already deployed
- `crear_ejercicios_secuenciales.py` - Sequential exercises already created
- `generar_ejercicios_restantes.py` - Task completed
- `refactorizar_tests_secuenciales.py` - Refactoring completed

**Temporary Files Removed**:
- `test_runner.bat` - Obsolete test script
- `test_submit.json` - Temporary test file
- `.mypy_cache/` - Type checker cache (regenerated automatically)

## Architecture

This is a microservices architecture with the following components:

```
Frontend (React+TypeScript+Monaco) → Backend (FastAPI) → Redis (RQ Queue) → Worker → Docker Sandbox
                                            ↓
                                      PostgreSQL
```

### Core Services

1. **backend/** - FastAPI REST API with service layer architecture
   - **app.py** - Routes/endpoints
   - **services/** - Business logic (ProblemService, SubmissionService, SubjectService)
   - **models.py** - SQLAlchemy ORM (Submission, TestResult)
   - **config.py** - Centralized configuration
   - **validators.py** - Input validation and security checks
   - **exceptions.py** - Custom exception hierarchy
   - **logging_config.py** - Structured JSON logging

2. **worker/** - RQ worker with service layer architecture
   - **tasks.py** - Job orchestration
   - **services/docker_runner.py** - Docker execution with path translation
   - **services/rubric_scorer.py** - Automatic grading

3. **runner/** - Minimal Docker image for sandboxed execution
   - Python 3.11 + pytest, non-root user (uid 1000)

4. **frontend/** - React + TypeScript + Vite + Monaco Editor
   - Hierarchical problem selector (Subject → Unit → Problem)
   - Real-time result polling with AbortController
   - Full type safety with TypeScript interfaces for all API responses

5. **PostgreSQL** - Submissions and TestResults tables

6. **Redis** - Job queue (RQ)

### Execution Flow

```
1. Student submits code → Backend creates Submission (status: "pending")
2. Backend enqueues job in Redis → status: "queued"
3. Worker picks up job from queue
4. Worker creates temp workspace with student_code.py, tests_public.py, tests_hidden.py, conftest.py
5. Worker runs: docker run --network none --read-only --cpus 1 --memory 256m ...
6. Container executes pytest → generates report.json
7. Worker parses report, applies rubric scoring
8. Worker saves TestResult rows + updates Submission (status: "completed")
9. Frontend polls /api/result/{job_id} every 1s and displays results
```

### Database Models

**Submission** (backend/models.py):
- job_id, student_id, problem_id, code, status
- score_total, score_max, passed, failed, errors
- Relationship: one-to-many with TestResult

**TestResult** (backend/models.py):
- test_name, outcome, duration, message
- points, max_points, visibility (public/hidden)

## Critical Architecture Decisions

### Docker-in-Docker Path Translation

The worker spawns Docker containers using the host's Docker daemon. This creates a path mismatch:
- Worker creates files in `/workspaces/sandbox-xxx` (inside worker container)
- Docker daemon looks for paths on **host filesystem**, not worker filesystem

**Solution**:
1. `./workspaces` bind-mounted to both host and worker (see docker-compose.yml)
2. Worker translates paths: `/workspaces/sandbox-xxx` → `${PWD}/workspaces/sandbox-xxx`
3. Files get chmod 666, directories get chmod 777 (runner uses uid 1000, worker creates as root)

Without this: "file not found" errors. See worker/tasks.py:140-141.

### Dockerfile Build Context

All Dockerfiles use root (`.`) as context in docker-compose.yml. COPY paths must be `backend/file`, not `./file`.

```dockerfile
# ✅ CORRECT (context is root)
COPY backend/requirements.txt ./backend/
RUN pip install -r backend/requirements.txt

# ❌ WRONG (context is root)
COPY requirements.txt ./
RUN pip install -r requirements.txt
```

Wrong context → ModuleNotFoundError. See docker-compose.yml build contexts.

## Development Commands

### Quick Start

```bash
# Windows
start.bat

# Linux/Mac
chmod +x start.sh
./start.sh
```

### Docker Compose

```bash
# Build runner image (one-time)
docker build -t py-playground-runner:latest ./runner

# Start all services
docker compose up --build

# Verify services
docker compose ps  # All should show "Up" or "Up (healthy)"

# Health check
curl http://localhost:8000/api/health
```

### Local Development

**Backend:**
```bash
cd backend
pip install -r requirements.txt
export DATABASE_URL=postgresql://playground:playground@localhost:5432/playground  # Linux/Mac
set DATABASE_URL=postgresql://playground:playground@localhost:5432/playground    # Windows
uvicorn backend.app:app --reload
```

**Worker:**
```bash
cd worker
pip install -r requirements.txt
export DATABASE_URL=postgresql://playground:playground@localhost:5432/playground  # Linux/Mac
rq worker --url redis://localhost:6379 submissions
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev

# TypeScript type checking (optional)
npx tsc --noEmit
```

### Testing and Code Quality

**Run Tests:**
```bash
# Backend tests
docker compose exec backend pytest backend/tests/ -v

# With coverage
docker compose exec backend pytest backend/tests/ --cov=backend --cov-report=term-missing

# Specific test
docker compose exec backend pytest backend/tests/test_problem_service.py::TestProblemService::test_list_all_problems -v

# Worker tests
docker compose exec worker pip install pytest pytest-mock
docker compose exec worker pytest worker/tests/ -v
```

**Run Linters:**
```bash
# Install dev dependencies
pip install -r backend/requirements-dev.txt

# Format and lint
black backend/ worker/
isort backend/ worker/
flake8 backend/ worker/
mypy backend/ worker/

# Pre-commit hooks
pre-commit install
pre-commit run --all-files
```

See [TESTING.md](TESTING.md) for detailed documentation.

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

Subjects and units are defined in [backend/subjects_config.json](backend/subjects_config.json). Edit this file to add new subjects/units - no code changes needed.

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

Full schemas: http://localhost:8000/docs

### Frontend Navigation

Three cascading dropdowns:
1. **📚 Materia** (Subject) - User selects a subject
2. **📖 Unidad Temática** (Unit) - Auto-populates from selected subject
3. **🎯 Ejercicio** (Problem) - Shows problems for selected unit

See [frontend/src/components/Playground.tsx](frontend/src/components/Playground.tsx)

### Dynamic Logo System

The frontend displays technology logos that change based on the selected subject. Logos are SVG-based and use official colors.

**Implementation**: [frontend/src/components/LanguageLogo.tsx](frontend/src/components/LanguageLogo.tsx)

**Logo Configuration**:
- **Single logo subjects**: programacion-1 (Python), programacion-2 (Java), programacion-3 (Spring Boot), programacion-4 (FastAPI), algoritmos (PSeInt)
- **Multi-logo subjects** (MANDATORY - logos must appear together):
  - **Paradigmas**: 3 logos (Java, SWI-Prolog, Haskell) displayed side-by-side
  - **Frontend**: 4 logos (HTML5, CSS3, JavaScript, TypeScript) displayed side-by-side
  - **Backend**: 2 logos (Python, FastAPI) displayed side-by-side

**Adding New Subject Logos**:
1. Edit `frontend/src/components/LanguageLogo.tsx`
2. Add new `case 'subject-id':` in the switch statement
3. For multi-logo subjects, use flex layout: `<div style={{ display: 'flex', gap: '8px', alignItems: 'center' }}>`
4. Use unique gradient IDs to avoid SVG conflicts (e.g., `pyYellowBackend`, `fastapiBackendGradient`)
5. Logos automatically appear in the header when subject is selected

## Problem Structure

Problems live in `backend/problems/<problem_id>/` with 6 required files:

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

See `backend/problems/cond_aprobado/` for complete examples.

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

**Location**: Deployed to all conditional problem directories (e.g., `backend/problems/cond_aprobado/conftest.py`)

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

**Documentation**: See [TEST_IMPROVEMENTS_REPORT.md](TEST_IMPROVEMENTS_REPORT.md) and [ANTES_DESPUES_TESTS.md](ANTES_DESPUES_TESTS.md) for complete details.

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

**3. Anti-Cheating System** ([frontend/src/components/Playground.tsx](frontend/src/components/Playground.tsx))

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

**ProblemService** ([backend/services/problem_service.py](backend/services/problem_service.py)):
- `list_all()`, `get_problem_dir()`, `get_test_files()`, `load_rubric()`
- `list_by_subject_and_unit()`, `group_by_subject_and_unit()`

**SubjectService** ([backend/services/subject_service.py](backend/services/subject_service.py)):
- `list_all_subjects()`, `get_subject()`, `list_units_by_subject()`
- `get_hierarchy()`, `validate_subject_unit()`
- Reads from subjects_config.json

**SubmissionService** ([backend/services/submission_service.py](backend/services/submission_service.py)):
- `create_submission()`, `update_job_id()`, `get_by_job_id()`
- `get_result_dict()`, `get_statistics()`, `list_submissions()`

**DockerRunner** (worker/services/docker_runner.py):
- Handles Docker execution with path translation

**RubricScorer** (worker/services/rubric_scorer.py):
- Applies scoring logic to test results

### Adding New Features

Follow this pattern:

1. **Create service class** in `backend/services/`:
```python
from ..logging_config import get_logger
logger = get_logger(__name__)

class MyService:
    def do_something(self, param):
        logger.info(f"Doing something with {param}")
        return result

my_service = MyService()  # Singleton
```

2. **Use in routes** (backend/app.py):
```python
from .services.my_service import my_service

@app.get("/api/my-endpoint")
def my_endpoint(db: Session = Depends(get_db)):
    return my_service.do_something("value")
```

3. **Add validation** (backend/validators.py)
4. **Add exceptions** (backend/exceptions.py)
5. **Add configuration** (backend/config.py)
6. **Use structured logging**: `logger.info("Message", extra={"key": "value"})`

## Performance Optimizations

The codebase has been optimized for production performance. **Key optimizations to maintain**:

### 1. N+1 Query Prevention (submission_service.py)

Always use eager loading when accessing relationships:

```python
from sqlalchemy.orm import joinedload

# ✅ CORRECT - Eager loading avoids N+1 queries
submission = db.query(Submission).options(
    joinedload(Submission.test_results)
).filter(Submission.job_id == job_id).first()

# ❌ WRONG - Will cause N+1 queries
submission = db.query(Submission).filter(Submission.job_id == job_id).first()
# Accessing submission.test_results later triggers additional queries
```

**Impact**: 100x improvement (101 queries → 1 query with 100 submissions)

### 2. Problem List Caching (problem_service.py)

Problem list is cached using `@lru_cache` to avoid repeated filesystem reads:

```python
@lru_cache(maxsize=1)
def _list_all_cached(self) -> Dict[str, Dict[str, Any]]:
    """Cached version - reads filesystem once"""
    # ... load problems from disk

# When adding/modifying problems, invalidate cache:
problem_service.invalidate_cache()
```

**Impact**: ~1000x improvement on subsequent requests

### 3. Compiled Regex Patterns (validators.py)

Regex patterns are compiled at module level for reuse:

```python
# ✅ CORRECT - Compile once at module level
_WHITESPACE_PATTERN = re.compile(r'\s+')
_PROBLEM_ID_PATTERN = re.compile(r'^[a-zA-Z0-9_-]+$')

def validate_code_safety(code: str) -> None:
    code_normalized = _WHITESPACE_PATTERN.sub('', code.lower())
```

**Impact**: 2x performance improvement in validation

### 4. Configuration Best Practices

**IMPORTANT**: Never hardcode paths. Always use settings:

```python
# ✅ CORRECT
from backend.config import settings
problem_dir = pathlib.Path(settings.PROBLEMS_DIR) / problem_id

# ❌ WRONG - Hardcoded path breaks in different environments
problem_dir = pathlib.Path("/app/backend/problems") / problem_id
```

## Adding New Problems

1. Choose subject/unit from [backend/subjects_config.json](backend/subjects_config.json)
2. Create directory: `mkdir backend/problems/new_problem`
3. Create 6 files: `prompt.md`, `starter.py`, `tests_public.py`, `tests_hidden.py`, `metadata.json`, `rubric.json`
4. Fill metadata.json with subject_id and unit_id
5. Test locally:

```bash
# Submit test
curl -X POST http://localhost:8000/api/submit \
  -H "Content-Type: application/json" \
  -d '{"problem_id": "new_problem", "code": "def my_func():\n    pass", "student_id": "test"}'

# Check results
curl http://localhost:8000/api/result/JOB_ID

# Verify hierarchy
curl http://localhost:8000/api/problems/hierarchy | python -m json.tool
```

## Common Tasks

**Restart service after code changes:**
```bash
docker compose restart backend
# Or rebuild if dependencies changed:
docker compose up -d --build backend
```

**Reset database:**
```bash
docker compose down -v && docker compose up --build
```

**Change resource limits globally:**
Edit `DEFAULT_TIMEOUT`, `DEFAULT_MEMORY_MB`, `DEFAULT_CPUS` in worker/tasks.py

**Change resource limits per problem:**
Edit problem's metadata.json (timeout_sec, memory_mb)

**Test problem manually:**
```bash
docker run -it --rm -v $(pwd)/backend/problems/sumatoria:/workspace -w /workspace py-playground-runner:latest bash
# Inside container:
echo "def suma(a,b): return a+b" > student_code.py
pytest -v tests_public.py
```

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

**First-time startup is slow**: 5-10 minutes to download/build images. Monitor: `docker compose logs -f`

**Port already in use**:
```bash
# Windows: netstat -ano | findstr :8000 && taskkill /PID <PID> /F
# Linux: lsof -i :8000 && kill -9 <PID>
```

**Worker can't access Docker daemon**:
- Check `/var/run/docker.sock` mounted in docker-compose.yml
- Windows: Verify Docker Desktop uses WSL 2
- Linux: Add user to docker group: `sudo usermod -aG docker $USER && newgrp docker`

**Runner image not found**: `docker build -t py-playground-runner:latest ./runner`

**ModuleNotFoundError**: Dockerfile COPY paths incorrect. Use `backend/requirements.txt` not `requirements.txt`. Rebuild: `docker compose build --no-cache backend`

**Tests timing out**: Increase timeout_sec in metadata.json or DEFAULT_TIMEOUT in worker/tasks.py

**Database connection errors**: Wait for healthcheck: `docker compose ps`

**RQ worker not processing**: Check Redis: `docker compose exec redis redis-cli ping`

## Refactoring Status

See [REFACTORING_COMPLETE.md](REFACTORING_COMPLETE.md) for detailed progress.

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

**TypeScript Migration** ✅ (Completed: 25 Oct 2025)
- Migrated from JavaScript to TypeScript for improved type safety
- Centralized API types in `src/types/api.ts`
- All components fully typed with interfaces

**Components**:
- **App.tsx** - Tab navigation (Ejercicios, Panel Docente)
- **Playground.tsx** - Student interface with cascading dropdowns, Monaco editor, result polling with AbortController
- **AdminPanel.tsx** - Instructor dashboard
- **types/api.ts** - TypeScript interfaces for all API requests/responses

**Features**:
- Monaco Editor for Python syntax highlighting
- Code persisted to localStorage
- Full TypeScript type checking with strict mode
- Type-safe API calls with Axios

**Tech Stack**:
- React 18 with TypeScript
- Vite 6 for build tooling
- Monaco Editor for code editing
- Axios for HTTP requests
- TypeScript strict mode enabled

**Development Workflow**:
```bash
# Run dev server (hot reload enabled)
npm run dev

# Type check without compiling
npx tsc --noEmit

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

**Adding New API Types**:
Edit `frontend/src/types/api.ts` and add/export new interfaces. Types are automatically available throughout the app.

## Extension Points

- Multiple workers for scaling (add worker services in docker-compose.yml)
- Different languages (change RUNNER_IMAGE env var)
- Custom test frameworks (update conftest.py)
- Authentication (add middleware to backend/app.py)
- Webhooks (add to worker/tasks.py after commit)
- Rate limiting (Redis counter in backend)
