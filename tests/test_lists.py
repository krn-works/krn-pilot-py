from __future__ import annotations

from collections.abc import Iterable
from typing import Any

import pytest

import humanize


@pytest.mark.parametrize(
    "test_args, expected",
    [
        ([["1", "2", "3"]], "1, 2 and 3"),
        ([["one", "two", "three"]], "one, two and three"),
        ([["one", "two"]], "one and two"),
        ([["one"]], "one"),
        ([[]], ""),
        ([[""]], ""),
        ([[1, 2, 3]], "1, 2 and 3"),
        ([[1, "two"]], "1 and two"),
        ([("one", "two", "three")], "one, two and three"),
        ([("one", "two")], "one and two"),
        ([("one",)], "one"),
        ([{"one": 1, "two": 2}.keys()], "one and two"),
        ([(x for x in ["one", "two", "three"])], "one, two and three"),
        ([range(1, 4)], "1, 2 and 3"),
    ],
)
def test_natural_list(test_args: Iterable[Any], expected: str) -> None:
    assert humanize.natural_list(*test_args) == expected


@pytest.mark.parametrize(
    "items, conjunction, expected",
    [
        ([1, 2, 3], False, "1, 2 or 3"),
        (["one", "two"], False, "one or two"),
        (["one"], False, "one"),
        ([], False, ""),
        ([1, 2, 3], True, "1, 2 and 3"),
        (["one", "two"], True, "one and two"),
        (iter(["a", "b", "c"]), True, "a, b and c"),
        (iter(["a", "b", "c"]), False, "a, b or c"),
    ],
)
def test_natural_list_conjunction(
    items: Iterable[Any], conjunction: bool, expected: str
) -> None:
    assert humanize.natural_list(items, conjunction=conjunction) == expected


def test_natural_list_default_is_and() -> None:
    assert humanize.natural_list([1, 2, 3]) == "1, 2 and 3"
    assert humanize.natural_list(["one", "two"]) == "one and two"
