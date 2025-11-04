"""
Public tests for sec_promedio problem.
Tests average calculation of three numbers.
"""
import pytest


class TestFunctionExistence:
    """Tests to verify required function exists."""

    def test_main_function_exists(self, student_module):
        """Verify that the main() function is defined."""
        assert hasattr(student_module, 'main'), \
            'La función main() debe estar definida en el código'


class TestBasicAverage:
    """Tests for basic average calculations."""

    def test_promedio_ejemplo(self, capture_main_output, student_module):
        """Test with example from prompt (10, 20, 30)."""
        output = capture_main_output("10\n20\n30", student_module)

        # Promedio = (10 + 20 + 30) / 3 = 20.0
        assert "20" in output or "20.0" in output, \
            "El promedio de 10, 20, 30 debe ser 20"
        assert "promedio" in output.lower(), \
            "Debe mencionar 'promedio' en el mensaje"

    def test_promedio_numeros_iguales(self, capture_main_output, student_module):
        """Test with three equal numbers."""
        output = capture_main_output("5\n5\n5", student_module)

        # Promedio = (5 + 5 + 5) / 3 = 5.0
        assert "5" in output or "5.0" in output, \
            "El promedio de tres números iguales debe ser ese número"

    def test_promedio_con_cero(self, capture_main_output, student_module):
        """Test with one zero value."""
        output = capture_main_output("0\n10\n20", student_module)

        # Promedio = (0 + 10 + 20) / 3 = 10.0
        assert "10" in output or "10.0" in output, \
            "El promedio de 0, 10, 20 debe ser 10"


class TestVariousAverages:
    """Tests with various number combinations."""

    @pytest.mark.parametrize("num1,num2,num3,promedio_esperado", [
        ("6", "9", "12", "9"),
        ("15", "25", "35", "25"),
        ("100", "200", "300", "200"),
    ])
    def test_promedios_varios(self, capture_main_output, student_module, num1, num2, num3, promedio_esperado):
        """Test various average calculations."""
        output = capture_main_output(f"{num1}\n{num2}\n{num3}", student_module)

        # Verificar que el promedio está presente
        assert promedio_esperado in output or f"{promedio_esperado}.0" in output, \
            f"El promedio de {num1}, {num2}, {num3} debe ser {promedio_esperado}"


class TestDecimalAverages:
    """Tests that result in decimal averages."""

    def test_promedio_decimal_simple(self, capture_main_output, student_module):
        """Test average resulting in decimal."""
        output = capture_main_output("1\n2\n3", student_module)

        # Promedio = (1 + 2 + 3) / 3 = 2.0
        assert "2" in output or "2.0" in output, \
            "El promedio de 1, 2, 3 debe ser 2"

    def test_promedio_con_decimales(self, capture_main_output, student_module):
        """Test average with decimal result."""
        output = capture_main_output("10\n15\n20", student_module)

        # Promedio = (10 + 15 + 20) / 3 = 15.0
        assert "15" in output or "15.0" in output, \
            "El promedio de 10, 15, 20 debe ser 15"

    @pytest.mark.parametrize("num1,num2,num3", [
        ("5", "6", "7"),
        ("8", "9", "10"),
        ("11", "12", "13"),
    ])
    def test_promedios_consecutivos(self, capture_main_output, student_module, num1, num2, num3):
        """Test averages of consecutive numbers."""
        output = capture_main_output(f"{num1}\n{num2}\n{num3}", student_module)

        # El promedio de números consecutivos es el del medio
        n1, n2, n3 = float(num1), float(num2), float(num3)
        promedio = (n1 + n2 + n3) / 3

        # Verificar que el promedio calculado está presente
        assert str(promedio) in output or str(int(promedio)) in output, \
            f"El promedio debe estar presente en la salida"


class TestOutputFormat:
    """Tests for output format validation."""

    def test_formato_mensaje_completo(self, capture_main_output, student_module):
        """Test that output contains complete message."""
        output = capture_main_output("5\n10\n15", student_module)

        # Debe contener las palabras clave
        assert "promedio" in output.lower(), \
            "Debe mencionar 'promedio'"
        assert "tres" in output.lower() or "3" in output, \
            "Debe mencionar 'tres' o '3' números"

    def test_formato_incluye_resultado(self, capture_main_output, student_module):
        """Test that output includes the calculated result."""
        output = capture_main_output("12\n18\n24", student_module)

        # Promedio = (12 + 18 + 24) / 3 = 18.0
        assert "18" in output or "18.0" in output, \
            "Debe incluir el resultado del promedio"


class TestInputDecimalNumbers:
    """Tests with decimal input numbers."""

    def test_numeros_decimales_entrada(self, capture_main_output, student_module):
        """Test with decimal input numbers."""
        output = capture_main_output("5.5\n7.5\n9.0", student_module)

        # Promedio = (5.5 + 7.5 + 9.0) / 3 = 7.333...
        assert "7.3" in output or "7" in output, \
            "Debe calcular correctamente con números decimales"

    def test_promedio_decimal_precision(self, capture_main_output, student_module):
        """Test decimal precision in average."""
        output = capture_main_output("2.5\n3.5\n4.0", student_module)

        # Promedio = (2.5 + 3.5 + 4.0) / 3 = 3.333...
        assert "3.3" in output or "3" in output, \
            "Debe mostrar el promedio con precisión adecuada"
