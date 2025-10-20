# Data Model: Thebe LiveCode Integration

**Feature**: 001-thebe-livecode-integration  
**Created**: 2025-10-20  
**Status**: Design Complete

---

## Overview

This document defines the data entities, relationships, validation rules, and state transitions for the Thebe LiveCode Integration feature. The data model supports browser-based Python execution via Pyodide with per-tema configuration.

---

## Entity 1: CodeCell

**Description**: Represents a single executable Python code cell in a tema page.

**Attributes**:

| Attribute | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `cellId` | String | Yes | Auto-generated | Unique identifier (UUID v4) |
| `sourceCode` | String | Yes | `""` | Python code to execute |
| `metadata` | CellMetadata | No | `{}` | Cell configuration (tags, images) |
| `output` | String | No | `null` | Execution result (stdout/stderr) |
| `status` | Enum | Yes | `ready` | Execution state (see states below) |
| `executionCount` | Integer | No | `0` | Number of times executed |
| `lastExecutedAt` | DateTime | No | `null` | Last execution timestamp (ISO 8601) |
| `error` | String | No | `null` | Error message if execution failed |

**States** (status field):

| State | Description | Transitions To |
|-------|-------------|---------------|
| `ready` | Cell not yet executed | `executing`, `disabled` |
| `executing` | Cell currently running | `completed`, `error` |
| `completed` | Execution succeeded | `executing`, `ready` |
| `error` | Execution failed | `executing`, `ready` |
| `disabled` | Thebe unavailable (fallback mode) | None (terminal state) |

**Validation Rules**:

1. `sourceCode` must be valid Python syntax (validated by Pyodide)
2. `cellId` must be unique per page
3. `executionCount` cannot be negative
4. `lastExecutedAt` must be in ISO 8601 format
5. `output` length limited to 1 MB (prevent memory exhaustion)

**Example**:

```json
{
  "cellId": "cell-a3f7b9c2",
  "sourceCode": "import numpy as np\nprint(np.__version__)",
  "metadata": {
    "tags": ["hide-input"],
    "fallbackImage": null
  },
  "output": "1.24.3",
  "status": "completed",
  "executionCount": 1,
  "lastExecutedAt": "2025-10-20T14:32:15Z",
  "error": null
}
```

---

## Entity 2: Kernel

**Description**: Represents the Pyodide WebAssembly Python runtime instance for a page.

**Attributes**:

| Attribute | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `kernelId` | String | Yes | Auto-generated | Unique kernel identifier (UUID v4) |
| `status` | Enum | Yes | `uninitialized` | Kernel state (see states below) |
| `pyodideVersion` | String | No | `null` | Pyodide version (e.g., "0.23.0") |
| `loadedPackages` | Array<String> | No | `[]` | Pre-loaded packages (e.g., ["numpy", "matplotlib"]) |
| `memoryUsageMB` | Integer | No | `0` | Current memory usage in MB |
| `initializationTime` | Integer | No | `null` | Init latency in milliseconds |
| `createdAt` | DateTime | Yes | Auto-set | Kernel creation timestamp (ISO 8601) |
| `lastActivityAt` | DateTime | No | `null` | Last cell execution timestamp |

**States** (status field):

| State | Description | Transitions To |
|-------|-------------|---------------|
| `uninitialized` | Kernel not loaded | `initializing`, `failed` |
| `initializing` | Pyodide downloading/loading | `ready`, `failed` |
| `ready` | Kernel operational | `busy`, `restarting`, `shutdown` |
| `busy` | Cell executing | `ready`, `error` |
| `error` | Execution error (recoverable) | `ready`, `restarting` |
| `restarting` | Manual restart triggered | `ready`, `failed` |
| `shutdown` | Kernel destroyed (page unload) | None (terminal state) |
| `failed` | Initialization failed | `restarting` |

**Validation Rules**:

1. `kernelId` must be unique per page session
2. `loadedPackages` must contain only Pyodide-available packages
3. `memoryUsageMB` must be ≥ 0
4. `initializationTime` must be ≥ 0 milliseconds
5. `createdAt` and `lastActivityAt` must be in ISO 8601 format

**Example**:

```json
{
  "kernelId": "kernel-f4e8a1d3",
  "status": "ready",
  "pyodideVersion": "0.23.0",
  "loadedPackages": ["numpy", "matplotlib", "scipy"],
  "memoryUsageMB": 245,
  "initializationTime": 8500,
  "createdAt": "2025-10-20T14:30:00Z",
  "lastActivityAt": "2025-10-20T14:32:15Z"
}
```

---

## Entity 3: CellMetadata

**Description**: Configuration and display options for a code cell.

**Attributes**:

| Attribute | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `tags` | Array<String> | No | `[]` | Jupyter-standard tags (e.g., ["hide-input"]) |
| `fallbackImage` | String | No | `null` | Relative path to static image (e.g., "figures/plot.png") |
| `localKernelRecommended` | Boolean | No | `false` | Show warning for heavy computation |
| `expectedExecutionTime` | Integer | No | `null` | Expected duration in seconds |

**Standard Tags** (subset of Jupyter-supported):

| Tag | Description | Thebe Support |
|-----|-------------|--------------|
| `hide-input` | Hide code, show output | ✅ Yes |
| `hide-output` | Show code, hide output | ✅ Yes |
| `remove-cell` | Hide entire cell | ✅ Yes |
| `thebe-init` | Auto-run on kernel start | ✅ Yes |
| `raises-exception` | Expected error | ✅ Yes |
| `skip-execution` | Don't run during build | ✅ Yes |

**Custom Tags** (TIF-specific):

| Tag | Description | Phase |
|-----|-------------|-------|
| `fallback-image` | Show static image + Run button | Phase 2B |
| `local-kernel-recommended` | Warn about browser performance | Phase 2B |
| `heavy-computation` | Expected >5 sec execution | Phase 2B |

**Validation Rules**:

1. `tags` array must contain only recognized tags
2. `fallbackImage` must be valid relative path (if set)
3. `expectedExecutionTime` must be > 0 seconds (if set)
4. If `fallbackImage` is set, `fallback-image` tag must be present

**Example**:

```json
{
  "tags": ["hide-input", "fallback-image"],
  "fallbackImage": "figures/tema-02/grafico-ejemplo.png",
  "localKernelRecommended": false,
  "expectedExecutionTime": 3
}
```

---

## Entity 4: ThebeConfig

**Description**: Book-level and per-tema configuration for Thebe integration.

**Attributes**:

| Attribute | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `enabled` | Boolean | Yes | `true` | Global Thebe enable/disable |
| `pyodideUrl` | String | Yes | CDN URL | Pyodide distribution URL |
| `defaultPackages` | Array<String> | No | `["numpy", "matplotlib"]` | Pre-loaded packages (global) |
| `initTimeout` | Integer | No | `30000` | Kernel init timeout (milliseconds) |
| `executionTimeout` | Integer | No | `30000` | Per-cell execution timeout (ms) |
| `temaOverrides` | Map<String, TemaConfig> | No | `{}` | Per-tema custom config |

**TemaConfig** (nested in `temaOverrides`):

| Attribute | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `extraPackages` | Array<String> | No | `[]` | Additional packages for this tema |
| `env` | Map<String, String> | No | `{}` | Environment variables |

**Validation Rules**:

1. `pyodideUrl` must be valid HTTPS URL
2. `defaultPackages` must contain only Pyodide-available packages
3. `initTimeout` must be ≥ 5000 ms (5 seconds minimum)
4. `executionTimeout` must be ≥ 1000 ms (1 second minimum)
5. `temaOverrides` keys must match tema identifiers (e.g., "tema-01", "tema-02")

**Example**:

```yaml
# In book/_config.yml (global)
sphinx:
  config:
    thebe_config:
      use_thebe_lite: true
      pyodide_url: "https://cdn.jsdelivr.net/pyodide/v0.23.0/full/"
      default_packages: ["numpy", "matplotlib"]
      init_timeout: 30000
      execution_timeout: 30000

# In book/tif_python/tema-05/teoria.md (per-tema override)
---
thebe:
  extra_packages: ["pandas", "scipy"]
  env:
    TEMA: "tema-05"
---
```

**JSON Representation**:

```json
{
  "enabled": true,
  "pyodideUrl": "https://cdn.jsdelivr.net/pyodide/v0.23.0/full/",
  "defaultPackages": ["numpy", "matplotlib"],
  "initTimeout": 30000,
  "executionTimeout": 30000,
  "temaOverrides": {
    "tema-05": {
      "extraPackages": ["pandas", "scipy"],
      "env": {
        "TEMA": "tema-05"
      }
    }
  }
}
```

---

## Entity 5: FallbackImage

**Description**: Static image displayed when Thebe is unavailable or before code execution.

**Attributes**:

| Attribute | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `imagePath` | String | Yes | N/A | Relative path to image file |
| `cellId` | String | Yes | N/A | Associated code cell ID |
| `altText` | String | No | `"Static output"` | Accessibility alt text |
| `visible` | Boolean | Yes | `true` | Whether image is currently displayed |

**Validation Rules**:

1. `imagePath` must be valid relative path
2. Image file must exist in `book/figures/` or `book/_static/`
3. Supported formats: PNG, JPEG, SVG
4. `cellId` must reference existing CodeCell
5. `altText` length ≤ 200 characters

**Example**:

```json
{
  "imagePath": "figures/tema-02/plot-ejemplo.png",
  "cellId": "cell-a3f7b9c2",
  "altText": "Gráfico de ejemplo: línea con puntos",
  "visible": true
}
```

---

## Entity Relationships

```
┌───────────────┐
│  ThebeConfig  │ (1)
└───────────────┘
        │
        │ configures
        ▼
┌───────────────┐
│    Kernel     │ (1 per page)
└───────────────┘
        │
        │ executes
        ▼
┌───────────────┐
│   CodeCell    │ (N per page)
└───────────────┘
        │
        │ contains
        ▼
┌───────────────┐
│ CellMetadata  │ (1 per cell)
└───────────────┘
        │
        │ may reference
        ▼
┌───────────────┐
│ FallbackImage │ (0-1 per cell)
└───────────────┘
```

**Relationships**:

| Relationship | Cardinality | Description |
|-------------|-------------|-------------|
| ThebeConfig → Kernel | 1:1 | One config per kernel |
| Kernel → CodeCell | 1:N | One kernel executes many cells |
| CodeCell → CellMetadata | 1:1 | Each cell has metadata |
| CellMetadata → FallbackImage | 1:0..1 | Optional fallback image |

---

## State Transition Diagrams

### CodeCell State Transitions

```
       ┌─────────┐
  ┌───→│  ready  │←───┐
  │    └─────────┘    │
  │         │         │
  │         │ Run clicked
  │         ▼         │
  │    ┌──────────┐   │
  │    │executing │   │
  │    └──────────┘   │
  │      │      │     │
  │ Success    Error  │
  │      │      │     │
  │      ▼      ▼     │
  │  ┌────────┬────┐  │
  └──│complete│error│──┘
     └────────┴────┘
     
     ┌────────┐
     │disabled│ (terminal)
     └────────┘
```

### Kernel State Transitions

```
┌──────────────┐
│uninitialized │
└──────────────┘
       │
       │ Init triggered
       ▼
┌──────────────┐    Timeout/Error
│ initializing │───────────────┐
└──────────────┘               │
       │                       │
       │ Success               ▼
       ▼                  ┌────────┐
┌──────────────┐          │ failed │
│    ready     │          └────────┘
└──────────────┘               │
       │                       │
       │ Cell execution        │ Restart
       ▼                       │
┌──────────────┐               │
│     busy     │               │
└──────────────┘               │
       │                       │
       │ Complete/Error        │
       ▼                       │
┌──────────────┐               │
│    ready     │←──────────────┘
└──────────────┘
       │
       │ Page unload
       ▼
┌──────────────┐
│   shutdown   │ (terminal)
└──────────────┘
```

---

## Validation Summary

**Global Constraints**:

1. **Kernel uniqueness**: Only 1 active Kernel per page
2. **Cell ID uniqueness**: All CodeCell IDs unique per page
3. **Memory limit**: Total kernel memory < 1 GB (browser limit)
4. **Execution timeout**: No cell execution > 30 seconds (configurable)
5. **Output size**: No cell output > 1 MB (prevent memory exhaustion)

**Data Integrity Rules**:

1. All timestamps must be ISO 8601 format
2. All URLs must be HTTPS (security)
3. All file paths must be relative (portability)
4. All numeric values must be non-negative
5. All enums must use defined values only

---

## Implementation Notes

**Storage**:
- Entities stored in browser memory (JavaScript objects)
- No backend persistence (stateless, page-scoped)
- Kernel state cleared on page unload

**Serialization**:
- JSON format for data exchange
- YAML format for configuration (Jupyter Book convention)
- ISO 8601 for timestamps
- UTF-8 encoding for all text

**Performance**:
- CodeCell execution: <5 seconds target (SC-002)
- Kernel initialization: <10 seconds target (SC-002)
- Memory monitoring: every 30 seconds (Phase 2C - T047)

---

**Status**: ✅ Design Complete  
**Next Step**: Implement contracts (T007) and integrate into Phase 2A
