# 🐛 Render Deployment - Troubleshooting

---

## ⚠️ LIMITACIÓN CRÍTICA: Docker NO disponible

**ANTES DE REPORTAR ERRORES**: Render.com free tier **NO soporta Docker**.

**Esto NO es un error** - es una limitación de la plataforma:
- ✅ El API funcionará (ver problemas, jerarquía, estadísticas)
- ❌ La ejecución de código NO funcionará (requiere Docker sandbox)

**Comportamiento esperado**:
- Backend se despliega correctamente ✅
- Worker se ejecuta sin errores ✅
- POST /api/submit retorna `status: "unavailable"` con mensaje explicativo ✅

Los estudiantes verán:
```
⚠️ La ejecución de código NO está disponible en Render.com (no soporta Docker).
El sistema solo permite ver problemas y jerarquía de contenidos.
```

**Alternativas para ejecución de código**:
- Railway.com ($5/mes, soporta Docker)
- Fly.io (con Docker runtime)
- VPS con Docker instalado

---

## Error: ModuleNotFoundError: No module named 'app'

Este es el error más común al desplegar en Render.

### Causa del Problema

Python no puede encontrar el módulo `backend.app` porque:
1. El directorio de trabajo no está configurado correctamente
2. La variable `PYTHONPATH` no está configurada
3. El Root Directory en Render no es correcto

### ✅ Solución 1: Configurar Root Directory (RECOMENDADO)

En Render Dashboard → Tu Web Service → Settings:

1. **Root Directory**: Déjalo en **BLANCO** o pon **`Back`**
2. **Build Command**:
   ```bash
   cd Back && pip install -r requirements.txt
   ```
3. **Start Command**:
   ```bash
   cd Back && gunicorn backend.app:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT
   ```

### ✅ Solución 2: Usar PYTHONPATH (Alternativa)

Si la Solución 1 no funciona, configura la variable de entorno:

**Environment Variables** (en Render):
```env
PYTHONPATH=/opt/render/project/src/Back
```

**Start Command** (sin cd):
```bash
gunicorn backend.app:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT
```

### ✅ Solución 3: Path Absoluto en Start Command

**Start Command** con path absoluto:
```bash
cd /opt/render/project/src/Back && gunicorn backend.app:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT
```

---

## Error: ModuleNotFoundError: No module named 'common'

### Causa

El módulo `common` no se encuentra en el PYTHONPATH.

### ✅ Solución

Agregar en **Environment Variables**:
```env
PYTHONPATH=/opt/render/project/src/Back
```

O usar el Start Command con `cd`:
```bash
cd /opt/render/project/src/Back && gunicorn backend.app:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT
```

---

## Error: Database connection failed

### Causa

La variable `DATABASE_URL` no está configurada o es incorrecta.

### ✅ Solución

1. Ve a tu PostgreSQL database en Render
2. Copia la **"Internal Database URL"** (no la External)
3. En Environment Variables del Web Service:
   ```env
   DATABASE_URL=postgresql://user:password@hostname.render.com/database
   ```

**Importante**:
- Usa la **Internal URL** (termina en `.render.com`)
- NO uses `localhost`
- El formato debe ser: `postgresql://user:pass@host/db`

---

## Error: Redis connection refused

### Causa

`REDIS_URL` no está configurado o Render no ofrece Redis gratis.

### ✅ Solución: Usar Upstash (Redis Gratis)

1. Ve a [console.upstash.com](https://console.upstash.com/)
2. Crea una base de datos Redis
3. Copia la **Redis URL**
4. En Environment Variables:
   ```env
   REDIS_URL=redis://default:password@hostname.upstash.io:6379
   ```

---

## Error: Worker no procesa jobs

### Síntomas

- Backend funciona
- Puedes enviar código
- Pero nunca recibe resultados

### ✅ Solución

1. **Verifica que el Worker Service esté creado y corriendo**
   - Ve a Render Dashboard
   - Debes tener DOS servicios: Web Service + Background Worker

2. **Verifica que `REDIS_URL` sea EXACTAMENTE igual** en:
   - Web Service (Backend)
   - Background Worker

3. **Verifica logs del Worker**:
   - Dashboard → Background Worker → Logs
   - Debe decir: `Listening on submissions`

4. **Start Command del Worker**:
   ```bash
   cd /opt/render/project/src/Back && python -m rq.cli worker submissions --url $REDIS_URL
   ```

---

## Error: CORS - Frontend no puede conectar

### Síntomas

En la consola del navegador:
```
Access to XMLHttpRequest at 'https://backend.onrender.com' from origin 'https://frontend.vercel.app' has been blocked by CORS policy
```

### ✅ Solución

En Environment Variables del Backend:
```env
CORS_ORIGINS=https://front-eight-rho-61.vercel.app
CORS_ALLOW_ALL_ORIGINS=false
```

**Importante**:
- Usa **HTTPS**, no HTTP
- Sin trailing slash al final
- Sin espacios
- Puedes agregar múltiples dominios separados por comas:
  ```env
  CORS_ORIGINS=https://frontend1.vercel.app,https://frontend2.vercel.app
  ```

---

## Error: Build failed - pip install error

### Síntomas

Build falla al instalar dependencias.

### ✅ Solución

1. **Verifica que `requirements.txt` esté en la raíz de Back/**
   ```bash
   ls Back/requirements.txt
   ```

2. **Build Command correcto**:
   ```bash
   cd Back && pip install -r requirements.txt
   ```

3. **Verifica que requirements.txt tenga Gunicorn**:
   ```bash
   grep gunicorn Back/requirements.txt
   ```
   Debe contener: `gunicorn==23.0.0`

---

## Error: Port $PORT not found

### Causa

Gunicorn no está usando la variable de entorno `$PORT` de Render.

### ✅ Solución

Start Command debe incluir `$PORT`:
```bash
gunicorn backend.app:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT
```

**NO uses un puerto fijo** como `:8000`

---

## Verificación Post-Deploy

Después de desplegar, verifica:

### 1. Health Check

```bash
curl https://tu-backend.onrender.com/api/health
```

Debe retornar:
```json
{
  "service": "api",
  "status": "healthy",
  "database": "healthy",
  "redis": "healthy"
}
```

### 2. CORS

```bash
curl -I -H "Origin: https://front-eight-rho-61.vercel.app" https://tu-backend.onrender.com/api/health
```

Busca el header:
```
access-control-allow-origin: https://front-eight-rho-61.vercel.app
```

### 3. Logs

Revisa los logs en Render Dashboard:
- **Web Service**: Debe mostrar `Uvicorn running on...`
- **Worker**: Debe mostrar `Listening on submissions`

---

## Checklist de Configuración Completa

### Web Service (Backend)

- [ ] **Root Directory**: `Back` o en blanco
- [ ] **Build Command**: `cd Back && pip install -r requirements.txt`
- [ ] **Start Command**: `cd Back && gunicorn backend.app:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT`
- [ ] **Environment Variables**:
  - [ ] `DATABASE_URL` (Internal URL de Render PostgreSQL)
  - [ ] `REDIS_URL` (de Upstash)
  - [ ] `CORS_ORIGINS` (URL de tu frontend en Vercel)
  - [ ] `PYTHONPATH=/opt/render/project/src/Back` (opcional)

### Background Worker

- [ ] **Root Directory**: `Back` o en blanco
- [ ] **Build Command**: `cd Back && pip install -r requirements.txt`
- [ ] **Start Command**: `cd Back && python -m rq.cli worker submissions --url $REDIS_URL`
- [ ] **Environment Variables**:
  - [ ] `DATABASE_URL` (mismo que Web Service)
  - [ ] `REDIS_URL` (mismo que Web Service)
  - [ ] `PYTHONPATH=/opt/render/project/src/Back` (opcional)

---

## ⚠️ Limitaciones de Render Free Tier (IMPORTANTES)

### 1. Docker NO disponible (CRÍTICO)

**Limitación de la plataforma - NO es un bug**:
- Render.com free tier NO permite ejecutar Docker containers
- El worker NO puede crear sandboxes aislados para ejecutar código
- Esto afecta: POST /api/submit (evaluación de código)

**Funcionalidades afectadas**:
- ❌ Ejecución de código de estudiantes
- ❌ Tests públicos/ocultos
- ❌ Puntajes automáticos
- ✅ Ver problemas y jerarquía (funciona)
- ✅ Panel administrativo (funciona)
- ✅ Sistema de pistas (funciona)

**Solución**: Para ejecución de código completa, usa:
- Railway.com ($5/mes) - Soporta Docker ✅
- Fly.io - Con Docker runtime ✅
- VPS con Docker instalado ✅

### 2. Sleep después de 15 minutos

- Primera petición será lenta (30-60 segundos de cold start)
- Usa [UptimeRobot](https://uptimerobot.com) para mantenerlo despierto

### 3. Redis NO incluido

- Render no ofrece Redis gratis
- Debes usar Upstash: https://console.upstash.com/
- Plan gratis: 10,000 comandos/día

---

## 🆘 ¿Aún tienes problemas?

1. **Revisa los logs** en Render Dashboard → Logs
2. **Verifica todas las Environment Variables**
3. **Compara con `RENDER_QUICKSTART.md`**
4. **Asegúrate de que `cd Back` esté en los comandos**

**Comando de debugging**:
```bash
# En el shell de Render (si está disponible):
cd /opt/render/project/src/Back && python -c "import sys; print(sys.path); from backend import app; print('OK')"
```

---

**Documentación Completa**: Ver [RENDER_QUICKSTART.md](./RENDER_QUICKSTART.md)
