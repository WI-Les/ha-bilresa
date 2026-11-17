"""The developer tools must not report a red gate as green."""

from __future__ import annotations

import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parents[1] / "tools"))

import check  # noqa: E402

LEGACY = (
    "custom_components/ikea_bilresa/legacy_triggers.py:68: error: Generator has "
    'incompatible item type "str | UndefinedType"; expected "str"  [misc]'
)
LINK = (
    "custom_components/ikea_bilresa/device_link.py:256: error: Argument 1 to "
    '"MatterDeviceLink" has incompatible type "X"; expected "Y"  [arg-type]'
)
NEW = "custom_components/ikea_bilresa/binding.py:10: error: Something new  [misc]"


def test_mypy_is_green_only_for_the_known_errors() -> None:
    known = f"{LEGACY}\n{LINK}\nFound 2 errors in 2 files"
    assert check._summary("mypy", known, 1)[0]
    assert check._summary("mypy", "Success: no issues found", 0)[0]
    # One fewer is fine; a new error is not, even when the count stays the same.
    assert check._summary("mypy", f"{LEGACY}\nFound 1 error", 1)[0]
    swapped = f"{LEGACY}\n{NEW}\nFound 2 errors in 2 files"
    assert check._summary("mypy", swapped, 1)[0] is False
    # mypy that crashed prints its summary and exits 2.
    assert check._summary("mypy", f"{LEGACY}\nFound 1 error", 2)[0] is False


def test_a_failing_gate_is_never_green() -> None:
    assert check._summary("pytest", "1 failed, 5 passed", 1)[0] is False
    assert check._summary("pytest", "6 passed in 1s", 0) == (True, "6 passed in 1s")
    assert check._summary("node", "ℹ pass 3\nℹ fail 1", 1)[0] is False


def test_a_missing_program_is_a_red_gate_not_a_traceback() -> None:
    name, ok, summary, _output, _seconds = check._run(
        ("tool", ["this-program-does-not-exist-anywhere"])
    )

    assert (name, ok) == ("tool", False)
    assert "cannot run" in summary


def test_every_documented_gate_runs() -> None:
    names = [name for name, _command in check._gates(fast=False)]

    for expected in ("json", "compile", "syntax", "diff", "format", "lint", "mypy"):
        assert expected in names
    assert "pytest" in names
    assert "pytest" not in [n for n, _c in check._gates(fast=True)]
