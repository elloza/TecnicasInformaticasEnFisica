# Phase 0 Research: Thebe LiveCode Integration

**Status**: Ready for Execution  
**Timeline**: 1-2 days (parallelizable)  
**Output**: Technical findings + recommendations for Phase 1 design

---

## Research Overview

This document will be populated during Phase 0 research execution. Each section below is a research task placeholder. Research should fill in findings, recommendations, and proof-of-concept code.

---

## Task 0.1: Jupyter Book + Thebe Configuration

**Objective**: Determine minimal `_config.yml` Thebe config + version compatibility

**Research Questions**:
1. What's the minimal Thebe configuration in Jupyter Book v1.0+?
2. Are there breaking changes between Jupyter Book versions?
3. What Thebe version is recommended?
4. Where is Thebe CDN hosted? Is there SLA?
5. Can Thebe be configured per-page or only globally?

**Deliverable Expected**:
- Thebe config YAML snippet (ready to paste into `_config.yml`)
- Version compatibility matrix (Jupyter Book × Thebe × Pyodide)
- Troubleshooting guide for common config errors
- Examples from Jupyter Book official docs
- Tested locally: `jupyter-book build book/` succeeds with Thebe enabled

**Status**: ⏳ Not Started
**Owner**: Dev Lead

---

## Task 0.2: Pyodide Package Loading

**Objective**: Understand pre-loading packages + performance trade-offs

**Research Questions**:
1. How are packages pre-loaded in Pyodide? (syntax, mechanism)
2. What's the kernel initialization latency for 0/1/5/10 packages?
3. What's the memory footprint per package?
4. Which packages are recommended for tema-00-06 curriculum?
5. Can packages be loaded dynamically after init? (lazy loading)
6. What happens if a pre-loaded package is unavailable?

**Deliverable Expected**:
- Package loading patterns documentation
- Latency benchmarks (kernel init time for various package counts)
- Memory footprint comparisons
- Recommended defaults for tema-00-06
- List of Pyodide-available packages relevant to TIF curriculum

**Status**: ⏳ Not Started
**Owner**: Dev Lead

---

## Task 0.3: Cell Metadata & Rendering

**Objective**: Map Jupyter metadata to Thebe rendering behavior

**Research Questions**:
1. What standard Jupyter cell metadata does Thebe respect?
2. How does Thebe render cell metadata (tags, hide-input, hide-output)?
3. Can custom metadata be added? (e.g., `fallback-image`)
4. How are CSS classes applied to cells for styling?
5. Can fallback images be rendered with Thebe hooks?
6. What JavaScript events are available for custom logic?

**Deliverable Expected**:
- Standard cell metadata table (tags, hide-output, hide-input, cell-id, etc.)
- Thebe rendering hooks (CSS classes, JS callbacks)
- Fallback image rendering approach (CSS + HTML structure)
- Tested examples showing metadata effect on output HTML
- Author documentation for using metadata

**Status**: ⏳ Not Started
**Owner**: Frontend Dev

---

## Task 0.4: Graceful Degradation & Failure Modes

**Objective**: Document Pyodide failures + recommended UX

**Research Questions**:
1. What are the failure modes when Pyodide fails to load?
2. Can we detect WASM unsupported browsers?
3. How to handle network timeouts?
4. What's the browser memory limit before Pyodide crashes?
5. Can we detect + report these failures to users?
6. What's the recommended UX flow for each failure?

**Deliverable Expected**:
- Pyodide failure scenarios (WASM unsupported, network timeout, memory exhaustion, version mismatch)
- Error detection code (JavaScript snippets to catch failures)
- Recovery strategies + UX flows
- Recommended error messaging (user-friendly, actionable)
- Fallback content rendering approach (static HTML cells)
- Tested failure scenarios with screenshots

**Status**: ⏳ Not Started
**Owner**: Frontend Dev + QA

---

## Task 0.5: Kernel Lifecycle & Multi-Page Isolation

**Objective**: Understand Thebe kernel architecture + page-scoping approach

**Research Questions**:
1. How does Thebe manage kernel lifecycle? (init, exec, cleanup)
2. Can Thebe isolate kernels per page?
3. What's the browser memory footprint of a kernel instance?
4. Are there browser memory leaks when kernels are created/destroyed?
5. How do page transitions affect kernel state?
6. Can we reset kernel state on demand?

**Deliverable Expected**:
- Thebe kernel lifecycle diagram (init → execute → destroy)
- Multi-page kernel isolation patterns (per-page instances vs. shared)
- Implementation approach (JavaScript event listeners, page transitions)
- Browser memory implications + leak testing
- Tested prototype: kernel isolation demo showing page independence
- Performance profile (memory usage over time, multiple kernels)

**Status**: ⏳ Not Started
**Owner**: Dev Lead + Frontend Dev

---

## Key References (To be filled during research)

- Jupyter Book documentation: https://jupyterbook.org/
- Thebe documentation: https://thebe.readthedocs.io/
- Pyodide documentation: https://pyodide.org/
- Jupyter metadata standards: https://jupyter.org/

---

## Consolidated Findings (To be populated)

*This section will contain executive summary of all research findings after tasks complete.*

### Decision: Minimal Thebe Configuration
[To be filled after Task 0.1]

### Recommendation: Package Pre-Loading Strategy
[To be filled after Task 0.2]

### Decision: Cell Metadata Handling
[To be filled after Task 0.3]

### Recommendation: Graceful Degradation UX
[To be filled after Task 0.4]

### Decision: Kernel Isolation Architecture
[To be filled after Task 0.5]

---

## Timeline & Dependencies

**Parallelizable Tasks**: All 5 tasks can run in parallel (different team members)

**Critical Path**:
- Task 0.1 (Jupyter Book config) — blocks Phase 1 start
- Task 0.5 (Kernel architecture) — blocks Phase 1 design

**Target Completion**: [DATE 1-2 days from start]

**Blockers to Phase 1 Start**:
- ✅ All 5 research tasks complete
- ✅ Consolidated findings documented
- ✅ Recommendations agreed by team
- ✅ Proof-of-concept code written + tested

---

**Research Status**: Ready for Phase 0 Execution  
**Next Step**: Assign tasks to research team; schedule Phase 0 kickoff