"""
Hidden tests for sec_circulo problem.
Tests advanced scenarios and precision.
"""
import pytest
import math


class TestPrecision:
    """Tests for calculation precision."""

    @pytest.mark.parametrize("radio", ["1.5", "7.3", "9.8"])
    def test_precision_decimales(self, capture_main_output, student_module, radio):
        """Test precision with decimal radius."""
        output = capture_main_output(radio, student_module)
        lines = output.strip().split('\n')

        r = float(radio)
        area = float(lines[0])
        perimetro = float(lines[1])
        area_esperada = math.pi * r ** 2
        perimetro_esperado = 2 * math.pi * r

        assert abs(area - area_esperada) < 0.001, \
            f"Precisión insuficiente en área para radio {radio}"
        assert abs(perimetro - perimetro_esperado) < 0.001, \
            f"Precisión insuficiente en perímetro para radio {radio}"


class TestLargeValues:
    """Tests with very large values."""

    def test_radio_muy_grande(self, capture_main_output, student_module):
        """Test with very large radius."""
        output = capture_main_output("1000", student_module)
        lines = output.strip().split('\n')

        area = float(lines[0])
        perimetro = float(lines[1])
        area_esperada = math.pi * 1000000
        perimetro_esperado = 2000 * math.pi

        assert abs(area - area_esperada) < 10, \
            f"Área con radio 1000 incorrecta"
        assert abs(perimetro - perimetro_esperado) < 1, \
            f"Perímetro con radio 1000 incorrecto"


class TestSmallValues:
    """Tests with very small values."""

    @pytest.mark.parametrize("radio", ["0.1", "0.01", "0.5"])
    def test_radios_pequenos(self, capture_main_output, student_module, radio):
        """Test with small radius values."""
        output = capture_main_output(radio, student_module)
        lines = output.strip().split('\n')

        r = float(radio)
        area = float(lines[0])
        perimetro = float(lines[1])
        area_esperada = math.pi * r ** 2
        perimetro_esperado = 2 * math.pi * r

        assert abs(area - area_esperada) < 0.0001, \
            f"Área incorrecta para radio pequeño {radio}"
        assert abs(perimetro - perimetro_esperado) < 0.0001, \
            f"Perímetro incorrecto para radio pequeño {radio}"
