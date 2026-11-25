"""Verify the development version and upstream provenance without claiming a release."""

import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent


def test_manifest_version_is_valid() -> None:
    manifest = json.loads(
        (ROOT / "custom_components/ikea_bilresa/manifest.json").read_text(
            encoding="utf-8"
        )
    )
    assert re.fullmatch(r"\d+\.\d+\.\d+(?:-rc\.\d+)?", manifest["version"])
    assert manifest["domain"] == "ikea_bilresa"


def test_current_user_guides_match_manifest_version() -> None:
    manifest = json.loads(
        (ROOT / "custom_components/ikea_bilresa/manifest.json").read_text(
            encoding="utf-8"
        )
    )
    version = manifest["version"]
    for name in (
        "README.md",
        "README.nl.md",
        "docs/QUICK-START.md",
        "docs/INSTALLATION.md",
        "docs/USER-GUIDE.md",
        "docs/nl/QUICK-START.md",
        "docs/nl/INSTALLATION.md",
        "docs/nl/USER-GUIDE.md",
        "docs/RELEASE-0.2.1.md",
        "docs/nl/RELEASE-0.2.1.md",
    ):
        assert version in (ROOT / name).read_text(encoding="utf-8"), name


def test_development_status_records_upstream_source() -> None:
    notice = (ROOT / "THIRD_PARTY_NOTICES.md").read_text(encoding="utf-8")
    status = (ROOT / "PROJECT_STATUS.md").read_text(encoding="utf-8")
    assert "67639e18d6d8595e87a31993802ae76745915a97" in notice
    assert "67639e18d6d8595e87a31993802ae76745915a97" in status
    assert "Vituhlos" in (ROOT / "LICENSE").read_text(encoding="utf-8")
