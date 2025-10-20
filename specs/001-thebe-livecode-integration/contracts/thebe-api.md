# API Contracts: Thebe LiveCode Integration

**Feature**: 001-thebe-livecode-integration  
**Created**: 2025-10-20  
**Status**: Design Complete

---

## Overview

This document defines the JavaScript API contracts for the Thebe LiveCode Integration. All APIs are browser-side only (no backend). Contracts map user actions to function signatures, input/output schemas, and error handling.

---

## Contract 1: Initialize Kernel

**User Action**: Learner loads a page with Thebe-enabled code cells

**API**: `ThebeKernelManager.initialize()`

**Description**: Initializes Pyodide WebAssembly kernel with configured packages.

### Request

**Function Signature**:
```javascript
async initialize(config?: ThebeConfig): Promise<InitializeResult>
```

**Input Schema** (`ThebeConfig`):
```typescript
interface ThebeConfig {
  pyodideUrl?: string;              // Default: "https://cdn.jsdelivr.net/pyodide/v0.23.0/full/"
  packages?: string[];              // Default: ["numpy", "matplotlib"]
  timeout?: number;                 // Default: 30000 ms
  onProgress?: (progress: number) => void;  // Optional progress callback (0-100)
}
```

**Example Request**:
```javascript
const result = await kernelManager.initialize({
  pyodideUrl: "https://cdn.jsdelivr.net/pyodide/v0.23.0/full/",
  packages: ["numpy", "matplotlib", "scipy"],
  timeout: 30000,
  onProgress: (progress) => {
    console.log(`Initializing: ${progress}%`);
  }
});
```

### Response

**Output Schema** (`InitializeResult`):
```typescript
interface InitializeResult {
  success: boolean;
  kernelId: string;                 // UUID of created kernel
  pyodideVersion: string;           // e.g., "0.23.0"
  loadedPackages: string[];
  initializationTime: number;       // Milliseconds
  memoryUsageMB: number;
  error?: string;                   // Error message if success=false
}
```

**Success Response** (200 OK equivalent):
```json
{
  "success": true,
  "kernelId": "kernel-f4e8a1d3",
  "pyodideVersion": "0.23.0",
  "loadedPackages": ["numpy", "matplotlib", "scipy"],
  "initializationTime": 8500,
  "memoryUsageMB": 245,
  "error": null
}
```

**Error Response** (failure cases):
```json
{
  "success": false,
  "kernelId": null,
  "pyodideVersion": null,
  "loadedPackages": [],
  "initializationTime": 0,
  "memoryUsageMB": 0,
  "error": "Timeout: Pyodide failed to load in 30 seconds"
}
```

### Error Codes

| Error Type | Error Message | User Action |
|-----------|--------------|-------------|
| `WASM_UNSUPPORTED` | "Browser does not support WebAssembly" | Show fallback mode |
| `NETWORK_TIMEOUT` | "Timeout: Pyodide failed to load in {timeout} seconds" | Show retry button |
| `NETWORK_ERROR` | "Network error: {details}" | Show retry button |
| `MEMORY_ERROR` | "Out of memory: {details}" | Show restart kernel button |
| `PACKAGE_ERROR` | "Package load failed: {packageName}" | Continue with warning |

### Testing Scenarios

| Scenario | Input | Expected Output |
|----------|-------|----------------|
| **Success** | Default config | `success: true`, kernel initialized |
| **Custom packages** | `packages: ["pandas"]` | `loadedPackages: ["pandas"]` |
| **Timeout** | `timeout: 100` (too short) | `success: false`, `error: "Timeout..."` |
| **WASM unsupported** | Test on IE11 | `success: false`, `error: "Browser does not support..."` |

---

## Contract 2: Execute Code Cell

**User Action**: Learner clicks "Run" button on a code cell

**API**: `ThebeKernelManager.executeCell()`

**Description**: Executes Python code in the active kernel and returns output.

### Request

**Function Signature**:
```javascript
async executeCell(cellId: string, sourceCode: string, options?: ExecuteOptions): Promise<ExecuteResult>
```

**Input Schema** (`ExecuteOptions`):
```typescript
interface ExecuteOptions {
  timeout?: number;                 // Default: 30000 ms
  silent?: boolean;                 // Default: false (don't show output)
  storeHistory?: boolean;           // Default: true (increment execution count)
}
```

**Example Request**:
```javascript
const result = await kernelManager.executeCell(
  "cell-a3f7b9c2",
  "import numpy as np\nprint(np.__version__)",
  { timeout: 30000, silent: false, storeHistory: true }
);
```

### Response

**Output Schema** (`ExecuteResult`):
```typescript
interface ExecuteResult {
  success: boolean;
  cellId: string;
  output: string;                   // stdout + stderr combined
  executionTime: number;            // Milliseconds
  executionCount: number;           // Number of times this cell executed
  memoryUsageMB: number;            // Current kernel memory
  error?: string;                   // Error message if failed
  errorType?: string;               // Python exception type (e.g., "NameError")
}
```

**Success Response**:
```json
{
  "success": true,
  "cellId": "cell-a3f7b9c2",
  "output": "1.24.3\n",
  "executionTime": 150,
  "executionCount": 1,
  "memoryUsageMB": 250,
  "error": null,
  "errorType": null
}
```

**Error Response** (Python exception):
```json
{
  "success": false,
  "cellId": "cell-a3f7b9c2",
  "output": "",
  "executionTime": 50,
  "executionCount": 1,
  "memoryUsageMB": 245,
  "error": "NameError: name 'x' is not defined",
  "errorType": "NameError"
}
```

### Error Codes

| Error Type | Error Message | User Action |
|-----------|--------------|-------------|
| `SYNTAX_ERROR` | "SyntaxError: {details}" | Show error, highlight code |
| `NAME_ERROR` | "NameError: name '{variable}' is not defined" | Show error message |
| `TIMEOUT` | "Execution timeout after {timeout} seconds" | Show warning, offer restart |
| `MEMORY_ERROR` | "MemoryError: Out of memory" | Show restart kernel button |
| `MODULE_NOT_FOUND` | "ModuleNotFoundError: No module named '{module}'" | Show package installation guide |

### Testing Scenarios

| Scenario | Input | Expected Output |
|----------|-------|----------------|
| **Success** | `print("Hello")` | `output: "Hello\n"`, `success: true` |
| **Variable** | `x = 5; print(x)` | `output: "5\n"` |
| **Error** | `print(undefined_var)` | `success: false`, `errorType: "NameError"` |
| **Timeout** | `import time; time.sleep(100)` | `error: "Execution timeout..."` |
| **Missing module** | `import tensorflow` | `error: "ModuleNotFoundError..."` |

---

## Contract 3: Restart Kernel

**User Action**: Learner clicks "Restart Kernel" button

**API**: `ThebeKernelManager.restart()`

**Description**: Shuts down current kernel and creates a fresh instance.

### Request

**Function Signature**:
```javascript
async restart(config?: ThebeConfig): Promise<InitializeResult>
```

**Input Schema**: Same as `initialize()` (reuses config)

**Example Request**:
```javascript
const result = await kernelManager.restart({
  packages: ["numpy", "matplotlib"]
});
```

### Response

**Output Schema**: Same as `InitializeResult` (reuses schema)

**Success Response**:
```json
{
  "success": true,
  "kernelId": "kernel-new-uuid",
  "pyodideVersion": "0.23.0",
  "loadedPackages": ["numpy", "matplotlib"],
  "initializationTime": 3500,
  "memoryUsageMB": 200,
  "error": null
}
```

### Error Codes

Same as `initialize()` contract.

### Testing Scenarios

| Scenario | Input | Expected Output |
|----------|-------|----------------|
| **Success** | Default config | New kernel created, old variables cleared |
| **After error** | Kernel in error state | Fresh kernel, error cleared |
| **Memory cleanup** | High memory usage | Memory drops to baseline (~200 MB) |

---

## Contract 4: Clear Cell Output

**User Action**: Learner clicks "Clear Output" button on a cell

**API**: `ThebeKernelManager.clearCellOutput()`

**Description**: Clears the output area of a code cell (doesn't affect kernel state).

### Request

**Function Signature**:
```javascript
clearCellOutput(cellId: string): void
```

**Input Schema**:
```typescript
interface ClearCellInput {
  cellId: string;                   // UUID of cell
}
```

**Example Request**:
```javascript
kernelManager.clearCellOutput("cell-a3f7b9c2");
```

### Response

**Output Schema**: None (void return, synchronous operation)

**Success Behavior**:
- Cell output DOM element cleared
- `executionCount` preserved
- Kernel state unchanged
- No error thrown

**Error Behavior**:
- If `cellId` not found: Console warning, no throw
- If cell not executed yet: No-op

### Testing Scenarios

| Scenario | Input | Expected Output |
|----------|-------|----------------|
| **Success** | Valid `cellId` | Output cleared, no error |
| **Invalid cell** | Non-existent `cellId` | Console warning, no throw |
| **Not executed** | Cell with no output | No-op |

---

## Contract 5: Get Kernel Status

**User Action**: Page checks if kernel is ready before executing cells

**API**: `ThebeKernelManager.getStatus()`

**Description**: Returns current kernel state and metadata.

### Request

**Function Signature**:
```javascript
getStatus(): KernelStatus
```

**Input Schema**: None (no parameters)

**Example Request**:
```javascript
const status = kernelManager.getStatus();
```

### Response

**Output Schema** (`KernelStatus`):
```typescript
interface KernelStatus {
  initialized: boolean;
  status: 'uninitialized' | 'initializing' | 'ready' | 'busy' | 'error' | 'shutdown';
  kernelId: string | null;
  pyodideVersion: string | null;
  loadedPackages: string[];
  memoryUsageMB: number;
  uptime: number;                   // Milliseconds since kernel created
}
```

**Example Response** (kernel ready):
```json
{
  "initialized": true,
  "status": "ready",
  "kernelId": "kernel-f4e8a1d3",
  "pyodideVersion": "0.23.0",
  "loadedPackages": ["numpy", "matplotlib"],
  "memoryUsageMB": 250,
  "uptime": 45000
}
```

**Example Response** (kernel not initialized):
```json
{
  "initialized": false,
  "status": "uninitialized",
  "kernelId": null,
  "pyodideVersion": null,
  "loadedPackages": [],
  "memoryUsageMB": 0,
  "uptime": 0
}
```

### Testing Scenarios

| Scenario | Expected Output |
|----------|----------------|
| **Before init** | `status: "uninitialized"` |
| **During init** | `status: "initializing"` |
| **After init** | `status: "ready"` |
| **During execution** | `status: "busy"` |
| **After error** | `status: "error"` |
| **After page unload** | `status: "shutdown"` |

---

## Event Listeners

### Available Events

| Event Name | Trigger | Payload |
|-----------|---------|---------|
| `kernel:initialized` | Kernel ready | `{ kernelId, pyodideVersion }` |
| `kernel:error` | Kernel failed | `{ error, errorType }` |
| `cell:executing` | Cell starts execution | `{ cellId }` |
| `cell:executed` | Cell completes | `{ cellId, output, executionTime }` |
| `cell:error` | Cell execution fails | `{ cellId, error, errorType }` |
| `memory:warning` | Memory >80% limit | `{ memoryUsageMB, limitMB }` |

### Event Registration

**Function Signature**:
```javascript
ThebeKernelManager.on(eventName: string, callback: Function): void
```

**Example Usage**:
```javascript
kernelManager.on('kernel:initialized', (payload) => {
  console.log(`Kernel ready: ${payload.kernelId}`);
  document.body.classList.add('thebe-ready');
});

kernelManager.on('cell:error', (payload) => {
  console.error(`Cell ${payload.cellId} error: ${payload.error}`);
  showErrorBanner(payload.error);
});
```

---

## Error Handling Strategy

### Global Error Handler

```javascript
ThebeKernelManager.setErrorHandler((error) => {
  console.error('Thebe error:', error);
  
  switch (error.type) {
    case 'WASM_UNSUPPORTED':
      showFallbackMode('wasm_unsupported');
      break;
    case 'NETWORK_TIMEOUT':
      showRetryButton();
      break;
    case 'MEMORY_ERROR':
      showRestartKernelButton();
      break;
    default:
      showGenericError(error.message);
  }
});
```

### Per-Cell Error Handling

```javascript
try {
  const result = await kernelManager.executeCell(cellId, code);
  if (!result.success) {
    showCellError(cellId, result.error, result.errorType);
  }
} catch (error) {
  console.error('Unexpected error:', error);
  showCellError(cellId, 'Unexpected error occurred', 'UnknownError');
}
```

---

## Performance Requirements

| Operation | Target | Maximum |
|-----------|--------|---------|
| `initialize()` | <10 sec | 30 sec (timeout) |
| `executeCell()` | <5 sec | 30 sec (timeout) |
| `restart()` | <5 sec | 30 sec (timeout) |
| `clearCellOutput()` | <50 ms | 100 ms |
| `getStatus()` | <10 ms | 50 ms |

---

## Security Considerations

1. **No eval()**: All code executed in Pyodide sandbox (no access to DOM)
2. **CORS restrictions**: Network requests blocked by browser same-origin policy
3. **File access**: No access to local filesystem (WASM sandbox)
4. **Memory limits**: Browser enforces WASM memory limits (~4 GB Chrome/Firefox)
5. **Input validation**: All user code sanitized before execution (Pyodide handles)

---

**Status**: ✅ Design Complete  
**Next Step**: Implement contracts in Phase 2A (T012-T014)
