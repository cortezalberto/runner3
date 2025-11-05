"""
Hidden tests for cond_aprobado problem.
Tests advanced scenarios and stress cases.
"""
import pytest


class TestAdvancedBoundaries:
    """Advanced boundary testing."""

    @pytest.mark.parametrize("nota,esperado", [
        ("6.0", "Aprobado"),
        ("6.00", "Aprobado"),
        ("6.000", "Aprobado"),
        ("5.999", "Desaprobado"),
        ("5.9999", "Desaprobado"),
    ])
    def test_precision_boundaries(self, capture_main_output, student_module, nota, esperado):
        """Test floating point precision at boundary."""
        output = capture_main_output(nota, student_module)
        assert output == esperado, \
            f"Con nota {nota}, se esperaba '{esperado}', se obtuvo '{output}'"


class TestExtremeScores:
    """Tests for unusual but valid extreme values."""

    def test_nota_muy_alta(self, capture_main_output, student_module):
        """Test unusually high score (above 10)."""
        output = capture_main_output("15", student_module)
        assert output == "Aprobado", \
            "Una nota muy alta (15) debe ser 'Aprobado'"

    def test_nota_perfecta_con_decimales(self, capture_main_output, student_module):
        """Test perfect score with decimals."""
        output = capture_main_output("10.0", student_module)
        assert output == "Aprobado", \
            "La nota 10.0 debe ser 'Aprobado'"

    def test_nota_muy_baja(self, capture_main_output, student_module):
        """Test very low score."""
        output = capture_main_output("1", student_module)
        assert output == "Desaprobado", \
            "La nota 1 debe ser 'Desaprobado'"


class TestDecimalPrecision:
    """Tests for various decimal precision scenarios."""

    @pytest.mark.parametrize("nota,esperado", [
        ("7.5", "Aprobado"),
        ("7.25", "Aprobado"),
        ("7.125", "Aprobado"),
        ("6.1", "Aprobado"),
        ("6.01", "Aprobado"),
        ("6.001", "Aprobado"),
    ])
    def test_decimales_aprobados_precision(self, capture_main_output, student_module, nota, esperado):
        """Test decimal passing grades with various precision levels."""
        output = capture_main_output(nota, student_module)
        assert output == esperado, \
            f"Con nota {nota}, se esperaba '{esperado}', se obtuvo '{output}'"

    @pytest.mark.parametrize("nota,esperado", [
        ("5.5", "Desaprobado"),
        ("5.25", "Desaprobado"),
        ("5.125", "Desaprobado"),
        ("5.99", "Desaprobado"),
        ("5.999", "Desaprobado"),
    ])
    def test_decimales_desaprobados_precision(self, capture_main_output, student_module, nota, esperado):
        """Test decimal failing grades with various precision levels."""
        output = capture_main_output(nota, student_module)
        assert output == esperado, \
            f"Con nota {nota}, se esperaba '{esperado}', se obtuvo '{output}'"


class TestRangeValidation:
    """Test various grade ranges."""

    @pytest.mark.parametrize("nota", ["6", "7", "8", "9", "10"])
    def test_rango_aprobado_standard(self, capture_main_output, student_module, nota):
        """Test standard passing range (6-10)."""
        output = capture_main_output(nota, student_module)
        assert output == "Aprobado", \
            f"Todas las notas de 6 a 10 deben ser 'Aprobado', falló con {nota}"

    @pytest.mark.parametrize("nota", ["0", "1", "2", "3", "4", "5"])
    def test_rango_desaprobado_standard(self, capture_main_output, student_module, nota):
        """Test standard failing range (0-5)."""
        output = capture_main_output(nota, student_module)
        assert output == "Desaprobado", \
            f"Todas las notas de 0 a 5 deben ser 'Desaprobado', falló con {nota}"
