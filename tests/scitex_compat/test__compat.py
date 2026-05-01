#!/usr/bin/env python3
"""Tests for scitex_compat top-level surface (deprecated, notify, notify_async)."""

import asyncio
import warnings

import pytest

import scitex_compat
from scitex_compat import deprecated, notify, notify_async


class TestDeprecatedDecorator:
    def test_emits_deprecation_warning_with_new_name(self):
        @deprecated("new_thing")
        def old_thing():
            return 42

        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            result = old_thing()

        assert result == 42
        assert any(issubclass(w.category, DeprecationWarning) for w in caught)
        msg = str(caught[0].message)
        assert "old_thing" in msg
        assert "new_thing" in msg

    def test_warning_includes_removal_version(self):
        @deprecated("replacement", removal_version="3.5")
        def doomed():
            return None

        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            doomed()

        assert any("3.5" in str(w.message) for w in caught)

    def test_default_removal_version_is_2_0(self):
        @deprecated("replacement")
        def doomed():
            return None

        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            doomed()

        assert any("2.0" in str(w.message) for w in caught)

    def test_preserves_return_value_and_metadata(self):
        @deprecated("new_add")
        def add(a, b):
            """Add two numbers."""
            return a + b

        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            assert add(2, 3) == 5
        assert add.__name__ == "add"
        assert add.__doc__ == "Add two numbers."


class TestNotify:
    def test_warns_and_returns_none_when_scitex_notify_missing(self, monkeypatch):
        # Force the optional import to fail.
        import builtins

        real_import = builtins.__import__

        def fake_import(name, *a, **kw):
            if name == "scitex.notify":
                raise ImportError("forced for test")
            return real_import(name, *a, **kw)

        monkeypatch.setattr(builtins, "__import__", fake_import)
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            result = notify("hello")

        assert result is None
        # Two warnings: DeprecationWarning + RuntimeWarning (notify not installed)
        categories = {w.category for w in caught}
        assert DeprecationWarning in categories
        assert RuntimeWarning in categories


class TestNotifyAsync:
    def test_async_warns_and_returns_none_when_scitex_notify_missing(self, monkeypatch):
        import builtins

        real_import = builtins.__import__

        def fake_import(name, *a, **kw):
            if name == "scitex.notify":
                raise ImportError("forced for test")
            return real_import(name, *a, **kw)

        monkeypatch.setattr(builtins, "__import__", fake_import)
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            result = asyncio.run(notify_async("hello"))

        assert result is None
        categories = {w.category for w in caught}
        assert DeprecationWarning in categories
        assert RuntimeWarning in categories


class TestVersion:
    def test_has_string_version(self):
        assert isinstance(scitex_compat.__version__, str)
        assert scitex_compat.__version__  # non-empty

    def test_version_in_all(self):
        assert "__version__" in scitex_compat.__all__


if __name__ == "__main__":
    import os

    pytest.main([os.path.abspath(__file__), "-v"])

# EOF
