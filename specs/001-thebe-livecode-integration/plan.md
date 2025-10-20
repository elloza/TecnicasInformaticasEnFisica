# Implementation Plan: Thebe LiveCode Integration for TIF TeachBook

**Feature**: `001-thebe-livecode-integration` | **Date**: 2025-10-20 | **Constitution**: v1.0.0  
**Input**: Feature specification with 5 user stories, 15 FR, 10 SC, 5 clarifications  
**Status**: Phase 0 (Research) → Phase 1 (Design) → Phase 2 (Planning)

**Note**: This plan decomposes Thebe integration into phased implementation following speckit.plan workflow.

---

## Summary

Thebe LiveCode Integration enables learners to execute Python code directly in the browser (via Pyodide WebAssembly runtime) without installing Jupyter locally. This feature transforms passive reading into interactive learning, particularly valuable for remote/asynchronous education. Integration is phased: Phase 0 (research dependencies), Phase 1 (design contracts + data model), Phase 2 (task breakdown for implementation teams).

---

## Technical Context

### Technology Stack

| Component | Technology | Role | Version |
|-----------|-----------|------|---------|
| **Static Site Generator** | Jupyter Book | TeachBook build + HTML output | v1.0+ (in `requirements.txt`) |
| **Interactive Execution** | Thebe | Browser-based execution layer | Latest stable (CDN-hosted) |
| **Python Runtime** | Pyodide | WebAssembly Python (no install needed) | v0.23+ (auto-cached by browser) |
| **Pre-loaded Libraries** | NumPy, Matplotlib, stdlib | Default kernel dependencies | Latest Pyodide-compatible |
| **Configuration** | YAML (`_config.yml` + front matter) | Book-level + per-tema settings | Jupyter Book syntax |

### Known Unknowns (Phase 0 - Research Tasks)

1. **Thebe Integration with Jupyter Book**: How to configure Thebe in `_config.yml`? What's the minimum config? Are there breaking changes between Jupyter Book versions?
   - Task: Research Jupyter Book v1.0+ Thebe configuration best practices
   - Output: `research.md` with config snippet + version compatibility matrix

2. **Pyodide Package Management**: How to pre-load custom packages (scipy, pandas)? What's the init latency? Memory footprint?
   - Task: Research Pyodide package loading strategies + performance benchmarks
   - Output: `research.md` with package loading patterns + latency/memory trade-offs

3. **Cell Metadata & Rendering**: How does Thebe handle cell metadata (tags, hide-output, fallback images)? Are there standard Jupyter conventions?
   - Task: Research Jupyter cell metadata standards + Thebe rendering behavior
   - Output: `research.md` with metadata mapping + CSS/JS hooks for fallback image rendering

4. **Graceful Degradation**: What happens when Pyodide fails to load? Browser fallback? Error handling?
   - Task: Research Pyodide failure modes + browser WASM fallback patterns
   - Output: `research.md` with failure scenarios + recommended error UX

5. **Page-Scoped Kernels**: How to isolate kernel state per page? Thebe architecture + implementation approach?
   - Task: Research Thebe kernel lifecycle + multi-page kernel isolation patterns
   - Output: `research.md` with kernel architecture diagram + isolation strategy

### Dependencies & Blockers

- ✅ **Blocker**: Jupyter Book v1.0+ must be in `requirements.txt` (assumed present)
- ✅ **Blocker**: `_config.yml` exists and is modifiable (assumed present)
- ⏳ **Dependency**: tema-00 teoría + ejercicios complete (verified ✅ in spec dependencies)
- ⏳ **Dependency**: All `.md` files use `{code-cell} ipython3` syntax (requires audit before Phase 1)
- ⏳ **Dependency**: Research tasks complete before Phase 1 design

---

## Constitution Conformance Check

**GATE: Verify these before Phase 1 design**

| Principle | Requirement | Thebe Alignment | Status |
|-----------|------------|---------|--------|
| **I. Content-First, Resource-External** | All content in `/book/`, NO `resources_tif/` committed | Thebe is implementation-layer only; doesn't affect content location | ✅ Compliant |
| **II. Module-Structured** | Consistent `teoria.md` + `ejercicios.md` per tema | Thebe renders both; no structural impact required | ✅ Compliant |
| **III. Live Code + Local-First** | All code cells executable in browser + locally | Thebe directly implements this principle; Pyodide + local kernel parity required | ✅ Core Feature |
| **IV. Test-Driven Exercises** | Exercises with pedagogical objectives + automated tests | Thebe must preserve test cells; no removal of hidden test blocks | ✅ Compatible |

**Constitutional Violations**: None identified. Thebe is **fully aligned** with all 4 principles.

**Post-Phase-1 Re-Check Required**: Yes — After data model + contracts defined, verify no hidden violations.

---

## Phase 0: Research & Unknowns Resolution

### Research Tasks

**Task 0.1: Jupyter Book + Thebe Configuration**
- **Objective**: Determine minimal `_config.yml` Thebe config + version compatibility
- **Deliverable**: `research.md` section with:
  - Thebe config snippet (YAML syntax)
  - Jupyter Book version compatibility table
  - Troubleshooting common config errors
  - Examples from Jupyter Book docs
- **Owner**: Dev Lead
- **Timeline**: 1-2 hours
- **Success Criteria**: Config tested locally; builds TeachBook without errors

**Task 0.2: Pyodide Package Loading**
- **Objective**: Understand pre-loading packages + performance trade-offs
- **Deliverable**: `research.md` section with:
  - Package loading patterns (`extra_packages` syntax)
  - Latency benchmarks (kernel init time for 0/1/5 packages)
  - Memory footprint comparisons
  - Recommended defaults for tema-00-06
- **Owner**: Dev Lead
- **Timeline**: 2-3 hours
- **Success Criteria**: Benchmark data collected; recommendations documented

**Task 0.3: Cell Metadata & Rendering**
- **Objective**: Map Jupyter metadata to Thebe rendering behavior
- **Deliverable**: `research.md` section with:
  - Standard cell metadata (tags, hide-output, hide-input, cell-id)
  - Thebe rendering hooks (CSS classes, JS callbacks)
  - Fallback image rendering approach (CSS + HTML structure)
  - Tested examples
- **Owner**: Frontend Dev
- **Timeline**: 2-3 hours
- **Success Criteria**: Metadata table created; rendering tested in HTML output

**Task 0.4: Graceful Degradation & Failure Modes**
- **Objective**: Document Pyodide failures + recommended UX
- **Deliverable**: `research.md` section with:
  - Pyodide failure scenarios (WASM unsupported, network timeout, memory exhaustion)
  - Error detection + recovery strategies
  - Recommended error messaging + UX flows
  - Fallback content rendering (static cells)
  - Tested failure scenarios
- **Owner**: Frontend Dev + QA
- **Timeline**: 3 hours
- **Success Criteria**: All 4 failure modes tested; UX flows documented

**Task 0.5: Kernel Lifecycle & Multi-Page Isolation**
- **Objective**: Understand Thebe kernel architecture + page-scoping approach
- **Deliverable**: `research.md` section with:
  - Thebe kernel lifecycle diagram (init → execute → destroy)
  - Multi-page kernel isolation patterns (per-page instances vs. shared global)
  - Implementation approach (JavaScript event listeners, page transitions)
  - Browser memory implications
  - Tested prototype
- **Owner**: Dev Lead + Frontend Dev
- **Timeline**: 3-4 hours
- **Success Criteria**: Kernel isolation demo working; memory leaks tested

### Consolidated Research Output

**Deliverable**: `research.md` (400-600 lines)
- Executive summary of findings
- 5 sections (one per task above)
- Recommendation for each unknown
- Linked references to official docs
- Proof-of-concept code snippets

**Timeline**: Phase 0 = 11-15 hours (1-2 days, parallelizable)

---

## Phase 1: Design & Contracts

### Prerequisites

- ✅ Phase 0 research.md complete (all unknowns resolved)
- ✅ Constitution conformance verified (above)

### Design Deliverables

#### 1.1 Data Model (`data-model.md`)

**Entities** (extracted from spec):

```
CodeCell:
  - id: string (unique cell identifier)
  - code: string (Python source code)
  - language: string (always "ipython3" in v1)
  - metadata: CellMetadata
  - output: CellOutput[] (after execution)
  - state: enum [idle, running, error, completed]

CellMetadata:
  - tags: string[] (e.g., ["hide-output", "local-kernel-recommended"])
  - hide_input: boolean (default: false)
  - hide_output: boolean (default: false)
  - fallback_image: string | null (path to fallback PNG/SVG)
  - cell_id: string (unique within page)
  - timeout_seconds: integer (default: 120)

Kernel:
  - id: string (unique per page)
  - page_id: string (teoria.md, ejercicios.md, etc.)
  - language: string (always "python" in v1)
  - state: dict (global variables/imports)
  - memory_usage_bytes: integer
  - last_heartbeat_ms: timestamp
  - lifecycle_state: enum [initializing, ready, executing, error, destroyed]

ThebeConfig:
  - enabled: boolean (book-level)
  - pyodide_url: string (CDN URL)
  - pre_load_packages: string[] (e.g., ["numpy", "matplotlib"])
  - env_variables: dict[string, string]
  - timeout_seconds: integer
  - per_tema_overrides: dict[tema_id, ThebeConfig]

CellOutput:
  - type: enum [stdout, stderr, plot, table, error]
  - content: string | HTML
  - timestamp: string (ISO 8601)

FallbackImage:
  - path: string (relative to book/ root)
  - alt_text: string
  - width_px: integer (optional)
  - height_px: integer (optional)
```

**Validation Rules**:
- CodeCell.code must be valid Python ≥3.10 syntax (pre-checked by linter in Phase 2)
- CellMetadata.fallback_image must exist at specified path before build
- Kernel.id must be unique within session (collision detection required)
- ThebeConfig.pre_load_packages must be subset of Pyodide-available packages (verified against package list)
- CellOutput.type must match output type detected from execution

**State Transitions**:
```
Kernel: initializing → ready → executing → (completed | error) → executing → … → destroyed
  └─ destroy on: page navigation, manual reset button, session timeout

CodeCell: idle → (running → completed | error)
  └─ error transitions back to idle (can rerun)
```

**Relationships**:
- Page contains many CodeCells (1 Kernel per page, N CodeCells per page)
- CodeCell belongs to 1 Kernel (page-scoped)
- Kernel uses ThebeConfig (book-level + per-tema overrides)
- CodeCell may reference FallbackImage (optional, 0-or-1 per cell)

#### 1.2 API Contracts (`contracts/`)

**File**: `contracts/thebe-api.md`

**User Actions → Endpoints**:

```
Action: Learner clicks "Run" on a code cell
  Input: { page_id, cell_id, code }
  Process: Validate syntax → Initialize kernel if needed → Execute code
  Output: { cell_id, output[], state, errors }
  Error Handling: SyntaxError → display traceback; RuntimeError → display message + link to docs

Action: Learner clicks "Clear Kernel"
  Input: { page_id }
  Process: Destroy kernel instance
  Output: { page_id, status: "kernel_destroyed" }
  Idempotent: Yes (safe to click multiple times)

Action: Learner navigates to different page
  Input: { from_page_id, to_page_id }
  Process: Destroy from_page kernel → Initialize to_page kernel (if needed)
  Output: { from_page_id: "destroyed", to_page_id: "ready" }
  Side Effect: Variables from from_page lost (page-scoped isolation)

Action: System initializes page on load
  Input: { page_id, theme_config, per_tema_overrides }
  Process: Load Pyodide → Download packages → Initialize kernel
  Output: { page_id, kernel_id, status, latency_ms }
  Error Path: Pyodide fails to load → display banner + static cells

Action: System detects timeout (cell >2 min)
  Input: { cell_id, runtime_ms }
  Process: Stop execution → display warning
  Output: { cell_id, status: "timeout", message: "Execution exceeded 2 minutes" }
  UX: "Stop Execution" button offered to learner
```

**Status Codes**:
- 200 OK: Execution completed (output may contain errors)
- 400 BadRequest: Invalid Python syntax
- 500 ServerError: Pyodide kernel crash (recovery: reset kernel)
- 504 Timeout: Cell exceeded time limit

#### 1.3 Agent Context Update

**Task**: Run `.specify\scripts\powershell\update-agent-context.ps1 -AgentType copilot`

This updates the GitHub Copilot context with Thebe-specific technologies.

---

### Phase 1 Deliverables Summary

| Artifact | File | Lines | Owner | Timeline |
|----------|------|-------|-------|----------|
| Research Summary | `research.md` | 400-600 | Dev Lead | 1-2 days |
| Data Model | `data-model.md` | 150-200 | Dev Lead + Frontend | 1 day |
| API Contracts | `contracts/thebe-api.md` | 100-150 | Dev Lead | 1 day |
| Developer Quickstart | `quickstart.md` | 80-120 | Frontend Dev | 1 day |
| Agent Context | `.github/copilot-context-tech.json` | Updated | Agent Script | 30 min |

**Phase 1 Timeline**: 3-4 days (parallelizable)
**Blockers**: Phase 0 complete

---

## Phase 2: Task Breakdown & Implementation Planning

### Context After Phase 1

After Phase 1, we have:
- ✅ All technical unknowns resolved (research.md)
- ✅ Data model + validation rules defined (data-model.md)
- ✅ API contracts + user flows documented (contracts/)
- ✅ Developer quickstart with code examples (quickstart.md)
- ✅ Agent context updated with tech stack (copilot context)

### Phased Implementation Strategy

Thebe integration is decomposed into **3 implementation phases** (Phase A, B, C):

#### Phase A: MVP - Tema-00 Basic Interactivity (P1 User Stories)

**Scope**: User Stories 1-2 (Learner executes code, Author marks cells)  
**Target Outcome**: tema-00 teoría + ejercicios fully interactive in browser  
**Success Metric**: SC-001, SC-002, SC-003 (initial)

**Tasks**:
- A1: Configure Thebe in `_config.yml` + verify TeachBook build
- A2: Create JavaScript module for page-scoped kernel initialization
- A3: Implement cell rendering + "Run" button attachment
- A4: Implement Pyodide execution engine (sync + async execution)
- A5: Implement output rendering (stdout, stderr, plots, tables)
- A6: Test tema-00 teoría in browser (5 theory cells)
- A7: Test tema-00 ejercicios in browser (10 exercise cells)
- A8: Document learner + author workflows

**Duration**: 5-7 days  
**Team**: 2 developers (1 backend for Pyodide integration, 1 frontend for UI)  
**Dependencies**: research.md complete

#### Phase B: Extended Features - Metadata + Fallbacks (P2 User Stories)

**Scope**: User Stories 3-4 (Heavy dependencies, Fallback images)  
**Target Outcome**: Advanced features for remaining temas  
**Success Metric**: SC-006, SC-007, SC-009

**Tasks**:
- B1: Implement cell metadata parsing (tags, hide-input, hide-output)
- B2: Implement fallback image rendering + CSS styling
- B3: Implement "local-kernel-recommended" banner + UX messaging
- B4: Implement graceful degradation (Pyodide failure → static cells)
- B5: Implement error message UX (traceback formatting + help links)
- B6: Test all edge cases (file write sandbox, memory reset, CORS failures)
- B7: Verify SC-005 (zero JS console errors)

**Duration**: 4-5 days  
**Team**: 1-2 developers (frontend-heavy)  
**Dependencies**: Phase A complete + Phase 1 design complete

#### Phase C: Configuration & Ops (P3 User Stories)

**Scope**: User Story 5 (Per-tema config + opt-in/opt-out)  
**Target Outcome**: Operational control for full curriculum  
**Success Metric**: SC-007, SC-008, SC-010

**Tasks**:
- C1: Implement per-tema front matter parsing (`extra_packages`, `env`)
- C2: Implement kernel state persistence within page (SC-008)
- C3: Implement per-tema Thebe enable/disable logic
- C4: Implement "Reset Kernel" button + memory warnings
- C5: Implement timeout handling + "Stop Execution" button
- C6: Audit all temas (tema-01 through tema-06) for Pyodide compatibility
- C7: Create author migration guide (how to mark cells for Thebe)
- C8: Rollout to production + monitor satisfaction (SC-010)

**Duration**: 6-8 days  
**Team**: 1-2 developers + 1 QA + team for migration audit  
**Dependencies**: Phase B complete + all temas reviewed

### Task Dependencies Graph

```
Phase 0 (Research)
    ↓
Phase 1 (Design)
    ├─→ Phase A (MVP) [5-7 days]
    │      ├─→ A1-A8 (parallel, then sequential)
    │      └─→ PR review + merge
    │
    ├─→ Phase B (Features) [4-5 days, start after A3]
    │      ├─→ B1-B6 (parallel where possible)
    │      └─→ PR review + merge
    │
    └─→ Phase C (Ops) [6-8 days, start after B complete]
           ├─→ C1-C8 (parallel where possible)
           └─→ Full deployment

Total Timeline: ~20-25 days (3.5-4 weeks, with parallelization)
Critical Path: Phase 0 (1-2d) → Phase 1 (3-4d) → Phase A (5-7d) → Phase B (4-5d) → Phase C (6-8d)
```

### Success Criteria by Phase

| Phase | SC Targets | Acceptance Criteria |
|-------|-----------|-------------------|
| A (MVP) | SC-001, 002, 003, 004, 005 | tema-00 cells execute 100% error-free in browser; <5 sec output; JS console clean |
| B (Features) | SC-006, 007, 009 | Fallback images render; banners display; error messages user-friendly |
| C (Ops) | SC-007, 008, 010 | Per-tema config respected; kernel state persistent within page; learners >4/5 satisfaction |

---

## Next Steps (Post-Phase 2 Planning)

1. **Phase 0 Execution**: Start research tasks immediately (parallelizable, ~2 days)
2. **Phase 1 Execution**: Upon Phase 0 completion, begin design (3-4 days)
3. **Phase 2 Task Assignment**: Distribute Phase A/B/C tasks to team
4. **PR Gate**: Each phase requires:
   - Code review (by another dev)
   - QA verification against SC
   - Constitution compliance check
   - Merge to `001-thebe-livecode-integration` branch
5. **Final Merge**: After Phase C complete + all SC verified, merge to `main` + update `book/_config.yml`

---

**Plan Status**: ✅ Complete — Ready for Phase 0 Research Execution  
**Next Prompt**: Execute Phase 0 research or assign tasks to dev team
````

