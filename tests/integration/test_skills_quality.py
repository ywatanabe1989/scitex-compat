"""Enforces SciTeX skills quality checklist §1–§4."""

from pathlib import Path

import pytest

# `scitex_dev` lives in [dev] (not [project] dependencies), so guard the
# import per PA-303 — a fresh install without [dev] should skip this
# module rather than abort pytest collection.
pytest.importorskip("scitex_dev")
from scitex_dev._skills_quality_pytest import make_skill_quality_tests  # noqa: E402

test_skills_quality = make_skill_quality_tests(
    package_root=Path(__file__).resolve().parents[2]
)
