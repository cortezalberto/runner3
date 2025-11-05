# Python Playground Backend - Versión para Render.com

Backend API para plataforma de ejercicios de programación.

**Versión**: Render.com (sin Docker)
**Stack**: Python 3.11, FastAPI, PostgreSQL, Redis, RQ Worker

---

## ⚠️ LIMITACIÓN IMPORTANTE: Sin Ejecución de Código

**IMPORTANTE**: Esta versión está adaptada para **Render.com**, que NO soporta Docker.

### Funcionalidades Disponibles ✅

- **API REST completo**:
  - `GET /api/problems` - Listar todos los problemas
  - `GET /api/problems/{problem_id}` - Detalle de un problema
  - `GET /api/subjects` - Listar subjects (materias)
  - `GET /api/subjects/{subject_id}/units` - Listar units por subject
  - `GET /api/problems/hierarchy` - Jerarquía completa (subjects → units → problems)
  - `GET /api/health` - Health check (database + redis)
  - `GET /api/admin/summary` - Estadísticas agregadas

- **Panel administrativo**: Estadísticas, submissions recientes
- **Sistema de pistas**: 4 niveles progresivos por problema
- **CORS**: Configurado para frontend en Vercel
- **Persistent storage**: PostgreSQL + Redis

### Funcionalidades NO Disponibles ❌

- **Ejecución de código**: POST `/api/submit` retorna `status: "unavailable"`
- **Evaluación automática**: Sin tests públicos/ocultos
- **Puntajes**: Sin scoring automático

**Mensaje que verán los estudiantes**:
```
⚠️ La ejecución de código NO está disponible en Render.com (no soporta Docker).
El sistema solo permite ver problemas y jerarquía de contenidos.
Para evaluar código, despliega en Railway, Fly.io, o un VPS con Docker.
```

### ¿Por qué esta limitación?

Render.com free tier NO permite ejecutar Docker containers. El sistema requiere Docker para:
- Crear sandboxes aislados (seguridad)
- Ejecutar código de estudiantes sin acceso a red
- Ejecutar pytest con tests públicos/ocultos

**Alternativas para ejecución completa**:
- **Railway.com** (Hobby $5/mes) - ✅ Soporta Docker
- **Fly.io** - ✅ Con Docker runtime
- **DigitalOcean App Platform** - ✅ Con soporte Docker
- **VPS propio** - ✅ DigitalOcean Droplet, Linode con Docker instalado

---

## Estructura del Proyecto

```
Back/
├── backend/              # FastAPI application
│   ├── app.py            # Main routes/endpoints
│   ├── config.py         # Configuration (DATABASE_URL, REDIS_URL, CORS)
│   ├── models.py         # SQLAlchemy models (Submission, TestResult)
│   ├── services/         # Business logic layer
│   │   ├── problem_service.py
│   │   ├── submission_service.py
│   │   └── subject_service.py
│   ├── problems/         # 31 coding problems
│   │   ├── sec_hola_mundo/
│   │   ├── cond_aprobado/
│   │   └── ...
│   └── requirements.txt
├── worker/               # RQ Worker (adapted for no Docker)
│   ├── tasks.py          # Job processing (returns "unavailable")
│   └── requirements.txt
├── common/               # Shared code
│   ├── database.py
│   ├── models.py
│   ├── config.py
│   └── logging_config.py
├── Procfile              # Render start commands
├── runtime.txt           # Python 3.11.9
├── requirements.txt      # Combined dependencies
└── RENDER_QUICKSTART.md  # Deployment guide
```

---

## Deployment a Render.com

### Guías Disponibles

1. **RENDER_QUICKSTART.md** - ⭐ Guía rápida paso a paso (RECOMENDADO)
2. **RENDER_TROUBLESHOOTING.md** - Solución a errores comunes
3. **RENDER_ENV_VARS.txt** - Template de variables de entorno
4. **DEPLOY_RENDER.md** - Documentación completa

### Quick Start

1. **Crear PostgreSQL Database** en Render Dashboard
2. **Crear Redis en Upstash** (Render no ofrece Redis gratis): https://console.upstash.com/
3. **Crear Web Service**:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `cd Back && gunicorn backend.app:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT`
4. **Crear Background Worker**:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `cd Back && python -m rq.cli worker submissions --url $REDIS_URL`
5. **Configurar Variables de Entorno** (en ambos servicios):
   ```
   DATABASE_URL=postgresql://user:pass@host.render.com/database
   REDIS_URL=redis://default:pass@host.upstash.io:port
   CORS_ORIGINS=https://your-frontend.vercel.app
   CORS_ALLOW_ALL_ORIGINS=false
   ```

### Verificar Deployment

```bash
# Health check
curl https://your-backend.onrender.com/api/health

# Debe retornar:
{
  "service": "api",
  "status": "healthy",
  "database": "healthy",
  "redis": "healthy"
}

# Listar problemas
curl https://your-backend.onrender.com/api/problems | python -m json.tool
```

---

## Desarrollo Local (sin Docker)

### Requisitos

- Python 3.11+
- PostgreSQL 15+
- Redis 7+

### Setup

```bash
# 1. Crear virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# 2. Instalar dependencias
cd Back
pip install -r requirements.txt

# 3. Configurar variables de entorno
cp .env.example .env
# Edita .env con tus credenciales de PostgreSQL y Redis

# 4. Inicializar base de datos
# (Render hace esto automáticamente usando SQLAlchemy create_all)

# 5. Ejecutar backend
cd backend
uvicorn app:app --reload --host 0.0.0.0 --port 8000

# 6. Ejecutar worker (en otra terminal)
cd worker
python -m rq.cli worker submissions --url redis://localhost:6379/0
```

### Acceso

- API: http://localhost:8000
- Docs: http://localhost:8000/docs
- Health: http://localhost:8000/api/health

---

## Endpoints Principales

### Públicos (Estudiantes)

```bash
# Listar problemas
GET /api/problems

# Detalle de problema
GET /api/problems/{problem_id}

# Jerarquía completa (subjects → units → problems)
GET /api/problems/hierarchy

# Enviar código (retorna "unavailable" en Render)
POST /api/submit
{
  "problem_id": "sec_hola_mundo",
  "code": "def main():\n    print('Hola Mundo!')",
  "student_id": "123"
}

# Obtener resultado
GET /api/result/{job_id}
```

### Administrativos

```bash
# Estadísticas agregadas
GET /api/admin/summary

# Submissions recientes
GET /api/admin/submissions?limit=50
```

---

## Configuración CORS

Por defecto, el backend acepta requests desde:
- `http://localhost:5173` (Vite dev server)
- `http://localhost:5174` (Vite dev server - puerto alternativo)
- `https://front-eight-rho-61.vercel.app` (Vercel production)

Para agregar más orígenes:

**Desarrollo (.env)**:
```env
CORS_ALLOW_ALL_ORIGINS=true
```

**Producción (Render Dashboard)**:
```env
CORS_ORIGINS=https://frontend1.vercel.app,https://frontend2.vercel.app
CORS_ALLOW_ALL_ORIGINS=false
```

---

## Troubleshooting

### Backend no arranca

**Error**: `ModuleNotFoundError: No module named 'app'`

**Solución**: Verifica que el Start Command incluya `cd Back`:
```bash
cd Back && gunicorn backend.app:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT
```

### Database connection failed

**Causa**: `DATABASE_URL` incorrecta

**Solución**: Usa la "Internal Database URL" de Render (termina en `.render.com`), NO la External URL.

### CORS errors desde frontend

**Causa**: `CORS_ORIGINS` no incluye el dominio del frontend

**Solución**:
```env
CORS_ORIGINS=https://tu-frontend.vercel.app
```
- Sin trailing slash
- HTTPS (no HTTP)
- Sin espacios

### Worker no procesa jobs

**Causa**: `REDIS_URL` diferente en Web Service y Worker

**Solución**: Verifica que ambos servicios tengan EXACTAMENTE el mismo `REDIS_URL`.

Ver **RENDER_TROUBLESHOOTING.md** para más detalles.

---

## Documentación Adicional

- **RENDER_QUICKSTART.md** - Guía rápida de deployment (⭐ RECOMENDADO)
- **RENDER_TROUBLESHOOTING.md** - Errores comunes y soluciones
- **RENDER_ENV_VARS.txt** - Template de variables de entorno
- **DEPLOY_RENDER.md** - Documentación completa de deployment

---

## Stack Tecnológico

- **Framework**: FastAPI 0.115.2
- **ASGI Server**: Uvicorn 0.30.6 con Gunicorn workers
- **Database**: PostgreSQL 15+ (SQLAlchemy ORM)
- **Queue**: Redis 7+ con RQ (Redis Queue)
- **Validation**: Pydantic v2
- **Logging**: Structured JSON logging
- **Security**: Input validation, CORS, rate limiting ready

---

## Arquitectura

```
Frontend (Vercel)  ─HTTP─>  Backend (Render)  ─>  Redis Queue  ─>  Worker
                            [FastAPI + Gunicorn]               [RQ Worker]
                                   ↓                               ↓
                            PostgreSQL (Render)           (Returns "unavailable")
```

---

## Licencia

Proyecto educativo - Consultar con el propietario del repositorio.
