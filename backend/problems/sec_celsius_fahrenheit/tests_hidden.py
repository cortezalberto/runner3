"""
Hidden tests for sec_celsius_fahrenheit problem.
Tests edge cases and extreme temperatures.
"""
import pytest


class TestNegativeTemperatures:
    """Tests with negative (sub-zero) temperatures."""

    def test_temperatura_negativa(self, capture_main_output, student_module):
        """Test with negative temperature."""
        output = capture_main_output("-10", student_module)

        # F = (9/5) * (-10) + 32 = 14.0
        assert "-10" in output
        assert "14" in output or "14.0" in output, \
            "-10°C deben ser 14°F"

    def test_temperatura_muy_negativa(self, capture_main_output, student_module):
        """Test with very cold temperature."""
        output = capture_main_output("-40", student_module)

        # F = (9/5) * (-40) + 32 = -40.0 (¡único punto donde C = F!)
        assert "-40" in output, \
            "-40°C es igual a -40°F (punto de equivalencia)"

    @pytest.mark.parametrize("celsius,fahrenheit_esperado", [
        ("-5", "23"),
        ("-20", "-4"),
        ("-30", "-22"),
    ])
    def test_varias_temperaturas_negativas(self, capture_main_output, student_module, celsius, fahrenheit_esperado):
        """Test various negative temperatures."""
        output = capture_main_output(celsius, student_module)

        assert celsius in output
        # Verificar que el resultado está presente
        assert fahrenheit_esperado in output or f"{fahrenheit_esperado}.0" in output, \
            f"{celsius}°C deben ser {fahrenheit_esperado}°F"


class TestExtremeTemperatures:
    """Tests with extreme temperatures."""

    def test_temperatura_muy_alta(self, capture_main_output, student_module):
        """Test with very high temperature."""
        output = capture_main_output("200", student_module)

        # F = (9/5) * 200 + 32 = 392.0
        assert "200" in output
        assert "392" in output or "392.0" in output, \
            "200°C deben ser 392°F"

    def test_temperatura_cero_absoluto_aproximado(self, capture_main_output, student_module):
        """Test with temperature near absolute zero."""
        output = capture_main_output("-273", student_module)

        # F = (9/5) * (-273) + 32 = -459.4
        assert "-273" in output
        assert "-459" in output, \
            "Debe manejar temperaturas cercanas al cero absoluto"


class TestPrecisionCalculations:
    """Tests for calculation precision."""

    @pytest.mark.parametrize("celsius", ["12.5", "27.8", "33.3"])
    def test_precision_decimales(self, capture_main_output, student_module, celsius):
        """Test calculation precision with decimal values."""
        output = capture_main_output(celsius, student_module)

        c = float(celsius)
        f = (9/5) * c + 32

        # Verificar que el cálculo es correcto (con alguna tolerancia)
        assert str(c) in output or str(int(c)) in output
        # Verificar que el resultado Fahrenheit está presente
        f_str = str(f)[:5]  # Primeros 5 caracteres
        assert f_str in output or str(int(f)) in output


class TestBodyTemperatures:
    """Tests with human body temperature range."""

    def test_temperatura_corporal_normal(self, capture_main_output, student_module):
        """Test with normal body temperature."""
        output = capture_main_output("36.5", student_module)

        # F = (9/5) * 36.5 + 32 = 97.7
        assert "36.5" in output or "36" in output
        assert "97.7" in output or "97" in output, \
            "36.5°C es temperatura corporal normal"

    def test_temperatura_fiebre(self, capture_main_output, student_module):
        """Test with fever temperature."""
        output = capture_main_output("38.5", student_module)

        # F = (9/5) * 38.5 + 32 = 101.3
        assert "38.5" in output or "38" in output
        assert "101" in output, \
            "38.5°C indica fiebre"


class TestFormulaCorrectness:
    """Tests to ensure correct formula usage."""

    def test_formula_precision(self, capture_main_output, student_module):
        """Test that formula (9/5)*C + 32 is used correctly."""
        # Valores específicos para verificar la fórmula
        test_cases = [
            ("5", "41"),    # (9/5)*5 + 32 = 41
            ("15", "59"),   # (9/5)*15 + 32 = 59
            ("50", "122"),  # (9/5)*50 + 32 = 122
        ]

        for celsius, fahrenheit_esperado in test_cases:
            output = capture_main_output(celsius, student_module)
            assert fahrenheit_esperado in output or f"{fahrenheit_esperado}.0" in output, \
                f"Fórmula incorrecta: {celsius}°C deben ser {fahrenheit_esperado}°F"
