# scitex-compat

<!-- scitex-badges:start -->
[![PyPI](https://img.shields.io/pypi/v/scitex-compat.svg)](https://pypi.org/project/scitex-compat/)
[![Python](https://img.shields.io/pypi/pyversions/scitex-compat.svg)](https://pypi.org/project/scitex-compat/)
[![Tests](https://github.com/ywatanabe1989/scitex-compat/actions/workflows/test.yml/badge.svg)](https://github.com/ywatanabe1989/scitex-compat/actions/workflows/test.yml)
[![Install Test](https://github.com/ywatanabe1989/scitex-compat/actions/workflows/install-test.yml/badge.svg)](https://github.com/ywatanabe1989/scitex-compat/actions/workflows/install-test.yml)
[![Coverage](https://codecov.io/gh/ywatanabe1989/scitex-compat/graph/badge.svg)](https://codecov.io/gh/ywatanabe1989/scitex-compat)
[![Docs](https://readthedocs.org/projects/scitex-compat/badge/?version=latest)](https://scitex-compat.readthedocs.io/en/latest/)
[![License: AGPL v3](https://img.shields.io/badge/license-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
<!-- scitex-badges:end -->

<p align="center">
  <a href="https://scitex.ai">
    <img src="docs/scitex-logo-blue-cropped.png" alt="SciTeX" width="400">
  </a>
</p>

<p align="center"><b>Backward compatibility shims and deprecation wrappers for the SciTeX ecosystem.</b></p>

<p align="center">
  <a href="https://scitex-compat.readthedocs.io/">Full Documentation</a> · <code>pip install scitex-compat</code>
</p>

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

## Quick Start

```python
from scitex_compat import deprecated

@deprecated("new_function_name", removal_version="3.0")
def old_function():
    pass
```

## 1 Interfaces

<details>
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

## Part of SciTeX

`scitex-compat` is part of [**SciTeX**](https://scitex.ai).

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
