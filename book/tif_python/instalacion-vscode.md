# Primeros pasos con VS Code

Basado en `resources_tif/apuntes_md/teoria/ProgramacionPythonTIF-VSCode.md`.

## Instalación de VS Code y extensión de Python

- Descarga: https://code.visualstudio.com/Download
- Instala la extensión “Python” del Marketplace.

## Workspace y organización

- Trabaja dentro de una carpeta (workspace) con tu código y recursos.
- Control de versiones integrado (Git) y terminal incluida.

## Entornos virtuales (venv)

```bash
# macOS/Linux (puede requerir: sudo apt-get install python3-venv)
python3 -m venv .venv

# Windows
python -m venv .venv

# Activar
source .venv/bin/activate      # macOS/Linux
.\.venv\Scripts\activate       # Windows
```

En VS Code: “Python: Select Interpreter” y elige el de `.venv`.

## Hola mundo y depuración

- Crea `hola.py` con `print("Hola mundo")` y ejecútalo.
- Inicia el depurador, añade breakpoints (F9) y observa variables, pila y consola.

```{admonition} Consejos
:class: tip
- Usa `Ctrl+Shift+P` para abrir la paleta de comandos.
- Configura el depurador con “Run and Debug” si necesitas ajustes personalizados.
```
