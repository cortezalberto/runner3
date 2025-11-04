"""
Hidden tests for sec_operaciones_basicas problem.
Tests edge cases and advanced scenarios.
"""
import pytest


class TestNegativeNumbers:
    """Tests with negative numbers."""

    def test_resta_negativa(self, capture_main_output, student_module):
        """Test subtraction resulting in negative."""
        output = capture_main_output("5\n10", student_module)
        lines = output.strip().split('\n')
        assert len(lines) == 4

        # 5 - 10 = -5
        assert "-5" in output or "-5.0" in output, \
            "La resta 5 - 10 debe dar -5 (resultado negativo)"

    def test_numeros_negativos(self, capture_main_output, student_module):
        """Test with negative input numbers."""
        output = capture_main_output("-10\n2", student_module)
        lines = output.strip().split('\n')
        assert len(lines) == 4

        # -10 + 2 = -8
        assert "-8" in output or "-8.0" in output
        # -10 - 2 = -12
        assert "-12" in output or "-12.0" in output


class TestLargeNumbers:
    """Tests with large numbers."""

    def test_numeros_grandes(self, capture_main_output, student_module):
        """Test with large numbers."""
        output = capture_main_output("1000\n100", student_module)
        lines = output.strip().split('\n')
        assert len(lines) == 4, \
            "Debe imprimir 4 líneas incluso con números grandes"

        # Verificar algunos resultados
        assert "1100" in output or "1100.0" in output  # suma
        assert "900" in output or "900.0" in output    # resta
        assert "100000" in output or "100000.0" in output  # multiplicación


class TestZeroDivision:
    """Tests with zero values."""

    def test_division_por_cero_especial(self, capture_main_output, student_module):
        """Test special case with zero divisor (if handled)."""
        # Este test verifica que el programa no falle catastróficamente
        # Puede lanzar ZeroDivisionError o manejarlo de alguna forma
        try:
            output = capture_main_output("10\n0", student_module)
            # Si llega aquí, el estudiante manejó el caso especial
            # Verificar que al menos imprimió 3 líneas (suma, resta, mult)
            lines = output.strip().split('\n')
            assert len(lines) >= 3, \
                "Debe manejar la división por cero sin fallar completamente"
        except ZeroDivisionError:
            # Es aceptable que lance esta excepción
            pass

    def test_cero_como_primer_numero(self, capture_main_output, student_module):
        """Test with zero as first number."""
        output = capture_main_output("0\n5", student_module)
        lines = output.strip().split('\n')
        assert len(lines) == 4

        # 0 + 5 = 5
        assert "5" in output or "5.0" in output
        # 0 * 5 = 0
        # Debe haber al menos un 0 en la salida
        assert "0" in output


class TestPrecisionDecimal:
    """Tests for decimal precision."""

    def test_decimales_precision(self, capture_main_output, student_module):
        """Test operations with decimal precision."""
        output = capture_main_output("7.5\n2.5", student_module)
        lines = output.strip().split('\n')
        assert len(lines) == 4

        # 7.5 + 2.5 = 10.0
        assert "10" in output or "10.0" in output
        # 7.5 / 2.5 = 3.0
        assert "3" in output or "3.0" in output
