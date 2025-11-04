"""
Public tests for sec_celsius_fahrenheit problem.
Tests temperature conversion from Celsius to Fahrenheit.
"""
import pytest


class TestFunctionExistence:
    """Tests to verify required function exists."""

    def test_main_function_exists(self, student_module):
        """Verify that the main() function is defined."""
        assert hasattr(student_module, 'main'), \
            'La función main() debe estar definida en el código'


class TestBasicConversions:
    """Tests for basic temperature conversions."""

    def test_conversion_ejemplo(self, capture_main_output, student_module):
        """Test with example from prompt (25°C)."""
        output = capture_main_output("25", student_module)

        # F = (9/5) * 25 + 32 = 77.0
        assert "25" in output, "Debe mencionar la temperatura en Celsius"
        assert "77" in output or "77.0" in output, \
            "25°C deben ser 77°F"
        assert "°C" in output or "C" in output, \
            "Debe incluir símbolo de Celsius"
        assert "°F" in output or "F" in output, \
            "Debe incluir símbolo de Fahrenheit"

    def test_conversion_cero(self, capture_main_output, student_module):
        """Test with 0°C (freezing point)."""
        output = capture_main_output("0", student_module)

        # F = (9/5) * 0 + 32 = 32.0
        assert "0" in output, "Debe mencionar 0°C"
        assert "32" in output or "32.0" in output, \
            "0°C deben ser 32°F (punto de congelación del agua)"

    def test_conversion_100(self, capture_main_output, student_module):
        """Test with 100°C (boiling point)."""
        output = capture_main_output("100", student_module)

        # F = (9/5) * 100 + 32 = 212.0
        assert "100" in output, "Debe mencionar 100°C"
        assert "212" in output or "212.0" in output, \
            "100°C deben ser 212°F (punto de ebullición del agua)"


class TestVariousTemperatures:
    """Tests with various temperature values."""

    @pytest.mark.parametrize("celsius,fahrenheit_esperado", [
        ("10", "50"),
        ("20", "68"),
        ("30", "86"),
        ("37", "98.6"),
    ])
    def test_conversiones_varias(self, capture_main_output, student_module, celsius, fahrenheit_esperado):
        """Test various temperature conversions."""
        output = capture_main_output(celsius, student_module)

        assert celsius in output, f"Debe mencionar {celsius}°C"
        # Verificar que el resultado está presente (puede variar en decimales)
        assert fahrenheit_esperado[:2] in output, \
            f"{celsius}°C deben ser aproximadamente {fahrenheit_esperado}°F"


class TestOutputFormat:
    """Tests for output format validation."""

    def test_formato_incluye_equivalen(self, capture_main_output, student_module):
        """Test that output includes 'equivalen'."""
        output = capture_main_output("25", student_module)
        assert "equivalen" in output.lower(), \
            "Debe incluir la palabra 'equivalen' en el mensaje"

    def test_formato_completo(self, capture_main_output, student_module):
        """Test complete output format."""
        output = capture_main_output("15", student_module)

        # Debe contener: temperatura Celsius, equivalen, temperatura Fahrenheit
        assert "15" in output
        assert "59" in output  # 15°C = 59°F
        assert "equivalen" in output.lower()


class TestDecimalValues:
    """Tests with decimal input values."""

    def test_temperatura_decimal(self, capture_main_output, student_module):
        """Test with decimal temperature."""
        output = capture_main_output("23.5", student_module)

        # F = (9/5) * 23.5 + 32 = 74.3
        assert "23.5" in output or "23" in output
        assert "74.3" in output or "74" in output, \
            "Debe calcular correctamente con temperaturas decimales"

    @pytest.mark.parametrize("celsius", ["10.5", "36.5", "18.8"])
    def test_varias_decimales(self, capture_main_output, student_module, celsius):
        """Test various decimal temperatures."""
        output = capture_main_output(celsius, student_module)

        c = float(celsius)
        f = (9/5) * c + 32

        # Verificar que el valor calculado está presente
        assert str(c) in output or str(int(c)) in output
        # Verificar aproximación del resultado Fahrenheit
        assert str(f)[:4] in output or str(int(f)) in output
