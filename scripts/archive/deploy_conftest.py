#!/usr/bin/env python3
"""
Script to deploy shared conftest.py to all conditional problems.
"""
import shutil
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).parent / "backend" / "problems"
SHARED_CONFTEST = BASE_DIR / "SHARED_conftest.py"

# List of conditional problems
CONDITIONAL_PROBLEMS = [
    "cond_aprobado",
    "cond_categorias_edad",
    "cond_mayor_de_dos",
    "cond_mayor_edad",
    "cond_numero_par",
    "cond_termina_vocal",
    "cond_terremoto",
    "cond_transformar_nombre",
    "cond_validar_password",
]

def deploy_conftest():
    """Copy SHARED_conftest.py to all conditional problem directories as conftest.py"""
    if not SHARED_CONFTEST.exists():
        print(f"ERROR: {SHARED_CONFTEST} no existe!")
        return

    for problem in CONDITIONAL_PROBLEMS:
        problem_dir = BASE_DIR / problem
        if not problem_dir.exists():
            print(f"ADVERTENCIA: {problem_dir} no existe, saltando...")
            continue

        target = problem_dir / "conftest.py"
        shutil.copy2(SHARED_CONFTEST, target)
        print(f"OK: Copiado conftest.py a {problem}")

    print(f"\nCOMPLETADO: Desplegado conftest.py a {len(CONDITIONAL_PROBLEMS)} problemas")

if __name__ == "__main__":
    deploy_conftest()
