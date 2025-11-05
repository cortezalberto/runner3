# Problema: Mayor de edad

Escribe un programa que lea una edad desde la entrada estándar y determine si una persona es mayor de edad.

Una persona es **mayor de edad** si tiene **más de 18 años** (es decir, 19 años o más). Una persona es **menor de edad** si tiene **18 años o menos**.

## Concepto: Mayoría de edad

- **Mayor de edad:** Edad > 18 (19, 20, 21, 22, ..., 100, etc.)
- **Menor de edad:** Edad ≤ 18 (0, 1, 2, ..., 17, 18)

**IMPORTANTE:** La edad 18 se considera **menor de edad** porque la condición requiere ser **mayor** (estrictamente mayor, no igual).

**Operador de comparación en Python:**
```python
edad > 18  # True si mayor de edad, False si menor de edad
```

## Entrada
Un número entero que representa la edad de una persona.

## Salida
- Si la edad es **mayor de 18** (19 o más): `"Es mayor de edad"`
- Si la edad es **menor o igual a 18** (18 o menos): `"Es menor de edad"`

**IMPORTANTE:** El mensaje debe ser EXACTO, respetando mayúsculas, espacios y acentos.

## Ejemplos básicos

### Ejemplo 1 (claramente mayor de edad)
```
Entrada: 20
Salida: Es mayor de edad
```

### Ejemplo 2 (claramente menor de edad)
```
Entrada: 15
Salida: Es menor de edad
```

### Ejemplo 3 (justo en el límite - MENOR)
```
Entrada: 18
Salida: Es menor de edad
```
> **Nota crítica:** 18 NO es mayor de edad en este problema. Solo edades **mayores** de 18 (19+) son mayoría de edad.

### Ejemplo 4 (justo arriba del límite - MAYOR)
```
Entrada: 19
Salida: Es mayor de edad
```
> **Nota:** 19 es la primera edad considerada mayor de edad (19 > 18).

## ⚠️ Casos especiales importantes

### Valores límite (boundary values)

El valor crítico es 18. Los tests verifican que entiendas la diferencia entre "mayor de 18" (>) y "mayor o igual a 18" (>=):

**Ejemplo 5 (edad 18 - MENOR DE EDAD):**
```
Entrada: 18
Salida: Es menor de edad
```
> **Importante:** 18 NO es mayor de edad. La condición es `edad > 18`, NO `edad >= 18`.

**Ejemplo 6 (edad 17 - claramente menor):**
```
Entrada: 17
Salida: Es menor de edad
```

**Ejemplo 7 (edad 19 - primer mayor de edad):**
```
Entrada: 19
Salida: Es mayor de edad
```

### Rangos de edad verificados

Los tests verifican diferentes grupos etarios:

**Niñez (1-12 años):**
```
Entrada: 1    → Salida: Es menor de edad
Entrada: 5    → Salida: Es menor de edad
Entrada: 10   → Salida: Es menor de edad
```

**Adolescencia (13-18 años):**
```
Entrada: 13   → Salida: Es menor de edad
Entrada: 15   → Salida: Es menor de edad
Entrada: 17   → Salida: Es menor de edad
Entrada: 18   → Salida: Es menor de edad  ⚠️ Incluye 18!
```

**Adultez joven (19-30 años):**
```
Entrada: 19   → Salida: Es mayor de edad
Entrada: 21   → Salida: Es mayor de edad
Entrada: 25   → Salida: Es mayor de edad
```

**Adultez (30-70 años):**
```
Entrada: 30   → Salida: Es mayor de edad
Entrada: 40   → Salida: Es mayor de edad
Entrada: 60   → Salida: Es mayor de edad
```

**Adultos mayores (70+ años):**
```
Entrada: 80   → Salida: Es mayor de edad
Entrada: 100  → Salida: Es mayor de edad
Entrada: 120  → Salida: Es mayor de edad
```

### Valores extremos

**Ejemplo 8 (recién nacido):**
```
Entrada: 0
Salida: Es menor de edad
```

**Ejemplo 9 (bebé):**
```
Entrada: 1
Salida: Es menor de edad
```

**Ejemplo 10 (edad muy alta):**
```
Entrada: 150
Salida: Es mayor de edad
```

**Ejemplo 11 (récord mundial aproximado):**
```
Entrada: 122
Salida: Es mayor de edad
```

## Casos especiales probados

Los tests verificarán:
- ✅ **Menores de edad completos:** 0, 1, 5, 10, 13, 14, 15, 16, 17, 18
- ✅ **Mayores de edad jóvenes:** 19, 20, 21, 22, 25, 30
- ✅ **Adultos:** 35, 40, 50, 60, 70
- ✅ **Adultos mayores:** 71, 75, 80, 85, 90, 95, 100
- ✅ **Valores extremos:** 120, 150, 200, 999
- ✅ **Valor límite crítico:** 18 (menor de edad), 19 (mayor de edad)
- ✅ **Rangos completos:** Niñez (1-12), Adolescencia (13-18), Adultos (19+)

## Formato de salida estricto

**Mensajes EXACTOS (no los modifiques):**

Para mayores de edad (> 18):
```
Es mayor de edad
```

Para menores de edad (≤ 18):
```
Es menor de edad
```

**Errores comunes (serán rechazados por los tests):**
```
es mayor de edad            ❌ "Es" debe empezar con mayúscula
ES MAYOR DE EDAD            ❌ No debe estar en mayúsculas completo
Es mayor de edad.           ❌ No debe tener punto final
Mayor de edad               ❌ Falta "Es" al inicio
Es  mayor de edad           ❌ Dos espacios en lugar de uno
Es mayor de edad!           ❌ No debe tener signos de exclamación
Es menor de edad.           ❌ No debe tener punto final
```

## Restricciones técnicas

- Debes implementar la función `main()` que lea la entrada con `input()` y use `print()` para mostrar el resultado
- Convierte la entrada a número entero con `int(input())`
- La condición debe ser: `if edad > 18:` (mayor estrictamente, NO mayor o igual)
- Los mensajes de salida deben ser EXACTOS (respeta mayúsculas, espacios y acentos)
- No imprimas mensajes adicionales, prompts, ni espacios extra
- No modifiques la estructura de la función `main()` proporcionada en el starter code

## Notas adicionales

**Lógica del problema:**
```python
if edad > 18:
    # La persona es mayor de edad (19 o más)
else:
    # La persona es menor de edad (18 o menos)
```

**Sugerencia de implementación:**
```python
def main():
    edad = int(input())  # Lee la edad y conviértela a entero

    if edad > 18:
        print("Es mayor de edad")
    else:
        print("Es menor de edad")
```

**⚠️ Puntos clave para aprobar los tests:**
1. Usa `int(input())` para leer la edad (solo enteros)
2. La condición es `edad > 18` (estrictamente mayor, NO `>=`)
3. El límite es CRÍTICO: 18 es menor de edad, 19 es mayor de edad
4. Los mensajes deben ser EXACTOS: "Es mayor de edad" y "Es menor de edad"
5. Tu código debe funcionar con cualquier edad válida (0 a 999+)
6. No confundas "mayor de 18" (>) con "mayor o igual a 18" (>=)
