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

# Tema 04 · Ejercicios propuestos

Fuente: `resources_tif/apuntes_md/practica/Tema 4 Prácticas.md`

## Contenido del tema

- Definición, llamada y organización de funciones.
- Módulos externos y módulos propios.

## Enunciados básicos

1) Número de Reynolds en función.
- Implementa `reynolds(rho, v, D, mu)` → `(Re, regimen)` donde `regimen∈{"laminar","transición","turbulento"}`.

2) Implementa funciones (todas en el mismo fichero):
- `factorial(n)`, `csr(...)`, `is_leap_year(año)`, `ajuste_lineal(x, y)`.
- Añade un bloque de prueba al final para verificar su funcionamiento.

3) Módulo propio `TIF.py`.
- Mueve las funciones anteriores a `TIF.py`.
- Crea `Principal.py` que importe y use dichas funciones (p. ej. `from TIF import factorial`).
- Investiga el directorio `__pycache__`.

4) Función `get_haversine_distance`.
- Recibe cuatro parámetros: lat1, lon1, lat2, lon2 (grados decimales) y devuelve la distancia.

5) Función que extienda una lista con primos.
- Si la lista está vacía, añade los dos primeros primos; en otro caso, añade los dos siguientes al último primo de la lista. Llama 100 veces y cuenta.

6) Distancia de frenado.
- Dada `v0` (km/h) y `μ`, calcula la distancia `d` tras frenar; pasa `v0` a m/s.

```{admonition} Nota
:class: note
Para ejercicios con `requests` o APIs (Starlink), recuerda que requieren conexión y no se ejecutarán en el navegador sin kernel remoto.
```
