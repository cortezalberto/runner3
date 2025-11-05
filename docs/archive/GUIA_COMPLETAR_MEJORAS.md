# 📘 Guía para Completar Mejoras de Tests en Problemas Condicionales

Esta guía te ayudará a completar las mejoras de tests para los 5 problemas condicionales restantes usando los mismos patrones aplicados en los 4 ya completados.

---

## ✅ Estado Actual

### Completados (4/9):
1. ✅ **cond_aprobado** - Tests públicos y hidden mejorados
2. ✅ **cond_mayor_edad** - Tests públicos y hidden mejorados
3. ✅ **cond_mayor_de_dos** - Tests públicos mejorados
4. ✅ **cond_numero_par** - Tests públicos mejorados

### Pendientes (5/9):
5. ⏳ **cond_categorias_edad**
6. ⏳ **cond_termina_vocal**
7. ⏳ **cond_terremoto**
8. ⏳ **cond_transformar_nombre**
9. ⏳ **cond_validar_password**

**Nota**: Todos tienen `conftest.py` ya desplegado ✅

---

## 🎯 Patrón a Seguir

### Paso 1: Analizar el Problema

Lee el `prompt.md` y el `starter.py` para entender:
- ¿Qué función debe existir? (main() o función específica)
- ¿Qué entradas acepta?
- ¿Qué salidas produce?
- ¿Cuáles son los casos límite?

### Paso 2: Identificar Casos de Prueba

Categoriza los tests en:
1. **TestFunctionExistence** - Verifica que la función existe
2. **TestBasicCases** - Casos comunes de uso
3. **TestBoundaryValues** - Valores límite críticos
4. **TestEdgeCases** - Casos especiales
5. **TestExtremeValues** - Valores extremos

### Paso 3: Usar Parametrización

```python
@pytest.mark.parametrize("entrada,esperado", [
    (caso1, resultado1),
    (caso2, resultado2),
    ...
])
def test_categoria(self, fixture, student_module, entrada, esperado):
    # Test logic
    pass
```

### Paso 4: Escribir Mensajes Descriptivos

```python
assert output == esperado, \
    f"Con entrada {entrada}, se esperaba '{esperado}', se obtuvo '{output}'"
```

---

## 📋 Plantilla para Tests Públicos

```python
"""
Public tests for [PROBLEM_ID] problem.
Tests [BRIEF_DESCRIPTION].
"""
import pytest


class TestFunctionExistence:
    """Tests to verify required function exists."""

    def test_[function_name]_exists(self, student_module):
        """Verify that the [function_name]() function is defined."""
        assert hasattr(student_module, '[function_name]'), \
            'La función [function_name]() debe estar definida en el código'


class TestBasicCases:
    """Tests for basic scenarios."""

    @pytest.mark.parametrize("param,esperado", [
        # Add test cases here
    ])
    def test_basic(self, capture_main_output, student_module, param, esperado):
        """Test basic cases."""
        # For main() functions using stdin:
        output = capture_main_output(param, student_module)

        # OR for regular functions:
        # output = student_module.function_name(param)

        assert output == esperado, \
            f"Con entrada {param}, se esperaba '{esperado}', se obtuvo '{output}'"


class TestBoundaryValues:
    """Tests for boundary values (edge cases)."""

    def test_boundary_case(self, capture_main_output, student_module):
        """Test critical boundary value."""
        # Add boundary test logic
        pass


class TestEdgeCases:
    """Tests for special edge cases."""

    @pytest.mark.parametrize("param,esperado", [
        # Add edge cases
    ])
    def test_edge_cases(self, capture_main_output, student_module, param, esperado):
        """Test edge cases."""
        # Test logic
        pass
```

---

## 🔧 Problemas Específicos - Guía Rápida

### 5. cond_categorias_edad

**Función**: `main()` (lee stdin, imprime stdout)
**Lógica**: Clasifica edad en categorías (> 18 → mayor, ≤ 18 → menor)

**Casos de prueba sugeridos:**
```python
# Boundary values
("18", "No es mayor de edad")  # Límite exacto
("19", "Es mayor de edad")      # Justo arriba
("17", "No es mayor de edad")   # Justo debajo

# Basic cases
@pytest.mark.parametrize("edad,esperado", [
    ("0", "No es mayor de edad"),
    ("10", "No es mayor de edad"),
    ("18", "No es mayor de edad"),
    ("19", "Es mayor de edad"),
    ("25", "Es mayor de edad"),
    ("100", "Es mayor de edad"),
])

# Edge cases
("0", "No es mayor de edad")    # Mínimo
("200", "Es mayor de edad")      # Muy alto
```

**Advertencia**: El enunciado dice "mayor de 18" (> 18), no "mayor o igual".

---

### 6. cond_termina_vocal

**Función**: `procesar_string(texto)` (función regular, NO main)
**Lógica**: Si termina en vocal → agregar "!", sino → sin cambios

**Fixture a usar**: `call_function` o directamente `student_module.procesar_string()`

**Casos de prueba sugeridos:**
```python
class TestFunctionExistence:
    def test_procesar_string_exists(self, student_module):
        assert hasattr(student_module, 'procesar_string')

class TestBasicCases:
    @pytest.mark.parametrize("texto,esperado", [
        ("casa", "casa!"),      # Termina en 'a' minúscula
        ("papel", "papel"),     # No termina en vocal
        ("Chile", "Chile!"),    # Termina en 'e' mayúscula
        ("amor", "amor"),       # Termina en 'r'
    ])
    def test_basic(self, student_module, texto, esperado):
        output = student_module.procesar_string(texto)
        assert output == esperado

class TestVowelVariations:
    @pytest.mark.parametrize("texto,esperado", [
        ("A", "A!"),            # Solo vocal mayúscula
        ("a", "a!"),            # Solo vocal minúscula
        ("E", "E!"),
        ("I", "I!"),
        ("O", "O!"),
        ("U", "U!"),
    ])
    def test_all_vowels(self, student_module, texto, esperado):
        output = student_module.procesar_string(texto)
        assert output == esperado

class TestEdgeCases:
    @pytest.mark.parametrize("texto,esperado", [
        ("", ""),               # String vacío (si aplica)
        ("auto", "auto!"),      # Termina en 'o'
        ("MESA", "MESA!"),      # Mayúsculas
        ("AbCdE", "AbCdE!"),    # Mixto, termina vocal
        ("XyZ", "XyZ"),         # No termina vocal
    ])
    def test_edge_cases(self, student_module, texto, esperado):
        output = student_module.procesar_string(texto)
        assert output == esperado
```

---

### 7. cond_terremoto

**Función**: `clasificar_terremoto(magnitud)` (función regular)
**Lógica**: Escala de Richter con 6 categorías

**Rangos críticos:**
- < 3: "Muy leve"
- 3-4: "Leve"
- 4-5: "Moderado"
- 5-6: "Fuerte"
- 6-7: "Muy Fuerte"
- ≥ 7: "Extremo"

**Casos de prueba sugeridos:**
```python
class TestBoundaryValues:
    """Tests for exact boundaries."""

    @pytest.mark.parametrize("magnitud,esperado", [
        (3.0, "Leve"),          # Límite 3 exacto
        (2.99, "Muy leve"),     # Justo debajo
        (3.01, "Leve"),         # Justo arriba
        (4.0, "Moderado"),      # Límite 4
        (5.0, "Fuerte"),        # Límite 5
        (6.0, "Muy Fuerte"),    # Límite 6
        (7.0, "Extremo"),       # Límite 7
    ])
    def test_boundaries(self, student_module, magnitud, esperado):
        output = student_module.clasificar_terremoto(magnitud)
        assert output == esperado

class TestRanges:
    """Test each range category."""

    @pytest.mark.parametrize("magnitud", [0, 1, 2, 2.5, 2.9])
    def test_muy_leve_range(self, student_module, magnitud):
        output = student_module.clasificar_terremoto(magnitud)
        assert output == "Muy leve"

    @pytest.mark.parametrize("magnitud", [3.0, 3.3, 3.7, 3.9])
    def test_leve_range(self, student_module, magnitud):
        output = student_module.clasificar_terremoto(magnitud)
        assert output == "Leve"

    # ... similar para otros rangos

class TestExtremes:
    @pytest.mark.parametrize("magnitud,esperado", [
        (0.1, "Muy leve"),      # Mínimo
        (10.0, "Extremo"),      # Muy alto
        (9.5, "Extremo"),       # Chile 1960
    ])
    def test_extremes(self, student_module, magnitud, esperado):
        output = student_module.clasificar_terremoto(magnitud)
        assert output == esperado
```

---

### 8. cond_transformar_nombre

**Función**: `transformar_nombre(nombre, opcion)` (función regular)
**Lógica**: 1=upper(), 2=lower(), 3=title(), otro="Opción inválida"

**Casos de prueba sugeridos:**
```python
class TestBasicTransformations:
    @pytest.mark.parametrize("nombre,opcion,esperado", [
        ("pedro", 1, "PEDRO"),
        ("MARIA", 2, "maria"),
        ("juan", 3, "Juan"),
        ("ANA MARIA", 3, "Ana Maria"),  # title() capitaliza cada palabra
    ])
    def test_valid_options(self, student_module, nombre, opcion, esperado):
        output = student_module.transformar_nombre(nombre, opcion)
        assert output == esperado

class TestInvalidOptions:
    @pytest.mark.parametrize("nombre,opcion", [
        ("test", 0),
        ("test", 4),
        ("test", 5),
        ("test", -1),
        ("test", 100),
    ])
    def test_invalid_options(self, student_module, nombre, opcion):
        output = student_module.transformar_nombre(nombre, opcion)
        assert output == "Opción inválida"

class TestEdgeCases:
    @pytest.mark.parametrize("nombre,opcion,esperado", [
        ("", 1, ""),            # Nombre vacío
        ("a", 1, "A"),          # Un carácter
        ("HOLA", 1, "HOLA"),    # Ya en mayúsculas
        ("hola", 2, "hola"),    # Ya en minúsculas
    ])
    def test_edge_cases(self, student_module, nombre, opcion, esperado):
        output = student_module.transformar_nombre(nombre, opcion)
        assert output == esperado
```

---

### 9. cond_validar_password

**Función**: `validar_password(password)` (función regular)
**Lógica**: 8 ≤ len ≤ 14 → válida, sino → inválida

**Casos de prueba sugeridos:**
```python
class TestValidPasswords:
    @pytest.mark.parametrize("password", [
        "a" * 8,                # Mínimo válido
        "a" * 10,
        "a" * 14,               # Máximo válido
        "abc12345",             # Exactamente 8
        "password123456",       # Exactamente 14
    ])
    def test_valid_lengths(self, student_module, password):
        output = student_module.validar_password(password)
        assert output == "Ha ingresado una contraseña correcta"

class TestInvalidPasswords:
    @pytest.mark.parametrize("password", [
        "a" * 7,                # Muy corta (7)
        "a" * 15,               # Muy larga (15)
        "a" * 0,                # Vacía
        "a" * 1,                # 1 carácter
        "a" * 100,              # Extremadamente larga
    ])
    def test_invalid_lengths(self, student_module, password):
        output = student_module.validar_password(password)
        assert output == "Por favor, ingrese una contraseña de entre 8 y 14 caracteres"

class TestBoundaryValues:
    def test_length_7(self, student_module):
        """Justo debajo del mínimo."""
        output = student_module.validar_password("a" * 7)
        assert output == "Por favor, ingrese una contraseña de entre 8 y 14 caracteres"

    def test_length_8(self, student_module):
        """Mínimo válido."""
        output = student_module.validar_password("a" * 8)
        assert output == "Ha ingresado una contraseña correcta"

    def test_length_14(self, student_module):
        """Máximo válido."""
        output = student_module.validar_password("a" * 14)
        assert output == "Ha ingresado una contraseña correcta"

    def test_length_15(self, student_module):
        """Justo arriba del máximo."""
        output = student_module.validar_password("a" * 15)
        assert output == "Por favor, ingrese una contraseña de entre 8 y 14 caracteres"
```

---

## 🚀 Workflow Recomendado

### Para Cada Problema:

1. **Leer documentación existente**
   ```bash
   cat backend/problems/[problem_id]/prompt.md
   cat backend/problems/[problem_id]/starter.py
   ```

2. **Revisar tests actuales**
   ```bash
   cat backend/problems/[problem_id]/tests_public.py
   cat backend/problems/[problem_id]/tests_hidden.py
   ```

3. **Copiar plantilla de problema similar**
   - Si es main() → Copiar de `cond_aprobado`
   - Si es función → Copiar de `cond_termina_vocal` (cuando esté listo)

4. **Adaptar casos de prueba**
   - Identificar boundary values
   - Agregar parametrización
   - Organizar en clases

5. **Probar localmente (opcional)**
   ```bash
   # Dentro del container worker (que tiene pytest)
   docker compose exec worker python -m pytest /app/backend/problems/[problem_id]/tests_public.py -v
   ```

6. **Documentar con docstrings**
   - Cada clase: descripción de categoría
   - Cada test: qué se está probando

---

## 💡 Tips y Trucos

### 1. Reutiliza Código

Si varios tests tienen lógica similar, usa `@pytest.mark.parametrize`:

```python
# ❌ MAL - Repetitivo
def test_opcion_1():
    assert transformar("test", 1) == "TEST"

def test_opcion_2():
    assert transformar("TEST", 2) == "test"

# ✅ BIEN - Parametrizado
@pytest.mark.parametrize("nombre,opcion,esperado", [
    ("test", 1, "TEST"),
    ("TEST", 2, "test"),
])
def test_opciones(self, student_module, nombre, opcion, esperado):
    assert student_module.transformar(nombre, opcion) == esperado
```

### 2. Usa Fixtures Correctamente

```python
# Para main() que lee stdin:
output = capture_main_output("entrada", student_module)

# Para funciones regulares:
output = student_module.nombre_funcion(arg1, arg2)

# Para verificar existencia:
assert hasattr(student_module, 'nombre_funcion')
```

### 3. Mensajes Descriptivos

```python
# ✅ BIEN
assert output == esperado, \
    f"Con entrada {entrada}, se esperaba '{esperado}', se obtuvo '{output}'"

# ❌ MAL
assert output == esperado
```

### 4. Boundary Values Son Críticos

Para cada límite, prueba:
- Exactamente el límite
- Justo debajo
- Justo arriba

```python
# Ejemplo: límite en 18
("17", resultado_menor)   # Debajo
("18", resultado_limite)  # Exacto
("19", resultado_mayor)   # Arriba
```

---

## 📊 Checklist de Calidad

Antes de considerar un problema "completado", verifica:

- [ ] ✅ conftest.py existe y funciona
- [ ] ✅ tests_public.py tiene al menos 15 tests
- [ ] ✅ tests_hidden.py tiene tests adicionales
- [ ] ✅ Usa `@pytest.mark.parametrize` donde aplica
- [ ] ✅ Clases organizan tests por categoría
- [ ] ✅ Todos los tests tienen docstrings
- [ ] ✅ Boundary values están cubiertos
- [ ] ✅ Edge cases están cubiertos
- [ ] ✅ Mensajes de error son descriptivos
- [ ] ✅ Sin código duplicado significativo

---

## 🎯 Meta Final

Al completar los 5 problemas restantes, el proyecto tendrá:

- ✅ **150+ tests** para condicionales (vs 27 antes)
- ✅ **9/9 problemas** con tests de calidad profesional
- ✅ **~92% cobertura** promedio
- ✅ **Infraestructura reutilizable** (conftest)
- ✅ **Documentación completa** (docstrings)
- ✅ **Mantenibilidad alta** (DRY principle)

---

## 📚 Recursos

- **Ejemplos completos**: Ver `cond_aprobado` y `cond_mayor_edad`
- **Documentación pytest**: https://docs.pytest.org/
- **Informe de mejoras**: `TEST_IMPROVEMENTS_REPORT.md`
- **Antes/Después**: `ANTES_DESPUES_TESTS.md`

---

**¡Éxito en completar las mejoras! 🚀**

Las bases están sólidas y los patrones bien establecidos. Siguiendo esta guía, completar los 5 problemas restantes debería tomar ~2-3 horas de trabajo enfocado.
