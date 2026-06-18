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

## `@deprecated(reason=None, forward_to=None)`

Decorator that wraps a callable and emits a `DeprecationWarning` on each
call of the form `"<func_name> is deprecated: <reason>"`.

| Param        | Purpose                                                                 |
|--------------|-------------------------------------------------------------------------|
| `reason`     | Human-readable explanation of why the function was deprecated           |
| `forward_to` | Optional dotted path to the replacement; when set, calls are forwarded to it via `importlib` and the wrapper docstring is auto-generated |

```python
@deprecated("Use new.api instead")
def old_api(...): ...

@deprecated(reason="Use scitex.session.start instead", forward_to="..session.start")
def start(...): ...
```

When `forward_to` is omitted the wrapped function still runs normally —
this is opt-in deprecation, not a hard removal.

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
