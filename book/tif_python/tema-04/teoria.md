# Tema 04 · Funciones y módulos

Basado en `resources_tif/apuntes_md/teoria/ProgramacionPythonTIF-Tema4.md`.

## Funciones: definición y llamada

```{code-cell} ipython3
def sumando(a, b):
    c = a + b
    return c

x, y = 4, 8
z = sumando(x, y)
z
```

Reglas y notas:
- Paréntesis y separación por comas para argumentos; `return` devuelve el resultado y termina la función.
- Puede devolver múltiples valores: `return a, b`.
- Si no se indica `return`, el valor devuelto es `None`.

## Parámetros y mutabilidad

- Tipos inmutables (int, float, tuple) se comportan como “por valor”.
- Tipos mutables (list, dict, set) pueden modificarse dentro de la función.

```{code-cell} ipython3
def muta_lista(l):
    for i in range(len(l)):
        l[i] = 4

lista = [0, 1, 2]
muta_lista(lista)
lista
```

## Módulos externos y `import`

```{code-cell} ipython3
# import del módulo completo
import math
math.sqrt(2)

# import selectivo y alias
from math import pi, cos as c
c(pi)
```

Buenas prácticas:
- Coloca los imports al inicio del archivo.
- Usa alias concisos y claros cuando ayude a la lectura.

## Organización en módulos propios

- Define funciones en archivos `.py` (por ejemplo `TIF.py`).
- Impórtalas desde un script principal: `import TIF` o `from TIF import funcion`.
- El operador punto accede a funciones/variables definidas en el módulo.
