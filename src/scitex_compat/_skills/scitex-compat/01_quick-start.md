<!-- 01_quick-start.md -->

# scitex-compat — Quick Start

## Install

```bash
pip install scitex-compat
```

## Import

```python
import scitex_compat
```

## Mark a function deprecated

```python
from scitex_compat import deprecated

@deprecated(new_name="my_module.new_func", removal_version="2.0")
def old_func(x):
    return x + 1

old_func(1)  # emits DeprecationWarning, still returns 2
```

## Use the legacy notify shim

```python
from scitex_compat import notify, notify_async

# Prefer scitex.notify.alert / alert_async in new code.
notify("job done")              # DeprecationWarning; delegates to scitex.notify.alert
await notify_async("job done")  # DeprecationWarning; delegates to scitex.notify.alert_async
```

If `scitex.notify` is not installed, a `RuntimeWarning` is emitted and
`None` is returned — nothing is sent.

That is the entire public surface. For anything else, use the current
non-deprecated APIs directly.
