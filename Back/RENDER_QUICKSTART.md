# 🚀 Deploy a Render - Guía Rápida

**Frontend en Vercel**: ✅ https://front-eight-rho-61.vercel.app/
**Backend a desplegar**: Render.com

---

## ⚠️ LIMITACIÓN CRÍTICA: Docker NO Disponible

**IMPORTANTE**: Render.com free tier **NO soporta Docker**.

**Funcionalidades disponibles**:
- ✅ API REST completo (ver problemas, jerarquía, subjects)
- ✅ Panel administrativo (estadísticas)
- ✅ Frontend conecta correctamente con CORS

**Funcionalidades NO disponibles**:
- ❌ Ejecución de código de estudiantes (requiere Docker sandbox)
- ❌ Evaluación automática de submissions
- ❌ Tests públicos/ocultos

Los estudiantes verán un mensaje explicativo:
> "⚠️ La ejecución de código NO está disponible en Render.com (no soporta Docker). El sistema solo permite ver problemas y jerarquía de contenidos."

**Alternativas para ejecución de código**:
- **Railway.com** (Hobby $5/mes) - Soporta Docker ✅
- **Fly.io** - Con Docker runtime ✅
- **DigitalOcean App Platform** - Con soporte Docker ✅
- **VPS propio** (DigitalOcean, Linode) con Docker instalado ✅

---

## 📋 Checklist Pre-Deploy

✅ Gunicorn agregado a requirements.txt
✅ Procfile creado (sin referencias a Docker)
✅ runtime.txt configurado (Python 3.11.9)
✅ render.yaml con configuración completa
✅ CORS configurado para Vercel
✅ Variables de entorno preparadas
✅ Worker adaptado (sin ejecución Docker)

---

## 🎯 Opción 1: Deploy Manual (Recomendado)

### Paso 1: Crear PostgreSQL Database

1. Ve a [Render Dashboard](https://dashboard.render.com/)
2. Click **"New +"** → **"PostgreSQL"**
3. Configura:
   - **Name**: `python-playground-db`
   - **Database**: `playground`
   - **User**: `playground`
   - **Plan**: Free
4. Click **"Create Database"**
5. **Copia la "Internal Database URL"** - la necesitarás

### Paso 2: Crear Redis (Upstash - Gratis)

1. Ve a [Upstash Console](https://console.upstash.com/)
2. Click **"Create Database"**
3. Configura:
   - **Name**: `python-playground-redis`
   - **Region**: Elige el más cercano a tu Render region
4. Click **"Create"**
5. **Copia la "Redis URL"** (formato: `redis://default:password@host:port`)

### Paso 3: Crear Web Service (Backend API)

1. En Render Dashboard: **"New +"** → **"Web Service"**
2. Conecta tu repositorio de GitHub
3. Configura:

   **Basic Settings:**
   - **Name**: `python-playground-backend`
   - **Region**: Same as database
   - **Branch**: `main`
   - **Root Directory**: `Back`
   - **Runtime**: Python 3

   **Build & Deploy:**
   - **Build Command**:
     ```bash
     pip install -r requirements.txt
     ```
   - **Start Command**:
     ```bash
     gunicorn backend.app:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT
     ```

4. **Environment Variables** (Click "Advanced"):

   ```env
   # Database (copia la Internal Database URL de Render PostgreSQL)
   DATABASE_URL=postgresql://user:password@host/database

   # Redis (copia la URL de Upstash)
   REDIS_URL=redis://default:password@host:port

   # CORS - Tu frontend de Vercel
   CORS_ORIGINS=https://front-eight-rho-61.vercel.app
   CORS_ALLOW_ALL_ORIGINS=false

   # Python Path (IMPORTANTE!)
   PYTHONPATH=/opt/render/project/src/Back

   # Runner config (no usarás Docker, pero evita errores)
   RUNNER_IMAGE=py-playground-runner:latest
   WORKSPACE_DIR=/tmp/workspaces
   ```

5. Click **"Create Web Service"**

### Paso 4: Crear Worker Service (RQ Worker)

1. En Render Dashboard: **"New +"** → **"Background Worker"**
2. Conecta el mismo repositorio
3. Configura:

   **Basic Settings:**
   - **Name**: `python-playground-worker`
   - **Region**: Same as backend
   - **Branch**: `main`
   - **Root Directory**: `Back`
   - **Runtime**: Python 3

   **Build & Deploy:**
   - **Build Command**:
     ```bash
     pip install -r requirements.txt
     ```
   - **Start Command**:
     ```bash
     python -m rq.cli worker submissions --url $REDIS_URL
     ```

4. **Environment Variables** (copiar las MISMAS del Web Service):
   - `DATABASE_URL`
   - `REDIS_URL`
   - `PYTHONPATH=/opt/render/project/src/Back`

5. Click **"Create Background Worker"**

---

## 🎯 Opción 2: Deploy Automático con render.yaml

⚠️ **Nota**: render.yaml puede no funcionar en free tier porque no soporta Redis automáticamente.

1. Subir código a GitHub con `render.yaml` incluido
2. En Render Dashboard: **"New +"** → **"Blueprint"**
3. Conectar repositorio
4. Render detectará automáticamente `render.yaml`
5. Crear PostgreSQL y Redis manualmente (free tier)
6. Configurar variables de entorno manualmente

---

## ✅ Verificación Post-Deploy

### 1. Health Check del Backend

Una vez desplegado, verifica que funcione:

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

### 2. Test de CORS

```bash
curl -I -H "Origin: https://front-eight-rho-61.vercel.app" https://tu-backend.onrender.com/api/health
```

Busca el header:
```
access-control-allow-origin: https://front-eight-rho-61.vercel.app
```

### 3. Logs

Revisa los logs en Render Dashboard:
- **Web Service**: Debe mostrar "Uvicorn running on..."
- **Worker**: Debe mostrar "Listening on submissions"

---

## 🔧 Actualizar Frontend en Vercel

Una vez que el backend esté desplegado en Render, actualiza la variable de entorno del frontend:

1. Ve a [Vercel Dashboard](https://vercel.com/dashboard)
2. Selecciona tu proyecto frontend
3. Ve a **Settings** → **Environment Variables**
4. Agrega/actualiza:
   ```
   VITE_API_URL=https://tu-backend.onrender.com
   ```
5. Redeploy el frontend: **Deployments** → **Redeploy**

---

## ⚠️ Limitaciones Importantes

### 1. Docker NO Disponible (CRÍTICO)

El sistema de ejecución de código (Docker sandbox) **NO funciona** en Render.com.

**Lo que SÍ funciona**:
- ✅ API Backend completo (GET /api/problems, /api/subjects, /api/hierarchy)
- ✅ Panel administrativo (estadísticas, submissions)
- ✅ CORS con frontend de Vercel
- ✅ Sistema de pistas
- ✅ Base de datos PostgreSQL y Redis

**Lo que NO funciona**:
- ❌ POST /api/submit (retorna status "unavailable")
- ❌ Ejecutar código de estudiantes en sandbox Docker
- ❌ Evaluar submissions con tests públicos/ocultos
- ❌ Generar puntajes automáticos

**Mensaje que verán los estudiantes**:
```
⚠️ La ejecución de código NO está disponible en Render.com (no soporta Docker).
El sistema solo permite ver problemas y jerarquía de contenidos.
Para evaluar código, despliega en Railway, Fly.io, o un VPS con Docker.
```

**Soluciones para ejecución completa**:
1. **Railway.com** - Hobby plan $5/mes, soporta Docker ✅
2. **Fly.io** - Con Docker runtime habilitado ✅
3. **DigitalOcean App Platform** - Con soporte Docker ✅
4. **VPS Completo** - DigitalOcean Droplet, Linode con Docker instalado ✅

### 2. Free Tier se Duerme

El servicio gratuito se "duerme" después de 15 minutos sin uso:
- Primera petición será lenta (30-60 segundos de cold start)
- Usa [UptimeRobot](https://uptimerobot.com) para mantenerlo despierto (ping cada 5 min)

### 3. Redis Externo Requerido

Render no ofrece Redis gratis:
- Debes usar **Upstash Redis** (gratis hasta 10,000 comandos/día)
- Crea cuenta en: https://console.upstash.com/

---

## 🐛 Troubleshooting

### Error: "ModuleNotFoundError: No module named 'common'"

**Solución**: Verificar que `PYTHONPATH=/opt/render/project/src/Back` esté en Environment Variables

### Error: "Database connection failed"

**Solución**:
1. Verifica que `DATABASE_URL` sea la "Internal Database URL" de Render
2. Formato: `postgresql://user:pass@host/db`
3. NO uses `localhost`

### Error: "Redis connection refused"

**Solución**:
1. Verifica `REDIS_URL` en Environment Variables
2. Formato Upstash: `redis://default:password@host:port`
3. Verifica que sea la misma URL en backend y worker

### Worker no procesa jobs

**Solución**:
1. Verifica logs: debe decir "Listening on submissions"
2. Verifica que `REDIS_URL` sea exactamente igual en backend y worker
3. Prueba crear un submission y verifica que se encole

### CORS errors desde Vercel

**Solución**:
1. Verifica `CORS_ORIGINS=https://front-eight-rho-61.vercel.app`
2. Sin espacios ni trailing slash
3. HTTPS, no HTTP

---

## 📚 URLs de Referencia

- **Render Dashboard**: https://dashboard.render.com/
- **Upstash Console**: https://console.upstash.com/
- **Vercel Dashboard**: https://vercel.com/dashboard
- **Documentación Completa**: Ver [DEPLOY_RENDER.md](./DEPLOY_RENDER.md)

---

## ✅ Checklist Final

- [ ] PostgreSQL creado en Render
- [ ] Redis creado en Upstash
- [ ] Web Service creado
- [ ] Worker Service creado
- [ ] Todas las Environment Variables configuradas
- [ ] `PYTHONPATH` configurado en ambos servicios
- [ ] Health check funcionando (200 OK)
- [ ] CORS funcionando desde Vercel
- [ ] Logs sin errores críticos
- [ ] Frontend actualizado con URL del backend

---

**¿Problemas?** Revisa [DEPLOY_RENDER.md](./DEPLOY_RENDER.md) para troubleshooting detallado.

**¿Listo?** Abre tu frontend: https://front-eight-rho-61.vercel.app/ 🎉
