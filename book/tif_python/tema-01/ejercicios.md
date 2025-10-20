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

# Tema 01 · Ejercicios propuestos

Fuente: `resources_tif/apuntes_md/practica/Enunciados Tema 1 Python.md`

## Contenido del tema

- Familiarizarse con VS Code y el entorno de desarrollo.
- Variables y operadores. Casting entre tipos.
- Entrada/Salida por consola: `input`, `print`.
- `import`: importación de bibliotecas externas previamente instaladas.

## Enunciados básicos

1) Programa que determine si un número es par o impar.
- Usa `input` para leer (recuerda que devuelve `str`; haz casting cuando toque).
- Usa `print` para mostrar el resultado.
- Emplea el operador `%` (módulo).

2) Programa que pida nombre, apellidos, edad, peso, altura, número y letra del DNI y muestre exactamente:
- “Se llama XXX XXXX XXXX, tiene XX años, pesa XX.X kg, mide XX.XX m y su número de DNI es XXXXX y letra X.”
- Usa especificadores de formato o f-strings adecuadamente; realiza los castings necesarios.

3) Distancia entre dos coordenadas geográficas (grados decimales) usando la fórmula de Haversine.
- Importa `math` y usa `radians`, `cos`, `sin`, `asin`, `sqrt`.

```{math}
:label: eq-haversine
d = 2 r \arcsin\left(\sqrt{ \sin^2\!\left(\frac{\varphi_2-\varphi_1}{2}\right) + \cos\varphi_1\,\cos\varphi_2\,\sin^2\!\left(\frac{\lambda_2-\lambda_1}{2}\right) }\right)
```

Donde: `r = 6372.7954 km`; `\varphi` latitudes en radianes; `\lambda` longitudes en radianes.

4) Repite el ejercicio anterior utilizando la biblioteca `haversine`.
- Instálala en tu entorno local: `pip install haversine`.
- `import haversine` y consulta su documentación.

## Enunciados adicionales

1) Número de Reynolds para flujo en tubería circular.

```{math}
:label: eq-reynolds
\mathrm{Re} = \frac{\rho\, v\, D}{\mu}
```

- Pide por teclado `\rho` (kg/m^3), `v` (m/s), `D` (m) y `\mu` (Pa·s); calcula `Re` y clasifica el régimen: laminar (Re<2000), transición (2000≤Re<2700), turbulento (Re≥2700).
- Prueba con datos de la sangre en la aorta (aprox.):
  - Diámetro: 0.0238 m
  - Densidad: 1100 kg/m^3
  - Velocidad: 0.35 m/s
  - Viscosidad dinámica: 2.08×10^-2 Pa·s

```{admonition} Nota
:class: note
No incluyas soluciones; entrega solo los enunciados y, si procede, salidas de ejemplo.
```
