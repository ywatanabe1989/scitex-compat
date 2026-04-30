"""scitex-compat quickstart: deprecation decorator + notify helpers."""

import warnings

import scitex_compat


@scitex_compat.deprecated(new_name="new_api", removal_version="0.2.0")
def old_api(x):
    return x * 2


def main():
    # 1. The decorated callable still works...
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        result = old_api(3)
        assert result == 6
        # ...but emits a DeprecationWarning.
        assert any(issubclass(w.category, DeprecationWarning) for w in caught), [
            str(w.message) for w in caught
        ]
        print("old_api(3) ->", result, "[+ deprecation warning]")

    # 2. notify is callable (no-op when no backends are configured).
    try:
        scitex_compat.notify("hello from scitex-compat")
        print("notify call returned without error")
    except Exception as exc:
        print("notify raised (acceptable in CI):", type(exc).__name__, exc)


if __name__ == "__main__":
    main()
