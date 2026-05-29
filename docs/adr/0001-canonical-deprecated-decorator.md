# ADR-0001: Host the canonical `@deprecated` decorator in scitex-compat

## Status
Accepted (2026-05-29)

## Context
`@deprecated` is needed across the SciTeX ecosystem — any package that
renames a public symbol wants to keep the old name callable while
emitting `DeprecationWarning`, and frequently wants to *forward* the
call to the replacement so old code-paths keep working.

At the time of this decision, two independent implementations existed
side-by-side:

| Package | File | Signature | Features | Runtime deps |
| --- | --- | --- | --- | --- |
| scitex-compat | `_compat.py` (~12 LoC) | `deprecated(new_name, removal_version="2.0")` | warn only | none |
| scitex-decorators | `_deprecated.py` (~200 LoC) | `deprecated(reason=None, forward_to=None)` | warn + call-forwarding via `importlib`, auto-generated docstrings | numpy, tqdm, scitex-config, scitex-dev |

Live-caller scan (2026-05-29, excluding `_sphinx_html`, `_skills`,
tests, worktrees, `.claude`): only `scitex-gen/_legacy/_deprecated_*.py`
actually invokes `@deprecated(...)` in production source, and it uses
the **rich** forwarding signature (`reason=`, `forward_to=`). The
simpler compat signature has effectively zero current callers.

Two further constraints framed the choice:

1. **Layer 0 leaves can't pull numpy.** Any leaf package
   (scitex-types, scitex-path, scitex-str, scitex-logging,
   scitex-config, scitex-dev) that wants to mark an API deprecated must
   be able to import the decorator without dragging numpy / tqdm into
   its install. scitex-decorators currently does.
2. **scitex-decorators sits above scitex-config and scitex-dev in the
   dependency graph.** If scitex-config or scitex-dev tried to import
   `@deprecated` from scitex-decorators they'd create a cycle.

See `GITIGNORED/SOC.md` in `scitex-python` for the full layered
dependency rules (R5/R6, layer 0–5 diagram).

## Decision
**Canonical home: scitex-compat.** scitex-compat hosts the rich
`deprecated(reason=None, forward_to=None)` implementation.
scitex-decorators becomes a thin re-export.

**Placement principles**

1. **Decorators that need to be importable by Layer 0 leaves must
   themselves be Layer 0.** scitex-compat is pure stdlib (no runtime
   deps); the rich impl uses only `functools`, `importlib`, `warnings`.
   Nothing about forwarding required numpy. Promoting scitex-compat to
   canonical adds zero install cost.
2. **One implementation, one place.** Two copies of the same symbol
   silently drift. The richer signature subsumes the simpler one
   (`@deprecated(reason="use bar instead")` is equivalent to the old
   `@deprecated("bar")` modulo warning wording, which is acceptable).
3. **Public surface is preserved for both packages.**
   `from scitex_compat import deprecated` is the new canonical path;
   `from scitex_decorators import deprecated` continues to work
   indefinitely via re-export so existing callers don't break.
4. **No cycles.** scitex-decorators already depends on Layer 0
   (scitex-config, scitex-dev); adding scitex-compat to its deps is
   one more leaf, not a back-edge.

**Implementation summary (shipped together with this ADR)**

| Change | File | Effect |
| --- | --- | --- |
| Move rich impl in | `scitex-compat/src/scitex_compat/_compat.py` | becomes ~150 LoC; old simple sig removed |
| Update example | `scitex-compat/examples/quickstart.py` | uses `reason=` instead of `new_name=`, `removal_version=` |
| Update tests | `scitex-compat/tests/scitex_compat/test__compat.py` | drop two `removal_version`-specific tests; add two `forward_to=` tests with AAA structure |
| Thin re-export | `scitex-decorators/src/scitex_decorators/_deprecated.py` | now ~20 LoC: `from scitex_compat import deprecated` |
| Add dep | `scitex-decorators/pyproject.toml` | add `"scitex-compat>=0.1.0"` to `[project] dependencies` |

Verification: `pytest tests/ --ignore=tests/develop -q` in scitex-compat
shows 23 passed, 1 skipped (the cross-package smoke that needs
`scitex.notify`).

## Consequences
- Future Layer 0 packages can import `@deprecated` without pulling
  numpy / tqdm. The decorator is no longer a hidden taxation on the
  base install.
- A breaking signature change for any external caller still using the
  old `deprecated(new_name=, removal_version=)` form. Audit found zero
  such callers in the ecosystem; the risk is contained.
- A small runtime cost: scitex-decorators install now also installs
  scitex-compat. Both packages are deps-free at the stdlib layer, so
  total install delta is negligible.
- Long-term: prefer `from scitex_compat import deprecated` in new code;
  the scitex-decorators re-export remains as a backward-compat path
  for existing callers. It can stay indefinitely — re-export is
  essentially free.
- Removes a silent drift surface (two impls of the same name) which
  had already started to diverge — the warning wording differed
  between the two, and only one supported forwarding.

## Notes
Surfaced 2026-05-29 during the broader SoC audit that produced R5/R6
in `scitex-python/GITIGNORED/SOC.md`. The audit asked whether
scitex-compat was still justified as a standalone or whether its
contents could fold into scitex-decorators. The answer was the
opposite of the question — scitex-compat is the *better* home for
`@deprecated` precisely because it's zero-dep. This ADR records the
flip.

Related:
- `scitex-decorators/docs/adr/0001-thin-reexport-of-deprecated.md`
  (the mirror ADR documenting the re-export contract on the
  decorators side).
- `scitex-python/GITIGNORED/SOC.md` § "SSOT for `@deprecated`".
