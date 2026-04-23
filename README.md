# scitex-compat

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
