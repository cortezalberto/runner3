# Problema: Aprobado o Desaprobado

Escribe un programa que lea una nota desde la entrada estándar y determine si un estudiante aprobó o desaprobó.

Una nota es **aprobada** si es mayor o igual a 6. Una nota es **desaprobada** si es menor a 6.

## Concepto: Evaluación académica

- **Aprobado:** Nota ≥ 6 (6.0, 6.1, 7, 8, 9, 10, etc.)
- **Desaprobado:** Nota < 6 (5.99, 5.9, 5, 4, 3, 2, 1, 0, etc.)

**Operador de comparación en Python:**
```python
nota >= 6  # True si aprobado, False si desaprobado
```

## Entrada
Un número (puede ser entero o decimal) que representa la nota del estudiante.

## Salida
- Si la nota es mayor o igual a 6: `"Aprobado"`
- Si la nota es menor a 6: `"Desaprobado"`

**IMPORTANTE:** El mensaje debe ser EXACTO, respetando mayúsculas y acentos.

## Ejemplos básicos

### Ejemplo 1 (nota aprobada entera)
```
Entrada: 7
Salida: Aprobado
```

### Ejemplo 2 (nota aprobada en el límite)
```
Entrada: 6
Salida: Aprobado
```

### Ejemplo 3 (nota desaprobada)
```
Entrada: 4
Salida: Desaprobado
```

### Ejemplo 4 (nota aprobada decimal)
```
Entrada: 7.5
Salida: Aprobado
```

## ⚠️ Casos especiales importantes

### Valores límite (boundary values)

Los tests verifican que entiendas exactamente dónde está el límite entre aprobar y desaprobar:

**Ejemplo 5 (justo en el límite - APROBADO):**
```
Entrada: 6.0
Salida: Aprobado
```
> **Nota:** 6.0 es EXACTAMENTE el límite y se considera aprobado (nota >= 6)

**Ejemplo 6 (justo debajo del límite - DESAPROBADO):**
```
Entrada: 5.99
Salida: Desaprobado
```
> **Importante:** 5.99 es menor a 6, por lo tanto está desaprobado. No se redondea.

**Ejemplo 7 (justo arriba del límite - APROBADO):**
```
Entrada: 6.01
Salida: Aprobado
```

**Ejemplo 8 (casi aprobado pero desaprobado):**
```
Entrada: 5.999
Salida: Desaprobado
```

### Notas con diferentes precisiones decimales

Los tests verifican que tu programa funcione con notas que tienen diferentes cantidades de decimales:

**Ejemplo 9 (varias precisiones del límite):**
```
Entrada: 6        → Salida: Aprobado
Entrada: 6.0      → Salida: Aprobado
Entrada: 6.00     → Salida: Aprobado
Entrada: 6.000    → Salida: Aprobado
Entrada: 5.9999   → Salida: Desaprobado
```

### Valores extremos

Los tests también verifican notas inusuales pero válidas:

**Ejemplo 10 (nota perfecta):**
```
Entrada: 10
Salida: Aprobado
```

**Ejemplo 11 (nota cero):**
```
Entrada: 0
Salida: Desaprobado
```

**Ejemplo 12 (nota muy baja):**
```
Entrada: 0.1
Salida: Desaprobado
```

**Ejemplo 13 (nota superior a 10):**
```
Entrada: 15
Salida: Aprobado
```
> **Nota:** Aunque 15 está fuera del rango típico 0-10, es mayor a 6, por lo tanto está aprobado.

## Casos especiales probados

Los tests verificarán:
- ✅ **Notas enteras aprobadas:** 6, 7, 8, 9, 10
- ✅ **Notas enteras desaprobadas:** 0, 1, 2, 3, 4, 5
- ✅ **Notas decimales aprobadas:** 6.5, 7.3, 8.9, 9.5, 7.25, 7.125
- ✅ **Notas decimales desaprobadas:** 5.9, 4.5, 3.2, 2.1, 5.25, 5.125
- ✅ **Valores límite críticos:** 6.0 (aprobado), 5.99 (desaprobado), 6.01 (aprobado)
- ✅ **Alta precisión:** 6.000, 5.999, 5.9999, 6.001
- ✅ **Valores extremos:** 0, 0.1, 10, 15

## Formato de salida estricto

**Mensajes EXACTOS (no los modifiques):**

Para notas aprobadas (≥ 6):
```
Aprobado
```

Para notas desaprobadas (< 6):
```
Desaprobado
```

**Errores comunes (serán rechazados por los tests):**
```
aprobado                    ❌ Debe empezar con mayúscula
APROBADO                    ❌ No debe estar en mayúsculas completo
Aprobado.                   ❌ No debe tener punto final
Aprobado!                   ❌ No debe tener signos de exclamación
Aprobó                      ❌ Acento incorrecto
Desaprobado.                ❌ No debe tener punto final
desaprobado                 ❌ Debe empezar con mayúscula
```

## Restricciones técnicas

- Debes implementar la función `main()` que lea la entrada con `input()` y use `print()` para mostrar el resultado
- Convierte la entrada a número decimal con `float(input())` para soportar decimales
- La condición debe ser: `if nota >= 6:`
- Los mensajes de salida deben ser EXACTOS (respeta mayúsculas y acentos)
- No imprimas mensajes adicionales, prompts, ni espacios extra
- No modifiques la estructura de la función `main()` proporcionada en el starter code

## Notas adicionales

**Lógica del problema:**
```python
if nota >= 6:
    # El estudiante aprobó (nota mayor o igual a 6)
else:
    # El estudiante desaprobó (nota menor a 6)
```

**Sugerencia de implementación:**
```python
def main():
    nota = float(input())  # Lee la nota y conviértela a decimal

    if nota >= 6:
        print("Aprobado")
    else:
        print("Desaprobado")
```

**⚠️ Puntos clave para aprobar los tests:**
1. Usa `float(input())` para leer la nota (soporta decimales)
2. La condición es `nota >= 6` (mayor o IGUAL a 6)
3. El límite es EXACTO: 6.0 aprueba, 5.99 desaprueba (no se redondea)
4. Los mensajes deben ser EXACTOS: "Aprobado" y "Desaprobado"
5. Tu código debe funcionar con cualquier nota (incluso fuera de 0-10)
6. Presta especial atención a los valores límite (5.99, 6.0, 6.01)
