"""
Public tests for sec_tabla_multiplicar problem.
Tests multiplication table generation without loops.
"""
import pytest


class TestFunctionExistence:
    """Tests to verify required function exists."""

    def test_main_function_exists(self, student_module):
        """Verify that the main() function is defined."""
        assert hasattr(student_module, 'main'), \
            'La función main() debe estar definida en el código'


class TestBasicTable:
    """Tests for basic multiplication table."""

    def test_tabla_del_5(self, capture_main_output, student_module):
        """Test multiplication table for 5."""
        output = capture_main_output("5", student_module)
        lines = output.strip().split('\n')
        assert len(lines) == 10, \
            f"Debe imprimir exactamente 10 líneas, se obtuvieron {len(lines)}"

        # Verificar líneas específicas
        assert "5 x 1 = 5" in output, "Falta 5 x 1 = 5"
        assert "5 x 5 = 25" in output, "Falta 5 x 5 = 25"
        assert "5 x 10 = 50" in output, "Falta 5 x 10 = 50"

    def test_tabla_del_3(self, capture_main_output, student_module):
        """Test multiplication table for 3."""
        output = capture_main_output("3", student_module)
        lines = output.strip().split('\n')
        assert len(lines) == 10, \
            f"Debe imprimir exactamente 10 líneas"

        assert "3 x 1 = 3" in output
        assert "3 x 10 = 30" in output


class TestLineFormat:
    """Tests for line format validation."""

    def test_formato_linea_con_x(self, capture_main_output, student_module):
        """Test that each line contains ' x '."""
        output = capture_main_output("7", student_module)
        lines = output.strip().split('\n')

        for i, line in enumerate(lines, 1):
            assert " x " in line, \
                f"Línea {i} debe contener ' x ', se obtuvo: '{line}'"

    def test_formato_linea_con_igual(self, capture_main_output, student_module):
        """Test that each line contains ' = '."""
        output = capture_main_output("7", student_module)
        lines = output.strip().split('\n')

        for i, line in enumerate(lines, 1):
            assert " = " in line, \
                f"Línea {i} debe contener ' = ', se obtuvo: '{line}'"


class TestAllMultipliers:
    """Tests that all multipliers from 1 to 10 are present."""

    def test_multiplicadores_del_1_al_10(self, capture_main_output, student_module):
        """Test that all multipliers 1-10 are present."""
        output = capture_main_output("4", student_module)

        for i in range(1, 11):
            expected = f"4 x {i} ="
            assert expected in output, \
                f"Falta el multiplicador {i}: debe aparecer '4 x {i} ='"


class TestCorrectResults:
    """Tests for correct calculation results."""

    @pytest.mark.parametrize("numero", ["2", "6", "9"])
    def test_resultados_correctos(self, capture_main_output, student_module, numero):
        """Test that all results are calculated correctly."""
        output = capture_main_output(numero, student_module)
        num = int(numero)

        for i in range(1, 11):
            expected_result = num * i
            expected_line = f"{numero} x {i} = {expected_result}"
            assert expected_line in output, \
                f"Falta o es incorrecta la línea: '{expected_line}'"


class TestOutputLines:
    """Tests for output line count."""

    @pytest.mark.parametrize("numero", ["1", "8", "12"])
    def test_diez_lineas_exactas(self, capture_main_output, student_module, numero):
        """Test that output has exactly 10 lines."""
        output = capture_main_output(numero, student_module)
        lines = output.strip().split('\n')
        assert len(lines) == 10, \
            f"Debe imprimir exactamente 10 líneas, se obtuvieron {len(lines)}"


class TestSequentialOrder:
    """Tests that multipliers appear in sequential order."""

    def test_orden_secuencial(self, capture_main_output, student_module):
        """Test that multipliers appear in order 1-10."""
        output = capture_main_output("3", student_module)
        lines = output.strip().split('\n')

        for i, line in enumerate(lines, 1):
            expected_mult = f"3 x {i}"
            assert expected_mult in line, \
                f"Línea {i} debe contener '3 x {i}', se obtuvo: '{line}'"
