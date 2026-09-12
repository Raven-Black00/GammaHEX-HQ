#!/usr/bin/env python3
"""GammaHEX-HQ v1.0.0 — RavenBlack.

This repo file is the entry point. The command-center body and assets
(horn, marks, lightning frames) ship in the v1.0.0 source pack because
they are larger than the GitHub text connector can store in one commit.

If _src/part_*.py and assets/ are present next to this file, they are
joined and executed. Otherwise you get a short pointer.
"""
from pathlib import Path
import sys

_HERE = Path(__file__).resolve().parent
_PARTS = sorted((_HERE / "_src").glob("part_*.py"))
_ASSETS = _HERE / "assets"

if _PARTS:
    _code = "".join(p.read_text(encoding="utf-8") for p in _PARTS)
    exec(compile(_code, str(_HERE / "GammaHEX_HQ.py"), "exec"), globals())
else:
    print("GammaHEX-HQ v1.0.0")
    print()
    print("The command-center body is not in this clone yet.")
    print("Drop GammaHEX_HQ.py from the v1.0.0 pack next to assets/ and run:")
    print("    python GammaHEX_HQ.py")
    print()
    print("Repo: https://github.com/Raven-Black00/GammaHEX-HQ")
    sys.exit(2)
