#!/usr/bin/env python
"""
Script para generar los ejercicios secuenciales restantes (4-10)
"""
import os
import json

BASE_DIR = "backend/problems"

# Datos completos de cada ejercicio
EJERCICIOS = {
    "sec_circulo": {
        "metadata": {
            "title": "Área y perímetro de un círculo",
            "tags": ["matematica", "pi", "formulas"],
            "hints": [
                "Importa el módulo math para obtener math.pi con: import math",
                "Lee el radio con input() y conviértelo a float().",
                "Calcula el área con: math.pi * radio ** 2",
                "Calcula el perímetro con: 2 * math.pi * radio"
            ]
        },
        "prompt": """# Problema: Área y perímetro de un círculo

Escribe un programa que pida al usuario el radio de un círculo y calcule e imprima el área y el perímetro.

## Entrada
Un número float que representa el radio del círculo.

## Salida
Dos líneas:
1. El área del círculo
2. El perímetro del círculo

## Ejemplo
```
Entrada: 5
Salida:
78.53981633974483
31.41592653589793
```

## Restricciones
- Usa import math para obtener math.pi
- Área = π * radio²
- Perímetro = 2 * π * radio
""",
        "starter": """import math

def main():
    # Lee el radio desde la entrada estándar
    radio = float(input())

    # TODO: Calcula el área y perímetro
    # area = math.pi * radio ** 2
    # perimetro = 2 * math.pi * radio
    # Imprime ambos resultados en líneas separadas

    pass

if __name__ == "__main__":
    main()
"""
    },

    "sec_segundos_horas": {
        "metadata": {
            "title": "Conversión de segundos a horas",
            "tags": ["conversiones", "division"],
            "hints": [
                "Lee la cantidad de segundos con input() y conviértela a int().",
                "Para convertir segundos a horas, divide entre 3600.",
                "Usa print() para mostrar el resultado con el formato: '{segundos} segundos equivalen a {horas} horas'",
                "El resultado de la división será un float (puede tener decimales)."
            ]
        },
        "prompt": """# Problema: Conversión de segundos a horas

Crea un programa que pida al usuario una cantidad de segundos y muestre cuántas horas equivalen.

## Entrada
Un número entero que representa la cantidad de segundos.

## Salida
Un mensaje con el formato: `{segundos} segundos equivalen a {horas} horas`

## Ejemplo
```
Entrada: 3600
Salida: 3600 segundos equivalen a 1.0 horas
```

## Restricciones
- Divide entre 3600 para convertir a horas
- El resultado debe ser un float
""",
        "starter": """def main():
    # Lee los segundos desde la entrada estándar
    segundos = int(input())

    # TODO: Convierte segundos a horas
    # horas = segundos / 3600
    # Imprime el resultado con el formato exacto

    pass

if __name__ == "__main__":
    main()
"""
    },

    "sec_tabla_multiplicar": {
        "metadata": {
            "title": "Tabla de multiplicar",
            "tags": ["multiplicacion", "tablas"],
            "hints": [
                "Lee el número con input() y conviértelo a int().",
                "Debes imprimir 10 líneas, cada una con: 'numero x multiplicador = resultado'.",
                "Calcula cada multiplicación por separado (sin usar ciclos): resultado1 = numero * 1, resultado2 = numero * 2, etc.",
                "Usa f-strings para imprimir cada línea: print(f'{numero} x 1 = {resultado1}')"
            ]
        },
        "prompt": """# Problema: Tabla de multiplicar

Escribe un programa que solicite al usuario un número entero y muestre la tabla de multiplicar desde el 1 hasta el 10.

## Entrada
Un número entero.

## Salida
10 líneas, cada una con el formato: `numero x multiplicador = resultado`

## Ejemplo
```
Entrada: 5
Salida:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
```

## Restricciones
- NO uses ciclos (for o while)
- Calcula cada multiplicación individualmente
""",
        "starter": """def main():
    # Lee el número desde la entrada estándar
    numero = int(input())

    # TODO: Calcula cada multiplicación y muestra la tabla
    # resultado1 = numero * 1
    # resultado2 = numero * 2
    # ... hasta resultado10 = numero * 10
    # Imprime cada línea con formato: "numero x multiplicador = resultado"

    pass

if __name__ == "__main__":
    main()
"""
    },

    "sec_operaciones_basicas": {
        "metadata": {
            "title": "Operaciones aritméticas básicas",
            "tags": ["aritmetica", "operaciones"],
            "hints": [
                "Lee dos números con input(), conviértelos a float() para permitir decimales.",
                "Realiza las cuatro operaciones: suma, resta, multiplicación y división.",
                "Imprime cuatro líneas, una para cada operación: 'Suma: {resultado}'",
                "La división puede dar un número decimal, así que usa float() desde el inicio."
            ]
        },
        "prompt": """# Problema: Operaciones aritméticas básicas

Escribe un programa que pida dos números y muestre la suma, resta, multiplicación y división de ambos.

## Entrada
Dos números (pueden ser enteros o decimales).

## Salida
Cuatro líneas:
1. Suma: {resultado}
2. Resta: {resultado}
3. Multiplicación: {resultado}
4. División: {resultado}

## Ejemplo
```
Entrada:
10
2

Salida:
Suma: 12.0
Resta: 8.0
Multiplicación: 20.0
División: 5.0
```
""",
        "starter": """def main():
    # Lee dos números desde la entrada estándar
    num1 = float(input())
    num2 = float(input())

    # TODO: Realiza las operaciones y muestra los resultados
    # suma = num1 + num2
    # resta = num1 - num2
    # multiplicacion = num1 * num2
    # division = num1 / num2

    pass

if __name__ == "__main__":
    main()
"""
    },

    "sec_imc": {
        "metadata": {
            "title": "Índice de Masa Corporal",
            "tags": ["salud", "formulas", "decimales"],
            "hints": [
                "Lee altura y peso con input(), conviértelos a float().",
                "La fórmula del IMC es: peso / altura²  o  peso / (altura ** 2)",
                "Usa :.2f en el f-string para mostrar solo 2 decimales.",
                "Formato de salida: 'Tu índice de masa corporal (IMC) es: {imc:.2f}'"
            ]
        },
        "prompt": """# Problema: Índice de Masa Corporal

Desarrolla un programa que pida altura y peso, y calcule el Índice de Masa Corporal (IMC).

## Entrada
Dos números:
1. Altura en metros (float)
2. Peso en kilogramos (float)

## Salida
Un mensaje: `Tu índice de masa corporal (IMC) es: {imc:.2f}`

## Ejemplo
```
Entrada:
1.75
70

Salida:
Tu índice de masa corporal (IMC) es: 22.86
```

## Restricciones
- Fórmula: IMC = peso / altura²
- Muestra el resultado con 2 decimales
""",
        "starter": """def main():
    # Lee altura y peso desde la entrada estándar
    altura = float(input())
    peso = float(input())

    # TODO: Calcula el IMC y muestra el resultado
    # imc = peso / altura ** 2
    # Imprime con formato: "Tu índice de masa corporal (IMC) es: {imc:.2f}"

    pass

if __name__ == "__main__":
    main()
"""
    },

    "sec_celsius_fahrenheit": {
        "metadata": {
            "title": "Conversión Celsius a Fahrenheit",
            "tags": ["conversiones", "temperatura"],
            "hints": [
                "Lee la temperatura en Celsius con input() y conviértela a float().",
                "La fórmula es: fahrenheit = (9/5) * celsius + 32",
                "También puedes usar: fahrenheit = celsius * 1.8 + 32",
                "Formato de salida: '{celsius}°C equivalen a {fahrenheit}°F'"
            ]
        },
        "prompt": """# Problema: Conversión Celsius a Fahrenheit

Escribe un programa que pida una temperatura en grados Celsius y la convierta a grados Fahrenheit.

## Entrada
Un número float que representa la temperatura en Celsius.

## Salida
Un mensaje: `{celsius}°C equivalen a {fahrenheit}°F`

## Ejemplo
```
Entrada: 25
Salida: 25.0°C equivalen a 77.0°F
```

## Restricciones
- Fórmula: F = (9/5) * C + 32
""",
        "starter": """def main():
    # Lee la temperatura en Celsius
    celsius = float(input())

    # TODO: Convierte a Fahrenheit
    # fahrenheit = (9/5) * celsius + 32
    # Imprime con formato: "{celsius}°C equivalen a {fahrenheit}°F"

    pass

if __name__ == "__main__":
    main()
"""
    },

    "sec_promedio": {
        "metadata": {
            "title": "Promedio de tres números",
            "tags": ["promedio", "aritmetica"],
            "hints": [
                "Lee tres números con input(), conviértelos a float().",
                "El promedio se calcula sumando los tres y dividiendo entre 3.",
                "Usa la fórmula: promedio = (num1 + num2 + num3) / 3",
                "Formato de salida: 'El promedio de los tres números es: {promedio}'"
            ]
        },
        "prompt": """# Problema: Promedio de tres números

Crea un programa que pida tres números y calcule e imprima el promedio.

## Entrada
Tres números (pueden ser enteros o decimales).

## Salida
Un mensaje: `El promedio de los tres números es: {promedio}`

## Ejemplo
```
Entrada:
10
20
30

Salida:
El promedio de los tres números es: 20.0
```

## Restricciones
- Promedio = (num1 + num2 + num3) / 3
""",
        "starter": """def main():
    # Lee tres números desde la entrada estándar
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())

    # TODO: Calcula el promedio y muestra el resultado
    # promedio = (num1 + num2 + num3) / 3
    # Imprime: "El promedio de los tres números es: {promedio}"

    pass

if __name__ == "__main__":
    main()
"""
    }
}

def create_files(problem_id, data):
    """Crear todos los archivos para un ejercicio"""
    dir_path = os.path.join(BASE_DIR, problem_id)

    # metadata.json
    metadata = {
        "title": data["metadata"]["title"],
        "subject_id": "programacion-1",
        "unit_id": "estructuras-secuenciales",
        "difficulty": "easy",
        "tags": data["metadata"]["tags"],
        "timeout_sec": 3.0,
        "memory_mb": 128,
        "hints": data["metadata"]["hints"]
    }
    with open(os.path.join(dir_path, "metadata.json"), "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)

    # prompt.md
    with open(os.path.join(dir_path, "prompt.md"), "w", encoding="utf-8") as f:
        f.write(data["prompt"])

    # starter.py
    with open(os.path.join(dir_path, "starter.py"), "w", encoding="utf-8") as f:
        f.write(data["starter"])

    # tests_public.py (genérico)
    tests_public = '''"""
Public tests for ''' + problem_id + ''' problem.
"""
import pytest


class TestFunctionExistence:
    """Tests to verify required function exists."""

    def test_main_function_exists(self, student_module):
        """Verify that the main() function is defined."""
        assert hasattr(student_module, 'main'), \\
            'La función main() debe estar definida en el código'
'''
    with open(os.path.join(dir_path, "tests_public.py"), "w", encoding="utf-8") as f:
        f.write(tests_public)

    # tests_hidden.py (vacío por ahora)
    tests_hidden = '''"""
Hidden tests for ''' + problem_id + ''' problem.
"""
import pytest
'''
    with open(os.path.join(dir_path, "tests_hidden.py"), "w", encoding="utf-8") as f:
        f.write(tests_hidden)

    # rubric.json
    rubric = {
        "tests": [
            {"name": "test_main_function_exists", "points": 1, "visibility": "public"}
        ],
        "max_points": 10
    }
    with open(os.path.join(dir_path, "rubric.json"), "w", encoding="utf-8") as f:
        json.dump(rubric, f, indent=2)

    print(f"Creado: {problem_id}")

# Crear todos los ejercicios
for problem_id, data in EJERCICIOS.items():
    create_files(problem_id, data)

print("\nTodos los ejercicios restantes creados!")
