---
description: |
  [TOPIC] scitex-compat Python API
  [DETAILS] Three public symbols — @deprecated decorator and notify / notify_async legacy forwarders.
tags: [scitex-compat-python-api]
---

# Python API

## Imports

```python
from scitex_compat import deprecated, notify, notify_async
```

## `@deprecated(new_name, removal_version="2.0")`

Decorator that wraps a callable and emits a `DeprecationWarning` on each
call.

| Param             | Purpose                                              |
|-------------------|------------------------------------------------------|
| `new_name`        | Name of the replacement function or API               |
| `removal_version` | Version in which the deprecated function will be removed |

```python
@deprecated("new.api", removal_version="2.0")
def old_api(...): ...
```

The wrapped function still runs normally — this is opt-in deprecation,
not a hard removal.

## `notify(*args, **kwargs)`

Legacy forwarder to `scitex_notification.notify` (or equivalent).
Emits a `DeprecationWarning` directing the caller to migrate.

## `notify_async(*args, **kwargs)`

Async variant of the same forwarder. Behaves like `notify` but returns
a coroutine.

## Two import paths

```python
import scitex_compat        # standalone
import scitex.compat        # umbrella (requires `pip install scitex`)
```

## Policy

This package is a stable home for shims only. New deprecated aliases
should be added here; once the deprecation window expires they are
removed in a major release.
