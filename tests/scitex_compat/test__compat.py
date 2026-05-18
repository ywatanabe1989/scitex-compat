#!/usr/bin/env python3
"""Tests for scitex_compat top-level surface (deprecated, notify, notify_async).

Uses the `_swap_*` save/restore pattern (PA-306 §3 no-mocks) — no
monkeypatch, no unittest.mock. Each test follows the AAA marker
convention and exercises one observable behaviour.
"""

import asyncio
import builtins
import warnings
from contextlib import contextmanager
from typing import Callable, Iterator

import pytest

import scitex_compat
from scitex_compat import deprecated, notify, notify_async

# ---------------------------------------------------------------------------
# _swap_* helpers — restore the original on exit even if the test raises.
# ---------------------------------------------------------------------------


@contextmanager
def _swap_builtins_import(fake: Callable) -> Iterator[None]:
    """Replace ``builtins.__import__`` with ``fake`` for the test body."""
    saved = builtins.__import__
    builtins.__import__ = fake  # type: ignore[assignment]
    try:
        yield
    finally:
        builtins.__import__ = saved  # type: ignore[assignment]


def _make_import_blocker(blocked_module: str) -> Callable:
    """Return a fake ``__import__`` that raises ImportError for ``blocked_module``."""
    real_import = builtins.__import__

    def fake_import(name, *a, **kw):
        if name == blocked_module:
            raise ImportError(f"forced for test (blocked={blocked_module})")
        return real_import(name, *a, **kw)

    return fake_import


# ---------------------------------------------------------------------------
# deprecated decorator
# ---------------------------------------------------------------------------


class TestDeprecatedDecorator:
    def test_decorated_function_returns_original_value(self):
        # Arrange
        @deprecated("new_thing")
        def old_thing():
            return 42

        # Act
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            result = old_thing()

        # Assert
        assert result == 42

    def test_decorated_call_emits_deprecation_warning(self):
        # Arrange
        @deprecated("new_thing")
        def old_thing():
            return 42

        # Act
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            old_thing()

        # Assert
        assert any(issubclass(w.category, DeprecationWarning) for w in caught)

    def test_warning_message_names_the_old_function(self):
        # Arrange
        @deprecated("new_thing")
        def old_thing():
            return 42

        # Act
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            old_thing()

        # Assert
        assert "old_thing" in str(caught[0].message)

    def test_warning_message_names_the_replacement(self):
        # Arrange
        @deprecated("new_thing")
        def old_thing():
            return 42

        # Act
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            old_thing()

        # Assert
        assert "new_thing" in str(caught[0].message)

    def test_warning_includes_explicit_removal_version(self):
        # Arrange
        @deprecated("replacement", removal_version="3.5")
        def doomed():
            return None

        # Act
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            doomed()

        # Assert
        assert any("3.5" in str(w.message) for w in caught)

    def test_default_removal_version_is_2_0(self):
        # Arrange
        @deprecated("replacement")
        def doomed():
            return None

        # Act
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            doomed()

        # Assert
        assert any("2.0" in str(w.message) for w in caught)

    def test_decorator_preserves_return_value(self):
        # Arrange
        @deprecated("new_add")
        def add(a, b):
            """Add two numbers."""
            return a + b

        # Act
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            result = add(2, 3)

        # Assert
        assert result == 5

    def test_decorator_preserves_function_name(self):
        # Arrange
        @deprecated("new_add")
        def add(a, b):
            """Add two numbers."""
            return a + b

        # Act
        observed_name = add.__name__

        # Assert
        assert observed_name == "add"

    def test_decorator_preserves_docstring(self):
        # Arrange
        @deprecated("new_add")
        def add(a, b):
            """Add two numbers."""
            return a + b

        # Act
        observed_doc = add.__doc__

        # Assert
        assert observed_doc == "Add two numbers."


# ---------------------------------------------------------------------------
# notify (sync)
# ---------------------------------------------------------------------------


class TestNotify:
    def test_returns_none_when_scitex_notify_missing(self):
        # Arrange
        fake = _make_import_blocker("scitex.notify")

        # Act
        with _swap_builtins_import(fake):
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                result = notify("hello")

        # Assert
        assert result is None

    def test_emits_deprecation_warning_when_scitex_notify_missing(self):
        # Arrange
        fake = _make_import_blocker("scitex.notify")

        # Act
        with _swap_builtins_import(fake):
            with warnings.catch_warnings(record=True) as caught:
                warnings.simplefilter("always")
                notify("hello")

        # Assert
        assert DeprecationWarning in {w.category for w in caught}

    def test_emits_runtime_warning_when_scitex_notify_missing(self):
        # Arrange
        fake = _make_import_blocker("scitex.notify")

        # Act
        with _swap_builtins_import(fake):
            with warnings.catch_warnings(record=True) as caught:
                warnings.simplefilter("always")
                notify("hello")

        # Assert
        assert RuntimeWarning in {w.category for w in caught}


# ---------------------------------------------------------------------------
# notify_async (async)
# ---------------------------------------------------------------------------


class TestNotifyAsync:
    def test_async_returns_none_when_scitex_notify_missing(self):
        # Arrange
        fake = _make_import_blocker("scitex.notify")

        # Act
        with _swap_builtins_import(fake):
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                result = asyncio.run(notify_async("hello"))

        # Assert
        assert result is None

    def test_async_emits_deprecation_warning_when_scitex_notify_missing(self):
        # Arrange
        fake = _make_import_blocker("scitex.notify")

        # Act
        with _swap_builtins_import(fake):
            with warnings.catch_warnings(record=True) as caught:
                warnings.simplefilter("always")
                asyncio.run(notify_async("hello"))

        # Assert
        assert DeprecationWarning in {w.category for w in caught}

    def test_async_emits_runtime_warning_when_scitex_notify_missing(self):
        # Arrange
        fake = _make_import_blocker("scitex.notify")

        # Act
        with _swap_builtins_import(fake):
            with warnings.catch_warnings(record=True) as caught:
                warnings.simplefilter("always")
                asyncio.run(notify_async("hello"))

        # Assert
        assert RuntimeWarning in {w.category for w in caught}


# ---------------------------------------------------------------------------
# package version surface
# ---------------------------------------------------------------------------


class TestVersion:
    def test_version_attribute_is_a_string(self):
        # Arrange
        version = scitex_compat.__version__

        # Act
        observed_type = type(version)

        # Assert
        assert observed_type is str

    def test_version_attribute_is_non_empty(self):
        # Arrange
        version = scitex_compat.__version__

        # Act
        observed_truthy = bool(version)

        # Assert
        assert observed_truthy is True

    def test_version_is_listed_in_dunder_all(self):
        # Arrange
        exported = scitex_compat.__all__

        # Act
        contains_version = "__version__" in exported

        # Assert
        assert contains_version is True


if __name__ == "__main__":
    import os

    pytest.main([os.path.abspath(__file__), "-v"])

# EOF
