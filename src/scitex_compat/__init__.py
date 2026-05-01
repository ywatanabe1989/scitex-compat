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

try:
    from importlib.metadata import PackageNotFoundError
    from importlib.metadata import version as _v

    try:
        __version__ = _v("scitex-compat")
    except PackageNotFoundError:
        __version__ = "0.0.0+local"
    del _v, PackageNotFoundError
except ImportError:  # pragma: no cover — only on ancient Pythons
    __version__ = "0.0.0+local"

from ._compat import deprecated, notify, notify_async

__all__ = [
    "__version__",
    "deprecated",
    "notify",
    "notify_async",
]

# EOF
