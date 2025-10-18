# Tema 05 · Ejercicios propuestos

Fuente: `resources_tif/apuntes_md/practica/Enunciados Tema 5 Python.md`

## Contenido del tema

- Arrays y operaciones NumPy; representación con Matplotlib.

## Enunciados básicos

1) `f(x) = log(x) * sin(x)` en [-50, 50] con 200 puntos.
- Genera con `np.linspace`; representa con `plt.plot` como verde con asteriscos y línea discontinua.
- Título, ejes, límites adecuados y leyenda.

2) Indexación de submatrices y operaciones.
- Define la matriz dada y extrae submatrices (usa `np.ix_`).
- Multiplica submatrices; exponencial de elementos; máximos/mínimos por fila/columna.

3) Ajuste lineal y cuadrático de los datos dados en subplots.
- Muestra coeficientes y gráficas con datos y modelos.

4) CSV estaciones meteorológicas.
- Carga `estacion_2867.csv` (mismo directorio) y calcula:
  - Temperatura media de noviembre de 1990.
  - Temperatura máxima de noviembre de 1992.
  - Temperatura mínima de 2010.
- Representa las temperaturas de noviembre de 1990, 1992 y 2010 con colores distintos y leyenda.

## Enunciados adicionales

5) Representa la aproximación de π (Gregory–Leibniz) vs. número de términos.

6) Representa la aproximación de π por Monte Carlo.
- Circunferencia unidad y puntos: en azul dentro, rojo fuera; título con el valor aproximado de π.

```{admonition} Nota
:class: note
Estos ejercicios requieren NumPy/Matplotlib; para mejor experiencia, usa un kernel local en lugar de Pyodide.
```
