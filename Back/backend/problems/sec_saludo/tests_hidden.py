"""
Hidden tests for sec_saludo problem.
Tests advanced scenarios and edge cases.
"""
import pytest


class TestCompoundNames:
    """Tests with compound names."""

    @pytest.mark.parametrize("nombre,esperado", [
        ("Juan Carlos", "Hola Juan Carlos!"),
        ("María José", "Hola María José!"),
        ("Ana María", "Hola Ana María!"),
    ])
    def test_nombres_compuestos(self, capture_main_output, student_module, nombre, esperado):
        """Test with compound names."""
        output = capture_main_output(nombre, student_module)
        assert output == esperado, \
            f"Nombres compuestos deben funcionar, se esperaba '{esperado}', se obtuvo '{output}'"


class TestAccentedNames:
    """Tests with accented names."""

    @pytest.mark.parametrize("nombre", ["José", "María", "Andrés", "Sofía"])
    def test_nombres_con_acento(self, capture_main_output, student_module, nombre):
        """Test with accented names."""
        output = capture_main_output(nombre, student_module)
        esperado = f"Hola {nombre}!"
        assert output == esperado, \
            f"Nombres con acento deben funcionar, se esperaba '{esperado}', se obtuvo '{output}'"


class TestExactFormat:
    """Tests for exact format requirements."""

    def test_espacio_despues_de_hola(self, capture_main_output, student_module):
        """Test that there's exactly one space after 'Hola'."""
        output = capture_main_output("Test", student_module)
        assert "Hola " in output, \
            f"Debe haber un espacio después de 'Hola', se obtuvo '{output}'"
        assert not "Hola  " in output, \
            f"No debe haber espacios dobles, se obtuvo '{output}'"
