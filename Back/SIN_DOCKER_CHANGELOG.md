# Cambios para Deployment sin Docker (Render.com)

**Fecha**: Noviembre 2025
**Objetivo**: Adaptar el backend para Render.com, eliminando dependencia de Docker

---

## 🎯 Resumen de Cambios

El proyecto ha sido adaptado para funcionar en **Render.com**, que NO soporta Docker.

**Estado actual**:
- ✅ API REST completo funciona (ver problemas, jerarquía, estadísticas)
- ❌ Ejecución de código NO funciona (requiere Docker sandbox)

---

## 📁 Archivos Eliminados

### Docker y Runners
```
❌ Back/docker-compose.yml             - Orquestación Docker
❌ Back/backend/Dockerfile             - Imagen backend
❌ Back/worker/Dockerfile              - Imagen worker
❌ Back/runner/                        - Carpeta completa (sandbox Docker)
   ├── Dockerfile
   ├── README.md
   └── requirements.txt
❌ Back/worker/services/docker_runner.py    - Servicio de ejecución Docker
❌ Back/worker/tests/test_docker_runner.py  - Tests de Docker runner
```

**Total eliminado**: 6 archivos + 1 carpeta completa

---

## 🔧 Archivos Modificados

### 1. `Back/worker/tasks.py`
**Cambio**: Función `run_submission_in_sandbox()` simplificada

**Antes**: Ejecutaba código en Docker sandbox
**Ahora**: Retorna status "unavailable" con mensaje explicativo

**Comportamiento nuevo**:
```python
submission.status = "unavailable"
submission.error_message = (
    "⚠️ La ejecución de código NO está disponible en Render.com (no soporta Docker). "
    "El sistema solo permite ver problemas y jerarquía de contenidos. "
    "Para evaluar código, despliega en Railway, Fly.io, o un VPS con Docker."
)
```

### 2. `Back/backend/config.py`
**Cambio**: Eliminadas variables relacionadas con Docker

**Variables eliminadas**:
- `RUNNER_IMAGE` (imagen Docker del runner)
- `DEFAULT_TIMEOUT_SEC` (timeout de ejecución)
- `DEFAULT_MEMORY_MB` (límite de memoria)
- `DEFAULT_CPUS` (límite de CPU)
- `REDIS_HOST`, `REDIS_PORT` (reemplazados por `REDIS_URL` única)

**Variables agregadas**:
- `REDIS_URL` (URL completa de Upstash Redis)
- `CORS_ALLOW_ALL_ORIGINS` (bandera para desarrollo)

### 3. `Back/.env`
**Cambio**: Simplificado para desarrollo local sin Docker

**Contenido nuevo**:
```env
DATABASE_URL=postgresql://playground:playground@localhost:5432/playground
REDIS_URL=redis://localhost:6379/0
CORS_ORIGINS=http://localhost:5173,http://localhost:5174,https://front-eight-rho-61.vercel.app
CORS_ALLOW_ALL_ORIGINS=true
```

**Nota agregada**:
```
# La ejecución de código (Docker sandbox) NO está disponible en Render.com
# Solo el API para ver problemas y jerarquía funcionará.
```

### 4. `Back/.env.example`
**Cambio**: Template actualizado para Render deployment

**Contenido nuevo**:
```env
DATABASE_URL=postgresql://playground:CHANGE_PASSWORD@your-db-host.render.com/playground
REDIS_URL=redis://default:CHANGE_PASSWORD@your-redis-host.upstash.io:6379
CORS_ORIGINS=https://your-frontend.vercel.app
CORS_ALLOW_ALL_ORIGINS=false
```

### 5. `Back/RENDER_ENV_VARS.txt`
**Cambio**: Agregada sección de advertencia sobre Docker

**Nuevo contenido**:
```
# ⚠️ LIMITACIÓN CRÍTICA: Docker NO disponible en Render
# Render.com free tier NO soporta Docker.
# ✅ El API funcionará (ver problemas, jerarquía)
# ❌ La ejecución de código NO funcionará (requiere Docker sandbox)
```

### 6. `Back/RENDER_QUICKSTART.md`
**Cambio**: Agregada sección completa sobre limitación de Docker al inicio

**Nueva sección**:
```markdown
## ⚠️ LIMITACIÓN CRÍTICA: Docker NO Disponible

**IMPORTANTE**: Render.com free tier **NO soporta Docker**.

Funcionalidades disponibles:
- ✅ API REST completo
- ❌ Ejecución de código

Alternativas: Railway.com, Fly.io, VPS con Docker
```

### 7. `Back/RENDER_TROUBLESHOOTING.md`
**Cambio**: Agregada advertencia al inicio sobre Docker

**Nueva sección**:
```markdown
## ⚠️ LIMITACIÓN CRÍTICA: Docker NO disponible

ANTES DE REPORTAR ERRORES: Render.com free tier NO soporta Docker.

Comportamiento esperado:
- Backend se despliega correctamente ✅
- POST /api/submit retorna status: "unavailable" ✅
```

---

## 📝 Archivos Creados

### 1. `Back/README.md`
**Propósito**: Documentación principal del backend sin Docker

**Contenido**:
- Limitaciones de Render explicadas claramente
- Funcionalidades disponibles vs no disponibles
- Guía de deployment completa
- Troubleshooting
- Endpoints principales
- Configuración CORS

### 2. `Back/SIN_DOCKER_CHANGELOG.md` (este archivo)
**Propósito**: Registro de todos los cambios realizados

---

## 🎨 Estructura Nueva

```
Back/
├── backend/              # FastAPI app (sin cambios en código de negocio)
│   ├── app.py
│   ├── config.py         ✏️ Modificado (sin variables Docker)
│   ├── models.py
│   └── services/
├── worker/               # RQ Worker adaptado
│   ├── tasks.py          ✏️ Modificado (sin ejecución Docker)
│   └── requirements.txt
├── common/               # Shared code (sin cambios)
├── .env                  ✏️ Modificado (sin variables Docker)
├── .env.example          ✏️ Modificado (template Render)
├── Procfile              ✅ Sin cambios (ya estaba correcto)
├── runtime.txt           ✅ Sin cambios (Python 3.11.9)
├── requirements.txt      ✅ Sin cambios (Gunicorn incluido)
├── README.md             🆕 Creado (documentación principal)
├── RENDER_QUICKSTART.md  ✏️ Modificado (advertencias Docker)
├── RENDER_TROUBLESHOOTING.md  ✏️ Modificado (limitaciones Docker)
├── RENDER_ENV_VARS.txt   ✏️ Modificado (sin variables Docker)
└── SIN_DOCKER_CHANGELOG.md  🆕 Este archivo
```

**Leyenda**:
- ✅ Sin cambios
- ✏️ Modificado
- 🆕 Nuevo
- ❌ Eliminado

---

## 🚀 Deployment a Render

### Servicios Necesarios

1. **PostgreSQL Database** (Render)
2. **Redis Database** (Upstash - Render no ofrece Redis gratis)
3. **Web Service** (Backend API)
4. **Background Worker** (RQ Worker - adaptado, no ejecuta código)

### Variables de Entorno Requeridas

**Web Service Y Worker**:
```env
DATABASE_URL=postgresql://...@hostname.render.com/database
REDIS_URL=redis://default:...@hostname.upstash.io:6379
CORS_ORIGINS=https://your-frontend.vercel.app
CORS_ALLOW_ALL_ORIGINS=false
PYTHONPATH=/opt/render/project/src/Back  # Opcional
```

### Start Commands

**Web Service**:
```bash
cd Back && gunicorn backend.app:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT
```

**Background Worker**:
```bash
cd Back && python -m rq.cli worker submissions --url $REDIS_URL
```

---

## ⚠️ Comportamiento Actual

### Endpoints que Funcionan ✅

```bash
GET /api/health          # Health check (database + redis)
GET /api/problems        # Listar problemas
GET /api/problems/{id}   # Detalle de problema
GET /api/subjects        # Listar subjects
GET /api/problems/hierarchy  # Jerarquía completa
GET /api/admin/summary   # Estadísticas
```

### Endpoints con Limitación ❌

```bash
POST /api/submit         # Retorna status: "unavailable"
GET /api/result/{job_id} # Retorna submission con error_message
```

**Respuesta de POST /api/submit**:
```json
{
  "job_id": "...",
  "status": "queued"
}
```

**Respuesta de GET /api/result/{job_id}**:
```json
{
  "status": "unavailable",
  "ok": false,
  "score_total": 0,
  "score_max": 0,
  "error_message": "⚠️ La ejecución de código NO está disponible en Render.com (no soporta Docker). El sistema solo permite ver problemas y jerarquía de contenidos. Para evaluar código, despliega en Railway, Fly.io, o un VPS con Docker.",
  "test_results": [
    {
      "test_name": "system_check",
      "outcome": "unavailable",
      "message": "Docker no disponible en Render. Use Railway o Fly.io para ejecución de código."
    }
  ]
}
```

---

## 🔮 Próximos Pasos (Opcional)

Si quieres restaurar la funcionalidad completa de ejecución de código:

### Opción 1: Railway.com ($5/mes)
1. Crear cuenta en Railway.com
2. Conectar repositorio GitHub
3. Railway detecta automáticamente el Procfile
4. Agregar PostgreSQL y Redis (incluidos en plan Hobby)
5. Docker funciona out-of-the-box ✅

### Opción 2: Fly.io
1. Instalar `flyctl` CLI
2. `fly launch` (detecta la app Python)
3. Habilitar Docker runtime en fly.toml
4. Agregar PostgreSQL y Redis (Upstash)
5. `fly deploy`

### Opción 3: VPS con Docker
1. Contratar VPS (DigitalOcean Droplet, Linode)
2. Instalar Docker + Docker Compose
3. Clonar repositorio
4. Restaurar archivos Docker eliminados (de commit anterior)
5. `docker compose up -d`

---

## 📚 Documentación de Referencia

- **RENDER_QUICKSTART.md** - Guía rápida deployment (⭐ RECOMENDADO)
- **RENDER_TROUBLESHOOTING.md** - Errores comunes
- **RENDER_ENV_VARS.txt** - Template variables entorno
- **README.md** - Documentación principal
- **DEPLOY_RENDER.md** - Documentación completa

---

## 💡 Resumen Ejecutivo

**Antes**: Sistema completo con ejecución de código en Docker sandbox
**Ahora**: API REST funcional sin ejecución de código (limitación Render.com)

**Funcionalidades mantenidas**:
- 31 problemas de programación visibles ✅
- Jerarquía subjects → units → problems ✅
- Sistema de pistas (4 niveles) ✅
- Panel administrativo ✅
- CORS con Vercel frontend ✅

**Funcionalidades deshabilitadas temporalmente**:
- Ejecución de código estudiantes ❌
- Tests públicos/ocultos ❌
- Scoring automático ❌

**Recomendación**: Para sistema completo, migrar a Railway.com ($5/mes) o VPS con Docker.
