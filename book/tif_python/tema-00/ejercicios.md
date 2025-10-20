---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Tema 00: Ejercicios — Introducción a Python

:::{tip}
Completa todos los ejercicios en orden. Ejecuta cada celda y verifica que el resultado sea correcto.
:::

## Ejercicio 1: Variables y Tipos

:::{topic} Objetivo Pedagógico
Practicar la creación de variables y verificar sus tipos de datos.
:::

**Dificultad**: Básico | **Tiempo estimado**: 5 min

**Criterios de éxito**: 
- ✓ Crear 4 variables de diferentes tipos
- ✓ Mostrar sus tipos con `type()`
- ✓ Demostrar conversión de tipos (`int()`, `str()`, `float()`)

```{code-cell} ipython3
# TODO: Crea las siguientes variables y muestra su tipo
# - un número entero llamado 'edad' con valor 22
# - un número flotante llamado 'peso' con valor 75.5
# - una cadena llamada 'ciudad' con valor "Barcelona"
# - un booleano llamado 'es_programador' con valor True

# Tu código aquí:


# Muestra los tipos:

```

**Solución esperada**:
```python
edad = 22
peso = 75.5
ciudad = "Barcelona"
es_programador = True

print(f"edad: {type(edad)}")
print(f"peso: {type(peso)}")
print(f"ciudad: {type(ciudad)}")
print(f"es_programador: {type(es_programador)}")
```

---

## Ejercicio 2: Operaciones Aritméticas

:::{topic} Objetivo Pedagógico
Realizar operaciones matemáticas y entender el orden de operaciones.
:::

**Dificultad**: Básico | **Tiempo estimado**: 5 min

**Criterios de éxito**:
- ✓ Calcular el promedio de 3 números
- ✓ Usar paréntesis correctamente
- ✓ Mostrar resultado con precisión

```{code-cell} ipython3
# Dados tres números: a=10, b=20, c=30
# Calcula su promedio

a = 10
b = 20
c = 30

# Tu código aquí:
promedio = None

print(f"Promedio de {a}, {b}, {c}: {promedio}")

# TEST: check if promedio is correct
assert promedio == 20.0, f"Expected 20.0, got {promedio}"
print("✅ Test passed!")
```

---

## Ejercicio 3: Condicionales

:::{topic} Objetivo Pedagógico
Usar sentencias `if/elif/else` para tomar decisiones en el código.
:::

**Dificultad**: Básico | **Tiempo estimado**: 10 min

**Criterios de éxito**:
- ✓ Evaluar una calificación (0-10)
- ✓ Mostrar resultado de aprobado/reprobado
- ✓ Mensaje diferente por rango

```{code-cell} ipython3
# Escribe una función que califique una nota (0-10)
# Retorna: "Reprobado" si nota < 5, "Aprobado" si 5 <= nota < 8,
#          "Bueno" si 8 <= nota < 9.5, "Excelente" si nota >= 9.5

def calificar(nota):
    """Convierte una calificación numérica a texto."""
    # Tu código aquí:
    pass

# Prueba con diferentes notas
notas = [3, 6, 8, 9.8]
for nota in notas:
    print(f"Nota {nota}: {calificar(nota)}")

# TEST
assert calificar(3) == "Reprobado"
assert calificar(6) == "Aprobado"
assert calificar(8) == "Bueno"
assert calificar(9.8) == "Excelente"
print("✅ Todos los tests pasaron!")
```

---

## Ejercicio 4: Bucles

:::{topic} Objetivo Pedagógico
Usar bucles `for` y `while` para repetir código.
:::

**Dificultad**: Básico | **Tiempo estimado**: 10 min

**Criterios de éxito**:
- ✓ Imprimir tabla de multiplicación
- ✓ Usar bucle for
- ✓ Formato legible

```{code-cell} ipython3
# Imprime la tabla de multiplicación del 7 (7x1 hasta 7x10)

# Tu código aquí:

```

**Salida esperada**:
```
7 x 1 = 7
7 x 2 = 14
...
7 x 10 = 70
```

---

## Ejercicio 5: Listas

:::{topic} Objetivo Pedagógico
Crear y manipular listas, acceder a elementos e iterar.
:::

**Dificultad**: Intermedio | **Tiempo estimado**: 10 min

**Criterios de éxito**:
- ✓ Crear lista de números
- ✓ Calcular suma y promedio
- ✓ Encontrar máximo y mínimo

```{code-cell} ipython3
# Crea una lista con 5 números: [3, 7, 2, 9, 5]
# Calcula: suma, promedio, máximo, mínimo

numeros = [3, 7, 2, 9, 5]

# Tu código aquí (sin usar len(), sum(), min(), max()):
suma = None
promedio = None
maximo = None
minimo = None

print(f"Números: {numeros}")
print(f"Suma: {suma}")
print(f"Promedio: {promedio}")
print(f"Máximo: {maximo}")
print(f"Mínimo: {minimo}")

# TEST
assert suma == 26
assert promedio == 5.2
assert maximo == 9
assert minimo == 2
print("✅ Tests passed!")
```

---

## Ejercicio 6: Diccionarios

:::{topic} Objetivo Pedagógico
Trabajar con diccionarios para almacenar datos estructurados.
:::

**Dificultad**: Intermedio | **Tiempo estimado**: 10 min

**Criterios de éxito**:
- ✓ Crear diccionario de estudiante
- ✓ Acceder y modificar valores
- ✓ Iterar sobre pares clave-valor

```{code-cell} ipython3
# Crea un diccionario llamado 'persona' con:
# - nombre: "Laura"
# - edad: 21
# - carrera: "Ingeniería Física"
# - notas: [8.5, 9.0, 7.5]

# Tu código aquí:
persona = None

# Modifica la edad (suma 1)
# Agrega una clave nueva: "ciudad" con valor "Valencia"

# Imprime todos los datos
print("Datos de la persona:")
# Tu código aquí para iterar:

```

---

## Ejercicio 7: Funciones

:::{topic} Objetivo Pedagógico
Definir funciones reutilizables con parámetros y retorno de valores.
:::

**Dificultad**: Intermedio | **Tiempo estimado**: 15 min

**Criterios de éxito**:
- ✓ Crear función que calcule área de círculo
- ✓ Usar parámetro `radio`
- ✓ Retornar resultado correcto

```{code-cell} ipython3
import math

# Define una función area_circulo(radio) que retorne el área
# Fórmula: A = π * r²

def area_circulo(radio):
    """Calcula el área de un círculo dado su radio."""
    # Tu código aquí:
    pass

# Prueba con diferentes radios
radios = [1, 2, 5]
for r in radios:
    area = area_circulo(r)
    print(f"Radio {r}: Área = {area:.2f}")

# TEST
assert abs(area_circulo(1) - math.pi) < 0.01
assert abs(area_circulo(2) - 4*math.pi) < 0.01
print("✅ Tests passed!")
```

---

## Ejercicio 8: NumPy Básico

:::{topic} Objetivo Pedagógico
Crear y manipular arrays de NumPy.
:::

**Dificultad**: Intermedio | **Tiempo estimado**: 10 min

**Criterios de éxito**:
- ✓ Crear dos arrays
- ✓ Realizar operaciones vectorizadas
- ✓ Calcular productos escalares

```{code-cell} ipython3
import numpy as np

# Crea dos arrays:
# v1 = [1, 2, 3]
# v2 = [4, 5, 6]

v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

# Calcula:
# - v1 + v2
# - v1 * v2 (elemento a elemento)
# - Producto escalar (dot product)
# - Magnitud de v1 (||v1||)

suma = None
producto_elemento = None
producto_escalar = None
magnitud_v1 = None

print(f"v1 + v2 = {suma}")
print(f"v1 * v2 (elemento a elemento) = {producto_elemento}")
print(f"v1 · v2 (producto escalar) = {producto_escalar}")
print(f"||v1|| = {magnitud_v1}")

# TEST
assert np.allclose(suma, [5, 7, 9])
assert np.allclose(producto_escalar, 32)
assert abs(magnitud_v1 - np.sqrt(14)) < 0.01
print("✅ Tests passed!")
```

---

## Ejercicio 9: Matplotlib Básico

:::{topic} Objetivo Pedagógico
Crear gráficos simples con Matplotlib.
:::

**Dificultad**: Intermedio | **Tiempo estimado**: 10 min

**Criterios de éxito**:
- ✓ Crear array de valores x
- ✓ Calcular y = x²
- ✓ Graficar con etiquetas

```{code-cell} ipython3
import matplotlib.pyplot as plt
import numpy as np

# Crea arrays x e y donde y = x²
# x debe ir de -5 a 5 con 50 puntos

x = np.linspace(-5, 5, 50)
y = x**2

# Crea el gráfico con:
# - color azul
# - etiqueta en eje x: "x"
# - etiqueta en eje y: "y = x²"
# - título: "Función Cuadrática"
# - grid habilitado

plt.figure(figsize=(10, 6))
# Tu código aquí:

plt.show()
```

---

## Ejercicio 10: Desafío Integrador

:::{topic} Objetivo Pedagógico
Integrar todos los conceptos aprendidos en un programa completo.
:::

**Dificultad**: Avanzado | **Tiempo estimado**: 20 min

**Criterios de éxito**:
- ✓ Crear función que lea lista de velocidades
- ✓ Calcular energía cinética para m=1kg
- ✓ Mostrar resultados organizados

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt

# Desafío: Calcula la energía cinética para una masa de 1 kg
#          con velocidades de 0 a 10 m/s en pasos de 1
#
# E = 0.5 * m * v²

# Tu código aquí:
# 1. Crea array de velocidades
# 2. Calcula energías cinéticas
# 3. Muestra tabla velocidad vs energía
# 4. Haz un gráfico de v vs E

velocidades = None
energias = None

# Mostrar tabla
print("Velocidad (m/s) | Energía (J)")
print("-" * 30)
# Tu código aquí para imprimir tabla

# Gráfico
plt.figure(figsize=(10, 6))
# Tu código para graficar

```

---

## ✅ Checklist de Revisión

Antes de marcar como completado:

- Ejecuté todos los ejercicios localmente
- Todos los tests pasaron (✅)
- El código es legible y tiene comentarios
- Intenté desafiar los ejercicios (no solo copiar solución)
- Probé en navegador si es posible

---

**Siguiente:** Tema 01 — Variables y Asignación Avanzada
