#!/usr/bin/env python
"""
Script para crear ejercicios secuenciales con la estructura de los condicionales.
"""
import os
import json

# Definición de los ejercicios restantes
EJERCICIOS = [
    {
        "id": "sec_saludo",
        "title": "Saludo personalizado",
        "description": "Lee un nombre y muestra un saludo",
        "input_type": "string (nombre)",
        "output": "Hola {nombre}!",
        "ejemplo_entrada": "Juan",
        "ejemplo_salida": "Hola Juan!",
        "tags": ["strings", "input", "concatenacion"],
        "tests": [
            ("Juan", "Hola Juan!"),
            ("María", "Hola María!"),
            ("Pedro", "Hola Pedro!"),
        ]
    },
    {
        "id": "sec_presentacion",
        "title": "Presentación completa",
        "description": "Lee nombre, apellido, edad y ciudad, y muestra una presentación",
        "input_lines": ["nombre", "apellido", "edad", "ciudad"],
        "output": "Soy {nombre} {apellido}, tengo {edad} años y vivo en {ciudad}",
        "ejemplo_entrada": "Juan|Pérez|25|Madrid",
        "ejemplo_salida": "Soy Juan Pérez, tengo 25 años y vivo en Madrid",
        "tags": ["strings", "concatenacion", "input-multiple"],
    },
    {
        "id": "sec_circulo",
        "title": "Área y perímetro de un círculo",
        "description": "Calcula área y perímetro de un círculo dado el radio",
        "input_type": "float (radio)",
        "output_lines": ["area", "perimetro"],
        "ejemplo_entrada": "5",
        "tags": ["matematica", "pi", "formulas"],
    },
    {
        "id": "sec_segundos_horas",
        "title": "Conversión de segundos a horas",
        "description": "Convierte segundos a horas",
        "input_type": "int (segundos)",
        "output": "{segundos} segundos equivalen a {horas} horas",
        "ejemplo_entrada": "3600",
        "ejemplo_salida": "3600 segundos equivalen a 1.0 horas",
        "tags": ["conversiones", "division"],
    },
    {
        "id": "sec_tabla_multiplicar",
        "title": "Tabla de multiplicar",
        "description": "Muestra la tabla de multiplicar del 1 al 10",
        "input_type": "int (numero)",
        "output_lines": 10,  # 10 líneas de salida
        "ejemplo_entrada": "5",
        "tags": ["multiplicacion", "tablas"],
    },
    {
        "id": "sec_operaciones_basicas",
        "title": "Operaciones aritméticas básicas",
        "description": "Realiza suma, resta, multiplicación y división de dos números",
        "input_lines": ["num1", "num2"],
        "output_lines": ["suma", "resta", "multiplicacion", "division"],
        "ejemplo_entrada": "10|2",
        "tags": ["aritmetica", "operaciones"],
    },
    {
        "id": "sec_imc",
        "title": "Índice de Masa Corporal",
        "description": "Calcula el IMC dados altura y peso",
        "input_lines": ["altura (m)", "peso (kg)"],
        "output": "Tu índice de masa corporal (IMC) es: {imc:.2f}",
        "ejemplo_entrada": "1.75|70",
        "tags": ["salud", "formulas", "decimales"],
    },
    {
        "id": "sec_celsius_fahrenheit",
        "title": "Conversión Celsius a Fahrenheit",
        "description": "Convierte temperatura de Celsius a Fahrenheit",
        "input_type": "float (celsius)",
        "output": "{celsius}°C equivalen a {fahrenheit}°F",
        "ejemplo_entrada": "25",
        "ejemplo_salida": "25.0°C equivalen a 77.0°F",
        "tags": ["conversiones", "temperatura"],
    },
    {
        "id": "sec_promedio",
        "title": "Promedio de tres números",
        "description": "Calcula el promedio de tres números",
        "input_lines": ["num1", "num2", "num3"],
        "output": "El promedio de los tres números es: {promedio}",
        "ejemplo_entrada": "10|20|30",
        "ejemplo_salida": "El promedio de los tres números es: 20.0",
        "tags": ["promedio", "aritmetica"],
    },
]

def create_metadata(ejercicio):
    """Crear metadata.json"""
    return {
        "title": ejercicio["title"],
        "subject_id": "programacion-1",
        "unit_id": "estructuras-secuenciales",
        "difficulty": "easy",
        "tags": ejercicio.get("tags", ["basico"]),
        "timeout_sec": 3.0,
        "memory_mb": 128,
        "hints": [
            f"Lee cuidadosamente el enunciado del problema y identifica qué datos necesitas leer con input().",
            "Recuerda que debes crear una función main() que contenga toda tu lógica. Usa print() para mostrar el resultado.",
            "Revisa el código starter provisto. Completa la sección TODO con la lógica necesaria según el enunciado.",
            "Asegúrate de seguir el formato de salida exacto que pide el problema. Revisa los ejemplos de entrada/salida."
        ]
    }

def main():
    base_dir = "backend/problems"

    for ej in EJERCICIOS:
        problem_dir = os.path.join(base_dir, ej["id"])
        os.makedirs(problem_dir, exist_ok=True)

        # Crear metadata.json
        with open(os.path.join(problem_dir, "metadata.json"), "w", encoding="utf-8") as f:
            json.dump(create_metadata(ej), f, indent=2, ensure_ascii=False)

        print(f"✅ Creado directorio y metadata para {ej['id']}")

if __name__ == "__main__":
    main()
    print("\n✅ Todos los ejercicios creados exitosamente!")
