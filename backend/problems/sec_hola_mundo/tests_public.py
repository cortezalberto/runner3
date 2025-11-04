"""
Public tests for sec_hola_mundo problem.
Tests basic print() function usage.
"""
import pytest


class TestFunctionExistence:
    """Tests to verify required function exists."""

    def test_main_function_exists(self, student_module):
        """Verify that the main() function is defined."""
        assert hasattr(student_module, 'main'), \
            'La función main() debe estar definida en el código'


class TestBasicOutput:
    """Tests for basic output."""

    def test_salida_exacta(self, capture_main_output, student_module):
        """Test exact output format."""
        output = capture_main_output("", student_module)
        assert output == "Hola Mundo!", \
            f"Se esperaba 'Hola Mundo!', se obtuvo '{output}'"


class TestFormatValidation:
    """Tests to validate exact output format."""

    def test_comienza_con_hola(self, capture_main_output, student_module):
        """Test that output starts with 'Hola'."""
        output = capture_main_output("", student_module)
        assert output.startswith("Hola"), \
            f"El mensaje debe comenzar con 'Hola', se obtuvo '{output}'"

    def test_termina_con_exclamacion(self, capture_main_output, student_module):
        """Test that output ends with '!'."""
        output = capture_main_output("", student_module)
        assert output.endswith("!"), \
            f"El mensaje debe terminar con '!', se obtuvo '{output}'"

    def test_contiene_mundo(self, capture_main_output, student_module):
        """Test that output contains 'Mundo'."""
        output = capture_main_output("", student_module)
        assert "Mundo" in output, \
            f"El mensaje debe contener 'Mundo', se obtuvo '{output}'"


class TestCapitalization:
    """Tests for correct capitalization."""

    def test_mayuscula_hola(self, capture_main_output, student_module):
        """Test that 'Hola' starts with capital H."""
        output = capture_main_output("", student_module)
        assert output[0] == 'H', \
            f"'Hola' debe empezar con 'H' mayúscula, se obtuvo '{output}'"

    def test_mayuscula_mundo(self, capture_main_output, student_module):
        """Test that 'Mundo' starts with capital M."""
        output = capture_main_output("", student_module)
        palabras = output.split()
        assert len(palabras) >= 2, \
            f"El mensaje debe tener al menos dos palabras, se obtuvo '{output}'"
        assert palabras[1][0] == 'M', \
            f"'Mundo' debe empezar con 'M' mayúscula, se obtuvo '{output}'"


class TestNoExtraOutput:
    """Test that there's no extra output."""

    def test_sin_saltos_extra(self, capture_main_output, student_module):
        """Test that there are no extra line breaks."""
        output = capture_main_output("", student_module)
        assert output == "Hola Mundo!", \
            f"No debe haber espacios o saltos extra, se obtuvo '{output}'"
