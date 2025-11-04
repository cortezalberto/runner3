"""
Public tests for sec_circulo problem.
Tests circle area and perimeter calculations.
"""
import pytest
import math


class TestFunctionExistence:
    """Tests to verify required function exists."""

    def test_main_function_exists(self, student_module):
        """Verify that the main() function is defined."""
        assert hasattr(student_module, 'main'), \
            'La función main() debe estar definida en el código'


class TestBasicCalculations:
    """Tests for basic circle calculations."""

    def test_radio_uno(self, capture_main_output, student_module):
        """Test with radius = 1."""
        output = capture_main_output("1", student_module)
        lines = output.strip().split('\n')
        assert len(lines) == 2, \
            f"Debe imprimir exactamente 2 líneas (área y perímetro), se obtuvieron {len(lines)}"

        area = float(lines[0])
        perimetro = float(lines[1])

        assert abs(area - math.pi) < 0.01, \
            f"Área con radio 1 debe ser π ({math.pi}), se obtuvo {area}"
        assert abs(perimetro - 2 * math.pi) < 0.01, \
            f"Perímetro con radio 1 debe ser 2π ({2 * math.pi}), se obtuvo {perimetro}"

    def test_radio_cinco(self, capture_main_output, student_module):
        """Test with radius = 5."""
        output = capture_main_output("5", student_module)
        lines = output.strip().split('\n')

        area = float(lines[0])
        perimetro = float(lines[1])
        area_esperada = math.pi * 25
        perimetro_esperado = 10 * math.pi

        assert abs(area - area_esperada) < 0.01, \
            f"Área con radio 5 debe ser {area_esperada}, se obtuvo {area}"
        assert abs(perimetro - perimetro_esperado) < 0.01, \
            f"Perímetro con radio 5 debe ser {perimetro_esperado}, se obtuvo {perimetro}"


class TestDecimalRadius:
    """Tests with decimal radius values."""

    @pytest.mark.parametrize("radio", ["2.5", "3.7", "4.2"])
    def test_radios_decimales(self, capture_main_output, student_module, radio):
        """Test with decimal radius values."""
        output = capture_main_output(radio, student_module)
        lines = output.strip().split('\n')
        assert len(lines) == 2, \
            f"Debe imprimir 2 líneas, se obtuvieron {len(lines)}"

        r = float(radio)
        area = float(lines[0])
        perimetro = float(lines[1])
        area_esperada = math.pi * r ** 2
        perimetro_esperado = 2 * math.pi * r

        assert abs(area - area_esperada) < 0.01, \
            f"Área incorrecta para radio {radio}"
        assert abs(perimetro - perimetro_esperado) < 0.01, \
            f"Perímetro incorrecto para radio {radio}"


class TestEdgeCases:
    """Tests for edge cases."""

    def test_radio_cero(self, capture_main_output, student_module):
        """Test with radius = 0."""
        output = capture_main_output("0", student_module)
        lines = output.strip().split('\n')

        area = float(lines[0])
        perimetro = float(lines[1])

        assert area == 0, \
            f"Área con radio 0 debe ser 0, se obtuvo {area}"
        assert perimetro == 0, \
            f"Perímetro con radio 0 debe ser 0, se obtuvo {perimetro}"

    def test_radio_grande(self, capture_main_output, student_module):
        """Test with large radius."""
        output = capture_main_output("100", student_module)
        lines = output.strip().split('\n')

        area = float(lines[0])
        perimetro = float(lines[1])
        area_esperada = math.pi * 10000
        perimetro_esperado = 200 * math.pi

        assert abs(area - area_esperada) < 1, \
            f"Área con radio 100 debe ser aproximadamente {area_esperada}"
        assert abs(perimetro - perimetro_esperado) < 1, \
            f"Perímetro con radio 100 debe ser aproximadamente {perimetro_esperado}"


class TestOutputFormat:
    """Tests for output format validation."""

    def test_dos_lineas_salida(self, capture_main_output, student_module):
        """Test that output has exactly 2 lines."""
        output = capture_main_output("3", student_module)
        lines = output.strip().split('\n')
        assert len(lines) == 2, \
            f"La salida debe tener exactamente 2 líneas (área y perímetro), se obtuvieron {len(lines)}"

    def test_valores_numericos(self, capture_main_output, student_module):
        """Test that output values are numeric."""
        output = capture_main_output("2", student_module)
        lines = output.strip().split('\n')

        try:
            float(lines[0])
            float(lines[1])
        except ValueError:
            pytest.fail(f"Las salidas deben ser números válidos, se obtuvo: {output}")
