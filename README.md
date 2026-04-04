# scitex-compat

Backward compatibility shims and deprecation wrappers for the SciTeX ecosystem.

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
