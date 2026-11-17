"""Verify the development version and upstream provenance without claiming a release."""

import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent


def test_manifest_version_is_valid() -> None:
    manifest = json.loads((ROOT / "custom_components/ikea_bilresa/manifest.json").read_text(encoding="utf-8"))
    assert re.fullmatch(r"\d+\.\d+\.\d+(?:-rc\.\d+)?", manifest["version"])
    assert manifest["domain"] == "ikea_bilresa"


def test_development_status_records_upstream_source() -> None:
    notice = (ROOT / "THIRD_PARTY_NOTICES.md").read_text(encoding="utf-8")
    status = (ROOT / "PROJECT_STATUS.md").read_text(encoding="utf-8")
    assert "67639e18d6d8595e87a31993802ae76745915a97" in notice
    assert "67639e18d6d8595e87a31993802ae76745915a97" in status
    assert "Vituhlos" in (ROOT / "LICENSE").read_text(encoding="utf-8")
