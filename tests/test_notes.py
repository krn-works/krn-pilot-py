from __future__ import annotations

from pathlib import Path

NOTE = Path(__file__).parent.parent / "docs" / "notes" / "t-0zf6ehp.md"


def test_clause_1() -> None:
    assert NOTE.read_text() == "Proof note 10: t-0zf6ehp\n"


def test_clause_2() -> None:
    assert NOTE.read_text().splitlines() == ["Proof note 10: t-0zf6ehp"]


def test_clause_3() -> None:
    assert len(list(NOTE.parent.glob("t-0zf6ehp*"))) == 1


def test_clause_4() -> None:
    assert NOTE.exists()
    assert "t-0zf6ehp" in NOTE.read_text()
