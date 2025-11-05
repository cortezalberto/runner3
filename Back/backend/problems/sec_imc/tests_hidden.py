"""
Hidden tests for sec_imc problem.
Tests advanced scenarios and edge cases.
"""
import pytest


class TestExtremeValues:
    """Tests with extreme values."""

    def test_imc_muy_bajo(self, capture_main_output, student_module):
        """Test with very low BMI."""
        output = capture_main_output("1.80\n45", student_module)

        # IMC = 45 / (1.80 ** 2) = 13.888...
        assert "13.89" in output or "13.88" in output, \
            "Debe calcular correctamente IMC muy bajo"

    def test_imc_muy_alto(self, capture_main_output, student_module):
        """Test with very high BMI."""
        output = capture_main_output("1.60\n100", student_module)

        # IMC = 100 / (1.60 ** 2) = 39.062...
        assert "39.06" in output or "39.07" in output, \
            "Debe calcular correctamente IMC muy alto"


class TestDecimalPrecision:
    """Tests for decimal precision in calculations."""

    @pytest.mark.parametrize("altura,peso,imc_esperado", [
        ("1.73", "68", "22.72"),
        ("1.82", "75", "22.64"),
        ("1.68", "62", "21.97"),
    ])
    def test_precision_calculo(self, capture_main_output, student_module, altura, peso, imc_esperado):
        """Test calculation precision with various inputs."""
        output = capture_main_output(f"{altura}\n{peso}", student_module)

        # Verificar que el IMC calculado es correcto
        assert imc_esperado in output, \
            f"Con altura {altura}m y peso {peso}kg, el IMC debe ser {imc_esperado}"


class TestUnusualHeights:
    """Tests with unusual but valid heights."""

    def test_altura_muy_baja(self, capture_main_output, student_module):
        """Test with very short height."""
        output = capture_main_output("1.40\n45", student_module)

        # IMC = 45 / (1.40 ** 2) = 22.959...
        assert "22.96" in output or "22.95" in output, \
            "Debe calcular correctamente con alturas muy bajas"

    def test_altura_muy_alta(self, capture_main_output, student_module):
        """Test with very tall height."""
        output = capture_main_output("2.10\n105", student_module)

        # IMC = 105 / (2.10 ** 2) = 23.809...
        assert "23.81" in output or "23.80" in output, \
            "Debe calcular correctamente con alturas muy altas"


class TestRoundingEdgeCases:
    """Tests for rounding edge cases."""

    def test_redondeo_hacia_arriba(self, capture_main_output, student_module):
        """Test rounding up."""
        output = capture_main_output("1.75\n72", student_module)

        # IMC = 72 / (1.75 ** 2) = 23.510...
        assert "23.51" in output, \
            "Debe redondear correctamente hacia arriba"

    def test_redondeo_hacia_abajo(self, capture_main_output, student_module):
        """Test rounding down."""
        output = capture_main_output("1.75\n69", student_module)

        # IMC = 69 / (1.75 ** 2) = 22.530...
        assert "22.53" in output, \
            "Debe redondear correctamente hacia abajo"


class TestWeightVariations:
    """Tests with different weight values for same height."""

    def test_mismo_altura_diferentes_pesos(self, capture_main_output, student_module):
        """Test same height with different weights."""
        # Altura fija: 1.70m
        # Peso 1: 55kg
        output1 = capture_main_output("1.70\n55", student_module)
        # IMC = 55 / (1.70 ** 2) = 19.031...
        assert "19.03" in output1

        # Peso 2: 85kg
        output2 = capture_main_output("1.70\n85", student_module)
        # IMC = 85 / (1.70 ** 2) = 29.411...
        assert "29.41" in output2
