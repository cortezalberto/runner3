# Problema: Mayor de dos números

Escribe un programa que lea dos números desde la entrada estándar y muestre el mayor de los dos.

El programa debe comparar dos números y mostrar el que sea mayor. Si ambos números son iguales, debe mostrar ese número (cualquiera de los dos, ya que son iguales).

## Concepto: Comparación de números

Para encontrar el mayor de dos números, usamos el operador de comparación `>`:

```python
if a > b:
    # a es mayor
else:
    # b es mayor o igual
```

**IMPORTANTE:** Python también tiene la función integrada `max(a, b)` que devuelve el mayor, pero para este ejercicio debes usar condicionales (`if/else`).

## Entrada
Dos números, uno por línea:
- Primer número en la primera línea
- Segundo número en la segunda línea
- Pueden ser enteros o decimales
- Pueden ser positivos, negativos, o cero

## Salida
El número mayor de los dos. Si son iguales, muestra ese número.

## Ejemplos básicos

### Ejemplo 1 (primer número mayor)
```
Entrada:
  10
  5
Salida: 10
```

### Ejemplo 2 (segundo número mayor)
```
Entrada:
  5
  10
Salida: 10
```

### Ejemplo 3 (números iguales)
```
Entrada:
  7
  7
Salida: 7
```

### Ejemplo 4 (números decimales)
```
Entrada:
  3.5
  2.1
Salida: 3.5
```

## ⚠️ Casos especiales importantes

### Números negativos

Los tests verifican que entiendas cómo comparar números negativos:

**Ejemplo 5 (ambos negativos - el "menos negativo" es mayor):**
```
Entrada:
  -5
  -10
Salida: -5
```
> **Importante:** -5 es MAYOR que -10 (está más cerca de cero). Recuerda que -5 > -10.

**Ejemplo 6 (positivo vs negativo):**
```
Entrada:
  2
  -3
Salida: 2
```
> **Nota:** Los números positivos siempre son mayores que los negativos.

**Ejemplo 7 (negativo vs positivo):**
```
Entrada:
  -3
  2
Salida: 2
```

### Comparaciones con cero

**Ejemplo 8 (cero vs negativo):**
```
Entrada:
  0
  -5
Salida: 0
```
> **Importante:** 0 es mayor que cualquier número negativo.

**Ejemplo 9 (positivo vs cero):**
```
Entrada:
  3
  0
Salida: 3
```

**Ejemplo 10 (ambos cero):**
```
Entrada:
  0
  0
Salida: 0
```

**Ejemplo 11 (cero vs negativo, orden inverso):**
```
Entrada:
  -10
  0
Salida: 0
```

### Números decimales

Los tests también verifican números con decimales:

**Ejemplo 12 (decimales diferentes):**
```
Entrada:
  7.8
  9.2
Salida: 9.2
```

**Ejemplo 13 (decimales iguales):**
```
Entrada:
  1.5
  1.5
Salida: 1.5
```

**Ejemplo 14 (decimales muy cercanos):**
```
Entrada:
  10.75
  10.25
Salida: 10.75
```

### Valores extremos

**Ejemplo 15 (números grandes):**
```
Entrada:
  999999
  1000000
Salida: 1000000
```

**Ejemplo 16 (números muy negativos):**
```
Entrada:
  -1000
  -999
Salida: -999
```
> **Recordatorio:** -999 es mayor que -1000 (menos negativo).

## Casos especiales probados

Los tests verificarán:
- ✅ **Primer número mayor:** (10, 5), (20, 15), (100, 50), (7, 3)
- ✅ **Segundo número mayor:** (3, 8), (5, 10), (15, 20), (50, 100)
- ✅ **Números iguales:** (5, 5), (10, 10), (0, 0), (100, 100), (-5, -5)
- ✅ **Números decimales:** (3.5, 2.1), (7.8, 9.2), (1.5, 1.5), (10.75, 10.25)
- ✅ **Números negativos:** (-5, -10), (-10, -5), (-3, 2), (2, -3), (-100, -50)
- ✅ **Comparaciones con cero:** (0, -5), (3, 0), (0, 0), (-10, 0)
- ✅ **Valores extremos:** (1000, 999), (999999, 1000000), (-1000, -999)

## Formato de salida

- Imprime solo el número mayor (sin texto adicional)
- Puede ser entero o decimal según la entrada
- Si los números son iguales, imprime ese número
- No agregues mensajes como "El mayor es:" o similar

**Ejemplos de formato correcto:**
```
10          ✓ Solo el número
3.5         ✓ Con decimales si corresponde
-5          ✓ Con signo negativo si corresponde
```

**Ejemplos de formato incorrecto:**
```
El mayor es: 10       ❌ No agregar texto
10.0 es mayor         ❌ No agregar explicación
mayor = 10            ❌ No usar formato de variable
```

## Restricciones técnicas

- Debes implementar la función `main()` que lea la entrada con `input()` y use `print()` para mostrar el resultado
- Lee ambos números con `input()` y conviértelos con `float()` para soportar decimales
- Usa condicionales `if/else` para comparar (no uses `max()` directamente)
- Solo imprime el número mayor, sin texto adicional
- No modifiques la estructura de la función `main()` proporcionada en el starter code

## Notas adicionales

**Lógica del problema:**
```python
if a > b:
    # a es el mayor
elif b > a:
    # b es el mayor
else:
    # son iguales (a == b)
```

**Simplificación (usando if/else):**
```python
if a > b:
    print(a)  # a es mayor
else:
    print(b)  # b es mayor o igual
```

**Sugerencia de implementación:**
```python
def main():
    # Lee los dos números
    numero1 = float(input())
    numero2 = float(input())

    # Compara y muestra el mayor
    if numero1 > numero2:
        print(numero1)
    else:
        print(numero2)  # Incluye el caso de igualdad
```

**⚠️ Puntos clave para aprobar los tests:**
1. Usa `float(input())` para leer los números (soporta decimales)
2. Lee DOS números, uno por línea (dos llamadas a `input()`)
3. La comparación debe ser correcta: -5 > -10 (el menos negativo es mayor)
4. Si los números son iguales, imprime cualquiera (ambos son iguales)
5. Solo imprime el número, sin texto adicional
6. Funciona con enteros, decimales, positivos, negativos, y cero
