---
name: scitex-compat
description: |
  [WHAT] Backward-compatibility shims — `@deprecated` decorator and legacy `notify`/`notify_async` forwarders so old SciTeX code keeps working while the ecosystem migrates.
  [WHEN] Marking a function/class as deprecated with replacement info, keeping an old SciTeX alias alive, or forwarding a legacy call to the new module.
  [HOW] `from scitex_compat import deprecated, notify, notify_async` — wrap with `@deprecated(reason=..., version=..., replacement=...)`.
tags: [scitex-compat]
primary_interface: python
interfaces:
  python: 3
  cli: 0
  mcp: 0
  skills: 1
  http: 0
---

# scitex-compat

> **Interfaces:** Python ⭐⭐⭐ (primary) · CLI — · MCP — · Skills ⭐ · Hook — · HTTP —

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

- [01_installation.md](01_installation.md) — pip install + smoke verify
- [02_quick-start.md](02_quick-start.md) — @deprecated + legacy notify forwarders
- [03_python-api.md](03_python-api.md) — public symbols and signatures
- [10_quick-start.md](10_quick-start.md) — legacy quick-start (kept for context)
- [11_python-api.md](11_python-api.md) — legacy API notes (kept for context)

No CLI, no MCP tools, no extra modules.
