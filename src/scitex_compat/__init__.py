#!/usr/bin/env python3
# File: src/scitex_compat/__init__.py

"""SciTeX Backward Compatibility Module.

This module provides aliases and wrappers for deprecated APIs.
Import from here to use old function names that delegate to new implementations.

Deprecation Timeline:
- v1.x: Old APIs work with deprecation warnings
- v2.x: Old APIs removed, use new APIs directly
"""

from __future__ import annotations

import warnings
from functools import wraps
from typing import Callable


def deprecated(new_name: str, removal_version: str = "2.0"):
    """Decorator to mark functions as deprecated."""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            warnings.warn(
                f"{func.__name__} is deprecated. "
                f"Use {new_name} instead. "
                f"Will be removed in v{removal_version}.",
                DeprecationWarning,
                stacklevel=2,
            )
            return func(*args, **kwargs)

        return wrapper

    return decorator


# UI/Notification compatibility
def notify(*args, **kwargs):
    """Deprecated: Use scitex.notify.alert() instead.

    In standalone mode, this only emits a deprecation warning.
    The actual notification requires scitex.notify to be installed.
    """
    warnings.warn(
        "scitex.compat.notify is deprecated. Use scitex.notify.alert instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    try:
        from scitex.notify import alert
        return alert(*args, **kwargs)
    except ImportError:
        warnings.warn(
            "scitex.notify is not installed. Notification not sent.",
            RuntimeWarning,
            stacklevel=2,
        )
        return None


async def notify_async(*args, **kwargs):
    """Deprecated: Use scitex.notify.alert_async() instead.

    In standalone mode, this only emits a deprecation warning.
    The actual notification requires scitex.notify to be installed.
    """
    warnings.warn(
        "scitex.compat.notify_async is deprecated. Use scitex.notify.alert_async instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    try:
        from scitex.notify import alert_async
        return await alert_async(*args, **kwargs)
    except ImportError:
        warnings.warn(
            "scitex.notify is not installed. Notification not sent.",
            RuntimeWarning,
            stacklevel=2,
        )
        return None


__all__ = [
    "deprecated",
    "notify",
    "notify_async",
]

# EOF
