# Tema 01 · Introducción a Python

En este capítulo introducimos Python, su contexto, primeros pasos y conceptos básicos de entrada/salida y módulos.

::::::{topic} Objetivos
- Comprender el contexto y ventajas de Python.
- Ejecutar código y manejar entrada/salida básica.
- Conocer la importación y uso de módulos.
::::::

## Funcionamiento del ordenador

- El procesador ejecuta las instrucciones de un programa.
- Las instrucciones están en lenguaje máquina (bajo nivel y ligado al hardware).
- Programar en lenguaje máquina es posible, pero difícil y poco abstracto.

## El lenguaje Python

- Creado a finales de los 80, software libre y multiplataforma.
- Gran ecosistema de módulos (PyPI) y amplia comunidad.
- De alto nivel, interpretado, multiparadigma (estructural y OO).
- Extensión habitual `.py`; sensible a mayúsculas/minúsculas.

### Ventajas

| Ventajas          |
|-------------------|
| Simple y elegante |
| Productivo        |
| Portable          |
| Gran soporte      |
| Multiplataforma   |

## Instalando Python

- Opción mínima: instalador de python.org (intérprete + pip).
- Opción “completa”: gestores/entornos que añaden bibliotecas y utilidades.
- Para escribir/ejecutar: terminal o IDE (VS Code, Spyder, Colab…).

## ¿Qué es VS Code?

- Editor potente y extensible, multiplataforma.
- Soporta múltiples lenguajes y gestor de extensiones.
- Documentación de inicio rápido para Python en VS Code: https://code.visualstudio.com/docs/python/python-quick-start

## Mi primer programa en Python

```{code-cell} ipython3
print("hola mundo")
```

## Entrada de datos (input)

```{code-cell} ipython3
nombre = input("¿Cómo te llamas? ")
edad = int(input("¿Qué edad tienes? "))
print(f"Te llamas {nombre} y tienes {edad} años")
```

## Salida de datos (print)

Formas habituales de formatear cadenas:

```{code-cell} ipython3
nombre = "Juana"; edad = 18

# f-strings
print(f"Me llamo {nombre} y tengo {edad} años.")

# Especificadores de formato estilo %
print("Me llamo %s y tengo %d años" % (nombre, edad))

# .format
print("Me llamo {} y tengo {} años.".format(nombre, edad))
print("Me llamo {1} y tengo {0} años.".format(edad, nombre))
print("Me llamo {a} y tengo {b} años.".format(a=nombre, b=edad))
```

### Especificadores de formato (estilo `%`)

| Tipo  | Especificador | Significado      |
|-------|---------------|------------------|
| str   | %s            | Cadena de texto  |
| int   | %d, %i        | Entero           |
| float | %f, %g        | Real             |

Notas: `\t` tabulación, `\n` salto de línea, para imprimir `%` usa `%%`.

## Sentencia `import` y módulos

- Algunas funcionalidades están en módulos externos (p. ej., trigonometría en `math`).
- Para usarlos: instalarlos si es necesario y luego importarlos.
- Formas comunes:

```{code-cell} ipython3
# Importar el módulo completo
import math
x = math.pi/2
print("cos(x) =", math.cos(x))

# Importar símbolos concretos
from math import sin, radians
print("sin(90°) =", sin(radians(90)))

# Alias de módulo
import math as m
print("sqrt(2) =", m.sqrt(2))

# Inspección rápida (en local)
dir(math)[:5]
```

```{admonition} Recomendación
:class: tip
Para celdas ejecutables en el navegador, prefiere `math` y librerías de la stdlib. 
Evita dependencias pesadas salvo que definas kernels remotos.
```
