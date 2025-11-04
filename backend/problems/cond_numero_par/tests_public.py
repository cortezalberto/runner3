"""
Public tests for cond_numero_par problem.
Tests conditional logic for even number verification.
"""
import pytest


class TestFunctionExistence:
    """Tests to verify required function exists."""

    def test_main_function_exists(self, student_module):
        """Verify that the main() function is defined."""
        assert hasattr(student_module, 'main'), \
            'La función main() debe estar definida en el código'


class TestEvenNumbers:
    """Tests for even number inputs."""

    @pytest.mark.parametrize("numero", ["0", "2", "4", "6", "8", "10", "100", "1000"])
    def test_numeros_pares(self, capture_main_output, student_module, numero):
        """Test even numbers."""
        output = capture_main_output(numero, student_module)
        assert output == "Ha ingresado un número par", \
            f"El número {numero} es par, debe imprimir 'Ha ingresado un número par'"


class TestOddNumbers:
    """Tests for odd number inputs."""

    @pytest.mark.parametrize("numero", ["1", "3", "5", "7", "9", "99", "1001"])
    def test_numeros_impares(self, capture_main_output, student_module, numero):
        """Test odd numbers."""
        output = capture_main_output(numero, student_module)
        assert output == "Por favor, ingrese un número par", \
            f"El número {numero} es impar, debe imprimir 'Por favor, ingrese un número par'"


class TestZero:
    """Special test for zero (is even)."""

    def test_cero_es_par(self, capture_main_output, student_module):
        """Verify that 0 is correctly identified as even."""
        output = capture_main_output("0", student_module)
        assert output == "Ha ingresado un número par", \
            "El número 0 es par"


class TestNegativeNumbers:
    """Tests with negative numbers."""

    @pytest.mark.parametrize("numero,esperado", [
        ("-2", "Ha ingresado un número par"),
        ("-4", "Ha ingresado un número par"),
        ("-1", "Por favor, ingrese un número par"),
        ("-3", "Por favor, ingrese un número par"),
        ("-100", "Ha ingresado un número par"),
        ("-99", "Por favor, ingrese un número par"),
    ])
    def test_numeros_negativos(self, capture_main_output, student_module, numero, esperado):
        """Test negative even and odd numbers."""
        output = capture_main_output(numero, student_module)
        assert output == esperado, \
            f"El número {numero} debe producir '{esperado}'"


class TestBoundaries:
    """Test boundary values."""

    @pytest.mark.parametrize("numero", ["2", "4", "6", "8"])
    def test_pares_pequenos(self, capture_main_output, student_module, numero):
        """Test small even numbers."""
        output = capture_main_output(numero, student_module)
        assert output == "Ha ingresado un número par"

    @pytest.mark.parametrize("numero", ["1", "3", "5", "7"])
    def test_impares_pequenos(self, capture_main_output, student_module, numero):
        """Test small odd numbers."""
        output = capture_main_output(numero, student_module)
        assert output == "Por favor, ingrese un número par"


class TestLargeNumbers:
    """Tests with large numbers."""

    @pytest.mark.parametrize("numero,esperado", [
        ("1000", "Ha ingresado un número par"),
        ("1001", "Por favor, ingrese un número par"),
        ("9998", "Ha ingresado un número par"),
        ("9999", "Por favor, ingrese un número par"),
    ])
    def test_numeros_grandes(self, capture_main_output, student_module, numero, esperado):
        """Test large even and odd numbers."""
        output = capture_main_output(numero, student_module)
        assert output == esperado
