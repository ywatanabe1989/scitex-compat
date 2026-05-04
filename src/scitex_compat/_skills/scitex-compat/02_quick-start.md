---
description: |
  [TOPIC] scitex-compat Quick start
  [DETAILS] Mark a function as @deprecated; legacy notify/notify_async forwarders to scitex-notification.
tags: [scitex-compat-quick-start]
---

# Quick Start

## Mark a function as deprecated

```python
from scitex_compat import deprecated

@deprecated(
    reason="renamed for clarity",
    version="2.0.0",
    replacement="new_compute",
)
def compute(x):
    return new_compute(x)
```

A `DeprecationWarning` is emitted on each call, including the version
removed-in and the suggested replacement.

## Legacy notify forwarders

```python
from scitex_compat import notify, notify_async

notify("hello")                # warns + forwards to scitex-notification
await notify_async("hello")    # async variant
```

These exist so old `from scitex.gen import notify` user code keeps
working while the ecosystem migrates to `scitex-notification`.

## Next

- [03_python-api.md](03_python-api.md) — full signatures
- [SKILL.md](SKILL.md) — overview + deprecation policy
