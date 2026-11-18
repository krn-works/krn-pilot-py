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


NOTE_4 = NOTE.parent / "t-2s70evn.md"


def test_clause_1_proof_note_4() -> None:
    assert NOTE_4.read_text().splitlines() == ["Proof note 4: t-2s70evn"]


def test_clause_2_proof_note_4() -> None:
    assert NOTE_4.read_text() == "Proof note 4: t-2s70evn\n"


def test_clause_3_proof_note_4() -> None:
    assert len(list(NOTE.parent.glob("t-2s70evn*"))) == 1


def test_clause_4_proof_note_4() -> None:
    assert NOTE_4.exists()
    assert "t-2s70evn" in NOTE_4.read_text()


def test_clause_3_proof_note_4_no_duplicate_or_blank_line() -> None:
    lines = NOTE_4.read_text().split("\n")
    assert lines == ["Proof note 4: t-2s70evn", ""]
    assert "" not in NOTE_4.read_text().splitlines()

NOTE_5 = Path(__file__).parent.parent / "docs" / "notes" / "t-03pvpwp.md"


def test_clause_1_proof_note_5() -> None:
    assert NOTE_5.read_text() == "Proof note 5: t-03pvpwp\n"


def test_clause_2_proof_note_5() -> None:
    assert NOTE_5.read_text().splitlines() == ["Proof note 5: t-03pvpwp"]


def test_clause_3_proof_note_5() -> None:
    assert len(list(NOTE_5.parent.glob("t-03pvpwp*"))) == 1


def test_clause_4_proof_note_5() -> None:
    assert NOTE_5.exists()
    assert "t-03pvpwp" in NOTE_5.read_text()


def test_clause_3_proof_note_5_no_duplicate_or_empty_note() -> None:
    # boundary: exactly one note names this task, and none is empty
    matches = list(NOTE_5.parent.glob("t-03pvpwp*"))
    assert matches == [NOTE_5]
    assert NOTE_5.read_text().strip() != ""
