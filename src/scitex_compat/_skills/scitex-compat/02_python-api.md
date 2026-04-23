<!-- 02_python-api.md -->

# scitex-compat — Python API

All public symbols are in `scitex_compat.__all__`:

| Symbol | Kind | One-liner |
|--------|------|-----------|
| `deprecated` | decorator factory | Mark a function deprecated; warns on call. |
| `notify` | function | Deprecated alias for `scitex.notify.alert`. |
| `notify_async` | coroutine function | Deprecated alias for `scitex.notify.alert_async`. |

## Signatures

```python
deprecated(new_name: str, removal_version: str = "2.0") -> Callable[[Callable], Callable]
notify(*args, **kwargs) -> Any
async notify_async(*args, **kwargs) -> Any
```

`notify` / `notify_async` try to import `scitex.notify` lazily; if the
dependency is missing they emit a `RuntimeWarning` and return `None` rather
than raising, so scripts that import them always succeed.
