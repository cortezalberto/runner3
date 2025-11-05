# Problema: Verificar número par

Escribe un programa que lea un número entero desde la entrada estándar y determine si es par o no.

Un número par es aquel que es divisible entre 2 (su resto al dividirlo por 2 es igual a cero). Usa el operador módulo `%` para determinar el resto de la división.

## Concepto: Números pares e impares

- **Número par:** Su resto al dividir entre 2 es 0. Ejemplos: 2, 4, 6, 8, 10, ...
- **Número impar:** Su resto al dividir entre 2 es 1. Ejemplos: 1, 3, 5, 7, 9, ...

**Operador módulo en Python:**
```python
numero % 2 == 0  # True si es par, False si es impar
```

## Entrada
Un número entero (puede ser positivo, negativo, o cero).

## Salida
- Si el número es par: `"Ha ingresado un número par"`
- Si el número no es par: `"Por favor, ingrese un número par"`

**IMPORTANTE:** El mensaje debe ser EXACTO, respetando mayúsculas, acentos y puntuación.

## Ejemplos básicos

### Ejemplo 1 (número par positivo)
```
Entrada: 4
Salida: Ha ingresado un número par
```

### Ejemplo 2 (número impar positivo)
```
Entrada: 7
Salida: Por favor, ingrese un número par
```

### Ejemplo 3 (caso especial: cero)
```
Entrada: 0
Salida: Ha ingresado un número par
```
> **Nota:** El cero se considera un número par porque 0 % 2 == 0

## ⚠️ Casos especiales importantes

### Números negativos
Los números negativos también pueden ser pares o impares:

**Ejemplo 4 (número par negativo):**
```
Entrada: -2
Salida: Ha ingresado un número par
```

**Ejemplo 5 (número impar negativo):**
```
Entrada: -3
Salida: Por favor, ingrese un número par
```

**Ejemplo 6 (número par negativo grande):**
```
Entrada: -100
Salida: Ha ingresado un número par
```

> **Importante:** El operador módulo `%` funciona correctamente con números negativos en Python. -2 % 2 == 0, por lo tanto -2 es par.

### Números grandes
Los tests también verificarán números grandes:

**Ejemplo 7:**
```
Entrada: 1000
Salida: Ha ingresado un número par
```

**Ejemplo 8:**
```
Entrada: 9999
Salida: Por favor, ingrese un número par
```

## Casos especiales probados

Los tests verificarán:
- ✅ **Cero:** Debe considerarse par (0 % 2 == 0)
- ✅ **Números positivos pares:** 2, 4, 6, 100, 1000
- ✅ **Números positivos impares:** 1, 3, 5, 99, 9999
- ✅ **Números negativos pares:** -2, -4, -6, -100
- ✅ **Números negativos impares:** -1, -3, -5, -99
- ✅ **Números pequeños:** 1, 2
- ✅ **Números grandes:** 1000, 9999

## Formato de salida estricto

**Mensajes EXACTOS (no los modifiques):**

Para números pares:
```
Ha ingresado un número par
```

Para números impares:
```
Por favor, ingrese un número par
```

**Errores comunes (serán rechazados por los tests):**
```
ha ingresado un número par          ❌ "Ha" debe empezar con mayúscula
Ha ingresado un numero par          ❌ Falta acento en "número"
Ha ingresado un número par.         ❌ No debe tener punto final
Ha ingresado un número  par         ❌ Dos espacios en lugar de uno
Por favor ingrese un número par     ❌ Falta coma después de "favor"
```

## Restricciones técnicas

- Debes implementar la función `main()` que lea la entrada con `input()` y use `print()` para mostrar el resultado
- Usa el operador módulo `%` para determinar si el número es par
- La condición debe ser: `if numero % 2 == 0:`
- Los mensajes de salida deben ser EXACTOS (respeta mayúsculas, acentos, y espacios)
- No imprimas mensajes adicionales, prompts, ni espacios extra
- No modifiques la estructura de la función `main()` proporcionada en el starter code

## Notas adicionales

**Lógica del problema:**
```python
if numero % 2 == 0:
    # El número es par
else:
    # El número es impar
```

**Sugerencia de implementación:**
```python
def main():
    numero = int(input())  # Lee el número y conviértelo a entero

    if numero % 2 == 0:
        print("Ha ingresado un número par")
    else:
        print("Por favor, ingrese un número par")
```

**⚠️ Puntos clave para aprobar los tests:**
1. El cero (0) es par
2. Los números negativos también tienen paridad (-2 es par, -3 es impar)
3. Los mensajes deben ser EXACTOS (con mayúsculas y acentos correctos)
4. Usa `numero % 2 == 0` para verificar paridad (no inventes otra lógica)
