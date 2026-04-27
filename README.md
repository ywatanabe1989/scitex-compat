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


Backward compatibility shims and deprecation wrappers for the SciTeX ecosystem.

## Problem and Solution


| # | Problem | Solution |
|---|---------|----------|
| 1 | **Renaming a public API silently breaks users** -- there's no stdlib way to say "this still works but is deprecated" | **`@deprecated` decorator** -- emits `DeprecationWarning` with replacement hint, keeps the old name working one release |
| 2 | **Migration legacy `notify()` calls** -- old scripts reference functions whose home moved | **Compat shims** -- `notify`, `notify_async` still callable, forward to the new home, warn once |

## Installation

```bash
pip install scitex-compat
```

## Usage

```python
from scitex_compat import deprecated

@deprecated("new_function_name", removal_version="3.0")
def old_function():
    pass
```

## License

AGPL-3.0
