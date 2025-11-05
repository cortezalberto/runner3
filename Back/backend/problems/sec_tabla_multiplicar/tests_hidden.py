"""
Hidden tests for sec_tabla_multiplicar problem.
Tests advanced scenarios with large numbers, zero, and edge cases.
"""
import pytest


class TestLargeNumbers:
    """Tests with large numbers."""

    def test_tabla_numero_grande(self, capture_main_output, student_module):
        """Test with large number 99."""
        output = capture_main_output("99", student_module)
        lines = output.strip().split('\n')
        assert len(lines) == 10, \
            f"Debe imprimir 10 líneas, se obtuvieron {len(lines)}"

        # Verificar algunas líneas específicas
        assert "99 x 1 = 99" in output, "Falta 99 x 1 = 99"
        assert "99 x 5 = 495" in output, "Falta 99 x 5 = 495"
        assert "99 x 10 = 990" in output, "Falta 99 x 10 = 990"

    def test_tabla_numero_muy_grande(self, capture_main_output, student_module):
        """Test with very large number 999."""
        output = capture_main_output("999", student_module)
        lines = output.strip().split('\n')
        assert len(lines) == 10

        # Verificar cálculos correctos con números grandes
        assert "999 x 10 = 9990" in output, "Falta 999 x 10 = 9990"


class TestZero:
    """Tests with zero."""

    def test_tabla_del_cero(self, capture_main_output, student_module):
        """Test multiplication table for 0."""
        output = capture_main_output("0", student_module)
        lines = output.strip().split('\n')
        assert len(lines) == 10, \
            f"Debe imprimir 10 líneas para tabla del 0"

        # Todos los resultados deben ser 0
        for i in range(1, 11):
            expected = f"0 x {i} = 0"
            assert expected in output, \
                f"Falta o es incorrecta la línea: '{expected}'"


class TestNegativeNumbers:
    """Tests with negative numbers."""

    def test_tabla_numero_negativo(self, capture_main_output, student_module):
        """Test with negative number."""
        output = capture_main_output("-5", student_module)
        lines = output.strip().split('\n')
        assert len(lines) == 10

        # Verificar resultados negativos
        assert "-5 x 1 = -5" in output, "Falta -5 x 1 = -5"
        assert "-5 x 5 = -25" in output, "Falta -5 x 5 = -25"
        assert "-5 x 10 = -50" in output, "Falta -5 x 10 = -50"


class TestDecimalNumbers:
    """Tests with decimal numbers."""

    @pytest.mark.parametrize("numero", ["2.5", "3.7", "1.5"])
    def test_tabla_numeros_decimales(self, capture_main_output, student_module, numero):
        """Test with decimal numbers."""
        output = capture_main_output(numero, student_module)
        lines = output.strip().split('\n')
        assert len(lines) == 10, \
            f"Debe imprimir 10 líneas para número decimal {numero}"

        num = float(numero)
        # Verificar algunos cálculos
        for i in [1, 5, 10]:
            expected_result = num * i
            # Buscar el resultado (puede tener diferentes formatos decimales)
            assert f"{numero} x {i} =" in output, \
                f"Falta la línea para {numero} x {i}"
