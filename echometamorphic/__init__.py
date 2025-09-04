"""Utilities for analyzing recursive complexity in Python code.

This package exposes tools for detecting excessively nested function
definitions.  It is primarily intended for use in pre-commit hooks to keep
codebases from growing unmaintainably complex.
"""

from .recursive_complexity_check import check_file, main

__all__ = ["check_file", "main"]
