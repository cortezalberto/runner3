#!/usr/bin/env python
"""
Script para refactorizar TODOS los tests de ejercicios secuenciales
para que evalúen correctamente lo que pide cada enunciado.
"""
import os
import json

BASE_DIR = "backend/problems"

# Tests completos para cada ejercicio
TESTS_COMPLETOS = {
    "sec_segundos_horas": {
        "tests_public": '''"""
Public tests for sec_segundos_horas problem.
Tests seconds to hours conversion.
"""
import pytest


class TestFunctionExistence:
    """Tests to verify required function exists."""

    def test_main_function_exists(self, student_module):
        """Verify that the main() function is defined."""
        assert hasattr(student_module, 'main'), \\
            'La función main() debe estar definida en el código'


class TestBasicConversions:
    """Tests for basic conversions."""

    def test_conversion_3600_segundos(self, capture_main_output, student_module):
        """Test with 3600 seconds (1 hour)."""
        output = capture_main_output("3600", student_module)
        assert "3600" in output, "Debe mencionar la cantidad de segundos"
        assert "1.0" in output or "1" in output, "Debe mostrar 1 hora"
        assert "horas" in output, "Debe incluir la palabra 'horas'"

    def test_conversion_7200_segundos(self, capture_main_output, student_module):
        """Test with 7200 seconds (2 hours)."""
        output = capture_main_output("7200", student_module)
        assert "7200" in output, "Debe mencionar 7200 segundos"
        assert "2.0" in output or "2" in output, "Debe mostrar 2 horas"


class TestVariousConversions:
    """Tests with various second values."""

    @pytest.mark.parametrize("segundos,horas_esperadas", [
        ("1800", 0.5),
        ("5400", 1.5),
        ("10800", 3.0),
    ])
    def test_conversiones_varias(self, capture_main_output, student_module, segundos, horas_esperadas):
        """Test various conversions."""
        output = capture_main_output(segundos, student_module)
        assert segundos in output, f"Debe mencionar {segundos} segundos"
        horas_str = str(horas_esperadas)
        assert horas_str in output, f"Debe mostrar {horas_str} horas"


class TestEdgeCases:
    """Tests for edge cases."""

    def test_cero_segundos(self, capture_main_output, student_module):
        """Test with 0 seconds."""
        output = capture_main_output("0", student_module)
        assert "0" in output and "horas" in output

    def test_un_segundo(self, capture_main_output, student_module):
        """Test with 1 second."""
        output = capture_main_output("1", student_module)
        result = 1 / 3600
        # Should be very small number
        assert "0.000" in output or str(result)[:6] in output


class TestOutputFormat:
    """Tests for output format."""

    def test_formato_incluye_equivalen(self, capture_main_output, student_module):
        """Test that output includes 'equivalen'."""
        output = capture_main_output("3600", student_module)
        assert "equivalen" in output.lower(), "Debe incluir la palabra 'equivalen'"

    def test_formato_incluye_segundos(self, capture_main_output, student_module):
        """Test that output includes 'segundos'."""
        output = capture_main_output("3600", student_module)
        assert "segundos" in output.lower(), "Debe incluir la palabra 'segundos'"
''',
        "tests_hidden": '''"""
Hidden tests for sec_segundos_horas problem.
"""
import pytest


class TestLargeValues:
    """Tests with large values."""

    @pytest.mark.parametrize("segundos", ["86400", "172800", "360000"])
    def test_valores_grandes(self, capture_main_output, student_module, segundos):
        """Test with large second values."""
        output = capture_main_output(segundos, student_module)
        horas = int(segundos) / 3600
        assert segundos in output
        assert str(horas) in output or str(int(horas)) in output


class TestDecimalResults:
    """Tests that result in decimal hours."""

    @pytest.mark.parametrize("segundos", ["1000", "5000", "7500"])
    def test_resultados_decimales(self, capture_main_output, student_module, segundos):
        """Test conversions that result in decimal hours."""
        output = capture_main_output(segundos, student_module)
        horas = int(segundos) / 3600
        assert segundos in output
        # Check that decimal is present
        assert "." in output, "El resultado debe incluir decimales"
''',
        "rubric": {
            "tests": [
                {"name": "test_main_function_exists", "points": 1, "visibility": "public"},
                {"name": "test_conversion_3600_segundos", "points": 2, "visibility": "public"},
                {"name": "test_conversion_7200_segundos", "points": 2, "visibility": "public"},
                {"name": "test_conversiones_varias", "points": 2, "visibility": "public"},
                {"name": "test_cero_segundos", "points": 1, "visibility": "public"},
                {"name": "test_un_segundo", "points": 1, "visibility": "public"},
                {"name": "test_formato_incluye_equivalen", "points": 1, "visibility": "public"},
                {"name": "test_formato_incluye_segundos", "points": 1, "visibility": "public"},
                {"name": "test_valores_grandes", "points": 2, "visibility": "hidden"},
                {"name": "test_resultados_decimales", "points": 2, "visibility": "hidden"},
            ],
            "max_points": 15
        }
    },

    "sec_tabla_multiplicar": {
        "tests_public": '''"""
Public tests for sec_tabla_multiplicar problem.
Tests multiplication table generation.
"""
import pytest


class TestFunctionExistence:
    """Tests to verify required function exists."""

    def test_main_function_exists(self, student_module):
        """Verify that the main() function is defined."""
        assert hasattr(student_module, 'main'), \\
            'La función main() debe estar definida en el código'


class TestBasicTable:
    """Tests for basic multiplication table."""

    def test_tabla_del_5(self, capture_main_output, student_module):
        """Test multiplication table for 5."""
        output = capture_main_output("5", student_module)
        lines = output.strip().split('\\n')
        assert len(lines) == 10, f"Debe imprimir 10 líneas, se obtuvieron {len(lines)}"

        # Verificar algunas líneas
        assert "5 x 1 = 5" in output
        assert "5 x 5 = 25" in output
        assert "5 x 10 = 50" in output

    def test_tabla_del_3(self, capture_main_output, student_module):
        """Test multiplication table for 3."""
        output = capture_main_output("3", student_module)
        lines = output.strip().split('\\n')
        assert len(lines) == 10
        assert "3 x 1 = 3" in output
        assert "3 x 10 = 30" in output


class TestLineFormat:
    """Tests for line format."""

    def test_formato_linea(self, capture_main_output, student_module):
        """Test that each line follows the format: 'numero x mult = resultado'."""
        output = capture_main_output("7", student_module)
        lines = output.strip().split('\\n')

        for i, line in enumerate(lines, 1):
            assert " x " in line, f"Línea {i} debe contener ' x '"
            assert " = " in line, f"Línea {i} debe contener ' = '"


class TestAllMultipliers:
    """Tests that all multipliers from 1 to 10 are present."""

    def test_multiplicadores_completos(self, capture_main_output, student_module):
        """Test that all multipliers 1-10 are present."""
        output = capture_main_output("4", student_module)

        for i in range(1, 11):
            expected = f"4 x {i} ="
            assert expected in output, f"Falta el multiplicador {i}"


class TestCorrectResults:
    """Tests for correct calculation results."""

    @pytest.mark.parametrize("numero", ["2", "6", "9"])
    def test_resultados_correctos(self, capture_main_output, student_module, numero):
        """Test that results are calculated correctly."""
        output = capture_main_output(numero, student_module)
        num = int(numero)

        for i in range(1, 11):
            expected_result = num * i
            expected_line = f"{numero} x {i} = {expected_result}"
            assert expected_line in output, \\
                f"Falta o es incorrecta la línea: {expected_line}"
''',
        "tests_hidden": '''"""
Hidden tests for sec_tabla_multiplicar problem.
"""
import pytest


class TestLargeNumbers:
    """Tests with large numbers."""

    def test_tabla_numero_grande(self, capture_main_output, student_module):
        """Test with large number."""
        output = capture_main_output("99", student_module)
        lines = output.strip().split('\\n')
        assert len(lines) == 10
        assert "99 x 10 = 990" in output


class TestZero:
    """Tests with zero."""

    def test_tabla_del_cero(self, capture_main_output, student_module):
        """Test multiplication table for 0."""
        output = capture_main_output("0", student_module)
        lines = output.strip().split('\\n')
        assert len(lines) == 10

        for i in range(1, 11):
            assert f"0 x {i} = 0" in output
''',
        "rubric": {
            "tests": [
                {"name": "test_main_function_exists", "points": 1, "visibility": "public"},
                {"name": "test_tabla_del_5", "points": 2, "visibility": "public"},
                {"name": "test_tabla_del_3", "points": 2, "visibility": "public"},
                {"name": "test_formato_linea", "points": 2, "visibility": "public"},
                {"name": "test_multiplicadores_completos", "points": 2, "visibility": "public"},
                {"name": "test_resultados_correctos", "points": 2, "visibility": "public"},
                {"name": "test_tabla_numero_grande", "points": 2, "visibility": "hidden"},
                {"name": "test_tabla_del_cero", "points": 2, "visibility": "hidden"},
            ],
            "max_points": 15
        }
    },

    "sec_operaciones_basicas": {
        "tests_public": '''"""
Public tests for sec_operaciones_basicas problem.
Tests basic arithmetic operations.
"""
import pytest


class TestFunctionExistence:
    """Tests to verify required function exists."""

    def test_main_function_exists(self, student_module):
        """Verify that the main() function is defined."""
        assert hasattr(student_module, 'main'), \\
            'La función main() debe estar definida en el código'


class TestBasicOperations:
    """Tests for basic arithmetic operations."""

    def test_operaciones_10_y_2(self, capture_main_output, student_module):
        """Test operations with 10 and 2."""
        output = capture_main_output("10\\n2", student_module)
        lines = output.strip().split('\\n')
        assert len(lines) == 4, f"Debe imprimir 4 líneas, se obtuvieron {len(lines)}"

        # Buscar resultados en cualquier orden
        assert "12" in output or "12.0" in output, "Suma: 10+2=12"
        assert "8" in output or "8.0" in output, "Resta: 10-2=8"
        assert "20" in output or "20.0" in output, "Multiplicación: 10*2=20"
        assert "5" in output or "5.0" in output, "División: 10/2=5"


class TestOperationLabels:
    """Tests that operations are labeled."""

    def test_etiquetas_presentes(self, capture_main_output, student_module):
        """Test that operation labels are present."""
        output = capture_main_output("6\\n3", student_module)

        # Las etiquetas pueden estar en español
        assert any(word in output.lower() for word in ["suma", "sum"]), \\
            "Debe etiquetar la suma"
        assert any(word in output.lower() for word in ["resta", "rest", "subtraction"]), \\
            "Debe etiquetar la resta"
        assert any(word in output.lower() for word in ["multiplicación", "multiplicacion", "mult"]), \\
            "Debe etiquetar la multiplicación"
        assert any(word in output.lower() for word in ["división", "division", "div"]), \\
            "Debe etiquetar la división"


class TestDifferentNumbers:
    """Tests with different number pairs."""

    @pytest.mark.parametrize("num1,num2", [
        ("15", "3"),
        ("20", "4"),
        ("100", "10"),
    ])
    def test_diferentes_numeros(self, capture_main_output, student_module, num1, num2):
        """Test with various number pairs."""
        output = capture_main_output(f"{num1}\\n{num2}", student_module)
        n1, n2 = float(num1), float(num2)

        # Verificar que contiene los resultados (como string o como parte de una línea)
        suma = n1 + n2
        resta = n1 - n2
        mult = n1 * n2
        div = n1 / n2

        assert str(suma) in output or str(int(suma)) in output
        assert str(resta) in output or str(int(resta)) in output
        assert str(mult) in output or str(int(mult)) in output
        assert str(div)[:4] in output  # Al menos primeros 4 caracteres


class TestDecimalResults:
    """Tests that produce decimal results."""

    def test_division_decimal(self, capture_main_output, student_module):
        """Test division that results in decimal."""
        output = capture_main_output("10\\n3", student_module)
        # 10/3 = 3.333...
        assert "3.3" in output, "La división debe mostrar decimales"
''',
        "tests_hidden": '''"""
Hidden tests for sec_operaciones_basicas problem.
"""
import pytest


class TestNegativeNumbers:
    """Tests with negative results."""

    def test_resta_negativa(self, capture_main_output, student_module):
        """Test subtraction resulting in negative."""
        output = capture_main_output("5\\n10", student_module)
        # 5-10 = -5
        assert "-5" in output, "Debe manejar resultados negativos"


class TestLargeNumbers:
    """Tests with large numbers."""

    def test_numeros_grandes(self, capture_main_output, student_module):
        """Test with large numbers."""
        output = capture_main_output("1000\\n100", student_module)
        lines = output.strip().split('\\n')
        assert len(lines) == 4
''',
        "rubric": {
            "tests": [
                {"name": "test_main_function_exists", "points": 1, "visibility": "public"},
                {"name": "test_operaciones_10_y_2", "points": 3, "visibility": "public"},
                {"name": "test_etiquetas_presentes", "points": 2, "visibility": "public"},
                {"name": "test_diferentes_numeros", "points": 2, "visibility": "public"},
                {"name": "test_division_decimal", "points": 2, "visibility": "public"},
                {"name": "test_resta_negativa", "points": 2, "visibility": "hidden"},
                {"name": "test_numeros_grandes", "points": 2, "visibility": "hidden"},
            ],
            "max_points": 14
        }
    }
}

def aplicar_tests(problem_id, tests_data):
    """Aplicar los tests refactorizados a un ejercicio."""
    dir_path = os.path.join(BASE_DIR, problem_id)

    # tests_public.py
    with open(os.path.join(dir_path, "tests_public.py"), "w", encoding="utf-8") as f:
        f.write(tests_data["tests_public"])

    # tests_hidden.py
    with open(os.path.join(dir_path, "tests_hidden.py"), "w", encoding="utf-8") as f:
        f.write(tests_data["tests_hidden"])

    # rubric.json
    with open(os.path.join(dir_path, "rubric.json"), "w", encoding="utf-8") as f:
        json.dump(tests_data["rubric"], f, indent=2)

    print(f"✓ Refactorizado: {problem_id}")

# Aplicar refactorización
for problem_id, tests_data in TESTS_COMPLETOS.items():
    aplicar_tests(problem_id, tests_data)

print("\n✓ Tests refactorizados aplicados exitosamente!")
