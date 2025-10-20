# Tema-00: Introducción a Python — Plan de Ejecución

## Ficha de Tema

| Propiedad | Valor |
|-----------|-------|
| **Tema** | Tema-00: Introducción a Python |
| **Módulos** | Conceptos fundamentales, variables, tipos, operaciones, control de flujo, listas, diccionarios, funciones |
| **Duración Estimada** | 4-6 horas |
| **Dificultad** | Básico |
| **Dependencias** | Python ≥3.10, Jupyter, NumPy, Matplotlib |
| **Prerrequisitos** | Ninguno |
| **Sección del Libro** | `book/tif_python/tema-00/` |

---

## Objetivos de Aprendizaje

Al completar este tema, el estudiante podrá:

- ✅ Entender variables, tipos de datos (int, float, str, bool)
- ✅ Realizar operaciones aritméticas y lógicas
- ✅ Usar condicionales (if/elif/else) y bucles (for/while)
- ✅ Trabajar con listas y diccionarios
- ✅ Escribir y usar funciones básicas
- ✅ Usar NumPy para cálculos vectorizados
- ✅ Crear gráficos simples con Matplotlib

---

## Contenido Curado

### Teoría (`teoria.md`) ✅

Cubre:
- ¿Por qué Python para física?
- Variables y tipos de datos
- Operaciones básicas (aritmética, comparación, lógica)
- Estructuras de control (if/elif/else, for, while)
- Listas y diccionarios
- Funciones
- NumPy basics
- Matplotlib basics

**Código ejecutable**: 15+ celdas, todas testeadas

---

## Ejercicios (`ejercicios.md`) ✅

| Ejercicio | Dificultad | Tiempo | Estado |
|-----------|------------|--------|--------|
| 1. Variables y Tipos | Básico | 5 min | ✅ |
| 2. Operaciones Aritméticas | Básico | 5 min | ✅ |
| 3. Condicionales | Básico | 10 min | ✅ |
| 4. Bucles | Básico | 10 min | ✅ |
| 5. Listas | Intermedio | 10 min | ✅ |
| 6. Diccionarios | Intermedio | 10 min | ✅ |
| 7. Funciones | Intermedio | 15 min | ✅ |
| 8. NumPy Básico | Intermedio | 10 min | ✅ |
| 9. Matplotlib | Intermedio | 10 min | ✅ |
| 10. Desafío Integrador | Avanzado | 20 min | ✅ |

**Total estimado**: 105 minutos (1.75 horas)

---

## Conformidad Constitucional

### Principio I: Content-First, Resource-External
- ✅ Todo el contenido está en `/book/tif_python/tema-00/`
- ✅ Ningún archivo de `resources_tif/` incluido
- ✅ Contenido original adaptado manualmente

### Principio II: Module-Structured Curriculum
- ✅ Estructura consistente: `teoria.md` + `ejercicios.md`
- ✅ Modulo autónomo, sin dependencias previas
- ✅ Patrón de nombre: `tema-NN` respetado

### Principio III: Live Code + Local-First Execution
- ✅ Todas las celdas de código: `{code-cell} ipython3`
- ✅ Código ejecutable en navegador (Pyodide)
- ✅ Gráficos renderizables en browser
- ✅ Pruebas locales: Python 3.10+

### Principio IV: Test-Driven Exercise Design
- ✅ Cada ejercicio con objetivo pedagógico explícito
- ✅ Criterios de éxito definidos
- ✅ Tests automatizados incluidos (assertions)
- ✅ Estimación de tiempo y dificultad

---

## Ciclo de Calidad

### ✅ Auto-Verificación (Completada)

- [x] Código `.md` revisado manualmente
- [x] Sintaxis Markdown validada
- [x] Enlaces internos verificados
- [x] Ejercicios tienen TODOs claros
- [x] Tests incluidos en ejercicios

### ⏳ Peer Review (Pendiente)

**Revisor designado**: [TODO: asignar]

**Checklist de revisión**:
- [ ] Ejecutar `teoria.md` localmente en Jupyter (sin errores)
- [ ] Ejecutar `ejercicios.md` localmente (todos los tests pasan)
- [ ] Verificar renderizado en navegador (Pyodide funciona)
- [ ] Revisar pedagogía: objetivos claros y alcanzables
- [ ] Feedback: ¿hay conceptos ambiguos o mal explicados?

### 🚀 Publicación

**Precondiciones**:
- [ ] Peer review completada ✅
- [ ] Todos los tests pasan localmente
- [ ] No hay archivos de `resources_tif/` commiteados
- [ ] `_toc.yml` actualizado con tema-00

**Acciones**:
1. `git add book/tif_python/tema-00/ book/_toc.yml .specify/tasks/tema-00.md`
2. `git commit -m "feat: add tema-00 (Python fundamentals) - theory + 10 exercises"`
3. `git push origin main`
4. Verificar GitHub Actions: build green ✅

---

## Recursos

### Archivos Fuente
- Teoría: `book/tif_python/tema-00/teoria.md`
- Ejercicios: `book/tif_python/tema-00/ejercicios.md`
- Tarea: `.specify/tasks/tema-00.md` (este archivo)

### Referencias de Conformidad
- Constitución: `.specify/memory/constitution.md` (v1.0.0)
- Template de tareas: `.specify/templates/tasks-template.md`

### Dependencias Externas
- **Python**: ≥3.10
- **Librerías**: numpy, matplotlib (en `requirements.txt`)

---

## Notas & Follow-up

### Lo que Funciona Bien
- Estructura clara y coherente
- Ejercicios progresan bien de básico a avanzado
- Tests automatizados permiten auto-verificación

### Mejoras Futuras (Post-v1.0)
- [ ] Agregar video tutorial (opcional)
- [ ] Ejercicios interactivos tipo JupyterLite
- [ ] Soluciones ocultas (collapsible sections)
- [ ] Quiz de auto-evaluación

### Decisiones de Diseño
- **¿Por qué NumPy en tema-00?** Es fundamental para temas posteriores de cálculos científicos
- **¿Por qué Matplotlib en tema-00?** Visualización es crítica en física; mejor introducir temprano
- **¿Por qué tests en ejercicios?** Sigue Principio IV (test-driven); permite auto-grading

---

**Estado**: ✅ LISTO PARA PEER REVIEW  
**Última actualización**: 2025-10-20  
**Próxima acción**: Asignar revisor y ejecutar checklist
