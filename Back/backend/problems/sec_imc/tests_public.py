"""
Public tests for sec_imc problem.
Tests BMI (Body Mass Index) calculation.
"""
import pytest


class TestFunctionExistence:
    """Tests to verify required function exists."""

    def test_main_function_exists(self, student_module):
        """Verify that the main() function is defined."""
        assert hasattr(student_module, 'main'), \
            'La función main() debe estar definida en el código'


class TestBasicIMC:
    """Tests for basic IMC calculations."""

    def test_imc_ejemplo(self, capture_main_output, student_module):
        """Test with example from prompt (1.75m, 70kg)."""
        output = capture_main_output("1.75\n70", student_module)

        # IMC = 70 / (1.75 ** 2) = 22.857...
        assert "22.86" in output, \
            "Con altura 1.75m y peso 70kg, el IMC debe ser 22.86"
        assert "imc" in output.lower(), \
            "Debe mencionar 'IMC' en el mensaje"

    def test_imc_valor_bajo(self, capture_main_output, student_module):
        """Test with low BMI value."""
        output = capture_main_output("1.80\n60", student_module)

        # IMC = 60 / (1.80 ** 2) = 18.518...
        assert "18.52" in output or "18.51" in output, \
            "Con altura 1.80m y peso 60kg, el IMC debe ser aproximadamente 18.52"

    def test_imc_valor_alto(self, capture_main_output, student_module):
        """Test with high BMI value."""
        output = capture_main_output("1.65\n85", student_module)

        # IMC = 85 / (1.65 ** 2) = 31.221...
        assert "31.22" in output or "31.21" in output, \
            "Con altura 1.65m y peso 85kg, el IMC debe ser aproximadamente 31.22"


class TestDecimalFormat:
    """Tests for output format with 2 decimals."""

    def test_formato_dos_decimales(self, capture_main_output, student_module):
        """Test that output has exactly 2 decimal places."""
        output = capture_main_output("1.70\n65", student_module)

        # IMC = 65 / (1.70 ** 2) = 22.491...
        assert "22.49" in output, \
            "El IMC debe mostrarse con exactamente 2 decimales"

    @pytest.mark.parametrize("altura,peso", [
        ("1.60", "55"),
        ("1.90", "90"),
        ("1.75", "80"),
    ])
    def test_varios_casos_formato(self, capture_main_output, student_module, altura, peso):
        """Test format with various height/weight combinations."""
        output = capture_main_output(f"{altura}\n{peso}", student_module)

        # Calcular IMC esperado
        h = float(altura)
        p = float(peso)
        imc = p / (h ** 2)

        # Verificar que el IMC está presente con formato correcto
        imc_str = f"{imc:.2f}"
        assert imc_str in output, \
            f"Con altura {altura}m y peso {peso}kg, el IMC debe ser {imc_str}"


class TestOutputMessage:
    """Tests for output message format."""

    def test_mensaje_completo(self, capture_main_output, student_module):
        """Test that output contains expected message format."""
        output = capture_main_output("1.75\n70", student_module)

        # Debe contener las palabras clave del mensaje
        assert "indice" in output.lower() or "índice" in output.lower(), \
            "Debe mencionar 'índice' en el mensaje"
        assert "masa" in output.lower(), \
            "Debe mencionar 'masa' en el mensaje"
        assert "corporal" in output.lower(), \
            "Debe mencionar 'corporal' en el mensaje"


class TestEdgeCases:
    """Tests for edge cases."""

    def test_altura_baja(self, capture_main_output, student_module):
        """Test with short height."""
        output = capture_main_output("1.50\n50", student_module)

        # IMC = 50 / (1.50 ** 2) = 22.222...
        assert "22.22" in output, \
            "Debe calcular correctamente con alturas bajas"

    def test_altura_alta(self, capture_main_output, student_module):
        """Test with tall height."""
        output = capture_main_output("2.00\n100", student_module)

        # IMC = 100 / (2.00 ** 2) = 25.0
        assert "25.00" in output or "25.0" in output, \
            "Debe calcular correctamente con alturas altas"
