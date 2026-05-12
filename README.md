# scitex-compat

<p align="center">
  <a href="https://scitex.ai">
    <img src="docs/scitex-logo-blue-cropped.png" alt="SciTeX" width="400">
  </a>
</p>

<p align="center"><b>Backward compatibility shims and deprecation wrappers for the SciTeX ecosystem.</b></p>

<p align="center">
  <a href="https://scitex-compat.readthedocs.io/">Full Documentation</a> · <code>uv pip install scitex-compat[all]</code>
</p>

<!-- scitex-badges:start -->
<p align="center">
  <a href="https://pypi.org/project/scitex-compat/"><img src="https://img.shields.io/pypi/v/scitex-compat.svg" alt="PyPI"></a>
  <a href="https://pypi.org/project/scitex-compat/"><img src="https://img.shields.io/pypi/pyversions/scitex-compat.svg" alt="Python"></a>
  <a href="https://github.com/ywatanabe1989/scitex-compat/actions/workflows/test.yml"><img src="https://github.com/ywatanabe1989/scitex-compat/actions/workflows/test.yml/badge.svg" alt="Tests"></a>
  <a href="https://codecov.io/gh/ywatanabe1989/scitex-compat"><img src="https://codecov.io/gh/ywatanabe1989/scitex-compat/branch/develop/graph/badge.svg" alt="Coverage"></a>
  <a href="https://scitex-compat.readthedocs.io/en/latest/"><img src="https://readthedocs.org/projects/scitex-compat/badge/?version=latest" alt="Docs"></a>
  <a href="https://www.gnu.org/licenses/agpl-3.0"><img src="https://img.shields.io/badge/license-AGPL_v3-blue.svg" alt="License: AGPL v3"></a>
</p>
<!-- scitex-badges:end -->

---

## Problem and Solution

| # | Problem | Solution |
|---|---------|----------|
| 1 | **Renaming a public API silently breaks users** — there's no stdlib way to say "this still works but is deprecated" | **`@deprecated` decorator** — emits `DeprecationWarning` with replacement hint, keeps the old name working one release |
| 2 | **Migrating legacy `notify()` calls** — old scripts reference functions whose home moved | **Compat shims** — `notify`, `notify_async` still callable, forward to the new home, warn once |

## Installation

```bash
pip install scitex-compat
```

## Architecture

```
scitex-compat/
├── src/scitex_compat/
│   ├── __init__.py              # deprecated, notify, notify_async
│   ├── _deprecated.py           # @deprecated decorator (warns once,
│   │                            #   forwards to replacement, removal_version)
│   └── _shims/
│       ├── _notify.py           # legacy notify() -> scitex.notify
│       └── _notify_async.py     # legacy notify_async() -> scitex.notify
└── tests/
```

## Quick Start

```python
from scitex_compat import deprecated

@deprecated("new_function_name", removal_version="3.0")
def old_function():
    pass
```

## 1 Interfaces

<details open>
<summary><strong>Python API</strong></summary>

<br>

```python
from scitex_compat import deprecated, notify, notify_async

@deprecated("new_func", removal_version="2.0")
def old_func(*args, **kwargs):
    ...

# Compat shims (forward to scitex.notify if installed)
notify("hello")
await notify_async("hello")
```

</details>

## Demo

```mermaid
sequenceDiagram
    participant U as user code
    participant O as old_func (deprecated)
    participant N as new_func
    participant W as warnings
    U->>O: old_func(x=1)
    O->>W: DeprecationWarning("use new_func; removal_version=2.0")
    O->>N: new_func(x=1)
    N-->>U: result
    Note over U,N: One release later, old_func is removed.
```

## Part of SciTeX

`scitex-compat` is part of [**SciTeX**](https://scitex.ai). Install via
the umbrella with `pip install scitex[compat]` to use as
`scitex.compat` (Python) or `scitex compat ...` (CLI).

>Four Freedoms for Research
>
>0. The freedom to **run** your research anywhere — your machine, your terms.
>1. The freedom to **study** how every step works — from raw data to final manuscript.
>2. The freedom to **redistribute** your workflows, not just your papers.
>3. The freedom to **modify** any module and share improvements with the community.
>
>AGPL-3.0 — because we believe research infrastructure deserves the same freedoms as the software it runs on.

## License

AGPL-3.0

---

<p align="center">
  <a href="https://scitex.ai" target="_blank"><img src="docs/scitex-icon-navy-inverted.png" alt="SciTeX" width="40"/></a>
</p>
