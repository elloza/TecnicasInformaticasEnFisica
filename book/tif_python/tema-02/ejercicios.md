# Tema 02 · Ejercicios propuestos

Fuente: `resources_tif/apuntes_md/practica/Enunciados Tema 2.md`

## Contenido del tema

- Sentencias selectivas: `if`, `elif`, `else`.
- Bucles: `for`, `while`.
- Interrupción: `break`, `continue`, `pass`.

## Enunciados básicos

1) Conversor de binario sin signo a decimal.
- Pide al usuario una cadena con el binario.
- Recorre las cifras con `enumerate` y acumula el valor en base 2.
- Salida de ejemplo: “El número binario 10111011 es 187 en decimal”.

2) Factorial de un número natural.
- Solicita un entero positivo; valida y repite entrada hasta que cumpla `n > 0`.
- Discute el crecimiento y límites prácticos al calcular factoriales grandes.

3) Patrón con asteriscos por consola.
- Construye el patrón indicado utilizando bucles (pueden ser anidados).

4) FizzBuzz personalizado.
- Recorre desde 1 hasta un número `N` introducido por el usuario.
- Múltiplos de 7: “Fizz”, múltiplos de 5: “Buzz”, de ambos: “FizzBuzz”.

5) Aproximación de π (Gregory–Leibniz).
- Pide una diferencia máxima entre dos términos consecutivos.
- Calcula términos hasta cumplir el criterio con `abs`.

```{math}
:label: eq-gregory
\frac{\pi}{4} = \sum_{k=0}^{\infty} \frac{(-1)^k}{2k+1}
```

## Enunciado adicional: π por Monte Carlo

- Tablero 1x1 con un cuarto de círculo de radio 1.
- Genera puntos `(x, y)` uniformes en `[0,1]` y cuenta los que caen en el cuarto de círculo.
- Para `t` lanzamientos y `g` aciertos: `\pi \approx 4 g / t`.

Sugerencias:
- `from random import random`
- Distancia: `d = sqrt(x**2 + y**2)`

```{admonition} Nota de ejecución
:class: note
Estos ejercicios se ejecutan localmente. En el navegador, evita dependencias externas o usa kernels remotos.
```
