#!/usr/bin/env python3
"""Backward-compatible wrapper for PDF extraction.

Prefer extract_source_notes.py for new work.
"""

from pathlib import Path
import runpy


if __name__ == "__main__":
    runpy.run_path(str(Path(__file__).with_name("extract_source_notes.py")), run_name="__main__")

