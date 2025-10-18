# Tema 06 · Programación avanzada y análisis de datos

Basado en `resources_tif/apuntes_md/teoria/ProgramacionPythonTIF-Tema6.md`.

## Ecosistema de análisis

- NumPy: básicos y ajustes polinómicos.
- SciPy (`from scipy import stats`): estadística descriptiva y correlaciones.
- Pandas: estructuras tabulares y análisis.
- Seaborn: visualización estadística.
- scikit-learn: modelos y validación (fuera de alcance básico).

## Estadística descriptiva (NumPy + SciPy)

```{code-cell} ipython3
import numpy as np
from scipy import stats

d = np.random.randn(850)
np.mean(d), np.median(d), stats.mode(d, keepdims=True)[0]
```

Dispersión y relación entre variables:

```{code-cell} ipython3
d1 = np.random.randn(850)
d2 = np.random.randn(850)

np.var(d1), np.std(d1), np.cov(d1, d2)
stats.pearsonr(d1, d2), stats.spearmanr(d1, d2)
```

Forma de la distribución:

```{code-cell} ipython3
stats.skew(d), stats.kurtosis(d)
```

```{admonition} Nota
:class: note
En versiones recientes de SciPy, `stats.mode` requiere `keepdims=True` para mantener compatibilidad en el valor devuelto.
```
