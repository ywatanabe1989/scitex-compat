---
name: scitex-compat
description: Backward-compatibility shims for deprecated SciTeX APIs — holds legacy aliases so old user code keeps working while the ecosystem migrates. Public API (3 symbols) — `@deprecated(reason=..., version=..., replacement=...)` decorator (wraps a function/class to emit `DeprecationWarning` on call with a helpful message pointing at the new location) and legacy notification wrappers `notify(...)` + `notify_async(...)` that forward to the modern `scitex.notify` package. No CLI, no MCP tools, intentionally minimal — new features belong in the proper module, not here. Drop-in replacement for ad-hoc `warnings.warn("X is deprecated, use Y", DeprecationWarning, stacklevel=2)` boilerplate and hand-rolled `def notify(...): from .new_location import notify as _n; return _n(...)` forwarders. Use whenever the user asks to "mark a function as deprecated", "keep an old SciTeX alias working", "forward a legacy call to the new module", "add a DeprecationWarning with replacement info", or mentions `scitex.compat`, `@deprecated`, API migration shim.
user-invocable: false
primary_interface: python
---

# scitex-compat

> **Primary interface: Python API.** Import in scripts/notebooks — CLI & MCP are thin wrappers over the Python functions.

Thin compatibility layer. Holds deprecated aliases so old user code keeps
working (with a `DeprecationWarning`) while the ecosystem migrates to new
module locations. This package is intentionally minimal; do not add new
features here — add them in the proper module and, if needed, a shim here.

## Installation & import (two equivalent paths)

The same module is reachable via two install paths. Both forms work at
runtime; which one a user has depends on their install choice.

```python
# Standalone — pip install scitex-compat
import scitex_compat
scitex_compat.deprecated(...)

# Umbrella — pip install scitex
import scitex.compat
scitex.compat.deprecated(...)
```

`pip install scitex-compat` alone does NOT expose the `scitex` namespace;
`import scitex.compat` raises `ModuleNotFoundError`. To use the
`scitex.compat` form, also `pip install scitex`.

See [../../general/02_interface-python-api.md] for the ecosystem-wide
rule and empirical verification table.

## Sub-skills

- [01_quick-start.md](01_quick-start.md) — install, import, usage snippets
- [02_python-api.md](02_python-api.md) — public symbols and signatures

No CLI, no MCP tools, no extra modules.
