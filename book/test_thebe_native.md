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

# Test de Integración Nativa Thebe

Este es un documento de prueba para verificar que la integración nativa de sphinx-thebe funciona correctamente.

## Test 1: Código Python Básico

Ejecuta esta celda para verificar que Pyodide funciona:

```{code-cell} ipython3
print("¡Hola desde Thebe nativo!")
print("Python está funcionando correctamente ✓")
resultado = 2 + 2
print(f"2 + 2 = {resultado}")
```

## Test 2: Operaciones Matemáticas

Prueba operaciones matemáticas básicas:

```{code-cell} ipython3
# Cálculos físicos básicos
velocidad = 10  # m/s
tiempo = 5      # s
distancia = velocidad * tiempo

print(f"Velocidad: {velocidad} m/s")
print(f"Tiempo: {tiempo} s")
print(f"Distancia recorrida: {distancia} m")
```

## Test 3: Importar Módulos (NumPy)

Verifica que se pueden cargar paquetes científicos:

```{code-cell} ipython3
import numpy as np

# Crear un array
arr = np.array([1, 2, 3, 4, 5])
print(f"Array: {arr}")
print(f"Media: {np.mean(arr)}")
print(f"Suma: {np.sum(arr)}")
```

## Test 4: Matplotlib (Gráficos)

Prueba la generación de gráficos:

```{code-cell} ipython3
import matplotlib.pyplot as plt
import numpy as np

# Crear datos
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

# Crear gráfico
plt.figure(figsize=(8, 4))
plt.plot(x, y, 'b-', linewidth=2)
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Función Seno')
plt.grid(True)
plt.show()
```

## Test 5: Estado Persistente

Verifica que las variables se mantienen entre celdas:

```{code-cell} ipython3
# Define una variable
mi_variable = "Esta variable debería estar disponible en la siguiente celda"
numero = 42
print(f"Variable definida: {mi_variable}")
print(f"Número: {numero}")
```

Ahora usa la variable de la celda anterior:

```{code-cell} ipython3
# Usa la variable de la celda anterior
print(f"Recuperando variable: {mi_variable}")
print(f"Número * 2 = {numero * 2}")
```

---

## ✅ Checklist de Verificación

Para confirmar que todo funciona:

1. **Botón "Live Code"**: Debe aparecer en la esquina superior derecha
2. **Activar Live Code**: Al hacer clic, debe mostrar "Loading Pyodide..." o similar
3. **Botones "run"**: Deben aparecer en cada celda de código
4. **Ejecutar Test 1**: Debe mostrar el mensaje "¡Hola desde Thebe nativo!"
5. **Ejecutar Test 2**: Debe calcular y mostrar la distancia (50 m)
6. **Ejecutar Test 3**: Debe cargar NumPy y mostrar estadísticas del array
7. **Ejecutar Test 4**: Debe mostrar un gráfico de la función seno
8. **Ejecutar Tests 5**: Debe mantener las variables entre celdas

Si todos los tests funcionan: **✅ La integración nativa es suficiente, NO necesitamos implementación custom**
