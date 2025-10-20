<!--
SYNC IMPACT REPORT
==================
Version: 0.0.0 (template) → 1.0.0 (MINOR: 4 core principles + governance framework)
Bump Rationale: Initial TeachBook constitution; establishes content migration workflow, testing discipline, and module-first curriculum architecture.

Modified Principles: N/A (first instantiation)
Added Sections: Repository Structure & Build, Development Workflow (lifecycle table), complete Governance
Removed Sections: N/A

Templates Requiring Updates:
  ✅ .specify/templates/tasks-template.md — add "Pre-Publication Verification" phase
  ⚠ .specify/templates/plan-template.md — verify tema planning checklist aligns with principles
  ⚠ .specify/templates/spec-template.md — add "Exercise Success Criteria" requirement

Deferred Items: None

Follow-up Actions:
  1. Verify resources_tif/ exclusion in .gitignore (confirm presence & test with `git check-ignore`)
  2. Create tema-00 (setup/environment) as proof-of-concept
  3. Establish GitHub Actions pre-commit check for resources_tif/ leakage
-->

# Técnicas Informáticas en Física (TIF) TeachBook Constitution

**Project**: TIF — Jupyter Book migration and publication platform
**Scope**: Educational content (theory + exercises) for a physics informatics course
**Platform**: TeachBooks (Jupyter Book + Sphinx extensions)

---

## Core Principles

### I. Content-First, Resource-External

- All published content lives in `/book/` (theory, exercises, examples, figures)
- Original sources in `resources_tif/` are reference-only and **MUST NOT** be committed to the repository
- `.gitignore` enforces `resources_tif/` exclusion; verify on every merge via GitHub Actions
- Content migration: manually curate and adapt from `resources_tif/` → write/test in `/book/` → commit only the final product
- **Rationale**: Keeps repository lean, simplifies collaboration, respects source licensing, enables clean history

### II. Module-Structured Curriculum

- Each topic (Tema 01, Tema 02, …) is a self-contained module with consistent internal structure:
  - **Teoría** (`teoria.md`): conceptual explanation, code examples, diagrams, learning objectives
  - **Ejercicios** (`ejercicios.md`): graded practice problems (basic → advanced), expected outputs
  - **Setup** (if required): environment configuration, dependency installation, system checks
- Modules follow naming convention: `tif_python/tema-NN/teoria.md`, `tif_python/tema-NN/ejercicios.md`
- Cross-module dependencies documented in `_toc.yml` and exercise preambles (e.g., "Requires: Tema 02")
- **Rationale**: Enables independent study, parallel content review, flexible sequencing, easy maintenance

### III. Live Code + Local-First Execution

- All code cells marked executable (`{code-cell} ipython3`) render in browser via Pyodide (no install required for learners)
- Heavy dependencies (requests, file I/O, system commands, remote APIs) explicitly labeled with deprecation warning + local-kernel recommendation in cell metadata
- All plots, tables, and visualizations **MUST** render in browser OR include fallback static image (`.png` in `figures/`)
- Code output expected to be reproducible in both browser and local Python environments (≥3.10)
- **Rationale**: Maximizes accessibility and peer-learning; preserves scientific workflows; lowers barrier to entry

### IV. Test-Driven Exercise Design

- Every exercise **MUST** declare (before code):
  - **Objetivo Pedagógico** (`:topic:` admonition): what learner will demonstrate
  - **Criterios de Éxito** (expected output, plots, file artifacts, or automated assertions)
  - **Dificultad** (básico/intermedio/avanzado) and estimated time
- Exercises may include optional **hidden test cells** (e.g., `# TEST: check if result > 0`) for auto-grading in Jupyter
- Before publishing cada tema, **one independent reviewer** executes all exercises locally + in browser; documents pass/fail + feedback
- **Rationale**: Ensures pedagogical quality, catches regressions early, supports self-assessment, reduces support burden

---

## Repository Structure & Build

### Folder Layout

```
book/
├── intro.md                         (Course overview, prerequisites)
├── _config.yml                      (TeachBooks config)
├── _toc.yml                         (Table of contents, theme ordering)
├── tif_python/
│   ├── instalacion-vscode.md        (Environment setup guide)
│   ├── tema-00/
│   │   ├── teoria.md                (Introduction to Python basics)
│   │   └── ejercicios.md
│   ├── tema-01/
│   │   ├── teoria.md
│   │   └── ejercicios.md
│   ├── tema-02/
│   │   ├── teoria.md
│   │   ├── ejercicios.md
│   │   └── recursos/                (data files, example datasets)
│   └── …
├── figures/                         (images, logos, screenshots)
│   ├── vscode-setup.png
│   ├── tema-01-architecture.svg
│   └── …
├── requirements.txt                 (Python + Jupyter dependencies)
└── _static/                         (Custom CSS, branding)

resources_tif/                        ⛔ NEVER COMMITTED (in .gitignore)
├── apuntes_md/teoria/
├── apuntes_md/practica/
├── originals/
└── …

.github/
├── workflows/
│   └── call-deploy-book.yml         (Build + publish on main push)
└── …
```

### Build & Deploy Workflow

- **Local build**: `pip install -r requirements.txt && jupyter-book build book`
- **Local preview**: Open `book/_build/html/index.html` in browser
- **CI/CD**: GitHub Actions (`.github/workflows/call-deploy-book.yml`) auto-builds on push to `main`
- **Site**: Published to `https://<username>.github.io/TecnicasInformaticasEnFisica/`
- **Pre-commit check**: Verify `resources_tif/` files NOT staged via GitHub Actions

---

## Development Workflow

### Per-Tema Lifecycle

| Phase | Owner | Deliverable | Checkpoint |
|-------|-------|-------------|-----------|
| **Plan** | Author | Tema outline, learning objectives, exercise list | Documented in `.specify/tasks/tema-NN.md` |
| **Draft** | Author | `.md` or `.ipynb` with all sections + code cells | Local execution succeeds |
| **Self-Test** | Author | All code cells execute locally; exercises produce expected output | Test report in PR description |
| **Peer Review** | Reviewer | Browser + local execution verification; pedagogical feedback | Checklist in `.specify/templates/tasks-template.md` |
| **Publish** | Author | Merge to `main`; build succeeds; site updates | GitHub Actions green + site live |

### Quality Gates (MUST PASS)

- ✅ No `resources_tif/` files in Git history
- ✅ All code cells execute without errors (local Python ≥3.10)
- ✅ Exercises render in browser without dependency errors
- ✅ At least one peer has manually verified exercise outputs
- ✅ Cross-module references (if any) documented and tested

---

## Governance

### Compliance & Principle Enforcement

- **Constitution supersedes** all other practices and style guides
- **All PRs** MUST verify:
  - No `resources_tif/` commits via GitHub Actions pre-commit check
  - Principle compliance checklist completed (see `.specify/templates/tasks-template.md`)
  - Constitution-level violations trigger request for revision BEFORE merge
- **Non-compliance** does NOT block merge if remediation plan is documented in PR and completion timeline agreed

### Amendment Procedure

1. **Proposed Change**: Open GitHub issue or discussion with rationale & affected sections
2. **Review Window**: Minimum 1 week for feedback; resolve objections asynchronously
3. **Approval**: Consensus from authors; merge PR to `.specify/memory/constitution.md`
4. **Communication**: Update linked runtime docs (`README.md`, `book/intro.md` references)
5. **Version Bump**: Increment per semver rules; document change rationale in commit message
6. **Propagate**: Update dependent templates (`tasks-template.md`, `spec-template.md`, etc.)

### Versioning Policy

- **MAJOR** (x.0.0): Principle removal OR fundamental workflow redefinition (rare; requires 2-week notice)
- **MINOR** (1.x.0): New principle added, significant section expansion, new module archetype, governance clarification
- **PATCH** (1.0.x): Typo fixes, wording clarification, non-breaking corrections, date updates

### Review Cadence & Metrics

- **Per-Tema**: Before publishing, one-pass verification of all 4 principles (checklist in task template)
- **Monthly**: Spot-check recent commits against principles (automated via GitHub discussions)
- **Quarterly**: Full constitution review; propose amendments if patterns emerge

---

**Version**: 1.0.0 | **Ratified**: 2025-10-20 | **Last Amended**: 2025-10-20
