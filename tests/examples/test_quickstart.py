"""Smoke test for examples/quickstart.py.

Per scitex-dev audit-project PS303: every example must have a matching
test under tests/examples/. Validates the example parses cleanly. The
full end-to-end execution is covered by tests/integration/test_examples.py.
"""

import subprocess
import sys
from pathlib import Path

EXAMPLE = Path(__file__).resolve().parents[2] / "examples" / "quickstart.py"


def test_quickstart_example_file_exists_on_disk():
    # Arrange
    expected_path = EXAMPLE

    # Act
    found = expected_path.exists()

    # Assert
    assert found is True, f"missing example: {expected_path}"


def test_quickstart_example_compiles_with_py_compile():
    # Arrange
    cmd = [sys.executable, "-m", "py_compile", str(EXAMPLE)]

    # Act
    completed = subprocess.run(cmd, capture_output=True, text=True)

    # Assert
    assert completed.returncode == 0, completed.stderr
