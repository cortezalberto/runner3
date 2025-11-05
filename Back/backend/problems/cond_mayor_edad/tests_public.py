"""
Public tests for cond_mayor_edad problem.
Tests conditional logic for age verification (>18).
"""
import pytest


class TestFunctionExistence:
    """Tests to verify required function exists."""

    def test_main_function_exists(self, student_module):
        """Verify that the main() function is defined."""
        assert hasattr(student_module, 'main'), \
            'La función main() debe estar definida en el código'


class TestBasicCases:
    """Tests for basic mayor/menor de edad scenarios."""

    @pytest.mark.parametrize("edad,esperado", [
        ("20", "Es mayor de edad"),
        ("25", "Es mayor de edad"),
        ("30", "Es mayor de edad"),
        ("50", "Es mayor de edad"),
        ("19", "Es mayor de edad"),  # Just above boundary
    ])
    def test_mayor_de_edad(self, capture_main_output, student_module, edad, esperado):
        """Test ages that are greater than 18 (mayor de edad)."""
        output = capture_main_output(edad, student_module)
        assert output == esperado, \
            f"Con edad {edad}, se esperaba '{esperado}', se obtuvo '{output}'"

    @pytest.mark.parametrize("edad,esperado", [
        ("15", "Es menor de edad"),
        ("10", "Es menor de edad"),
        ("5", "Es menor de edad"),
        ("0", "Es menor de edad"),
        ("17", "Es menor de edad"),
    ])
    def test_menor_de_edad(self, capture_main_output, student_module, edad, esperado):
        """Test ages that are 18 or less (menor de edad)."""
        output = capture_main_output(edad, student_module)
        assert output == esperado, \
            f"Con edad {edad}, se esperaba '{esperado}', se obtuvo '{output}'"


class TestBoundaryValues:
    """Tests for critical boundary value (18)."""

    def test_edad_18_exacta(self, capture_main_output, student_module):
        """Test the exact boundary age of 18 (should be menor de edad)."""
        output = capture_main_output("18", student_module)
        assert output == "Es menor de edad", \
            "La edad 18 debe ser 'Es menor de edad' según el enunciado (> 18 para mayor)"

    def test_edad_19_limite_superior(self, capture_main_output, student_module):
        """Test age 19 (first age that is mayor de edad)."""
        output = capture_main_output("19", student_module)
        assert output == "Es mayor de edad", \
            "La edad 19 debe ser 'Es mayor de edad' (primera edad > 18)"

    def test_edad_17_limite_inferior(self, capture_main_output, student_module):
        """Test age 17 (clearly menor de edad)."""
        output = capture_main_output("17", student_module)
        assert output == "Es menor de edad", \
            "La edad 17 debe ser 'Es menor de edad'"


class TestExtremeValues:
    """Tests for extreme and edge case values."""

    def test_edad_muy_alta(self, capture_main_output, student_module):
        """Test very high age (100+)."""
        output = capture_main_output("100", student_module)
        assert output == "Es mayor de edad", \
            "Una edad muy alta (100) debe ser 'Es mayor de edad'"

    def test_edad_muy_baja(self, capture_main_output, student_module):
        """Test very low age (infant)."""
        output = capture_main_output("1", student_module)
        assert output == "Es menor de edad", \
            "Una edad muy baja (1) debe ser 'Es menor de edad'"

    def test_edad_cero(self, capture_main_output, student_module):
        """Test age zero (newborn)."""
        output = capture_main_output("0", student_module)
        assert output == "Es menor de edad", \
            "La edad 0 debe ser 'Es menor de edad'"

    def test_edad_adolescente(self, capture_main_output, student_module):
        """Test typical adolescent age."""
        output = capture_main_output("16", student_module)
        assert output == "Es menor de edad", \
            "La edad 16 debe ser 'Es menor de edad'"


class TestRangeValidation:
    """Test comprehensive age ranges."""

    @pytest.mark.parametrize("edad", ["19", "20", "21", "25", "30", "40", "60", "80"])
    def test_rango_mayores(self, capture_main_output, student_module, edad):
        """Test range of ages > 18."""
        output = capture_main_output(edad, student_module)
        assert output == "Es mayor de edad", \
            f"Edad {edad} (> 18) debe ser 'Es mayor de edad'"

    @pytest.mark.parametrize("edad", ["0", "1", "5", "10", "15", "17", "18"])
    def test_rango_menores(self, capture_main_output, student_module, edad):
        """Test range of ages <= 18."""
        output = capture_main_output(edad, student_module)
        assert output == "Es menor de edad", \
            f"Edad {edad} (<= 18) debe ser 'Es menor de edad'"
