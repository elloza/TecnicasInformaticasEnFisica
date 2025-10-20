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

# Tema 05 · NumPy y Matplotlib

Basado en `resources_tif/apuntes_md/teoria/ProgramacionPythonTIF-Tema5.md`.

## Ecosistema científico

`math`, `numpy`, `matplotlib`, `scipy`, `pandas`, `seaborn`, `scikit-learn`.

## NumPy: arrays y operaciones vectoriales

```{code-cell} ipython3
import numpy as np

a = np.array([1, 2, 3], dtype=float)
a.dtype, a[0], a[-1], a[0:3:2]
```

Arrays 2D y slicing:

```{code-cell} ipython3
A = np.array([[1,2,3],[4,5,6]])
A[0,2], A[-1,:], A[:,1]
```

Creación:

```{code-cell} ipython3
np.arange(0, 0.5, 0.1), np.linspace(-1, 1, 5)
```

Tipos y conversión:

```{code-cell} ipython3
b = np.array([1, 2., 3])
b.dtype
b = b.astype(int)
b.dtype
```

Operaciones elementwise y agregados:

```{code-cell} ipython3
v = np.array([1,2,3], float)
w = np.array([4,5,6], float)
v + w, v * w, v @ w, v.mean(), v.max()
```

## Matplotlib: gráficos básicos

```{code-cell} ipython3
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi, 400)
y = np.log(np.abs(x)+1e-9) * np.sin(x)

plt.figure(figsize=(6,3))
plt.plot(x, y, 'g--*', label='log(x)*sin(x)')
plt.xlim(x.min(), x.max())
plt.xlabel('x'); plt.ylabel('f(x)'); plt.title('Ejemplo')
plt.legend(); plt.tight_layout()
plt.show()
```

Subplots y ajustes:

```{code-cell} ipython3
x = np.array([1.2,2.5,3.4,4.0,5.4,6.1,7.2,8.1,9.0,10.1])
y = np.array([24.8,24.5,24.0,23.3,22.4,21.3,20.0,18.5,16.8,14.9])

coef_lin = np.polyfit(x, y, 1)
coef_quad = np.polyfit(x, y, 2)

xx = np.linspace(x.min(), x.max(), 200)
yl = np.polyval(coef_lin, xx)
yq = np.polyval(coef_quad, xx)

fig, ax = plt.subplots(1,2, figsize=(8,3), sharex=True, sharey=True)
ax[0].scatter(x, y); ax[0].plot(xx, yl); ax[0].set_title('Lineal')
ax[1].scatter(x, y); ax[1].plot(xx, yq); ax[1].set_title('Cuadrático')
plt.tight_layout(); plt.show()
coef_lin, coef_quad
```

```{admonition} Nota sobre ejecución en navegador
:class: note
NumPy/Matplotlib pueden ejecutarse en Pyodide, pero con limitaciones de rendimiento y compatibilidad. Para gráficos complejos o lectura de archivos, usa un kernel local/remoto.
```
