"""Tests for the add function and CLI behavior."""

import pathlib
import sys

import pytest

# Ensure project root is on import path so app module resolves
ROOT = pathlib.Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (0, 0, 0),
        (-5, -7, -12),
        (-3, 3, 0),
        (10, -2, 8),
        (2**30, 2**30, 2**31),
    ],
)
def test_add_various_cases(a: int, b: int, expected: int) -> None:
    from app import add

    assert add(a, b) == expected


def test_cli_success(capsys: pytest.CaptureFixture[str]) -> None:
    from app import run

    exit_code = run(["4", "5"])
    captured = capsys.readouterr()

    assert exit_code == 0
    assert captured.out.strip() == "9"
    assert captured.err == ""


def test_cli_invalid_integer(capsys: pytest.CaptureFixture[str]) -> None:
    from app import run

    exit_code = run(["four", "5"])
    captured = capsys.readouterr()

    assert exit_code == 2
    assert "usage:" in captured.err.lower()
    assert "both arguments must be integers" in captured.err


def test_cli_missing_argument(capsys: pytest.CaptureFixture[str]) -> None:
    from app import run

    with pytest.raises(SystemExit) as exc:
        run(["5"])

    assert exc.value.code == 2
    captured = capsys.readouterr()
    assert "usage:" in captured.err.lower()


def test_cli_version_flag(capsys: pytest.CaptureFixture[str]) -> None:
    from app import run

    with pytest.raises(SystemExit) as exc:
        run(["--version"])

    assert exc.value.code == 0
    captured = capsys.readouterr()
    assert "add-cli" in captured.out
