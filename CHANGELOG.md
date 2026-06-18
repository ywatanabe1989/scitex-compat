# Changelog

All notable changes to `scitex-compat` are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/);
versions follow [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [0.1.9]

- fix(deprecated): release the canonical `@deprecated(reason=None, forward_to=None)` signature to PyPI. The SSOT refactor (ADR-0001, 2026-05-29) replaced the old `deprecated(new_name, removal_version="2.0")` form on `main` but was never published, so PyPI still served the pre-SSOT v0.1.8 with a **required** `new_name` argument. That broke every consumer that uses the canonical signature — notably `scitex-decorators` (thin re-export) and `scitex-gen/_legacy/_deprecated_*.py` — with `TypeError: deprecated() missing 1 required positional argument: 'new_name'`. No source change to `_compat.py` was needed; this is purely the release that ships the already-fixed source.
- docs(skills): correct the `@deprecated` signature in the bundled `_skills` API/quick-start docs (`reason` / `forward_to`) — they still described the removed `new_name` / `removal_version` form.

## [0.1.5]

- Initial CHANGELOG entry — see git log for prior history.
