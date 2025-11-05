# 🚀 Deploy a Render - Guía Completa

Esta guía te ayudará a desplegar el backend de Python Playground en Render.com.

## 📋 Prerequisitos

1. **Cuenta en Render**: Crea una cuenta gratuita en [render.com](https://render.com)
2. **Repositorio Git**: Tu código debe estar en GitHub, GitLab o Bitbucket
3. **Archivos preparados**: ✅ Ya están incluidos en este repositorio

## 📁 Archivos para Deploy

Los siguientes archivos ya están configurados en la carpeta `Back/`:

- ✅ `backend/requirements.txt` - Incluye Gunicorn
- ✅ `Procfile` - Comandos de inicio para web y worker
- ✅ `runtime.txt` - Especifica Python 3.11
- ✅ `render.yaml` - Configuración de servicios (opcional)
- ✅ `.env.example` - Plantilla de variables de entorno

## 🔧 Paso 1: Preparar el Repositorio

### Opción A: Usar el directorio Back/ completo

```bash
# Subir la carpeta Back/ a un repositorio de GitHub
cd Back
git init
git add .
git commit -m "Initial commit - Backend for Render"
git branch -M main
git remote add origin https://github.com/tu-usuario/python-playground-backend.git
git push -u origin main
```

### Opción B: Ya tienes el repositorio

Si ya tienes el código en GitHub, asegúrate de que la carpeta `Back/` esté en el repositorio.

## 🗄️ Paso 2: Crear Base de Datos PostgreSQL

1. Ve a tu [Dashboard de Render](https://dashboard.render.com/)
2. Click en **"New +"** → **"PostgreSQL"**
3. Configura:
   - **Name**: `python-playground-db`
   - **Database**: `playground`
   - **User**: `playground`
   - **Region**: Elige el más cercano a tu ubicación
   - **Plan**: Free (o el que prefieras)
4. Click **"Create Database"**
5. **Guarda la "Internal Database URL"** - la necesitarás después

## 🔴 Paso 3: Crear Redis Instance

### Opción A: Usar Upstash (Recomendado para Free Tier)

Render no ofrece Redis gratis. Usa Upstash:

1. Crea cuenta en [upstash.com](https://upstash.com)
2. Crea una nueva base de datos Redis
3. Copia la "Redis URL" (formato: `redis://default:password@host:port`)

### Opción B: Render Redis (Pago)

1. En Render Dashboard: **"New +"** → **"Redis"**
2. Configura y crea
3. Guarda la "Internal Redis URL"

## 🌐 Paso 4: Crear Web Service (Backend API)

1. En Render Dashboard: **"New +"** → **"Web Service"**
2. Conecta tu repositorio de GitHub
3. Configura:

   **Basic Settings:**
   - **Name**: `python-playground-backend`
   - **Region**: Mismo que la base de datos
   - **Branch**: `main`
   - **Root Directory**: `Back` (si tu repo tiene la carpeta Back)
   - **Runtime**: `Python 3`
   - **Build Command**:
     ```bash
     pip install -r backend/requirements.txt && pip install -r common/requirements.txt 2>/dev/null || true
     ```
   - **Start Command**:
     ```bash
     gunicorn backend.app:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT
     ```

   **Advanced Settings:**
   - **Plan**: Free (o el que prefieras)
   - **Environment**: Python 3.11 (ver runtime.txt)

4. **Variables de Entorno** (Environment Variables):

   Click en **"Advanced"** → **"Add Environment Variable"** y agrega:

   ```env
   # Database (copia de Render PostgreSQL)
   DATABASE_URL=postgresql://user:password@host/database

   # Redis (de Upstash o Render Redis)
   REDIS_URL=redis://default:password@host:port

   # CORS - Agrega tu dominio de frontend
   CORS_ORIGINS=https://tu-frontend.com,https://www.tu-frontend.com
   CORS_ALLOW_ALL_ORIGINS=false

   # PostgreSQL credentials (para docker-compose local - opcional)
   POSTGRES_DB=playground
   POSTGRES_USER=playground
   POSTGRES_PASSWORD=random_secure_password_here

   # Runner config (no usarás Docker en Render, pero evita errores)
   RUNNER_IMAGE=py-playground-runner:latest
   WORKSPACE_DIR=/tmp/workspaces

   # Python path (importante!)
   PYTHONPATH=/opt/render/project/src/Back
   ```

5. Click **"Create Web Service"**

## 👷 Paso 5: Crear Worker Service (RQ Worker)

1. En Render Dashboard: **"New +"** → **"Background Worker"**
2. Conecta el mismo repositorio
3. Configura:

   **Basic Settings:**
   - **Name**: `python-playground-worker`
   - **Region**: Mismo que backend y DB
   - **Branch**: `main`
   - **Root Directory**: `Back`
   - **Runtime**: `Python 3`
   - **Build Command**:
     ```bash
     pip install -r worker/requirements.txt && pip install -r common/requirements.txt 2>/dev/null || true
     ```
   - **Start Command**:
     ```bash
     python -m rq.cli worker submissions --url $REDIS_URL
     ```

4. **Variables de Entorno**:
   - Copia las MISMAS variables que usaste en el Web Service
   - Importante: `DATABASE_URL`, `REDIS_URL`, `PYTHONPATH`

5. Click **"Create Background Worker"**

## ⚠️ Limitaciones Importantes de Render (Free Tier)

### 1. **Docker NO está disponible** ❌

El sistema de ejecución de código (runner) usa Docker para sandbox. Esto **NO funcionará** en Render Free Tier porque no permite Docker-in-Docker.

**Soluciones**:

**Opción A: Deploy simplificado (solo API sin ejecución)**
- Desplegar solo el backend API para ver problemas
- Deshabilitar la ejecución de código temporalmente
- Útil para testing y desarrollo del frontend

**Opción B: Usar otro servicio para el runner**
- Backend y Worker en Render
- Runner/Sandbox en un servicio que soporte Docker:
  - [Railway.app](https://railway.app) - Soporta Docker
  - [Fly.io](https://fly.io) - Soporta Docker
  - VPS tradicional (DigitalOcean, Linode, etc.)

**Opción C: Arquitectura sin Docker (Refactorización)**
- Usar RestrictedPython o PyPy sandbox
- Ejecutar código en proceso con límites de recursos
- Menos seguro pero funcional en Render

### 2. **Filesystem efímero**

Los archivos en `/tmp/workspaces` se borran en cada deploy. Esto está OK porque el worker limpia después de cada ejecución.

### 3. **Free tier se duerme**

El servicio gratuito se "duerme" después de 15 minutos sin uso. Primera petición será lenta (30-60 segundos).

## ✅ Paso 6: Verificar Deploy

1. **Backend API**: Ve a la URL que Render te dio (ej: `https://python-playground-backend.onrender.com`)

   Prueba:
   ```bash
   curl https://tu-backend.onrender.com/api/health
   ```

   Deberías ver:
   ```json
   {
     "service": "api",
     "status": "healthy",
     "database": "healthy",
     "redis": "healthy"
   }
   ```

2. **Logs**: Revisa los logs en Render Dashboard
   - Web Service: Verifica que Gunicorn inició
   - Worker: Verifica que RQ worker se conectó a Redis

3. **Test de CORS**:
   ```bash
   curl -I -H "Origin: https://tu-frontend.com" https://tu-backend.onrender.com/api/health
   ```

   Busca el header: `access-control-allow-origin`

## 🔧 Configuración Avanzada

### Escalar Workers

Si necesitas más workers para procesamiento paralelo:

```bash
# En Start Command del worker:
python -m rq.cli worker submissions --url $REDIS_URL --burst
```

O crear múltiples worker services en Render.

### Health Checks

Render automáticamente hace health checks en `/` cada 30 segundos. Para mejorar:

1. Ve a Settings del Web Service
2. **Health Check Path**: `/api/health`

### Custom Domain

1. En Settings del Web Service
2. **Custom Domains** → Add custom domain
3. Configura DNS según instrucciones de Render
4. Actualiza `CORS_ORIGINS` con tu dominio

## 🐛 Troubleshooting

### Error: "ModuleNotFoundError: No module named 'common'"

**Solución**: Agregar a Environment Variables:
```env
PYTHONPATH=/opt/render/project/src/Back
```

### Error: "Database connection failed"

**Solución**:
1. Verifica que `DATABASE_URL` sea la "Internal Database URL" de Render
2. Formato: `postgresql://user:pass@host/db`
3. NO uses `localhost` - usa el host interno de Render

### Error: "Redis connection refused"

**Solución**:
1. Verifica `REDIS_URL` en Environment Variables
2. Si usas Upstash, verifica que la URL sea correcta
3. Formato: `redis://default:password@host:port`

### Worker no procesa jobs

**Solución**:
1. Verifica logs del worker: `Listening on submissions`
2. Verifica que `REDIS_URL` sea exactamente igual en backend y worker
3. Prueba manualmente:
   ```bash
   curl -X POST https://tu-backend.onrender.com/api/submit \
     -H "Content-Type: application/json" \
     -d '{"problem_id":"sec_hola_mundo","student_id":"test","code":"def main():\n    print(\"Hola Mundo!\")"}'
   ```

### App se duerme (Free Tier)

**Solución**: Usar un servicio de "keep-alive":
- [UptimeRobot](https://uptimerobot.com) - Ping cada 5 minutos
- [Cron-job.org](https://cron-job.org) - Scheduled pings
- Nota: Solo despierta el backend, el worker se despierta cuando hay jobs

## 📊 Monitoreo

Render provee métricas básicas:

1. Dashboard → Tu servicio → Metrics
2. CPU, Memory, Request/sec
3. Logs en tiempo real

Para monitoreo avanzado:
- [Sentry](https://sentry.io) - Error tracking
- [LogDNA](https://logdna.com) - Log management
- [New Relic](https://newrelic.com) - APM

## 💰 Costos

**Free Tier**:
- Web Service: Gratis (duerme después 15 min)
- Background Worker: Gratis (duerme cuando no hay jobs)
- PostgreSQL: 1 DB gratis (90 días, luego $7/mes)
- Redis: NO incluido (usar Upstash gratis)

**Paid Plans** (si necesitas más):
- Starter: $7/mes por servicio
- Standard: $25/mes por servicio
- Pro: $85/mes por servicio

## 🔗 Recursos

- [Render Docs - FastAPI](https://render.com/docs/deploy-fastapi)
- [Render Docs - Python](https://render.com/docs/python-version)
- [Render Docs - Environment Variables](https://render.com/docs/environment-variables)
- [Gunicorn Docs](https://docs.gunicorn.org/)

## ✅ Checklist Final

- [ ] Repositorio en GitHub con código de `Back/`
- [ ] PostgreSQL creado en Render
- [ ] Redis creado (Upstash o Render)
- [ ] Web Service creado con todas las env vars
- [ ] Worker Service creado con todas las env vars
- [ ] `PYTHONPATH` configurado en ambos servicios
- [ ] Health check funcionando (`/api/health` retorna 200)
- [ ] CORS configurado con tu dominio de frontend
- [ ] Logs sin errores
- [ ] (Opcional) Custom domain configurado

---

**¿Problemas?** Revisa los logs en Render Dashboard o abre un issue en GitHub.
