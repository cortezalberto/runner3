# Problema: Saludo personalizado

Escribe un programa en Python que pida al usuario su nombre y luego muestre un saludo personalizado en pantalla.

Este ejercicio te ayudará a practicar:
- Lectura de entrada del usuario con `input()`
- Formateo de strings con f-strings
- Impresión de resultados con `print()`

## Entrada
Un string que representa el nombre del usuario (una sola palabra, sin espacios).

## Salida
Un saludo con el formato EXACTO: `Hola {nombre}!`

**Importante:** NO uses coma después de "Hola". El formato correcto es "Hola Juan!" NO "Hola, Juan!"

## Ejemplos

### Ejemplo 1
```
Entrada: Juan
Salida: Hola Juan!
```

### Ejemplo 2
```
Entrada: María
Salida: Hola María!
```

### Ejemplo 3 (nombre corto)
```
Entrada: Lu
Salida: Hola Lu!
```

### Ejemplo 4 (nombre largo)
```
Entrada: Alejandra
Salida: Hola Alejandra!
```

## ⚠️ Casos especiales probados

Los tests verificarán:
- ✅ **Nombres cortos** (2-3 caracteres): "Lu", "Ana"
- ✅ **Nombres largos** (10+ caracteres): "Alessandro"
- ✅ **Nombres con acentos**: "José", "María"
- ✅ **Nombres compuestos** (con espacios): "Juan Pablo", "María José"

## Formato de salida estricto

**Correcto:**
```
Hola Juan!
```

**Incorrecto (serán rechazados por los tests):**
```
Hola, Juan!        ❌ Tiene coma
Hola Juan          ❌ Falta signo de exclamación
hola Juan!         ❌ "Hola" debe empezar con mayúscula
Hola  Juan!        ❌ Dos espacios en lugar de uno
Hola Juan!!        ❌ Dos signos de exclamación
```

## Restricciones técnicas

- Debes implementar la función `main()` que lea la entrada con `input()` y use `print()` para mostrar el resultado
- Usa f-strings para formatear el mensaje: `f"Hola {nombre}!"`
- El formato debe ser EXACTO (mayúsculas, un solo espacio, un signo de exclamación)
- No imprimas mensajes adicionales, prompts, ni espacios extra
- No modifiques la estructura de la función `main()` proporcionada en el starter code

## Notas adicionales

**Sugerencia de implementación:**
```python
def main():
    nombre = input()  # Lee el nombre
    print(f"Hola {nombre}!")  # Imprime el saludo con formato exacto
```

**Palabras clave que los tests verifican:**
- El saludo debe contener la palabra "Hola"
- El saludo debe contener el nombre ingresado
- Debe terminar con signo de exclamación "!"
