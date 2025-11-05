# 🔧 Fix: ModuleNotFoundError en Render

## Error Actual

```
ModuleNotFoundError: No module named 'backend'
```

Este error ocurre porque Gunicorn no puede encontrar el módulo `backend.app`.

---

## ✅ Solución: Configurar Root Directory en Render

### Opción 1: Root Directory en Render Dashboard (RECOMENDADO)

1. Ve a tu Web Service en Render Dashboard
2. Click en **Settings** (izquierda)
3. Busca la sección **Build & Deploy**
4. **Root Directory**: Déjalo **VACÍO** (blank)
5. **Build Command**:
   ```bash
   cd Back && pip install -r requirements.txt
   ```
6. **Start Command**:
   ```bash
   cd Back && gunicorn backend.app:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT --log-level info
   ```
7. Click **Save Changes**
8. Render automáticamente redesplegará

---

### Opción 2: Usar PYTHONPATH (Alternativa)

Si la Opción 1 no funciona:

1. Ve a **Environment** en Render Dashboard
2. Agrega esta variable:
   ```
   PYTHONPATH=/opt/render/project/src/Back
   ```
3. **Start Command** (sin cd):
   ```bash
   gunicorn backend.app:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT --log-level info
   ```
4. Click **Save Changes**

---

### Opción 3: Path Absoluto (Última Opción)

Si las anteriores fallan:

**Start Command**:
```bash
cd /opt/render/project/src/Back && gunicorn backend.app:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT --log-level info
```

---

## 🔍 Verificar Configuración Actual

En Render Dashboard → Tu Web Service → Settings:

### ✅ Configuración Correcta

```yaml
Root Directory: (vacío/blank)
Build Command: cd Back && pip install -r requirements.txt
Start Command: cd Back && gunicorn backend.app:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT --log-level info
```

### ❌ Configuración Incorrecta (NO usar)

```yaml
Root Directory: Back  ← ESTO CAUSA PROBLEMAS
Build Command: pip install -r requirements.txt
Start Command: gunicorn backend.app:app ...
```

**Por qué NO funciona**: Si pones `Root Directory: Back`, Render cambia el directorio de trabajo ANTES de ejecutar los comandos, causando que `cd Back` falle.

---

## 🔧 Worker Service (Background Worker)

El Worker necesita la MISMA configuración:

**Root Directory**: (vacío/blank)
**Build Command**:
```bash
cd Back && pip install -r requirements.txt
```
**Start Command**:
```bash
cd Back && python -m rq.cli worker submissions --url $REDIS_URL
```

---

## 📋 Checklist de Variables de Entorno

Verifica que TODAS estas variables estén configuradas en Render Dashboard → Environment:

```env
DATABASE_URL=postgresql://user:password@hostname.render.com/database
REDIS_URL=redis://default:password@hostname.upstash.io:6379
CORS_ORIGINS=https://front-eight-rho-61.vercel.app
CORS_ALLOW_ALL_ORIGINS=false
```

**Opcional** (solo si usas Opción 2):
```env
PYTHONPATH=/opt/render/project/src/Back
```

---

## 🐛 Debugging en Render

Si el error persiste, revisa los logs:

1. Render Dashboard → Tu Web Service → **Logs**
2. Busca líneas que contengan:
   - `ModuleNotFoundError`
   - `ImportError`
   - `working directory`
3. Verifica que el path sea correcto: `/opt/render/project/src/Back`

**Comando de debug** (agregar temporalmente al Start Command):
```bash
cd Back && pwd && ls -la && python -c "import sys; print(sys.path)" && gunicorn backend.app:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT
```

Este comando mostrará:
- Directorio actual (`pwd`)
- Archivos disponibles (`ls -la`)
- Python paths (`sys.path`)
- Luego intentará iniciar Gunicorn

---

## ✅ Verificación Post-Fix

Una vez que el deploy sea exitoso:

```bash
# Test health check
curl https://tu-backend.onrender.com/api/health

# Debe retornar:
{
  "service": "api",
  "status": "healthy",
  "database": "healthy",
  "redis": "healthy"
}
```

---

## 📚 Documentación Relacionada

- **RENDER_TROUBLESHOOTING.md** - Errores comunes completos
- **RENDER_QUICKSTART.md** - Guía de deployment paso a paso
- **RENDER_ENV_VARS.txt** - Template de variables de entorno

---

## 🆘 Si Nada Funciona

1. Verifica que `Back/backend/app.py` exista en tu repositorio
2. Verifica que `Back/requirements.txt` tenga `gunicorn==23.0.0`
3. Prueba hacer un commit y push para forzar redeploy:
   ```bash
   git add .
   git commit -m "Fix Render deployment paths"
   git push
   ```
4. En Render Dashboard, click **Manual Deploy** → **Clear build cache & deploy**

---

## 🎯 Resumen Rápido

**El problema**: Gunicorn busca `backend.app` desde el directorio incorrecto.

**La solución**: Usar `cd Back &&` en el Start Command para cambiar al directorio correcto ANTES de ejecutar Gunicorn.

**Configuración ganadora**:
- Root Directory: **(vacío)**
- Build Command: `cd Back && pip install -r requirements.txt`
- Start Command: `cd Back && gunicorn backend.app:app ...`
