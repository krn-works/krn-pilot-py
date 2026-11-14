"""Lists related humanization."""

from __future__ import annotations

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any

__all__ = ["natural_list"]


def natural_list(items: Iterable[Any], *, conjunction: bool = True) -> str:
    """Natural list.

    Convert an iterable of items into a human-readable string with commas and 'and'.

    Examples:
        >>> natural_list(["one", "two", "three"])
        'one, two and three'
        >>> natural_list(["one", "two"])
        'one and two'
        >>> natural_list(["one"])
        'one'
        >>> natural_list([1, 2, 3], conjunction=False)
        '1, 2 or 3'

    Args:
        items (Iterable): An iterable of items.
        conjunction (bool): Join the last item with 'and' if True, 'or' if False.

    Returns:
        str: A string with commas and 'and' in the right places.
    """
    word = "and" if conjunction else "or"
    item_list = [str(item) for item in items]
    if not item_list:
        return ""
    if len(item_list) == 1:
        return item_list[0]
    elif len(item_list) == 2:
        return f"{item_list[0]} {word} {item_list[1]}"
    else:
        return ", ".join(item_list[:-1]) + f" {word} {item_list[-1]}"
