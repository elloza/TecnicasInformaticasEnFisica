# Implementation Tasks: Thebe LiveCode Integration for TIF TeachBook

**Feature**: Thebe LiveCode Integration (001-thebe-livecode-integration)  
**Specification**: `specs/001-thebe-livecode-integration/spec.md`  
**Plan**: `specs/001-thebe-livecode-integration/plan.md`  
**Created**: 2025-10-20  
**Status**: Ready for Phase 0 Execution

---

## Overview

This document breaks down the Thebe LiveCode Integration into executable tasks organized by **User Story + Implementation Phase**. Each task is:
- **Independently testable** (can be completed in isolation)
- **Specifically scoped** (exact file paths provided)
- **Scheduled** (phases ensure dependencies are resolved first)
- **Parallelizable** (marked with [P] where applicable)

---

## Phase 0: Research & Technical Validation (1-2 days)

**Goal**: Resolve all technical unknowns from implementation plan

### Research Tasks

- [ ] T001 Research Jupyter Book + Thebe configuration (`specs/001-thebe-livecode-integration/research.md` - Task 0.1)
  - Document: minimal `_config.yml` Thebe config, version compatibility, troubleshooting
  - Success: Config tested locally; `jupyter-book build book/` succeeds with Thebe enabled
  
- [ ] T002 [P] Research Pyodide package loading (`specs/001-thebe-livecode-integration/research.md` - Task 0.2)
  - Document: package loading patterns, latency benchmarks, memory footprint comparisons
  - Success: Benchmark data collected; recommendations documented for tema-00-06
  
- [ ] T003 [P] Research cell metadata & rendering (`specs/001-thebe-livecode-integration/research.md` - Task 0.3)
  - Document: Jupyter metadata standards, Thebe rendering hooks, fallback image approach
  - Success: Metadata table created; rendering tested in HTML output
  
- [ ] T004 [P] Research graceful degradation & failure modes (`specs/001-thebe-livecode-integration/research.md` - Task 0.4)
  - Document: Pyodide failure scenarios, error detection, recommended UX flows
  - Success: All 4 failure modes tested; UX flows documented
  
- [ ] T005 [P] Research kernel lifecycle & multi-page isolation (`specs/001-thebe-livecode-integration/research.md` - Task 0.5)
  - Document: Thebe kernel architecture, page-scoping approach, memory implications
  - Success: Kernel isolation demo working; memory leaks tested

**Phase 0 Blockers**: All 5 research tasks must complete before Phase 1 begins

---

## Phase 1: Design & Infrastructure (3-4 days)

**Goal**: Create design documents, contracts, and developer resources

### Design Tasks

- [ ] T006 Create data model specification (`specs/001-thebe-livecode-integration/data-model.md`)
  - Extract entities from spec: CodeCell, Kernel, CellMetadata, ThebeConfig, FallbackImage
  - Document: fields, types, relationships, validation rules, state transitions
  - Success: All 5 entities defined with complete attribute lists + validation rules

- [ ] T007 [P] Create API contracts (`specs/001-thebe-livecode-integration/contracts/thebe-api.md`)
  - Map user actions to endpoints: "Run cell", "Clear kernel", "Navigate page", "Init page", "Timeout"
  - Document: input/output schemas, status codes, error handling
  - Success: All 5 user actions documented with request/response examples

- [ ] T008 Update agent context for GitHub Copilot (`.github/copilot-context-tech.json`)
  - Run: `.specify/scripts/powershell/update-agent-context.ps1 -AgentType copilot`
  - Document: Add Thebe, Pyodide, Jupyter Book technologies to copilot context
  - Success: Script runs without errors; context file updated

- [ ] T009 Create developer quickstart walkthrough (`specs/001-thebe-livecode-integration/quickstart.md` - supplement)
  - Document: Architecture diagrams, phase-by-phase workflow examples, debugging tips
  - Success: Quickstart complete; developers can start Phase A implementation

**Phase 1 Blockers**: Phase 0 complete; Phases A/B/C cannot start until Phase 1 complete

---

## Phase 2A: MVP - User Stories 1-2 (5-7 days)

**Scope**: P1 features (Learner executes code, Author marks cells)  
**Target**: tema-00 fully interactive in browser  
**Success Criteria**: SC-001, SC-002, SC-003, SC-004, SC-005

### Configuration Tasks

- [ ] T010 [US1] Configure Thebe in book `_config.yml` (`book/_config.yml`)
  - Add thebe section with enabled=true, pyodide_url from research findings
  - Add extra_js to load thebe initialization script
  - Success: File syntax valid; `jupyter-book build book/` succeeds

- [ ] T011 [US1] Create Thebe initialization JavaScript module (`book/_static/thebe-init.js`)
  - Implement: Page-scoped kernel initialization, "Run" button event handlers
  - Reference: quickstart.md Phase A examples + research.md kernel isolation findings
  - Success: Module loads without JS errors; runs when page loads

### Backend/Kernel Tasks

- [ ] T012 [P] [US1] Implement Pyodide kernel initialization (`book/_static/thebe-kernel.js`)
  - Implement: Lazy kernel init on first cell run, Pyodide download/setup, NumPy/Matplotlib pre-load
  - Reference: research.md Task 0.2 (package loading) + quickstart.md Phase A examples
  - Success: Kernel initializes in <10 sec; pre-loaded packages available

- [ ] T013 [P] [US1] Implement code execution engine (`book/_static/thebe-executor.js`)
  - Implement: Code submission to Pyodide, async execution, state preservation across cells
  - Reference: plan.md API contracts - "Run cell" action
  - Success: Cell code executes; output returned; state persists within page

- [ ] T014 [P] [US1] Implement output rendering pipeline (`book/_static/thebe-output.js`)
  - Implement: Render stdout, stderr, plots (matplotlib), tables, errors inline
  - Reference: plan.md API contracts - output types + quickstart.md Phase A examples
  - Success: All output types render correctly below executed cell

### Frontend/UX Tasks

- [ ] T015 [P] [US2] Create cell detection + Run button injection (`book/_static/thebe-cells.js`)
  - Implement: Detect all `{code-cell} ipython3` blocks in rendered HTML
  - Implement: Inject "Run" button with styling + event binding
  - Reference: research.md Task 0.3 (metadata parsing) + quickstart.md Phase A examples
  - Success: All code cells have "Run" button; buttons are clickable

- [ ] T016 [P] [US2] Implement basic cell metadata parsing (`book/_static/thebe-metadata.js`)
  - Implement: Parse tags, hide-input, hide-output from cell attributes
  - Implement: Store metadata in memory for use by rendering pipeline
  - Reference: research.md Task 0.3 + plan.md data model (CellMetadata entity)
  - Success: Metadata extracted from 100% of cells; accessible to rendering pipeline

- [ ] T017 [US2] Create loading indicator + user feedback UI (`book/_static/thebe-ui.js`)
  - Implement: Show "Executing..." indicator while cell runs
  - Implement: Display execution time + status messages
  - Reference: spec.md US1 acceptance scenario 4 (loading indicator for >30 sec cells)
  - Success: Indicator appears on cell run; disappears when execution completes

### Integration Tasks

- [ ] T018 [US1] Integrate all JavaScript modules into `thebe-init.js` (`book/_static/thebe-init.js`)
  - Import: thebe-kernel.js, thebe-executor.js, thebe-output.js, thebe-cells.js, thebe-metadata.js, thebe-ui.js
  - Implement: Module initialization order + event binding coordination
  - Success: All modules load without circular dependencies; no JS console errors

- [ ] T019 [US1] Test tema-00 teoría in browser (HTML manual verification)
  - Prerequisite: T018 complete + `jupyter-book build book/` succeeds
  - Test: Open `book/_build/html/tif_python/tema-00/teoria.html` in browser
  - Verify: All 5+ code cells have "Run" buttons; clicking Run executes code; output displays
  - Success: All cells execute without errors; output renders inline; <5 sec execution time

- [ ] T020 [US1] Test tema-00 ejercicios in browser (HTML manual verification)
  - Prerequisite: T019 complete
  - Test: Open `book/_build/html/tif_python/tema-00/ejercicios.html` in browser
  - Verify: All 10 exercise cells have "Run" buttons; exercises execute; output displays correctly
  - Success: All exercise cells execute; outputs match expected results from spec.md

### Documentation Tasks

- [ ] T021 [US1] Document learner workflow for running code in browser (`book/thebe-learner-guide.md`)
  - Document: Step-by-step "How to run code" guide for learners
  - Include: Screenshots, common error solutions, troubleshooting
  - Success: Clear, non-technical instructions; learners can follow without help

- [ ] T022 [US2] Document author workflow for marking cells (`book/thebe-author-guide.md`)
  - Document: How to use `{code-cell} ipython3` syntax in `.md` files
  - Document: How to add cell metadata + what each tag does
  - Success: Authors can mark new cells for Thebe interactivity

**Phase 2A Blockers**: Phase 1 complete; Phase 2B cannot start until Phase 2A complete + PR merged

---

## Phase 2B: Extended Features - User Stories 3-4 (4-5 days)

**Scope**: P2 features (Heavy dependencies, Fallback images)  
**Target**: All temas can use advanced features  
**Success Criteria**: SC-006, SC-007, SC-009

### Metadata & Warning Tasks

- [ ] T023 [P] [US3] Implement cell metadata parser enhancements (`book/_static/thebe-metadata.js` - update)
  - Implement: Parse additional metadata: `tags`, especially `["local-kernel-recommended"]`
  - Implement: Extract `fallback-image` metadata reference
  - Reference: plan.md data model (CellMetadata) + quickstart.md Phase B examples
  - Success: All new metadata fields parsed correctly

- [ ] T024 [P] [US3] Implement "local-kernel-recommended" warning banner (`book/_static/thebe-banner.js`)
  - Implement: Detect `local-kernel-recommended` tag; display yellow warning banner above cell
  - Implement: Banner text: "This cell uses a library that may not work in the browser. Try running locally if you get an error."
  - Reference: spec.md US3 acceptance scenario 1
  - Success: Banner displays for cells with tag; doesn't display for others

- [ ] T025 [P] [US3] Add help link infrastructure for error messages (`book/_static/thebe-help.js`)
  - Implement: Append "Try running locally: [link]" to error messages
  - Implement: Link points to installation guide (from learner workflow doc)
  - Reference: spec.md US3 acceptance scenario 2 + success criteria SC-009
  - Success: Error messages include actionable help links

### Fallback Image Tasks

- [ ] T026 [P] [US4] Implement fallback image rendering (`book/_static/thebe-fallback.js`)
  - Implement: Detect `fallback-image` metadata
  - Implement: Load + display image from specified path in `book/figures/`
  - Implement: Position image above cell with note "Click 'Run' to execute code"
  - Reference: spec.md US4 acceptance scenario 1 + plan.md data model (FallbackImage)
  - Success: Images render correctly; "Run" button remains visible + functional

- [ ] T027 [P] [US4] Create CSS styling for fallback images + context (`book/_static/thebe-fallback.css`)
  - Create: Styles for fallback image container, alt text, "Run to execute" note
  - Create: Responsive design (works on mobile + desktop)
  - Success: Fallback images styled consistently with page design

### Graceful Degradation Tasks

- [ ] T028 [P] [US4] Implement Pyodide failure detection + graceful fallback (`book/_static/thebe-fallback-mode.js`)
  - Implement: Detect if Pyodide fails to load (WASM unsupported, network timeout)
  - Implement: Display banner: "Python execution unavailable. [Install instructions link]"
  - Implement: Render all code cells as static syntax-highlighted blocks (no "Run" buttons)
  - Reference: spec.md US4 edge case + plan.md graceful degradation
  - Success: Failures detected; banner displays; page remains readable

- [ ] T029 [P] [US4] Implement error boundary + console monitoring (`book/_static/thebe-errors.js`)
  - Implement: Catch JavaScript errors in Thebe execution
  - Implement: Monitor browser console for errors; log to memory
  - Implement: Ensure zero errors appear in DevTools console during cell execution
  - Reference: success criteria SC-004 (zero JS console errors)
  - Success: No JS errors in DevTools; execution errors displayed to user only

### Testing Tasks

- [ ] T030 [US4] Test fallback images in browser (HTML manual verification)
  - Prerequisite: T026 complete; fallback images added to test cells
  - Test: Open tema-00 cell with fallback-image metadata in browser
  - Verify: Image displays; "Run" button visible; clicking Run executes code
  - Success: Fallback feature works as specified

- [ ] T031 [US4] Test graceful degradation scenarios (QA testing)
  - Prerequisite: T028 complete
  - Test: Disable WASM in browser; load page; verify banner + static cells
  - Test: Block Pyodide CDN; load page; verify fallback behavior
  - Test: Execute cells with heavy operations; monitor memory; verify no crashes
  - Success: All failure modes handled gracefully; page always readable

- [ ] T032 [US3] [US4] Verify success criteria SC-005 (zero JS console errors)
  - Prerequisite: All of Phase 2B complete
  - Test: Open DevTools console; run multiple cells; monitor for errors
  - Verify: No errors in console; all user-facing errors displayed in UI only
  - Success: SC-005 verified

### Documentation Tasks

- [ ] T033 [US3] Document cell metadata usage for authors (`book/thebe-author-guide.md` - update)
  - Document: How to use `tags: ["local-kernel-recommended"]` for heavy dependencies
  - Document: When + why to use this tag
  - Success: Authors know how to mark cells with dependency warnings

- [ ] T034 [US4] Document fallback image workflow for authors (`book/thebe-author-guide.md` - update)
  - Document: How to add `fallback-image: "figures/path.png"` metadata
  - Document: How to create + check in fallback images
  - Success: Authors can add fallback images to complex visualization cells

**Phase 2B Blockers**: Phase 2A complete + PR merged; Phase 2C cannot start until Phase 2B complete + PR merged

---

## Phase 2C: Configuration & Full Rollout - User Story 5 (6-8 days)

**Scope**: P3 features (Per-tema config, operational control)  
**Target**: Full curriculum enabled; teams can opt temas in/out  
**Success Criteria**: SC-007, SC-008, SC-010

### Configuration Tasks

- [ ] T035 [P] [US5] Implement per-tema front matter parsing (`book/_static/thebe-config.js`)
  - Implement: Parse YAML front matter from `.md` files for `thebe` section
  - Implement: Extract `extra_packages`, `env` variables, `enabled` flag per-tema
  - Reference: spec.md US5 acceptance scenario 3 + plan.md per-tema config example
  - Success: Config extracted for all temas; available to kernel initialization

- [ ] T036 [P] [US5] Implement per-tema package pre-loading (`book/_static/thebe-packages.js`)
  - Implement: Pass `extra_packages` from per-tema config to Pyodide init
  - Implement: Environment variables from `env` config applied to kernel
  - Reference: research.md Task 0.2 (package loading) + plan.md Phase C Task C1
  - Success: Custom packages pre-loaded; environment variables applied; kernel works with custom config

- [ ] T037 [P] [US5] Implement per-tema Thebe enable/disable logic (`book/_static/thebe-config.js` - update)
  - Implement: Check `enabled` flag in per-tema config
  - Implement: If disabled: skip kernel init, render cells as static, no "Run" buttons
  - Reference: spec.md US5 acceptance scenario 2
  - Success: Disabled temas show static cells; enabled temas show interactive cells

### Kernel Management Tasks

- [ ] T038 [P] [US5] Implement kernel state persistence within page (`book/_static/thebe-kernel.js` - update)
  - Implement: Maintain kernel instance across all cells on same page
  - Implement: Verify variables from cell 1 available in cell 2 within same page
  - Reference: spec.md FR-004 + success criteria SC-008
  - Success: Kernel state persists across cells on same page; verified by test

- [ ] T039 [P] [US5] Implement "Reset Kernel" button + memory monitoring (`book/_static/thebe-reset.js`)
  - Implement: Add "Reset Kernel" button to page
  - Implement: Onclick: destroy kernel instance, clear outputs, reinitialize
  - Implement: Monitor kernel memory usage; warn user if >70%
  - Reference: spec.md FR-014 + edge case (memory fills)
  - Success: Reset button works; memory warnings display; kernel reinitializes cleanly

- [ ] T040 [P] [US5] Implement timeout handling + "Stop Execution" button (`book/_static/thebe-timeout.js`)
  - Implement: Monitor cell execution time; warn if >2 min
  - Implement: Show "Stop Execution" button during long-running cells
  - Implement: On Stop click: abort execution, display message
  - Reference: spec.md FR-015 + edge case (long-running cells)
  - Success: Timeout warnings display; Stop button works; execution aborts cleanly

### Global Configuration Tasks

- [ ] T041 [US5] Update book `_config.yml` for global Thebe settings (`book/_config.yml` - update)
  - Implement: Add book-level `thebe.enabled` toggle (default: true)
  - Implement: Configure Pyodide URL, pre-load packages (default: NumPy, Matplotlib, stdlib)
  - Reference: spec.md FR-010 + plan.md global vs. per-tema config
  - Success: Book-level config takes effect; affects all temas (unless overridden per-tema)

### Audit & Migration Tasks

- [ ] T042 [US5] Audit all temas (tema-01 through tema-06) for Pyodide compatibility (`AUDIT_REPORT.md`)
  - Audit: Scan all code cells in tema-01 through tema-06
  - Identify: Cells using non-Pyodide libraries (requests, file I/O, system commands)
  - Document: List of incompatible cells + recommended mitigation (mark with `local-kernel-recommended` or add fallback images)
  - Success: Audit complete; recommendations documented

- [ ] T043 [US5] Update temas with metadata for incompatible cells (`book/tif_python/tema-*/teoria.md` and `ejercicios.md`)
  - For each incompatible cell: Add appropriate metadata tag or fallback image
  - Reference: T042 audit results + thebe-author-guide.md
  - Success: All incompatible cells marked; temas ready for Thebe rollout

- [ ] T044 [US5] Create author migration guide (`book/THEBE_MIGRATION_GUIDE.md`)
  - Document: How to convert existing temas to use Thebe
  - Document: How to mark cells with `local-kernel-recommended` tag
  - Document: How to add fallback images for complex visualizations
  - Document: Best practices for Pyodide-compatible code
  - Success: Authors have clear guidance for migrating temas to Thebe

### Testing & Validation Tasks

- [ ] T045 [US5] Test per-tema configuration (QA testing)
  - Prerequisite: T035-T037 complete; T042 audit done
  - Test: Add custom config to tema-00 front matter; build; verify kernel uses config
  - Test: Disable Thebe in tema-00; rebuild; verify cells are static
  - Test: Re-enable; rebuild; verify cells are interactive again
  - Success: Per-tema config works correctly; enable/disable toggles work

- [ ] T046 [US5] Test kernel state persistence (QA testing)
  - Prerequisite: T038 complete
  - Test: Open tema-00 ejercicios; run exercise 1; define variable X
  - Test: Run exercise 2; verify variable X is accessible
  - Navigate to teoria.md; navigate back to ejercicios.md
  - Verify: Kernel destroyed + recreated; variable X no longer available
  - Success: SC-008 verified (kernel state persistent within page, fresh on navigation)

- [ ] T047 [US5] Test memory warnings + Reset button (QA testing)
  - Prerequisite: T039 complete
  - Test: Execute many heavy cells; monitor memory usage display
  - Test: Click "Reset Kernel" button; verify outputs cleared + kernel reinitializes
  - Success: Memory monitoring works; Reset button clears state

- [ ] T048 [US5] Test timeout handling (QA testing)
  - Prerequisite: T040 complete
  - Test: Execute cell with `time.sleep(120)` (>2 min timeout)
  - Verify: Warning displays; "Stop Execution" button appears
  - Click Stop; verify execution aborts
  - Success: Timeout warnings + Stop button work

### Deployment Tasks

- [ ] T049 [US5] Create deployment checklist + documentation (`DEPLOYMENT_CHECKLIST.md`)
  - Document: Steps to deploy Thebe integration to production
  - Include: Pre-deployment checks (all SC verified), rollback procedure, monitoring setup
  - Success: Deployment procedure documented + rehearsed

- [ ] T050 [US5] Deploy to production + monitor learner satisfaction (`book/_build/html/...` + surveys)
  - Prerequisite: All previous tasks complete + PR merged to main
  - Deploy: Publish TeachBook with Thebe enabled
  - Monitor: Track learner feedback on "ease of running code" (survey)
  - Success: SC-010 verified (learner satisfaction >4/5)

### Documentation Tasks

- [ ] T051 [US5] Update learner guide with per-tema Thebe information (`book/thebe-learner-guide.md` - update)
  - Document: Explain per-tema configurations (if user sees different features in different temas)
  - Document: Troubleshooting for per-tema issues (e.g., Tema-05 cells don't run)
  - Success: Learners understand per-tema differences

- [ ] T052 [US5] Create operations guide for maintainers (`book/THEBE_OPS_GUIDE.md`)
  - Document: How to monitor Thebe usage + errors (if analytics added in v2)
  - Document: How to enable/disable Thebe for new temas
  - Document: How to troubleshoot common issues (Pyodide load failures, memory issues)
  - Success: Maintainers have operational guidance

**Phase 2C Blockers**: Phase 2B complete + PR merged; Phase 2C is final phase before production deployment

---

## Phase 3: Polish & Cross-Cutting Concerns (2-3 days)

**Goal**: Final quality verification, documentation, and deployment preparation

### Code Quality Tasks

- [ ] T053 [P] Perform code review on all Phase 2A/B/C tasks
  - Review: JavaScript modules for code quality, error handling, performance
  - Verify: Adherence to coding standards + best practices
  - Success: All code approved for production

- [ ] T054 [P] Perform security audit on Thebe integration
  - Audit: JavaScript modules for security issues (XSS, injection, CORS)
  - Audit: Pyodide sandbox configuration + limitations documented
  - Success: No security vulnerabilities found; assumptions documented in spec.md

- [ ] T055 [P] Performance optimization (if needed)
  - Profile: Measure kernel init time, cell execution time, memory usage
  - Optimize: If any metric exceeds spec targets (SC-002: <5 sec, memory: <100MB)
  - Success: All performance metrics within spec targets

### Documentation Tasks

- [ ] T056 Documentation audit + completion (`specs/001-thebe-livecode-integration/`)
  - Review: All guide files complete + accurate (learner, author, ops guides)
  - Review: `research.md`, `plan.md`, `data-model.md`, `contracts/` all populated
  - Success: Documentation comprehensive + up-to-date

- [ ] T057 Create README for Thebe integration (`specs/001-thebe-livecode-integration/README.md`)
  - Document: Overview of Thebe integration, key features, target users
  - Document: Quick start for developers + users
  - Document: Links to all relevant guides + docs
  - Success: README comprehensive; entry point for new users

### Final Verification Tasks

- [ ] T058 Verify all success criteria (SC-001 through SC-010)
  - Verify: SC-001 (tema-00 100% executable in browser)
  - Verify: SC-002 (output within 5 sec)
  - Verify: SC-003 (95%+ NumPy/Matplotlib success)
  - Verify: SC-004 (zero JS console errors)
  - Verify: SC-005 (build succeeds)
  - Verify: SC-006 (fallback images work)
  - Verify: SC-007 (per-tema config respected)
  - Verify: SC-008 (kernel state persistent)
  - Verify: SC-009 (error messages user-friendly)
  - Verify: SC-010 (learner satisfaction >4/5)
  - Success: All 10 SC verified

- [ ] T059 Constitutional compliance verification
  - Verify: Principle I - Content-First (no resources_tif/ committed, all content in /book/)
  - Verify: Principle II - Module-Structured (teoria.md + ejercicios.md pattern maintained)
  - Verify: Principle III - Live Code (all code cells executable + local-first)
  - Verify: Principle IV - Test-Driven (exercises preserve test cells)
  - Success: All 4 principles verified for Thebe integration

### Deployment Tasks

- [ ] T060 Merge feature branch to main (`001-thebe-livecode-integration` → `main`)
  - Prerequisite: All tasks complete, all SC verified, all code reviewed
  - Action: Create PR from `001-thebe-livecode-integration` to `main`
  - Action: Merge PR after final approval
  - Success: Feature integrated into main codebase

- [ ] T061 Create release notes + version bump
  - Document: Summary of Thebe integration feature (user-facing)
  - Document: Implementation notes (developer-facing)
  - Bump: Version in `book/_config.yml` or equivalent version file
  - Success: Release notes published; version updated

---

## Task Dependency Graph

```
Phase 0 (Research):
  T001-T005 (parallelizable)
    ↓
Phase 1 (Design):
  T006 (data model)
  T007 (contracts)  ← depends on T006
  T008 (copilot)
  T009 (quickstart)  ← depends on T006, T007
    ↓
Phase 2A (MVP):
  T010, T011 (config)
  T012-T014 (kernel tasks, parallelizable)
  T015-T017 (frontend, parallelizable)  ← depends on T012-T014
  T018 (integration)  ← depends on T012-T017
  T019 (teoria test)  ← depends on T018
  T020 (ejercicios test)  ← depends on T019
  T021, T022 (docs)
    ↓
Phase 2B (Features):
  T023-T025 (metadata, parallelizable)  ← depends on Phase 2A
  T026-T027 (fallback images, parallelizable)  ← depends on Phase 2A
  T028-T029 (graceful degradation, parallelizable)  ← depends on Phase 2A
  T030-T032 (testing)  ← depends on T023-T029
  T033-T034 (docs)
    ↓
Phase 2C (Config):
  T035-T040 (config + kernel, parallelizable)  ← depends on Phase 2B
  T041 (global config)  ← depends on Phase 2B
  T042-T044 (audit + migration)  ← depends on Phase 2B
  T045-T048 (testing)  ← depends on T035-T040
  T049-T052 (deployment + docs)  ← depends on T045-T048
    ↓
Phase 3 (Polish):
  T053-T055 (quality)  ← depends on Phase 2C
  T056-T057 (documentation)  ← depends on all phases
  T058-T059 (verification)  ← depends on T053-T055
  T060-T061 (deployment)  ← depends on T058-T059
```

---

## Implementation Strategy

### MVP Scope (Recommended First Release)

**Minimum Viable Product = User Stories 1-2 (Phase 2A)**

**What learners get**:
- Run Python code directly in browser for tema-00 examples
- See output inline without installing Python
- Kernel state persists across cells on same page

**What authors get**:
- Mark cells with `{code-cell} ipython3` syntax
- Cells automatically become interactive when TeachBook builds
- Basic metadata support (hide-input, hide-output)

**Timeline**: 5-7 days (Phase 0 + Phase 1 + Phase 2A)  
**Success Criteria**: SC-001, SC-002, SC-003, SC-004, SC-005  
**Deployment**: After Phase 2A complete + all SC verified

### Extended Release (Phase 2B)

**Add**: Heavy dependency warnings + Fallback images  
**Timeline**: +4-5 days (Phase 2B only)  
**Success Criteria**: SC-006, SC-007, SC-009  
**Deployment**: After Phase 2B complete + Phase 2A already deployed

### Full Release (Phase 2C)

**Add**: Per-tema configuration + Full curriculum rollout  
**Timeline**: +6-8 days (Phase 2C only)  
**Success Criteria**: SC-007, SC-008, SC-010  
**Deployment**: After Phase 2C complete + all SC verified (all 10)

### Parallel Execution Opportunities

- **Phase 0**: All 5 research tasks run in parallel (different team members)
- **Phase 1**: Design tasks (T006-T009) can overlap; data model (T006) needed by contracts (T007)
- **Phase 2A**: 
  - Kernel tasks (T012-T014) run in parallel
  - Frontend tasks (T015-T017) run in parallel (after T012-T014)
  - Testing (T019-T020) must be sequential
- **Phase 2B**:
  - Metadata tasks (T023-T025) run in parallel
  - Fallback tasks (T026-T027) run in parallel
  - Graceful degradation (T028-T029) run in parallel
  - Testing (T030-T032) sequential but can start after T026
- **Phase 2C**:
  - Config tasks (T035-T040) run in parallel
  - Audit + Migration (T042-T044) run in parallel with T035-T041
  - Testing (T045-T048) sequential after config complete
- **Phase 3**: Most tasks can run in parallel (code review, security audit, docs)

**Recommended Parallelization**: 2-3 developers working on Phase 2A simultaneously

---

## Task Execution Checklist

**Before Starting Any Phase**:
- [ ] Prerequisites for that phase are complete (see dependency graph)
- [ ] Previous phase PR has been reviewed + merged
- [ ] Team understands user stories + acceptance criteria for phase

**For Each Task**:
- [ ] Task description is clear + file paths are specific
- [ ] Developer reads relevant spec sections + quickstart examples
- [ ] Developer creates branch for task (or works on feature branch)
- [ ] Developer completes task implementation
- [ ] Developer writes tests (if applicable) + verifies task works
- [ ] Developer commits with clear message (referencing task ID)
- [ ] Developer opens PR for code review

**After Phase Completion**:
- [ ] All tasks in phase complete
- [ ] All PRs merged to feature branch (`001-thebe-livecode-integration`)
- [ ] All success criteria (SC) verified for phase
- [ ] Team reviews + approves phase completion
- [ ] Phase merged to `001-thebe-livecode-integration` (or main, depending on deployment strategy)

---

## Notes for Development Team

1. **Constitutional Compliance**: Every task must maintain the 4 core principles (see plan.md). Especially:
   - Keep all content in `/book/`; don't commit to `resources_tif/`
   - Preserve test cells in ejercicios.md (Thebe shouldn't remove them)
   - Ensure all code cells remain executable locally + in browser

2. **Research First**: Phase 0 tasks must complete before Phase 1. Don't skip research; it resolves critical unknowns.

3. **Testing is Mandatory**: Each phase has testing tasks. Don't merge without verifying SC.

4. **Documentation Matters**: Author guides (T021-T022, T033-T034, T051-T052) are part of deliverables. Update them as features are added.

5. **Phased Rollout**: Don't merge all phases at once. Deploy MVP (Phase 2A) first, gather learner feedback, then add features (Phase 2B/C).

---

**Task Document Version**: 1.0.0 | **Created**: 2025-10-20 | **Status**: Ready for Execution