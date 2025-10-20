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

# Tema 03 · Tipos y estructuras de datos

Basado en `resources_tif/apuntes_md/teoria/ProgramacionPythonTIF-Tema3.md`.

## Objetos, clases y métodos (visión práctica)

- Todo en Python es un objeto (instancia de una clase) con atributos y métodos.
- Acceso con operador punto: `obj.atributo`, `obj.metodo(...)`.

## Cadenas (str)

```{code-cell} ipython3
s = "Hola, Python"
s.lower(), s.upper(), s.replace("Python", "TIF"), s.split()
```

Formateo: f-strings, `%`, `.format` (ver Tema 1).

## Listas (list)

```{code-cell} ipython3
nums = [3, 1, 4, 1, 5]
nums.append(9); nums.sort(); nums.count(1), 11 in nums
```

## Tuplas (tuple)

```{code-cell} ipython3
t = (1, 2, 3)
len(t), t[0]
```

## Diccionarios (dict)

```{code-cell} ipython3
d = {"a": 1, "b": 2}
d["c"] = 3
list(d.keys()), list(d.values()), d.get("x", 0)
```

## Conjuntos (set)

```{code-cell} ipython3
A = {1, 2, 3}
B = {3, 4}
A | B, A & B, A - B
```

## Rango (range)

```{code-cell} ipython3
list(range(5)), list(range(2, 7)), list(range(0, 10, 2))
```

## Comprensiones

```{code-cell} ipython3
[x*x for x in range(6) if x % 2 == 0]
{c: ord(c) for c in "abc"}
```
