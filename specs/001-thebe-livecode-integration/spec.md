# Feature Specification: Thebe LiveCode Integration for TIF TeachBook

**Feature Branch**: `001-thebe-livecode-integration`  
**Created**: 2025-10-20  
**Status**: Draft  
**Input**: User description: "Integrate Thebe for live code execution in all tema examples and exercises"

---

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Learner Executes Code Inline in Browser (Priority: P1) 🎯 MVP

Learners access teoria.md or ejercicios.md in the published TeachBook, see code examples with a **"Run"** button, click it, and the code executes in their browser without installation. Results display inline below the code cell.

**Why this priority**: This is the core value proposition of Thebe. Learners get immediate feedback without environment setup—critical for engagement and learning outcomes.

**Independent Test**: Can be fully tested by:
1. Publishing tema-00 with Thebe enabled
2. Opening teoria.md in browser
3. Clicking "Run" on any code cell
4. Verifying code executes and output displays

**Acceptance Scenarios**:

1. **Given** a learner reads `teoria.md` in the browser, **When** they click the "Run" button on a code cell, **Then** the code executes in a Pyodide kernel and output displays below the cell
2. **Given** multiple code cells in sequence, **When** a learner runs cell 1 then cell 2, **Then** cell 2 has access to variables defined in cell 1 (shared kernel state)
3. **Given** code that produces a plot (e.g., `matplotlib`), **When** code executes, **Then** the plot renders inline in the notebook
4. **Given** code that takes >30 seconds to run, **When** code executes, **Then** a loading indicator displays and user can still view output after completion
5. **Given** code with an error (e.g., `NameError`), **When** code executes, **Then** error message displays clearly with line number

---

### User Story 2 - Author Marks Code Cells for Live Execution (Priority: P1)

Authors create `.md` or `.ipynb` files in Jupyter Book format and mark code cells with metadata (`{code-cell} ipython3` directives in Markdown OR cell tags in notebooks). Thebe automatically converts these to interactive cells.

**Why this priority**: Without this, authors can't enable interactivity. This is a prerequisite for US1.

**Independent Test**: Can be fully tested by:
1. Creating a `.md` file with `{code-cell} ipython3` blocks
2. Adding to `_toc.yml`
3. Building TeachBook
4. Verifying cells are interactive

**Acceptance Scenarios**:

1. **Given** a `.md` file with `{code-cell} ipython3` blocks, **When** TeachBook builds, **Then** Thebe is attached to those blocks
2. **Given** a Jupyter `.ipynb` file, **When** TeachBook builds, **Then** all code cells are made interactive (no extra markup needed)
3. **Given** code cells marked with metadata (e.g., `tags: ["hide-output"]`), **When** rendered, **Then** Thebe respects cell metadata for visibility/execution behavior
4. **Given** a cell that should NOT be executable (e.g., pseudo-code or SQL), **When** author marks it differently, **Then** that cell is static (no Run button)

---

### User Story 3 - Heavy Dependencies Default to Local Kernel (Priority: P2)

Some libraries (NumPy, Matplotlib) work in Pyodide, but others (requests, pandas, etc.) may fail or be slow. Authors can mark cells as "local kernel recommended" with a deprecation banner explaining learners should run locally if they hit issues.

**Why this priority**: Manages learner expectations for cell dependencies. Prevents confusing failures.

**Independent Test**: Can be fully tested by:
1. Marking a cell with `{code-cell} ipython3` + cell metadata
2. Building TeachBook
3. Verifying banner displays
4. Confirming cell still runs in browser (with graceful degradation)

**Acceptance Scenarios**:

1. **Given** a cell that uses `requests` library (not in Pyodide), **When** author adds metadata `tags: ["local-kernel-recommended"]`, **Then** a yellow banner displays above the cell explaining local kernel needed
2. **Given** a cell with "local kernel recommended" banner, **When** learner clicks Run, **Then** code still attempts to execute in browser but with a note that results may vary

---

### User Story 4 - Fallback Static Outputs for Complex Visualizations (Priority: P2)

Some code produces outputs that don't render well in browser (3D plots, interactive dashboards). Authors can include `.png` images as fallbacks for browser users while code still executes locally.

**Why this priority**: Ensures accessibility—browser users see something meaningful even if interactivity limited.

**Independent Test**: Can be fully tested by:
1. Creating a cell with fallback image metadata
2. Building TeachBook
3. Verifying image displays in browser + cell also runs

**Acceptance Scenarios**:

1. **Given** a cell with a 3D plot and fallback image (metadata: `fallback-image: "figures/3d-plot.png"`), **When** rendered in browser, **Then** fallback image displays with note "Click 'Run' to execute code locally for full interactivity"
2. **Given** same cell executed locally, **When** run in Jupyter, **Then** interactive 3D plot renders (image fallback ignored)

---

### User Story 5 - Tema Configuration & Opt-In/Opt-Out (Priority: P3)

Book-level config (`_config.yml`) enables/disables Thebe globally. Per-tema config allows opting specific temas in/out (e.g., "Tema-05 uses advanced GPU code, Thebe disabled").

**Why this priority**: Operational control—team can pilot with tema-00, gradually expand to other temas.

**Independent Test**: Can be fully tested by:
1. Disabling Thebe globally in config
2. Building TeachBook
3. Verifying NO cells are interactive
4. Re-enabling + rebuilding + verifying cells ARE interactive

**Acceptance Scenarios**:

1. **Given** Thebe disabled in `_config.yml`, **When** TeachBook builds, **Then** ALL code cells are static (no Run buttons)
2. **Given** Thebe enabled globally but disabled for tema-05, **When** TeachBook builds, **Then** tema-00-04 cells are interactive, tema-05 cells are static
3. **Given** config for Pyodide kernel (custom packages, settings), **When** cell executes, **Then** Pyodide uses specified config

---

### Edge Cases

- What happens when a learner clicks "Run" on a cell that modifies global state (e.g., writes to a file)? → Code should execute safely in browser sandbox with no side effects; write operations fail gracefully
- How does system handle if learner runs 10 heavy cells in sequence and browser memory fills? → Kernel can be reset via button; learner sees warning if memory usage high
- What if Pyodide kernel initialization fails (e.g., browser lacks WASM support)? → Clear message explaining how to run locally; static cell displayed as fallback
- What if a cell references an external API (e.g., `requests.get("https://...")`)?  → Code runs but may fail due to CORS or network isolation; error message explains limitation

---

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST render all `{code-cell} ipython3` blocks in Jupyter Book with a "Run" button when Thebe is enabled
- **FR-002**: System MUST execute cell code in a Pyodide kernel (Python in browser) when learner clicks "Run"
- **FR-003**: System MUST display code output (stdout, stderr, plots, tables) inline below executed cell
- **FR-004**: System MUST maintain kernel state across consecutive cell executions (variables defined in cell 1 available in cell 2)
- **FR-005**: System MUST handle errors gracefully (display error traceback without crashing notebook)
- **FR-006**: System MUST support `.md` files with `{code-cell} ipython3` blocks and `.ipynb` Jupyter notebooks
- **FR-007**: System MUST allow authors to mark cells with metadata (e.g., `tags`, `hide-output`, `hide-input`)
- **FR-008**: System MUST allow authors to add deprecation/warning banners for cells with heavy dependencies
- **FR-009**: System MUST support fallback static images for complex visualizations (via cell metadata)
- **FR-010**: System MUST allow book-level enable/disable of Thebe via `_config.yml`
- **FR-011**: System MUST allow per-tema enable/disable of Thebe via front matter or metadata
- **FR-012**: System MUST initialize Pyodide kernel with NumPy, Matplotlib, and standard library (auto-loaded)
- **FR-013**: System MUST gracefully degrade if Pyodide fails to load (display static content + fallback message)
- **FR-014**: System MUST reset kernel state on demand (via "Clear Output" button or similar)
- **FR-015**: System MUST handle timeout for long-running cells (>2 min → warning, user can stop execution)

### Key Entities

- **Code Cell**: A `{code-cell}` block in Markdown or `.ipynb` cell with executable Python code
- **Kernel**: Pyodide-based Python runtime in browser; maintains state across cell executions
- **Cell Metadata**: Tags, output visibility settings, fallback image references, dependency warnings (stored in cell front matter or `.ipynb` metadata)
- **Thebe Config**: Book-level and per-tema settings controlling interactivity (stored in `_config.yml` + front matter)
- **Fallback Image**: Static `.png` or `.svg` displayed when code output not renderable in browser (referenced via metadata)

---

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 100% of code examples in tema-00 (theory + exercises) are executable in browser without errors
- **SC-002**: Learners can run any code cell and see output within 5 seconds (including kernel initialization on first run)
- **SC-003**: 95%+ of code cells using NumPy/Matplotlib execute successfully in Pyodide (failures documented with mitigation)
- **SC-004**: Zero JavaScript console errors when Thebe loads or cells execute (tested via browser DevTools)
- **SC-005**: Book builds successfully with Thebe config in `_config.yml` (no build failures or warnings)
- **SC-006**: Fallback images display correctly for marked cells; interactive code still executes locally when run
- **SC-007**: Per-tema config respected: disabled temas show static cells, enabled temas show interactive cells
- **SC-008**: Kernel state persistence verified: cell 2 can access variables from cell 1 (tested with dependent cells)
- **SC-009**: Error messages are user-friendly and actionable (e.g., "Try running locally: [link to instructions]")
- **SC-010**: Learners report satisfaction >4/5 on "ease of running code" survey (post-publish feedback)

---

## Assumptions

1. **Pyodide Capability**: NumPy, Matplotlib, and standard library packages are sufficient for tema-00 through tema-06 examples. (Larger WASM packages may be added later if needed.)
2. **Browser Support**: Target browsers support WebAssembly (all modern browsers: Chrome 74+, Firefox 79+, Safari 14.1+, Edge 79+).
3. **No Network Isolation**: Learner browsers have internet access to load Pyodide kernel (~50MB initial download, then cached).
4. **Author Best Practices**: Authors will follow Markdown syntax correctly (e.g., proper ` ```{code-cell} ipython3 ` fence formatting).
5. **Book Build Environment**: TeachBook build process can be configured to include Thebe (no custom build scripts required beyond standard Jupyter Book extensions).
6. **Fallback Images Provided**: Authors are responsible for creating + checking in fallback `.png` images; system assumes images exist at referenced paths.
7. **Local Kernel as Escape Hatch**: For cells that fail in Pyodide, learners are instructed to run locally (we do NOT attempt complex workarounds; simplicity first).

---

## Constraints

- **Scope**: Only Python code cells. Other languages (R, JavaScript) out of scope for v1.
- **Performance**: First kernel load may take 5-10 seconds (acceptable; subsequent cells are faster). Long-running cells (>2 min) should be rare in introductory curriculum.
- **Storage**: No persistent storage in browser. Each browser session is independent; learner code is NOT saved.
- **Dependencies**: Only libraries available in Pyodide can be auto-loaded. Missing dependencies fail gracefully with clear message.
- **Security**: Pyodide sandbox prevents file system access and network calls (except for CORS-enabled endpoints). This is a feature; learners cannot accidentally write to server.

---

## Dependencies & Blockers

- **Blocker**: Jupyter Book v1.0+ with Thebe extension support required (assumed available in `requirements.txt`)
- **Blocker**: `_config.yml` must be updated to enable Thebe (one-time setup by repo admin)
- **Dependency**: `tema-00` teoría + ejercicios must be finalized before testing Thebe (currently complete ✅)
- **Dependency**: All `.md` files in temas must use proper Jupyter Book syntax for code cells (`{code-cell} ipython3`)

---

## Notes & Implementation Guidance

### For Authors

- Mark all executable code with ` ```{code-cell} ipython3 ` fence + language specifier
- For cells with heavy dependencies (requests, pandas): Add cell metadata `tags: ["local-kernel-recommended"]`
- For cells with complex plots: Add metadata `fallback-image: "figures/tema-XX-figYY.png"` + check in image
- Test cells locally in Jupyter before publishing (Pyodide ≠ local Python; some edge cases differ)

### For Developers/DevOps

- Update `requirements.txt` to include Jupyter Book + Thebe extension (if not already present)
- Configure `_config.yml`:
  ```yaml
  html:
    use_issues_button: true
    use_repository_button: true
    extra_footer: "Powered by Jupyter Book + Thebe"
  
  execution:
    allow_errors: true
    
  thebe:
    enabled: true
    # Optional: pin Pyodide version
    # pyodide_url: "https://cdn.jsdelivr.net/pyodide/v0.23.4/full/"
  ```
- Verify TeachBook build succeeds: `jupyter-book build book/`
- Test a few cells manually in published site after first deploy

---

## Risks & Mitigations

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|-----------|
| Pyodide kernel fails to load in some browsers | Low | High (learners can't run code) | Graceful fallback: show static cells + link to local setup guide |
| Code cells have syntax errors learners can't debug | Medium | Medium (bad learning experience) | Provide clear error messages + link to Python debugging guide |
| Heavy library usage (NumPy, Matplotlib) causes slowdown | Medium | Low (some cells slow, others fast) | Document performance expectations; provide local alternatives for intensive tasks |
| Browser runs out of memory after many cell executions | Low | Medium (browser tab crashes) | Add "Reset Kernel" button; warn if memory usage >70% |

---

**Status**: Ready for Clarification Check (if needed) → Planning Phase

