"""
Public tests for sec_segundos_horas problem.
Tests seconds to hours conversion.
"""
import pytest


class TestFunctionExistence:
    """Tests to verify required function exists."""

    def test_main_function_exists(self, student_module):
        """Verify that the main() function is defined."""
        assert hasattr(student_module, 'main'), \
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
