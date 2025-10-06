"""Minimal CLI application exposing add()."""

from __future__ import annotations

import argparse
import sys
from typing import Sequence

VERSION = "add-cli 1.0.0"


def add(a: int, b: int) -> int:
    """Compute the sum of two integers.

    Args:
        a: The first integer operand.
        b: The second integer operand.

    Returns:
        The sum of ``a`` and ``b``.
    """
    return a + b


def build_parser() -> argparse.ArgumentParser:
    """Construct the argument parser for the CLI."""
    parser = argparse.ArgumentParser(description="Add two integers.")
    parser.add_argument("a", help="First integer")
    parser.add_argument("b", help="Second integer")
    parser.add_argument("--version", action="version", version=VERSION)
    return parser


def run(argv: Sequence[str] | None = None) -> int:
    """Run the CLI with the provided arguments.

    Args:
        argv: Optional sequence of argument strings. When ``None`` the values are read
            from ``sys.argv``.

    Returns:
        Process exit code. ``0`` indicates success; ``2`` indicates invalid input.
    """
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        first = int(args.a)
        second = int(args.b)
    except ValueError:
        parser.print_usage(sys.stderr)
        print(f"{parser.prog}: error: both arguments must be integers.", file=sys.stderr)
        return 2

    result = add(first, second)
    print(result)
    return 0


def main() -> None:
    """CLI entry point that exits with the status from :func:`run`."""
    sys.exit(run())


if __name__ == "__main__":
    main()
