#!/usr/bin/env python3
"""
Script para agregar metadatos Jupytext a archivos Markdown con celdas de código.
Esto permite que sphinx-thebe detecte y haga ejecutables las celdas {code-cell}.
"""

import os
from pathlib import Path

# Metadatos Jupytext que se agregarán al inicio de cada archivo
JUPYTEXT_FRONTMATTER = """---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

"""

def has_jupytext_metadata(file_path):
    """Verifica si el archivo ya tiene metadatos Jupytext."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        return content.startswith('---\njupytext:')

def add_jupytext_metadata(file_path):
    """Agrega metadatos Jupytext al inicio del archivo si no los tiene."""
    if has_jupytext_metadata(file_path):
        print(f"⏭️  Saltando {file_path.name} (ya tiene metadatos)")
        return False
    
    with open(file_path, 'r', encoding='utf-8') as f:
        original_content = f.read()
    
    # Agregar metadatos al inicio
    new_content = JUPYTEXT_FRONTMATTER + original_content
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ Agregados metadatos a {file_path.name}")
    return True

def process_directory(directory):
    """Procesa todos los archivos .md en el directorio y subdirectorios."""
    directory = Path(directory)
    
    # Buscar archivos teoria.md y ejercicios.md en tema-XX
    pattern_files = [
        'tema-*/teoria.md',
        'tema-*/ejercicios.md'
    ]
    
    files_processed = 0
    files_skipped = 0
    
    for pattern in pattern_files:
        for file_path in directory.glob(pattern):
            if add_jupytext_metadata(file_path):
                files_processed += 1
            else:
                files_skipped += 1
    
    return files_processed, files_skipped

def main():
    """Función principal."""
    print("🚀 Agregando metadatos Jupytext a archivos Markdown...")
    print("=" * 60)
    
    # Directorio base de tif_python
    base_dir = Path(__file__).parent / 'book' / 'tif_python'
    
    if not base_dir.exists():
        print(f"❌ Error: No se encontró el directorio {base_dir}")
        return
    
    processed, skipped = process_directory(base_dir)
    
    print("=" * 60)
    print(f"✅ Completado:")
    print(f"   - Archivos procesados: {processed}")
    print(f"   - Archivos saltados: {skipped}")
    print(f"   - Total: {processed + skipped}")
    print("\n💡 Próximo paso: Ejecutar 'jupyter-book build book --all'")

if __name__ == '__main__':
    main()
