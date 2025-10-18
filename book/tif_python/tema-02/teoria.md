# Tema 02 · Sentencias de control

Basado en `resources_tif/apuntes_md/teoria/ProgramacionPythonTIF-Tema2.md`.

## Estructura general de un programa

- Lectura de datos (`input`), operaciones, salida (`print`).
- Declaración implícita de variables (por asignación) y tipado dinámico.

## Sentencias de control: visión general

- Gobiernan el flujo de ejecución: selección y repetición.
- Evaluaciones lógicas devuelven `True`/`False` (y la sangría es esencial).

## Selección: `if`, `if-else`, `elif`

```{code-cell} ipython3
x = int(input("Introduce un entero: "))

if x > 0:
    print("positivo")
elif x == 0:
    print("cero")
else:
    print("negativo")
```

Reglas clave:
- Dos puntos (`:`) tras la condición, bloque sangrado con 4 espacios.
- Cualquier número de ramas `elif`; `else` es opcional y sin condición.

## Repetición: bucles `for` y `while`

### `for` sobre iterables y `range`

```{code-cell} ipython3
# from 1 to 100 inclusive
for i in range(1, 101):
    pass

# iterar sobre una cadena
for ch in "ABC":
    print(ch)

# iterar con índice y valor
nums = [10, 20, 30]
for idx, val in enumerate(nums):
    print(idx, val)
```

Notas: `range(m, n)` llega hasta `n-1`; usa `range(m, n+1)` si quieres incluir `n`.

### `while`

```{code-cell} ipython3
total = 0
n = 1
while n <= 5:
    total += n
    n += 1
total
```

## Interrupción y control de bucles

- `break`: sale del bucle más interno.
- `continue`: salta a la siguiente iteración.
- `pass`: no hace nada (marcador de posición).

```{code-cell} ipython3
for i in range(10):
    if i == 5:
        break
    if i % 2 == 0:
        continue
    print(i)
```

## Buenas prácticas con sangría y condiciones

- Usa 4 espacios por nivel y evita mezclar tabs/espacios.
- Prefiere condiciones legibles y evita anidamiento profundo; usa `elif`.
