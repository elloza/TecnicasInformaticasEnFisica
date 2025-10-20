# Developer Quickstart: Thebe LiveCode Integration

**Target Audience**: Backend/Frontend developers implementing Thebe integration  
**Duration**: 15-20 minutes to read + understand  
**Prerequisites**: Familiarity with Jupyter Book, Python, JavaScript  

---

## Quick Overview

**What is Thebe?**
Thebe is a browser-based execution layer for Jupyter Book that enables learners to run Python code directly in the browser using Pyodide (WebAssembly Python). No local Python installation required.

**What are we building?**
We're integrating Thebe into TIF TeachBook so that:
1. Code examples in `teoria.md` are "Run"-able in the browser
2. Exercises in `ejercicios.md` can be attempted + executed in-place
3. Output (plots, tables, errors) displays immediately inline
4. Kernel state persists within a page (but resets on navigation)

**Why?**
- **Accessibility**: No installation friction for learners
- **Engagement**: Immediate feedback loop enhances learning
- **Scalability**: Browser runtime is free + distributed (via CDN)

---

## Architecture at a Glance

```
┌─────────────────────────────────────────────────────┐
│ Browser (Learner's Machine)                         │
├─────────────────────────────────────────────────────┤
│                                                      │
│  TeachBook HTML                                     │
│  ├─ teoria.md (rendered)                           │
│  │  ├─ Code Cell 1 [Run] ← Thebe attaches UI      │
│  │  ├─ Code Cell 2 [Run]                           │
│  │  └─ Plot Output (after execution)               │
│  │                                                  │
│  └─ ejercicios.md (rendered)                       │
│     ├─ Exercise 1 code cell [Run]                  │
│     └─ Exercise 2 code cell [Run]                  │
│                                                      │
│  Thebe JavaScript Library (CDN)                     │
│  ├─ Cell detection + "Run" button injection        │
│  ├─ Event handlers (click "Run" → execute)         │
│  └─ Kernel management                              │
│                                                      │
│  Pyodide WebAssembly (CDN)                         │
│  ├─ Python runtime (v3.10+)                        │
│  ├─ NumPy, Matplotlib pre-loaded                   │
│  └─ Standard library                               │
│                                                      │
└─────────────────────────────────────────────────────┘
```

---

## Key Concepts

### Code Cells
Marked with `{code-cell} ipython3` in Markdown:
```markdown
```{code-cell} ipython3
import numpy as np
x = np.array([1, 2, 3])
print(x)
```
```

When rendered by Jupyter Book + Thebe:
- "Run" button appears (via Thebe)
- Clicking "Run" sends code to Pyodide kernel
- Output appears below cell

### Kernels
One **kernel instance per page** (teoría.md, ejercicios.md, etc.):
- Initialized lazily on first "Run" click
- Maintains global variables across cell executions within the page
- Destroyed on page navigation (fresh kernel on return)
- Can be manually reset via "Clear Kernel" button

### Cell Metadata
Used to control execution + rendering:
```yaml
---
tags: ["hide-output"]        # Don't show output
hide-input: false             # Show code
fallback-image: "fig.png"     # Static image fallback
---
```

### Pyodide
WebAssembly Python runtime:
- Pre-loaded packages: NumPy, Matplotlib, standard library
- Additional packages can be specified per-tema (Task 0.2)
- 50MB initial download (cached by browser)
- 5-10 sec kernel init (first run only)

---

## Development Workflow

### Phase A: MVP (Tema-00 Basic Interactivity)

**Goal**: Get "Run" button working + show output for tema-00

**Step 1: Configure Thebe in `_config.yml`**
```yaml
# book/_config.yml
html:
  extra_footer: "Powered by Jupyter Book + Thebe"

thebe:
  enabled: true
  pyodide_url: "https://cdn.jsdelivr.net/pyodide/v0.23.4/full/"
```

**Step 2: Create Thebe initialization script**
```javascript
// book/_static/thebe-init.js
window.addEventListener('DOMContentLoaded', () => {
  if (window.thebe) {
    window.thebe.bootstrap();
  }
});
```

**Step 3: Link script in `_config.yml`**
```yaml
html:
  extra_js:
    - "_static/thebe-init.js"
```

**Step 4: Build & test**
```bash
pip install -r requirements.txt
jupyter-book build book/
# Open book/_build/html/tif_python/tema-00/teoria.html
# Click "Run" on any code cell → should execute
```

### Phase B: Extended Features (Metadata + Fallbacks)

**Goal**: Support cell metadata + fallback images

**Step 1: Parse cell metadata from Jupyter Book output**
- Extract `tags`, `hide-input`, `hide-output`, `fallback-image` from cell attributes
- Store in memory when page loads

**Step 2: Render fallback images**
```javascript
if (cellMetadata.fallbackImage) {
  const fallbackDiv = document.createElement('div');
  fallbackDiv.innerHTML = `
    <img src="${cellMetadata.fallbackImage}" alt="Fallback output" />
    <p><small>Click 'Run' to execute code locally</small></p>
  `;
  cellElement.prepend(fallbackDiv);
}
```

**Step 3: Hide/show cell output based on metadata**
```javascript
if (cellMetadata.hideOutput) {
  cellElement.querySelector('.cell_output').style.display = 'none';
}
```

### Phase C: Configuration & Ops (Per-Tema Config)

**Goal**: Per-tema package loading + kernel reset

**Step 1: Parse per-tema config from front matter**
```yaml
---
thebe:
  extra_packages: ["scipy"]
  env:
    OMP_NUM_THREADS: "1"
---
```

**Step 2: Initialize Pyodide with custom packages**
```javascript
const config = {
  packages: ['numpy', 'matplotlib', 'scipy'], // from front matter
  env: { OMP_NUM_THREADS: '1' } // from front matter
};
const kernel = new Pyodide(config);
```

**Step 3: Add "Reset Kernel" button + memory monitor**
```javascript
// Add reset button to page
const resetBtn = document.createElement('button');
resetBtn.textContent = 'Clear Kernel';
resetBtn.onclick = () => kernel.destroy();
document.body.prepend(resetBtn);

// Monitor memory
setInterval(() => {
  const memUsage = kernel.memory.current_size;
  if (memUsage > MEMORY_THRESHOLD) {
    showWarning("Kernel using high memory; consider resetting");
  }
}, 5000);
```

---

## Testing Strategy

### Unit Tests
- **Kernel initialization**: Verify Pyodide loads without errors
- **Code execution**: Run sample Python snippets; verify output
- **Cell metadata parsing**: Parse + apply metadata correctly

### Integration Tests
- **Tema-00 teoría**: All 5 theory cells execute in browser
- **Tema-00 ejercicios**: All 10 exercise cells execute + produce expected output
- **Page navigation**: Kernel destroyed on nav; fresh kernel on return
- **Fallback images**: Display correctly; Run button still functional

### Browser Compatibility
- ✅ Chrome 74+
- ✅ Firefox 79+
- ✅ Safari 14.1+
- ✅ Edge 79+
- ✅ WASM support detection + graceful fallback

### Performance Baselines
- First kernel load: <10 seconds (SC-002)
- Cell execution: <5 seconds for typical operations (SC-002)
- Memory: <100MB per kernel (to avoid browser crash)

---

## Common Pitfalls

### ❌ Pitfall 1: Code works locally but fails in Pyodide
**Reason**: Pyodide doesn't have all packages/features
**Solution**: Test in browser during development; use fallbacks for unsupported features

### ❌ Pitfall 2: Kernel state leaks between pages
**Reason**: Shared global kernel instead of per-page
**Solution**: Verify kernel destroyed on `beforeunload` event

### ❌ Pitfall 3: Memory exhaustion after many cells
**Reason**: Kernels not garbage-collected
**Solution**: Implement memory monitoring + warn user to reset kernel

### ❌ Pitfall 4: Pyodide fails to load silently
**Reason**: Network issue or WASM unsupported
**Solution**: Wrap Pyodide init in try-catch; display user-friendly banner

---

## Debugging Tips

### Check if Thebe is loaded
```javascript
// In browser console:
console.log(window.thebe); // Should return Thebe object
console.log(window.pyodide); // Should return Pyodide instance
```

### Debug kernel execution
```javascript
// Add logging to kernel execution:
kernel.executeCode = function(code) {
  console.log('Executing:', code);
  const result = originalExecute(code);
  console.log('Result:', result);
  return result;
};
```

### Test cell rendering
```javascript
// In browser console:
const cells = document.querySelectorAll('.cell');
console.log('Found', cells.length, 'cells');
cells.forEach((cell, i) => {
  const runBtn = cell.querySelector('[role="button"]');
  console.log(`Cell ${i}: has Run button?`, !!runBtn);
});
```

---

## Resources

- **Jupyter Book Docs**: https://jupyterbook.org/interactive/thebe.html
- **Thebe GitHub**: https://github.com/executablebooks/thebe
- **Pyodide Docs**: https://pyodide.org/en/stable/
- **TIF Constitution**: `.specify/memory/constitution.md` (principles guide)
- **Feature Spec**: `specs/001-thebe-livecode-integration/spec.md` (requirements)
- **Implementation Plan**: `specs/001-thebe-livecode-integration/plan.md` (phases)

---

## Next Steps

1. **Phase 0**: Research tasks (1-2 days) → populate `research.md`
2. **Phase 1**: Design + data model (1 day) → create `data-model.md` + `contracts/`
3. **Phase A**: MVP implementation (5-7 days) → tema-00 interactive
4. **Phase B**: Extended features (4-5 days) → metadata + fallbacks
5. **Phase C**: Configuration (6-8 days) → full curriculum rollout

---

**Quickstart Version**: 1.0.0 | **Updated**: 2025-10-20