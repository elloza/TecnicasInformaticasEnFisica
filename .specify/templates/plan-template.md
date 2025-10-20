# Tema Plan: [NN-TITLE]

**Tema**: `tema-NN-[slug]` | **Date**: [DATE] | **Constitution**: v1.0.0
**Input**: Learning objectives, Content sources (`resources_tif/`), Curriculum map

**Note**: This template guides tema creation following TIF TeachBook constitution.

---

## Summary

[Brief 2-3 sentence description of what this tema teaches and why it matters for the curriculum]

**Example**: "Tema-02 covers list comprehensions and functional programming patterns in Python, essential foundations for data processing in numerical physics computations."

---

## Learning Context

**Position in Curriculum**: [Tema-NN] out of [total], comes after [Tema-MM], prerequisite for [Tema-PP]

**Learning Outcomes**: (What will learners demonstrate by tema end?)
- [ ] Learning Outcome 1 (concrete, testable skill)
- [ ] Learning Outcome 2 (concrete, testable skill)
- [ ] Learning Outcome 3 (concrete, testable skill)

**Pedagogical Approach**: [e.g., "Spiral learning: introduce concept → practice basics → apply to physics problem → extend"]

---

## Technical Requirements

**Python Version**: ≥3.10  
**Required Libraries**: [e.g., numpy, matplotlib, scipy — exact versions from `requirements.txt`]  
**External Dependencies**: [e.g., none, or "requests (local kernel only)" with explanation]  
**Data Files**: [if needed, e.g., "data/tema-02-dataset.csv"]  
**Estimated Time**: [X hours for theory] + [Y hours for exercises] = [total]  
**Target Audience**: [e.g., "Physics students with Python basics (Tema-00)"]  
**Difficulty**: [Básico / Intermedio / Avanzado]

---

## Constitution Conformance Check

**GATE: Verify these before drafting content**

| Principle | Requirement | Status |
|-----------|------------|--------|
| I. Content-First, Resource-External | All content in `/book/tif_python/tema-NN/`, NO `resources_tif/` committed | ☐ |
| II. Module-Structured | File pattern: `teoria.md` + `ejercicios.md` in `tema-NN/` folder | ☐ |
| III. Live Code + Local-First | All code cells: `{code-cell} ipython3`, executable locally + Pyodide | ☐ |
| IV. Test-Driven Exercises | Each exercise: pedagogical objective, success criteria, automated tests | ☐ |

**If ANY item unchecked**: Discuss with team before proceeding to Draft phase

---

## Content Structure

### Theory (`book/tif_python/tema-NN/teoria.md`)

**Sections** (adjust count/titles as needed):

- [ ] Section 1: Conceptual Foundation
  - Key concepts, definitions, equations
  - 3-5 executable code examples
  - Why this matters (connection to physics/practice)

- [ ] Section 2: Practical Applications
  - Real-world scenarios where concepts apply
  - 3-5 worked examples (with code)
  - Common pitfalls + how to avoid them

- [ ] Section 3: Advanced Topics (if applicable)
  - Extensions, optimizations, alternative approaches
  - 2-3 challenging examples
  - Integration with previous temas

**Diagrams/Figures**: [List diagrams to add to `book/figures/`]
- Figure 1: [description]
- Figure 2: [description]

### Exercises (`book/tif_python/tema-NN/ejercicios.md`)

**Difficulty Distribution**:

- **Básico** (40%): Direct application of theory, guided
  - Exercises 1-4: basic concepts, syntax practice
  - Expected time: 5-10 min each
  
- **Intermedio** (40%): Combine concepts, less scaffolding
  - Exercises 5-8: apply multiple concepts together
  - Expected time: 10-15 min each
  
- **Avanzado** (20%): Synthesis, open-ended, physics integration
  - Exercises 9-10+: real physics problems, design choices
  - Expected time: 20-30 min each

**Exercise Template** (each exercise must have):
```markdown
## Ejercicio N: [Title]

:::{topic} Objetivo Pedagógico
[What will learner demonstrate?]
:::

**Dificultad**: [básico/intermedio/avanzado] | **Tiempo estimado**: X min

**Criterios de éxito**:
- ✓ [Specific testable criterion 1]
- ✓ [Specific testable criterion 2]
- ✓ [Specific testable criterion 3]

[Code skeleton with TODOs]

[Expected output OR test assertions]
```

---

## Sourcing & Adaptation

**Source Materials** (from `resources_tif/`):

- [ ] Document 1: `resources_tif/apuntes_md/teoria/[filename].md`
  - [ ] Pages/sections to reuse: [X-Y]
  - [ ] Adaptation needed: [Yes/No] — if Yes, explain
  
- [ ] Document 2: `resources_tif/apuntes_md/practica/[filename].md`
  - [ ] Exercises to adapt: [list]
  - [ ] Changes: [simplify/extend/test-ify]

**New Content Created** (not from sources):
- [ ] Section/Topic X: [description]
- [ ] Exercise Y: [description]

**Decision Log**:
- Why not use [specific section] from sources? [Rationale]
- Why create new [section]? [Rationale]

---

## Project Structure

```
book/
├── tif_python/
│   └── tema-NN/
│       ├── teoria.md           (Theory with code examples)
│       └── ejercicios.md       (10-15 exercises with tests)
│
└── figures/
    ├── tema-NN-fig1.svg        (Diagram 1)
    ├── tema-NN-fig2.png        (Screenshot/plot fallback)
    └── …

.specify/
└── tasks/
    └── tema-NN.md              (Execution task plan)
```

---

## Cross-Tema Dependencies

**Prerequisite Temas**: [List Temas that must be completed first]
- Tema-00: Python Fundamentals ✓ (always required)
- Tema-NN: [topic] (if applicable)

**Prerequisite Knowledge**: [What learner must know before this tema]
- [Knowledge item 1]
- [Knowledge item 2]

**This Tema Enables**: [What future temas build on this]
- Tema-MM: [topic] will use [concept from this tema]
- Tema-PP: [topic] extends [concept from this tema]

---

## Complexity & Risk Assessment

**Pedagogical Complexity**: [1=simple / 5=complex]

| Aspect | Rating | Notes |
|--------|--------|-------|
| Conceptual difficulty | [1-5] | [Why? What's hardest?] |
| Required code skills | [1-5] | [What Python features needed?] |
| Interdependencies | [1-5] | [How many prior concepts?] |
| Physics integration | [1-5] | [How closely tied to physics?] |

**Execution Risks**: 

- [ ] Risk 1: [description] → Mitigation: [how to avoid]
- [ ] Risk 2: [description] → Mitigation: [how to avoid]

---

## Constitutional Violations (if any)

*Fill ONLY if this tema violates constitution; otherwise SKIP*

| Violation | Why Necessary | Simpler Alternative Rejected | Timeline to Fix |
|-----------|---------------|------------------------------|-----------------|
| [e.g., Heavy dependency outside Pyodide] | [business reason] | [why not viable] | [v1.1 or later] |

---

## Sign-Off Checklist (Before Drafting)

- [ ] Learning outcomes clearly defined + testable
- [ ] All 4 constitution principles understood + planned for
- [ ] Source materials reviewed and curation plan documented
- [ ] Technical dependencies identified (Python, libraries, data)
- [ ] Estimated time realistic + feasible within timeline
- [ ] Cross-tema dependencies mapped
- [ ] Team agrees on difficulty distribution + exercise count

**Plan Approved By**: [name/date] ✅

---

**Template Version**: 1.0.0 | **Aligned with Constitution**: v1.0.0 | **Last Updated**: 2025-10-20
````

