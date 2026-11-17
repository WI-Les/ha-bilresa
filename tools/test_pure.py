"""Run the protocol-only tests without loading Home Assistant's integration."""

from pathlib import Path
import sys
from types import ModuleType

import pytest

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root))
package = ModuleType("custom_components.ikea_bilresa")
package.__path__ = [str(root / "custom_components" / "ikea_bilresa")]
sys.modules[package.__name__] = package

raise SystemExit(
    pytest.main(
        ["-q", "-p", "no:cacheprovider", "-o", "asyncio_mode=auto",
         "tests/test_engine.py", "tests/test_model.py"]
    )
)
