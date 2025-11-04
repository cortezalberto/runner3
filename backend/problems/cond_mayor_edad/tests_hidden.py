"""
Hidden tests for cond_mayor_edad problem.
Tests advanced scenarios and edge cases.
"""
import pytest


class TestExtendedBoundaries:
    """Extended boundary testing around age 18."""

    @pytest.mark.parametrize("edad,esperado", [
        ("18", "Es menor de edad"),  # Exact boundary (<=18)
        ("19", "Es mayor de edad"),   # Just above
        ("20", "Es mayor de edad"),
        ("21", "Es mayor de edad"),
    ])
    def test_boundary_precision(self, capture_main_output, student_module, edad, esperado):
        """Test precise boundary behavior around 18."""
        output = capture_main_output(edad, student_module)
        assert output == esperado, \
            f"Con edad {edad}, se esperaba '{esperado}', se obtuvo '{output}'"


class TestExtremeLimits:
    """Test extreme age values."""

    @pytest.mark.parametrize("edad", ["120", "150", "200", "999"])
    def test_edades_muy_altas(self, capture_main_output, student_module, edad):
        """Test extremely high ages."""
        output = capture_main_output(edad, student_module)
        assert output == "Es mayor de edad", \
            f"Edad {edad} (extremadamente alta) debe ser 'Es mayor de edad'"

    def test_edad_maxima_razonable(self, capture_main_output, student_module):
        """Test maximum reasonable human age."""
        output = capture_main_output("122", student_module)  # Record mundial aproximado
        assert output == "Es mayor de edad", \
            "La edad máxima humana razonable debe ser 'Es mayor de edad'"


class TestAdolescentRange:
    """Test complete adolescent age range."""

    @pytest.mark.parametrize("edad", ["13", "14", "15", "16", "17", "18"])
    def test_adolescentes(self, capture_main_output, student_module, edad):
        """Test all adolescent ages (13-18)."""
        output = capture_main_output(edad, student_module)
        assert output == "Es menor de edad", \
            f"Edad {edad} (adolescente) debe ser 'Es menor de edad'"


class TestChildRange:
    """Test childhood age range."""

    @pytest.mark.parametrize("edad", ["1", "3", "5", "7", "9", "11", "12"])
    def test_ninos(self, capture_main_output, student_module, edad):
        """Test childhood ages (1-12)."""
        output = capture_main_output(edad, student_module)
        assert output == "Es menor de edad", \
            f"Edad {edad} (niñez) debe ser 'Es menor de edad'"


class TestAdultRange:
    """Test adult age range comprehensively."""

    @pytest.mark.parametrize("edad", ["19", "22", "25", "30", "35", "40", "50", "60", "70"])
    def test_adultos(self, capture_main_output, student_module, edad):
        """Test various adult ages (19-70)."""
        output = capture_main_output(edad, student_module)
        assert output == "Es mayor de edad", \
            f"Edad {edad} (adulto) debe ser 'Es mayor de edad'"

    @pytest.mark.parametrize("edad", ["71", "75", "80", "85", "90", "95", "100"])
    def test_adultos_mayores(self, capture_main_output, student_module, edad):
        """Test senior citizen ages (70+)."""
        output = capture_main_output(edad, student_module)
        assert output == "Es mayor de edad", \
            f"Edad {edad} (adulto mayor) debe ser 'Es mayor de edad'"


class TestBoundaryConsistency:
    """Ensure consistent behavior around boundaries."""

    def test_consistency_below_boundary(self, capture_main_output, student_module):
        """Test multiple calls with ages below 18."""
        test_ages = ["0", "5", "10", "15", "18"]
        for edad in test_ages:
            output = capture_main_output(edad, student_module)
            assert output == "Es menor de edad", \
                f"Edad {edad} debe consistentemente ser 'Es menor de edad'"

    def test_consistency_above_boundary(self, capture_main_output, student_module):
        """Test multiple calls with ages above 18."""
        test_ages = ["19", "25", "40", "60", "100"]
        for edad in test_ages:
            output = capture_main_output(edad, student_module)
            assert output == "Es mayor de edad", \
                f"Edad {edad} debe consistentemente ser 'Es mayor de edad'"
