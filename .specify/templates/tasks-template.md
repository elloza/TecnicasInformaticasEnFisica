---
description: "Task list template for TeachBook tema creation and publication"
---

# Tasks: Tema [NN] — [Title]

**Input**: Constitution (`.specify/memory/constitution.md`), Learning objectives, Content sources
**Prerequisites**: plan.md (required), spec.md (learning outcomes), research.md (source materials)

**Outputs**: 
- `book/tif_python/tema-NN/teoria.md` (theory with executable code cells)
- `book/tif_python/tema-NN/ejercicios.md` (10-15 exercises with tests)
- `.specify/tasks/tema-NN.md` (this task plan)

**Constitution Compliance**: All tasks MUST verify adherence to 4 core principles:
1. **Content-First, Resource-External**: No `resources_tif/` files committed
2. **Module-Structured Curriculum**: `teoria.md` + `ejercicios.md` pattern
3. **Live Code + Local-First Execution**: All code cells executable in Pyodide
4. **Test-Driven Exercise Design**: Exercises with pedagogical objectives + automated tests

---

## Format: `[ID] [P?] [Phase] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Phase]**: Workflow phase (Plan → Draft → Self-Test → Peer Review → Publish)
- Include exact file paths and constitution principles referenced

---

## Phase 1: Plan (Definition & Curation)

**Purpose**: Define tema scope, objectives, and map content from `resources_tif/`

**Conformance**: Principles II (Module-Structured) + I (Content-First)

- [ ] T001 Define learning objectives (3-5 concrete skills learners will demonstrate)
- [ ] T002 Outline theory sections (conceptual flow, key equations, visualizations)
- [ ] T003 Design 10-15 exercise problems (graduated: básico → intermedio → avanzado)
- [ ] T004 [P] Map source materials from `resources_tif/` (document what to reuse/adapt/create)
- [ ] T005 [P] List Python dependencies needed (NumPy, Matplotlib, SciPy, etc.)
- [ ] T006 Identify cross-tema dependencies (e.g., "Requires: Tema 02")
- [ ] T007 Estimate time investment (theory + exercises) per learner

**Checkpoint**: Plan documented in `.specify/tasks/tema-NN.md` — ready for Draft phase

---

## Phase 2: Draft (Content Creation)

**Purpose**: Write teoria + ejercicios from plan, prepare code cells

**Conformance**: Principles III (Live Code) + II (Module-Structured)

### Theory Writing

- [ ] T008 [P] Write Section 1: Conceptual foundation + 3-5 code examples in `book/tif_python/tema-NN/teoria.md`
- [ ] T009 [P] Write Section 2: Practical applications + 3-5 code examples
- [ ] T010 [P] Write Section 3: Advanced topics (if applicable) + 2-3 code examples
- [ ] T011 Add diagrams/figures to `book/figures/` (SVG or PNG)
- [ ] T012 Verify all code cells marked `{code-cell} ipython3`
- [ ] T013 Add rationale sections explaining "why" for each major concept

### Exercise Writing

- [ ] T014 [P] Write Exercise 1-3: Básico difficulty (direct application of theory)
  - Each with: `:topic:` admonition (pedagogical objective), success criteria, estimated time
  - Include code skeleton (TODOs) + solution section + tests
- [ ] T015 [P] Write Exercise 4-7: Intermedio difficulty (combining concepts)
- [ ] T016 [P] Write Exercise 8-10: Avanzado difficulty (synthesis/extension)
- [ ] T017 Add "Checklist de Revisión" section at end of `ejercicios.md`

**Checkpoint**: Draft complete — all sections written, code not yet tested

---

## Phase 3: Self-Test (Local Execution Verification)

**Purpose**: Ensure all code cells execute correctly in local Jupyter environment

**Conformance**: Principle III (Live Code + Local-First Execution)

- [ ] T018 Execute every code cell in `teoria.md` locally (Python ≥3.10)
  - [ ] Document any errors in PR description
  - [ ] Fix errors and re-run until all pass
- [ ] T019 Execute every exercise in `ejercicios.md` locally
  - [ ] Run all automated tests (assertions) — must all pass ✅
  - [ ] Verify expected outputs match documentation
  - [ ] Time each exercise — confirm estimates are realistic
- [ ] T020 Check for heavy dependencies (requests, file I/O, APIs)
  - [ ] If present: add deprecation warning + "local kernel recommended" note
- [ ] T021 Verify all plots/visualizations render correctly
  - [ ] If not: add fallback `.png` image to `book/figures/`
- [ ] T022 Validate Markdown syntax with `markdownlint` (optional)

**Checkpoint**: All code runs locally without errors — ready for Peer Review

---

## Phase 4: Peer Review (Independent Validation)

**Purpose**: Have independent reviewer verify pedagogical quality, code correctness, browser compatibility

**Conformance**: Principle IV (Test-Driven Exercise Design)

**Reviewer checklist**:

- [ ] T023 [Reviewer] Run all code cells locally in Jupyter — all pass? ✅
- [ ] T024 [Reviewer] Test exercises in browser (Pyodide) if possible
  - [ ] Which exercises work? Which fail? Document in review comment
- [ ] T025 [Reviewer] Verify pedagogical objectives are clear
  - [ ] Can you understand what each exercise expects the learner to demonstrate?
  - [ ] Are success criteria testable?
  - [ ] Provide feedback if ambiguous
- [ ] T026 [Reviewer] Check for confusing explanations or gaps
  - [ ] Highlight sections that could be clearer
  - [ ] Suggest additional examples if needed
- [ ] T027 [Reviewer] Verify exercises are appropriately graduated (básico → avanzado)
- [ ] T028 [Reviewer] Confirm no `resources_tif/` files referenced in content
- [ ] T029 [Reviewer] Sign-off: "✅ Approved for publication"

**Checkpoint**: Peer review complete + feedback addressed — ready for Publish

---

## Phase 5: Publish (Integration & Deployment)

**Purpose**: Commit tema to main branch, verify build succeeds, site updates

**Conformance**: Principle I (Content-First, Resource-External)

- [ ] T030 Address all peer review feedback
  - [ ] Re-test locally if changes made
- [ ] T031 Update `_toc.yml` to register tema-NN:
  ```yaml
  - file: tif_python/tema-NN/teoria.md
    sections:
    - file: tif_python/tema-NN/ejercicios.md
  ```
- [ ] T032 Verify no `resources_tif/` files in staging area:
  ```bash
  git diff --cached --name-only | grep resources_tif
  ```
  (Should return nothing)
- [ ] T033 Commit changes:
  ```bash
  git add book/tif_python/tema-NN/ book/_toc.yml .specify/tasks/tema-NN.md
  git commit -m "feat: add tema-NN ([title]) - theory + exercises + task plan"
  ```
- [ ] T034 Push to main: `git push origin main`
- [ ] T035 Verify GitHub Actions build succeeds (green ✅)
- [ ] T036 Verify site publishes and tema-NN appears in live book

**Checkpoint**: Tema published! Visible at `https://<username>.github.io/TecnicasInformaticasEnFisica/`

---

## Pre-Publication Verification Checklist

Before merging ANY tema to main, verify:

| Item | Principle | Status |
|------|-----------|--------|
| Theory: All code cells execute locally (Python ≥3.10) | III | ☐ |
| Exercises: All tests pass locally (no failures) | IV | ☐ |
| Exercises: Each has pedagogical objective + success criteria | IV | ☐ |
| Plots/visualizations render in browser OR have static fallback | III | ☐ |
| No `resources_tif/` files in Git history | I | ☐ |
| Module follows `tema-NN/teoria.md` + `tema-NN/ejercicios.md` pattern | II | ☐ |
| Cross-tema dependencies documented in `ejercicios.md` preamble | II | ☐ |
| Independent reviewer has signed off ✅ | IV | ☐ |
| `_toc.yml` updated with tema entry | — | ☐ |

**All items MUST be checked before publication**

---

## Dependencies & Execution Order

### Within-Tema Flow (Sequential)

1. **Phase 1: Plan** (define scope)
2. **Phase 2: Draft** (write content — can parallelize T008-T016)
3. **Phase 3: Self-Test** (verify locally — author only)
4. **Phase 4: Peer Review** (independent validation — reviewer only)
5. **Phase 5: Publish** (merge to main)

### Between-Temas (Parallel Allowed)

- Multiple authors can work on different temas in parallel
- Each tema follows the same 5-phase flow independently
- Temas can be published in any order (no dependencies)
- Earlier temas do NOT block later temas

### Critical Gates (DO NOT SKIP)

- ✋ Phase 3 (Self-Test) MUST pass before entering Peer Review
- ✋ Phase 4 (Peer Review) MUST complete + sign-off before Publish
- ✋ Pre-Publication Checklist ALL items must be ☑ before merge

---

## Constitution Compliance Throughout

| Phase | Principles Verified | How |
|-------|-------------------|-----|
| Plan | II (Module-Structured) | Check tema outline follows pattern |
| Draft | III (Live Code), II (Module-Structured) | Verify all cells `{code-cell} ipython3` |
| Self-Test | III (Live Code + Local-First) | Execute all code locally without errors |
| Peer Review | IV (Test-Driven) | Reviewer confirms tests + pedagogy quality |
| Publish | I (Content-First, Resource-External) | Verify no `resources_tif/` in commits |

---

## Notes

- **Parallel within Phase 2**: Sections T008-T016 can be written by different team members on different files
- **Serial across Phases**: Each phase must complete before next begins (gate-based)
- **Peer Review ≠ Approval**: Reviewer is independent (not author)
- **Test First**: Exercises should declare tests before solution shown
- **Commit Early**: Save progress after each phase checkpoint
- **Constitution is Law**: All deviations require amendment approval

---

**Template Version**: 1.0.0 | **Aligned with Constitution**: v1.0.0 | **Last Updated**: 2025-10-20

````

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create project structure per implementation plan
- [ ] T002 Initialize [language] project with [framework] dependencies
- [ ] T003 [P] Configure linting and formatting tools

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [ ] T004 Setup database schema and migrations framework
- [ ] T005 [P] Implement authentication/authorization framework
- [ ] T006 [P] Setup API routing and middleware structure
- [ ] T007 Create base models/entities that all stories depend on
- [ ] T008 Configure error handling and logging infrastructure
- [ ] T009 Setup environment configuration management

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - [Title] (Priority: P1) 🎯 MVP

**Goal**: [Brief description of what this story delivers]

**Independent Test**: [How to verify this story works on its own]

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

**NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T010 [P] [US1] Contract test for [endpoint] in tests/contract/test_[name].py
- [ ] T011 [P] [US1] Integration test for [user journey] in tests/integration/test_[name].py

### Implementation for User Story 1

- [ ] T012 [P] [US1] Create [Entity1] model in src/models/[entity1].py
- [ ] T013 [P] [US1] Create [Entity2] model in src/models/[entity2].py
- [ ] T014 [US1] Implement [Service] in src/services/[service].py (depends on T012, T013)
- [ ] T015 [US1] Implement [endpoint/feature] in src/[location]/[file].py
- [ ] T016 [US1] Add validation and error handling
- [ ] T017 [US1] Add logging for user story 1 operations

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - [Title] (Priority: P2)

**Goal**: [Brief description of what this story delivers]

**Independent Test**: [How to verify this story works on its own]

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [ ] T018 [P] [US2] Contract test for [endpoint] in tests/contract/test_[name].py
- [ ] T019 [P] [US2] Integration test for [user journey] in tests/integration/test_[name].py

### Implementation for User Story 2

- [ ] T020 [P] [US2] Create [Entity] model in src/models/[entity].py
- [ ] T021 [US2] Implement [Service] in src/services/[service].py
- [ ] T022 [US2] Implement [endpoint/feature] in src/[location]/[file].py
- [ ] T023 [US2] Integrate with User Story 1 components (if needed)

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - [Title] (Priority: P3)

**Goal**: [Brief description of what this story delivers]

**Independent Test**: [How to verify this story works on its own]

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [ ] T024 [P] [US3] Contract test for [endpoint] in tests/contract/test_[name].py
- [ ] T025 [P] [US3] Integration test for [user journey] in tests/integration/test_[name].py

### Implementation for User Story 3

- [ ] T026 [P] [US3] Create [Entity] model in src/models/[entity].py
- [ ] T027 [US3] Implement [Service] in src/services/[service].py
- [ ] T028 [US3] Implement [endpoint/feature] in src/[location]/[file].py

**Checkpoint**: All user stories should now be independently functional

---

[Add more user story phases as needed, following the same pattern]

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] TXXX [P] Documentation updates in docs/
- [ ] TXXX Code cleanup and refactoring
- [ ] TXXX Performance optimization across all stories
- [ ] TXXX [P] Additional unit tests (if requested) in tests/unit/
- [ ] TXXX Security hardening
- [ ] TXXX Run quickstart.md validation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Contract test for [endpoint] in tests/contract/test_[name].py"
Task: "Integration test for [user journey] in tests/integration/test_[name].py"

# Launch all models for User Story 1 together:
Task: "Create [Entity1] model in src/models/[entity1].py"
Task: "Create [Entity2] model in src/models/[entity2].py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence



