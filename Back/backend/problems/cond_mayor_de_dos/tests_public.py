"""
Public tests for cond_mayor_de_dos problem.
Tests conditional logic for finding the maximum of two numbers.
"""
import pytest


class TestFunctionExistence:
    """Tests to verify required function exists."""

    def test_main_function_exists(self, student_module):
        """Verify that the main() function is defined."""
        assert hasattr(student_module, 'main'), \
            'La función main() debe estar definida en el código'


class TestBasicComparisons:
    """Tests for basic number comparisons."""

    @pytest.mark.parametrize("a,b,esperado", [
        ("10\n5", "10"),
        ("20\n15", "20"),
        ("100\n50", "100"),
        ("7\n3", "7"),
    ])
    def test_primer_numero_mayor(self, capture_main_output, student_module, a, b, esperado):
        """Test cases where the first number is greater."""
        output = capture_main_output(a, student_module)
        # Accept both integer and float representations
        assert output == esperado or output == f"{esperado}.0", \
            f"Con entrada {a.replace(chr(10), ', ')}, se esperaba '{esperado}', se obtuvo '{output}'"

    @pytest.mark.parametrize("a,b,esperado", [
        ("3\n8", "8"),
        ("5\n10", "10"),
        ("15\n20", "20"),
        ("50\n100", "100"),
    ])
    def test_segundo_numero_mayor(self, capture_main_output, student_module, a, b, esperado):
        """Test cases where the second number is greater."""
        output = capture_main_output(a, student_module)
        assert output == esperado or output == f"{esperado}.0", \
            f"Con entrada {a.replace(chr(10), ', ')}, se esperaba '{esperado}', se obtuvo '{output}'"


class TestEqualNumbers:
    """Tests for equal number cases."""

    @pytest.mark.parametrize("numero", ["5", "10", "0", "100", "-5"])
    def test_numeros_iguales(self, capture_main_output, student_module, numero):
        """Test when both numbers are equal (can return either)."""
        entrada = f"{numero}\n{numero}"
        output = capture_main_output(entrada, student_module)
        assert output == numero or output == f"{numero}.0", \
            f"Con números iguales ({numero}), debe retornar {numero}"


class TestDecimalNumbers:
    """Tests with decimal numbers."""

    @pytest.mark.parametrize("a,b", [
        ("3.5\n2.1", "3.5"),
        ("7.8\n9.2", "9.2"),
        ("1.5\n1.5", "1.5"),
        ("10.75\n10.25", "10.75"),
    ])
    def test_decimales(self, capture_main_output, student_module, a, b):
        """Test decimal number comparisons."""
        output = capture_main_output(a, student_module)
        output_float = float(output)
        expected_float = float(b)
        assert abs(output_float - expected_float) < 0.01, \
            f"Con entrada {a.replace(chr(10), ', ')}, se esperaba '{b}', se obtuvo '{output}'"


class TestNegativeNumbers:
    """Tests with negative numbers."""

    @pytest.mark.parametrize("a,b,esperado", [
        ("-5\n-10", "-5"),
        ("-10\n-5", "-5"),
        ("-3\n2", "2"),
        ("2\n-3", "2"),
        ("-100\n-50", "-50"),
    ])
    def test_numeros_negativos(self, capture_main_output, student_module, a, b, esperado):
        """Test comparisons with negative numbers."""
        output = capture_main_output(a, student_module)
        output_float = float(output)
        expected_float = float(esperado)
        assert abs(output_float - expected_float) < 0.01, \
            f"Con entrada {a.replace(chr(10), ', ')}, se esperaba '{esperado}', se obtuvo '{output}'"


class TestZeroComparisons:
    """Tests involving zero."""

    @pytest.mark.parametrize("a,b,esperado", [
        ("0\n-5", "0"),
        ("3\n0", "3"),
        ("0\n0", "0"),
        ("-10\n0", "0"),
    ])
    def test_con_cero(self, capture_main_output, student_module, a, b, esperado):
        """Test comparisons involving zero."""
        output = capture_main_output(a, student_module)
        assert output == esperado or output == f"{esperado}.0", \
            f"Con entrada {a.replace(chr(10), ', ')}, se esperaba '{esperado}', se obtuvo '{output}'"


class TestExtremeValues:
    """Tests with extreme values."""

    @pytest.mark.parametrize("a,b,esperado", [
        ("1000\n999", "1000"),
        ("999999\n1000000", "1000000"),
        ("-1000\n-999", "-999"),
    ])
    def test_valores_extremos(self, capture_main_output, student_module, a, b, esperado):
        """Test with very large or very small numbers."""
        output = capture_main_output(a, student_module)
        output_float = float(output)
        expected_float = float(esperado)
        assert abs(output_float - expected_float) < 0.01, \
            f"Con entrada {a.replace(chr(10), ', ')}, se esperaba '{esperado}', se obtuvo '{output}'"
