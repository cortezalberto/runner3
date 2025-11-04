"""
Hidden tests for sec_hola_mundo problem.
Tests advanced scenarios and edge cases.
"""
import pytest


class TestOutputConsistency:
    """Tests for output consistency."""

    def test_salida_consistente_multiple_ejecuciones(self, capture_main_output, student_module):
        """Test that output is consistent across multiple executions."""
        output1 = capture_main_output("", student_module)
        output2 = capture_main_output("", student_module)
        assert output1 == output2 == "Hola Mundo!", \
            f"La salida debe ser consistente en múltiples ejecuciones"


class TestExactFormat:
    """Tests for exact format requirements."""

    def test_formato_exacto_sin_espacios_extra(self, capture_main_output, student_module):
        """Test exact format without extra spaces."""
        output = capture_main_output("", student_module)
        assert output == "Hola Mundo!", \
            f"No debe haber espacios adicionales, se obtuvo '{output}'"

    def test_sin_caracteres_extra(self, capture_main_output, student_module):
        """Test that there are no extra characters."""
        output = capture_main_output("", student_module)
        assert len(output) == 11, \
            f"La longitud debe ser exactamente 11 caracteres, se obtuvo {len(output)}"


class TestStringComponents:
    """Tests for string components."""

    def test_espacio_entre_palabras(self, capture_main_output, student_module):
        """Test that there's exactly one space between words."""
        output = capture_main_output("", student_module)
        assert " " in output, \
            f"Debe haber un espacio entre 'Hola' y 'Mundo', se obtuvo '{output}'"
        assert output.count(" ") == 1, \
            f"Debe haber exactamente un espacio, se encontraron {output.count(' ')}"
