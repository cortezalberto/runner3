"""
Public tests for sec_operaciones_basicas problem.
Tests basic arithmetic operations (suma, resta, multiplicación, división).
"""
import pytest


class TestFunctionExistence:
    """Tests to verify required function exists."""

    def test_main_function_exists(self, student_module):
        """Verify that the main() function is defined."""
        assert hasattr(student_module, 'main'), \
            'La función main() debe estar definida en el código'


class TestBasicOperations:
    """Tests for basic arithmetic operations."""

    def test_operaciones_10_y_2(self, capture_main_output, student_module):
        """Test operations with 10 and 2."""
        output = capture_main_output("10\n2", student_module)
        lines = output.strip().split('\n')
        assert len(lines) == 4, \
            f"Debe imprimir exactamente 4 líneas (una por operación), se obtuvieron {len(lines)}"

        # Verificar que contiene los resultados correctos
        assert "12" in output or "12.0" in output, "La suma de 10 + 2 debe ser 12"
        assert "8" in output or "8.0" in output, "La resta de 10 - 2 debe ser 8"
        assert "20" in output or "20.0" in output, "La multiplicación de 10 * 2 debe ser 20"
        assert "5" in output or "5.0" in output, "La división de 10 / 2 debe ser 5"

    def test_operaciones_6_y_3(self, capture_main_output, student_module):
        """Test operations with 6 and 3."""
        output = capture_main_output("6\n3", student_module)
        lines = output.strip().split('\n')
        assert len(lines) == 4

        assert "9" in output or "9.0" in output, "La suma de 6 + 3 debe ser 9"
        assert "3" in output or "3.0" in output, "La resta de 6 - 3 debe ser 3"
        assert "18" in output or "18.0" in output, "La multiplicación de 6 * 3 debe ser 18"
        assert "2" in output or "2.0" in output, "La división de 6 / 3 debe ser 2"


class TestOperationLabels:
    """Tests that operations are properly labeled."""

    def test_etiquetas_presentes(self, capture_main_output, student_module):
        """Test that each operation has a label."""
        output = capture_main_output("10\n5", student_module)

        # Verificar que cada operación tiene etiqueta (flexible con diferentes formatos)
        assert any(word in output.lower() for word in ["suma", "sum", "+"]), \
            "Debe etiquetar la suma"
        assert any(word in output.lower() for word in ["resta", "rest", "subtraction", "-"]), \
            "Debe etiquetar la resta"
        assert any(word in output.lower() for word in ["multiplicación", "multiplicacion", "mult", "*"]), \
            "Debe etiquetar la multiplicación"
        assert any(word in output.lower() for word in ["división", "division", "div", "/"]), \
            "Debe etiquetar la división"


class TestDifferentNumbers:
    """Tests with different number pairs."""

    @pytest.mark.parametrize("num1,num2", [
        ("15", "3"),
        ("20", "4"),
        ("100", "10"),
    ])
    def test_diferentes_numeros(self, capture_main_output, student_module, num1, num2):
        """Test with various number pairs."""
        output = capture_main_output(f"{num1}\n{num2}", student_module)
        n1, n2 = float(num1), float(num2)

        # Calcular resultados esperados
        suma = n1 + n2
        resta = n1 - n2
        mult = n1 * n2
        div = n1 / n2

        # Verificar que los resultados están presentes (flexibilidad con formatos)
        assert str(suma) in output or str(int(suma)) in output, \
            f"Debe mostrar la suma {suma}"
        assert str(resta) in output or str(int(resta)) in output, \
            f"Debe mostrar la resta {resta}"
        assert str(mult) in output or str(int(mult)) in output, \
            f"Debe mostrar la multiplicación {mult}"
        # División puede tener decimales, verificar primeros caracteres
        assert str(div)[:4] in output, \
            f"Debe mostrar la división (al menos primeros dígitos de {div})"


class TestDecimalResults:
    """Tests that produce decimal results."""

    def test_division_con_decimales(self, capture_main_output, student_module):
        """Test division that results in decimal."""
        output = capture_main_output("10\n3", student_module)

        # 10/3 = 3.333...
        assert "3.3" in output, \
            "La división 10/3 debe mostrar resultado decimal (aproximadamente 3.333)"

    def test_operaciones_con_decimales(self, capture_main_output, student_module):
        """Test operations with decimal inputs."""
        output = capture_main_output("5.5\n2.5", student_module)
        lines = output.strip().split('\n')
        assert len(lines) == 4

        # 5.5 + 2.5 = 8.0
        assert "8" in output or "8.0" in output
        # 5.5 - 2.5 = 3.0
        assert "3" in output or "3.0" in output


class TestOutputFormat:
    """Tests for output format validation."""

    def test_cuatro_lineas_exactas(self, capture_main_output, student_module):
        """Test that output has exactly 4 lines."""
        output = capture_main_output("8\n2", student_module)
        lines = output.strip().split('\n')
        assert len(lines) == 4, \
            f"La salida debe tener exactamente 4 líneas (suma, resta, multiplicación, división), se obtuvieron {len(lines)}"
