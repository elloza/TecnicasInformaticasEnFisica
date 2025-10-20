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

# Tema 06 · Ejercicios propuestos

Fuente: `resources_tif/apuntes_md/practica/Tema 6 Prácticas.md`

## Contenido del tema

- Pandas: `Series` y `DataFrame`.
- Lectura/escritura: CSV, Excel, SQL.
- Análisis, agregaciones y visualización.

## Enunciados básicos

1) DataFrame desde cero con la tabla de astronautas proporcionada.
- Crea el DataFrame a partir de un diccionario de listas.
- a) Países únicos (`pd.unique`) y su número.
- b) Número de registros.
- c) Convierte “Total Flight Time (ddd:hh:mm)” a minutos en una nueva columna.
- d) Astronauta con más horas de vuelo (`idxmax`, `loc`).
- e) Número de vuelos únicos (filtra por `Total Flights == 1`).
- f) Filtra astronautas de Estados Unidos.
- g) Media de horas por género.

2) Repite el análisis leyendo `astronautas.csv` desde disco.
- Barras por país (groupby→count→`sort_values`→`plot.bar`).
- Histograma de horas de vuelo (`plt.hist`, elige `bins`).

3) CO2.csv en DataFrame.
- a) Temperatura media, mínima y máxima y su gráfica.
- b) Humedad relativa media, mínima y máxima y su gráfica.
- c) CO2 con umbral de 800 ppm.
- d) Ocupación en el tiempo.

```{admonition} Consejos
:class: tip
- Usa `pd.to_datetime` para fechas y `df.set_index` para series temporales.
- Evita iterar filas; prefiere `groupby`, `agg`, `assign`, y operaciones vectorizadas.
```
