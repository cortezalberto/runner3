"""
Hidden tests for sec_presentacion problem.
Tests advanced scenarios.
"""
import pytest


class TestCompoundNames:
    """Tests with compound names."""

    @pytest.mark.parametrize("datos,esperado", [
        ("Juan Carlos\nPérez García\n28\nMadrid", "Soy Juan Carlos Pérez García, tengo 28 años y vivo en Madrid"),
        ("Ana María\nLópez\n35\nBarcelona", "Soy Ana María López, tengo 35 años y vivo en Barcelona"),
    ])
    def test_nombres_compuestos(self, capture_main_output, student_module, datos, esperado):
        """Test with compound names."""
        output = capture_main_output(datos, student_module)
        assert output == esperado, \
            f"Se esperaba '{esperado}', se obtuvo '{output}'"


class TestCitiesWithSpaces:
    """Tests with city names containing spaces."""

    def test_ciudad_con_espacios(self, capture_main_output, student_module):
        """Test with city names that have spaces."""
        datos = "Juan\nPérez\n30\nSan Sebastián"
        output = capture_main_output(datos, student_module)
        assert "San Sebastián" in output, \
            f"La ciudad 'San Sebastián' debe aparecer completa, se obtuvo '{output}'"
