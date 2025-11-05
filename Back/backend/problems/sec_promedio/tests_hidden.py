"""
Hidden tests for sec_promedio problem.
Tests advanced scenarios and edge cases for average calculation.
"""
import pytest


class TestNegativeNumbers:
    """Tests with negative numbers."""

    def test_promedio_con_negativos(self, capture_main_output, student_module):
        """Test average with negative numbers."""
        output = capture_main_output("-5\n10\n-15", student_module)

        # Promedio = (-5 + 10 + (-15)) / 3 = -10 / 3 = -3.333...
        assert "-3.3" in output or "-3" in output, \
            "Debe calcular correctamente con números negativos"

    def test_promedio_todos_negativos(self, capture_main_output, student_module):
        """Test average with all negative numbers."""
        output = capture_main_output("-10\n-20\n-30", student_module)

        # Promedio = (-10 + (-20) + (-30)) / 3 = -60 / 3 = -20.0
        assert "-20" in output or "-20.0" in output, \
            "El promedio de números negativos debe ser negativo"

    @pytest.mark.parametrize("num1,num2,num3", [
        ("-5", "-10", "-15"),
        ("-2", "-4", "-6"),
        ("-100", "-200", "-300"),
    ])
    def test_varios_negativos(self, capture_main_output, student_module, num1, num2, num3):
        """Test various negative number combinations."""
        output = capture_main_output(f"{num1}\n{num2}\n{num3}", student_module)

        n1, n2, n3 = float(num1), float(num2), float(num3)
        promedio = (n1 + n2 + n3) / 3

        # Verificar que el promedio está presente (con signo negativo)
        assert str(promedio)[:5] in output or str(int(promedio)) in output


class TestLargeNumbers:
    """Tests with large numbers."""

    def test_numeros_grandes(self, capture_main_output, student_module):
        """Test with large numbers."""
        output = capture_main_output("1000\n2000\n3000", student_module)

        # Promedio = (1000 + 2000 + 3000) / 3 = 2000.0
        assert "2000" in output or "2000.0" in output, \
            "Debe calcular correctamente con números grandes"

    def test_numeros_muy_grandes(self, capture_main_output, student_module):
        """Test with very large numbers."""
        output = capture_main_output("10000\n20000\n30000", student_module)

        # Promedio = (10000 + 20000 + 30000) / 3 = 20000.0
        assert "20000" in output or "20000.0" in output


class TestZeroEdgeCases:
    """Tests with zero values."""

    def test_todos_ceros(self, capture_main_output, student_module):
        """Test with all zeros."""
        output = capture_main_output("0\n0\n0", student_module)

        # Promedio = (0 + 0 + 0) / 3 = 0.0
        assert "0" in output or "0.0" in output, \
            "El promedio de ceros debe ser cero"

    def test_dos_ceros(self, capture_main_output, student_module):
        """Test with two zeros."""
        output = capture_main_output("0\n0\n30", student_module)

        # Promedio = (0 + 0 + 30) / 3 = 10.0
        assert "10" in output or "10.0" in output


class TestPrecisionDecimals:
    """Tests for decimal precision."""

    @pytest.mark.parametrize("num1,num2,num3", [
        ("1.5", "2.5", "3.5"),
        ("10.1", "20.2", "30.3"),
        ("5.55", "6.66", "7.77"),
    ])
    def test_precision_decimales(self, capture_main_output, student_module, num1, num2, num3):
        """Test precision with various decimal combinations."""
        output = capture_main_output(f"{num1}\n{num2}\n{num3}", student_module)

        n1, n2, n3 = float(num1), float(num2), float(num3)
        promedio = (n1 + n2 + n3) / 3

        # Verificar que el promedio está presente (al menos primeros dígitos)
        promedio_str = str(promedio)[:5]
        assert promedio_str in output or str(int(promedio)) in output


class TestNonIntegerAverages:
    """Tests that result in non-integer averages."""

    def test_promedio_no_entero(self, capture_main_output, student_module):
        """Test average that results in non-integer."""
        output = capture_main_output("1\n2\n4", student_module)

        # Promedio = (1 + 2 + 4) / 3 = 7 / 3 = 2.333...
        assert "2.3" in output or "2" in output, \
            "Debe calcular correctamente promedios no enteros"

    def test_promedio_con_tercios(self, capture_main_output, student_module):
        """Test average with thirds."""
        output = capture_main_output("10\n11\n12", student_module)

        # Promedio = (10 + 11 + 12) / 3 = 33 / 3 = 11.0
        assert "11" in output or "11.0" in output


class TestMixedValues:
    """Tests with mixed positive, negative, and zero values."""

    def test_valores_mixtos(self, capture_main_output, student_module):
        """Test with mixed positive and negative values."""
        output = capture_main_output("-10\n0\n10", student_module)

        # Promedio = (-10 + 0 + 10) / 3 = 0 / 3 = 0.0
        assert "0" in output or "0.0" in output, \
            "El promedio de valores que se cancelan debe ser 0"

    def test_valores_mixtos_positivos_negativos(self, capture_main_output, student_module):
        """Test with mixed values resulting in positive average."""
        output = capture_main_output("-5\n10\n20", student_module)

        # Promedio = (-5 + 10 + 20) / 3 = 25 / 3 = 8.333...
        assert "8.3" in output or "8" in output
