# Tema 03 · Ejercicios propuestos

Fuente: `resources_tif/apuntes_md/practica/Practicas Python Tema 3.md`

## Contenido del tema

- Uso práctico de clases/objetos: atributos y métodos.
- Estructuras de datos: `list`, `tuple`, `dict`, `set`, `range`.
- Trabajo con cadenas.

## Enunciados básicos

1) Letra del NIF a partir del número.
- Implementa versión con lista (índice por resto `dni % 23`).
- Implementa versión con diccionario (mapa de resto→letra).

2) Lista de 10 números y operaciones.
- Lee 10 valores, ordénalos con `list.sort()`.
- Cuenta cuántas veces aparece `1` (`list.count(1)`).
- Indica si `11` está en la lista y la posición de `9`.

3) Números primos hasta N.
- Genera primos hasta un `N` dado; muestra longitud de la lista (`len`).
- Opción: usar `sympy.isprime` (requiere instalación local).

4) Estadística básica de texto.
- Cuenta palabras (`split`), espacios (`count(' ')`) y letras.
- Reemplaza todas las apariciones de “de” por “xx” (`replace`).

5) Comparación de textos con conjuntos.
- Pide dos textos; muestra palabras comunes y exclusivas de cada texto.
- Convierte a `set` y usa `union`, `intersection`, `difference`.

6) Diccionario de planetas y densidad.
- Diccionario con planeta→(volumen, masa), calcula densidad relativa.
- Recorre claves y valores; muestra resultados formateados.

```{admonition} Nota
:class: note
Para datos de ejemplo (tablas), puedes anexarlos como CSV/MD en `book/figures` y cargarlos desde las celdas, o pegarlos como tabla Markdown si son breves.
```
