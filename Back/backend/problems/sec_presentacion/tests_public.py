"""
Public tests for sec_presentacion problem.
Tests string formatting with multiple inputs.
"""
import pytest


class TestFunctionExistence:
    """Tests to verify required function exists."""

    def test_main_function_exists(self, student_module):
        """Verify that the main() function is defined."""
        assert hasattr(student_module, 'main'), \
            'La función main() debe estar definida en el código'


class TestBasicPresentations:
    """Tests for basic presentation scenarios."""

    @pytest.mark.parametrize("datos,esperado", [
        ("Juan\nPérez\n25\nMadrid", "Soy Juan Pérez, tengo 25 años y vivo en Madrid"),
        ("María\nGómez\n30\nBarcelona", "Soy María Gómez, tengo 30 años y vivo en Barcelona"),
        ("Pedro\nLópez\n40\nValencia", "Soy Pedro López, tengo 40 años y vivo en Valencia"),
    ])
    def test_presentaciones_basicas(self, capture_main_output, student_module, datos, esperado):
        """Test basic presentations."""
        output = capture_main_output(datos, student_module)
        assert output == esperado, \
            f"Se esperaba '{esperado}', se obtuvo '{output}'"


class TestFormatValidation:
    """Tests to validate exact output format."""

    def test_formato_comienza_con_soy(self, capture_main_output, student_module):
        """Test that output starts with 'Soy '."""
        output = capture_main_output("Test\nApellido\n25\nCiudad", student_module)
        assert output.startswith("Soy "), \
            f"La presentación debe comenzar con 'Soy ', se obtuvo '{output}'"

    def test_formato_contiene_tengo_anos(self, capture_main_output, student_module):
        """Test that output contains 'tengo' and 'años'."""
        output = capture_main_output("Test\nApellido\n25\nCiudad", student_module)
        assert "tengo" in output, \
            f"Debe contener la palabra 'tengo', se obtuvo '{output}'"
        assert "años" in output, \
            f"Debe contener la palabra 'años', se obtuvo '{output}'"

    def test_formato_contiene_vivo_en(self, capture_main_output, student_module):
        """Test that output contains 'vivo en'."""
        output = capture_main_output("Test\nApellido\n25\nCiudad", student_module)
        assert "vivo en" in output, \
            f"Debe contener 'vivo en', se obtuvo '{output}'"


class TestDifferentAges:
    """Tests with different ages."""

    @pytest.mark.parametrize("edad", ["18", "21", "35", "50", "65"])
    def test_diferentes_edades(self, capture_main_output, student_module, edad):
        """Test with various ages."""
        datos = f"Juan\nPérez\n{edad}\nMadrid"
        output = capture_main_output(datos, student_module)
        assert edad in output, \
            f"La edad {edad} debe aparecer en la salida, se obtuvo '{output}'"
        assert "años" in output, \
            f"Debe incluir la palabra 'años', se obtuvo '{output}'"
