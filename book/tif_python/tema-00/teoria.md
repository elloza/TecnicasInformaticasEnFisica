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

# Tema 00: Introducción a Python — Conceptos Fundamentales

:::{topic} Objetivo Pedagógico
Comprender los conceptos fundamentales de programación en Python y practicar la sintaxis básica necesaria para los temas posteriores.
:::

## ¿Por Qué Python para Física?

Python es el lenguaje de facto en la comunidad científica. Ofrece:

- **Sintaxis clara y legible**: Código fácil de entender, ideal para aprendizaje
- **Biblioteca científica rica**: NumPy, SciPy, Matplotlib, Pandas — herramientas estándar para análisis de datos y modelado
- **Prototipado rápido**: Experimenta ideas físicas sin compilación
- **Comunidad global**: Millones de recursos, tutoriales y librerías especializadas

## Variables y Tipos de Datos

En Python, las variables almacenan valores sin necesidad de declarar su tipo explícitamente:

```{code-cell} ipython3
# Números enteros (int)
edad = 25
print(f"Mi edad es: {edad}")

# Números flotantes (float)
altura = 1.75
print(f"Mi altura es: {altura} metros")

# Strings (texto)
nombre = "Ana"
print(f"Hola, {nombre}")

# Valores booleanos (True/False)
estudiante = True
print(f"¿Soy estudiante? {estudiante}")
```

```{code-cell} ipython3
# Verificar tipo de variable
print(type(edad))
print(type(altura))
print(type(nombre))
print(type(estudiante))
```

## Operaciones Básicas

### Aritmética

```{code-cell} ipython3
# Operaciones aritméticas
a = 10
b = 3

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")  # División entera
print(f"{a} ** {b} = {a ** b}")  # Potencia
print(f"{a} % {b} = {a % b}")    # Módulo
```

### Comparación y Lógica

```{code-cell} ipython3
x = 5

# Comparaciones
print(f"x > 3: {x > 3}")
print(f"x == 5: {x == 5}")
print(f"x != 5: {x != 5}")

# Operadores lógicos
print(f"True and False: {True and False}")
print(f"True or False: {True or False}")
print(f"not True: {not True}")
```

## Estructuras de Control

### Condicionales

```{code-cell} ipython3
temperatura = 25

if temperatura < 0:
    print("¡Hace mucho frío!")
elif temperatura < 15:
    print("Es fresco")
elif temperatura < 25:
    print("Temperatura agradable")
else:
    print("¡Hace calor!")
```

### Bucles

```{code-cell} ipython3
# Bucle for
print("Conteo:")
for i in range(1, 6):
    print(i)

# Bucle while
print("\nCuadrados:")
n = 1
while n <= 5:
    print(f"{n}² = {n**2}")
    n += 1
```

## Listas y Diccionarios

### Listas (secuencias ordenadas)

```{code-cell} ipython3
# Crear una lista
frutas = ["manzana", "plátano", "naranja"]
print(f"Frutas: {frutas}")

# Acceder por índice (comienza en 0)
print(f"Primera fruta: {frutas[0]}")
print(f"Última fruta: {frutas[-1]}")

# Agregar elementos
frutas.append("fresa")
print(f"Después de append: {frutas}")

# Longitud
print(f"Número de frutas: {len(frutas)}")

# Iterar
print("Iterando:")
for fruta in frutas:
    print(f"  - {fruta}")
```

### Diccionarios (pares clave-valor)

```{code-cell} ipython3
# Crear un diccionario
estudiante = {
    "nombre": "Carlos",
    "edad": 20,
    "carrera": "Física",
    "promedio": 8.5
}

print(f"Estudiante: {estudiante}")
print(f"Nombre: {estudiante['nombre']}")
print(f"Edad: {estudiante['edad']}")

# Agregar clave nueva
estudiante["ciudad"] = "Madrid"
print(f"Con ciudad: {estudiante}")

# Iterar
print("Pares clave-valor:")
for clave, valor in estudiante.items():
    print(f"  {clave}: {valor}")
```

## Funciones

Las funciones son bloques de código reutilizable:

```{code-cell} ipython3
def saludar(nombre):
    """Función que saluda a una persona."""
    return f"¡Hola, {nombre}!"

print(saludar("María"))
print(saludar("Pedro"))
```

```{code-cell} ipython3
# Función con múltiples parámetros y valor por defecto
def calcular_energia_cinetica(masa, velocidad=0):
    """
    Calcula la energía cinética: E = 0.5 * m * v²
    
    Parámetros:
    - masa: en kilogramos
    - velocidad: en m/s (default=0)
    """
    energia = 0.5 * masa * velocidad**2
    return energia

E1 = calcular_energia_cinetica(2, 5)
E2 = calcular_energia_cinetica(2)

print(f"E con v=5 m/s: {E1} J")
print(f"E con v=0 m/s: {E2} J")
```

## NumPy: Arrays Numéricos

Para cálculos científicos, usamos **NumPy**:

```{code-cell} ipython3
import numpy as np

# Crear arrays
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

print(f"v1: {v1}")
print(f"v2: {v2}")

# Operaciones
print(f"v1 + v2 = {v1 + v2}")
print(f"v1 * v2 = {v1 * v2}")  # multiplicación elemento a elemento
print(f"v1 · v2 (producto escalar) = {np.dot(v1, v2)}")

# Funciones útiles
print(f"Promedio: {np.mean(v1)}")
print(f"Desv. estándar: {np.std(v1)}")
print(f"Máximo: {np.max(v1)}")
```

## Matplotlib: Visualización

```{code-cell} ipython3
import matplotlib.pyplot as plt
import numpy as np

# Crear datos
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

# Crear gráfico
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='sin(x)', linewidth=2)
plt.xlabel('x (radianes)')
plt.ylabel('y')
plt.title('Función Seno')
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()
```

## Resumen

| Concepto | Ejemplo |
|----------|---------|
| **Variables** | `x = 5` |
| **Tipos** | `int`, `float`, `str`, `bool` |
| **Listas** | `[1, 2, 3]` |
| **Diccionarios** | `{"clave": valor}` |
| **Funciones** | `def func(x): return x**2` |
| **NumPy** | `np.array([1, 2, 3])` |
| **Matplotlib** | `plt.plot(x, y)` |

---

**Próximo:** En los ejercicios practicarás todo lo aprendido.
