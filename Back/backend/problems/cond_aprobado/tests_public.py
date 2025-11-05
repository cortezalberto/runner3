"""
Public tests for cond_aprobado problem.
Tests basic conditional logic for pass/fail grading.
"""
import pytest


class TestFunctionExistence:
    """Tests to verify required function exists."""

    def test_main_function_exists(self, student_module):
        """Verify that the main() function is defined."""
        assert hasattr(student_module, 'main'), \
            'La función main() debe estar definida en el código'


class TestBasicCases:
    """Tests for basic approval/disapproval scenarios."""

    @pytest.mark.parametrize("nota,esperado", [
        ("7", "Aprobado"),
        ("8", "Aprobado"),
        ("9", "Aprobado"),
        ("10", "Aprobado"),
    ])
    def test_notas_aprobadas(self, capture_main_output, student_module, nota, esperado):
        """Test various passing grades."""
        output = capture_main_output(nota, student_module)
        assert output == esperado, \
            f"Con nota {nota}, se esperaba '{esperado}', se obtuvo '{output}'"

    @pytest.mark.parametrize("nota,esperado", [
        ("4", "Desaprobado"),
        ("3", "Desaprobado"),
        ("2", "Desaprobado"),
        ("1", "Desaprobado"),
        ("0", "Desaprobado"),
    ])
    def test_notas_desaprobadas(self, capture_main_output, student_module, nota, esperado):
        """Test various failing grades."""
        output = capture_main_output(nota, student_module)
        assert output == esperado, \
            f"Con nota {nota}, se esperaba '{esperado}', se obtuvo '{output}'"


class TestBoundaryValues:
    """Tests for boundary values (edge cases)."""

    def test_nota_limite_aprobado(self, capture_main_output, student_module):
        """Test the minimum passing grade (6)."""
        output = capture_main_output("6", student_module)
        assert output == "Aprobado", \
            "La nota 6 debe ser 'Aprobado' (límite inferior)"

    def test_nota_limite_superior_desaprobado(self, capture_main_output, student_module):
        """Test just below passing grade (5.99)."""
        output = capture_main_output("5.99", student_module)
        assert output == "Desaprobado", \
            "La nota 5.99 debe ser 'Desaprobado' (justo debajo del límite)"

    def test_nota_limite_inferior_aprobado(self, capture_main_output, student_module):
        """Test just above passing grade (6.01)."""
        output = capture_main_output("6.01", student_module)
        assert output == "Aprobado", \
            "La nota 6.01 debe ser 'Aprobado' (justo arriba del límite)"


class TestDecimalGrades:
    """Tests for decimal grade values."""

    @pytest.mark.parametrize("nota,esperado", [
        ("6.5", "Aprobado"),
        ("7.3", "Aprobado"),
        ("8.9", "Aprobado"),
        ("9.5", "Aprobado"),
    ])
    def test_notas_decimales_aprobadas(self, capture_main_output, student_module, nota, esperado):
        """Test decimal passing grades."""
        output = capture_main_output(nota, student_module)
        assert output == esperado, \
            f"Con nota {nota}, se esperaba '{esperado}', se obtuvo '{output}'"

    @pytest.mark.parametrize("nota,esperado", [
        ("5.9", "Desaprobado"),
        ("4.5", "Desaprobado"),
        ("3.2", "Desaprobado"),
        ("2.1", "Desaprobado"),
    ])
    def test_notas_decimales_desaprobadas(self, capture_main_output, student_module, nota, esperado):
        """Test decimal failing grades."""
        output = capture_main_output(nota, student_module)
        assert output == esperado, \
            f"Con nota {nota}, se esperaba '{esperado}', se obtuvo '{output}'"


class TestExtremeValues:
    """Tests for extreme and edge case values."""

    def test_nota_perfecta(self, capture_main_output, student_module):
        """Test perfect score (10)."""
        output = capture_main_output("10", student_module)
        assert output == "Aprobado", \
            "La nota perfecta (10) debe ser 'Aprobado'"

    def test_nota_cero(self, capture_main_output, student_module):
        """Test zero score."""
        output = capture_main_output("0", student_module)
        assert output == "Desaprobado", \
            "La nota 0 debe ser 'Desaprobado'"

    def test_nota_minima(self, capture_main_output, student_module):
        """Test minimum possible score."""
        output = capture_main_output("0.1", student_module)
        assert output == "Desaprobado", \
            "La nota mínima (0.1) debe ser 'Desaprobado'"
