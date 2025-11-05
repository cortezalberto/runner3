# 🚀 Deploy Quick Start

Este directorio (`Back/`) está listo para ser desplegado en **Render.com** como un servicio web con Gunicorn.

## ✅ Archivos de Deploy Incluidos

```
Back/
├── Procfile              # Comandos de inicio para Render/Heroku
├── runtime.txt           # Versión de Python (3.11.9)
├── requirements.txt      # Dependencias combinadas (backend + common)
├── render.yaml          # Configuración de servicios (opcional)
├── start-render.sh      # Script de inicio con DB init
├── DEPLOY_RENDER.md     # Guía completa de deploy
├── .env.example         # Template de variables de entorno
└── backend/
    └── requirements.txt  # Dependencias específicas del backend (incluye gunicorn)
```

## 🎯 Deploy Rápido en Render

### 1. Crear Web Service en Render

**Build Command:**
```bash
pip install -r requirements.txt
```

**Start Command (Opción A - Simple):**
```bash
gunicorn backend.app:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT
```

**Start Command (Opción B - Con DB Init):**
```bash
./start-render.sh
```

### 2. Variables de Entorno Requeridas

```env
DATABASE_URL=postgresql://user:password@host/database
REDIS_URL=redis://default:password@host:port
CORS_ORIGINS=https://tu-frontend.com
PYTHONPATH=/opt/render/project/src/Back
```

### 3. Servicios Necesarios

- **Web Service**: Backend API (este directorio)
- **PostgreSQL**: Database (crear en Render)
- **Redis**: Queue (usar Upstash gratis o Render pago)
- **Worker**: RQ Worker (crear como Background Worker)

## 📖 Guía Completa

Para instrucciones detalladas paso a paso, ver: **[DEPLOY_RENDER.md](./DEPLOY_RENDER.md)**

## ⚠️ Limitación Importante

**Docker no está disponible en Render Free Tier**, por lo que el sistema de ejecución de código (runner) NO funcionará. El backend API funcionará perfectamente para:

- ✅ Ver lista de problemas
- ✅ Ver jerarquía de materias/unidades
- ✅ Panel administrativo
- ❌ Ejecutar y evaluar código de estudiantes (requiere Docker)

### Soluciones:

1. **Backend Solo**: Deploy API sin ejecución de código (para testing)
2. **Hybrid**: Backend en Render + Runner en Railway/Fly.io (soportan Docker)
3. **Full VPS**: DigitalOcean, Linode, etc. con Docker instalado

## 🔧 Testing Local con Gunicorn

Antes de hacer deploy, puedes probar Gunicorn localmente:

```bash
# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
export DATABASE_URL=postgresql://playground:playground@localhost:5433/playground
export REDIS_URL=redis://localhost:6379/0
export PYTHONPATH=$(pwd)

# Iniciar con Gunicorn
gunicorn backend.app:app \
  --workers 2 \
  --worker-class uvicorn.workers.UvicornWorker \
  --bind 0.0.0.0:8000 \
  --reload
```

Luego abre: http://localhost:8000/docs

## 📚 Recursos

- [Render Deploy Guide](./DEPLOY_RENDER.md) - Guía completa con troubleshooting
- [Render Docs - FastAPI](https://render.com/docs/deploy-fastapi)
- [Gunicorn Docs](https://docs.gunicorn.org/)

## 🆘 Troubleshooting Rápido

**ModuleNotFoundError: No module named 'common'**
→ Agregar `PYTHONPATH=/opt/render/project/src/Back` en Environment Variables

**Database connection failed**
→ Verificar que `DATABASE_URL` sea la "Internal Database URL" de Render

**Worker no procesa jobs**
→ Verificar que `REDIS_URL` sea exactamente igual en backend y worker

**CORS errors**
→ Actualizar `CORS_ORIGINS` con tu dominio de frontend

Ver [DEPLOY_RENDER.md](./DEPLOY_RENDER.md) para más detalles.
