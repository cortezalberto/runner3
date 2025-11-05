"""
RQ Worker tasks - Simplified version for Render deployment (no Docker support)

IMPORTANT: Render.com free tier does NOT support Docker.
This worker marks submissions as "unavailable" instead of executing code.
Only the API for viewing problems and hierarchy will work.
"""
import pathlib
from datetime import datetime
from sqlalchemy.orm import Session

# Importar modelos y database
import sys
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))

from common.database import SessionLocal
from common.models import Submission, TestResult
from common.logging_config import get_logger

logger = get_logger(__name__)


def run_submission_in_sandbox(submission_id: int, problem_id: str, code: str,
                               timeout_sec=None, memory_mb=None):
    """
    Stub function for Render deployment.

    Docker execution is NOT available on Render free tier.
    This function marks submissions as "unavailable" with an explanatory message.

    For actual code execution, deploy to a platform that supports Docker:
    - Railway.com (Hobby plan - $5/month)
    - Fly.io (with Docker runtime)
    - DigitalOcean App Platform (with Docker support)
    - AWS ECS/Fargate
    - Self-hosted VPS with Docker installed
    """
    db: Session = SessionLocal()

    try:
        submission = db.query(Submission).filter(Submission.id == submission_id).first()
        if not submission:
            raise Exception(f"Submission {submission_id} not found")

        # Actualizar estado a "unavailable"
        submission.status = "unavailable"
        submission.ok = False
        submission.score_total = 0
        submission.score_max = 0
        submission.passed = 0
        submission.failed = 0
        submission.errors = 0
        submission.duration_sec = 0.0
        submission.completed_at = datetime.utcnow()
        submission.error_message = (
            "⚠️ La ejecución de código NO está disponible en Render.com (no soporta Docker). "
            "El sistema solo permite ver problemas y jerarquía de contenidos. "
            "Para evaluar código, despliega en Railway, Fly.io, o un VPS con Docker."
        )

        # Crear un TestResult explicativo
        test_result = TestResult(
            submission_id=submission_id,
            test_name="system_check",
            outcome="unavailable",
            duration=0.0,
            message="Docker no disponible en Render. Use Railway o Fly.io para ejecución de código.",
            points=0,
            max_points=0,
            visibility="public"
        )
        db.add(test_result)

        db.commit()

        logger.warning(
            "Code execution unavailable (Docker not supported on Render)",
            extra={
                "submission_id": submission_id,
                "problem_id": problem_id,
                "platform": "Render.com"
            }
        )

    except Exception as e:
        submission.status = "failed"
        submission.error_message = str(e)[:1000]
        submission.completed_at = datetime.utcnow()
        db.commit()
        logger.error(
            "Failed to process submission",
            extra={"submission_id": submission_id, "error": str(e)}
        )
        raise

    finally:
        db.close()
