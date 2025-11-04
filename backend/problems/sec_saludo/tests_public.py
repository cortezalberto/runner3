"""
Public tests for sec_saludo problem.
Tests basic string formatting and personalized greeting.
"""
import pytest


class TestFunctionExistence:
    """Tests to verify required function exists."""

    def test_main_function_exists(self, student_module):
        """Verify that the main() function is defined."""
        assert hasattr(student_module, 'main'), \
            'La función main() debe estar definida en el código'


class TestBasicGreetings:
    """Tests for basic greeting scenarios."""

    @pytest.mark.parametrize("nombre,esperado", [
        ("Juan", "Hola Juan!"),
        ("María", "Hola María!"),
        ("Pedro", "Hola Pedro!"),
        ("Ana", "Hola Ana!"),
    ])
    def test_saludos_nombres_comunes(self, capture_main_output, student_module, nombre, esperado):
        """Test greetings with common names."""
        output = capture_main_output(nombre, student_module)
        assert output == esperado, \
            f"Con nombre '{nombre}', se esperaba '{esperado}', se obtuvo '{output}'"


class TestNameVariations:
    """Tests with different name variations."""

    @pytest.mark.parametrize("nombre", ["Carlos", "Lucía", "Roberto", "Elena"])
    def test_diferentes_nombres(self, capture_main_output, student_module, nombre):
        """Test with various names."""
        output = capture_main_output(nombre, student_module)
        esperado = f"Hola {nombre}!"
        assert output == esperado, \
            f"Con nombre '{nombre}', se esperaba '{esperado}', se obtuvo '{output}'"


class TestShortNames:
    """Tests with short names."""

    @pytest.mark.parametrize("nombre", ["Jo", "Lu", "Al"])
    def test_nombres_cortos(self, capture_main_output, student_module, nombre):
        """Test with short names."""
        output = capture_main_output(nombre, student_module)
        esperado = f"Hola {nombre}!"
        assert output == esperado, \
            f"Nombres cortos deben funcionar, se esperaba '{esperado}', se obtuvo '{output}'"


class TestLongNames:
    """Tests with long names."""

    @pytest.mark.parametrize("nombre", ["Alejandro", "Valentina", "Sebastian"])
    def test_nombres_largos(self, capture_main_output, student_module, nombre):
        """Test with long names."""
        output = capture_main_output(nombre, student_module)
        esperado = f"Hola {nombre}!"
        assert output == esperado, \
            f"Nombres largos deben funcionar, se esperaba '{esperado}', se obtuvo '{output}'"


class TestFormatValidation:
    """Tests to validate exact output format."""

    def test_formato_comienza_con_hola(self, capture_main_output, student_module):
        """Test that output starts with 'Hola '."""
        output = capture_main_output("Test", student_module)
        assert output.startswith("Hola "), \
            f"El saludo debe comenzar con 'Hola ', se obtuvo '{output}'"

    def test_formato_termina_con_exclamacion(self, capture_main_output, student_module):
        """Test that output ends with '!'."""
        output = capture_main_output("Test", student_module)
        assert output.endswith("!"), \
            f"El saludo debe terminar con '!', se obtuvo '{output}'"

    def test_formato_contiene_nombre(self, capture_main_output, student_module):
        """Test that output contains the name."""
        nombre = "TestNombre"
        output = capture_main_output(nombre, student_module)
        assert nombre in output, \
            f"El saludo debe contener el nombre '{nombre}', se obtuvo '{output}'"
