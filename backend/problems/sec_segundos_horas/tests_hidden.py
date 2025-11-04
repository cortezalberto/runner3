"""
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
