"""Project Euler - Problem 31 Prototype."""

# Programmed by CoolCat467

from __future__ import annotations

# Project Euler - Problem 31 Prototype
# Copyright (C) 2025  CoolCat467
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https:#www.gnu.org/licenses/>.

__title__ = "Project Euler - Problem 31 Prototype"
__author__ = "CoolCat467"
__license__ = "GNU General Public License Version 3"


from typing import TYPE_CHECKING, Final

if TYPE_CHECKING:
    from collections.abc import Iterable, Sequence


COINS: Final = (1, 2, 5, 10, 20, 50, 100, 200)
MAX: Final = tuple(200 // x for x in COINS)


def get_total(scalars: Iterable[int], values: Iterable[int]) -> int:
    """Return total by multiplying scalars by values."""
    return sum(a * b for a, b in zip(scalars, values, strict=True))


def plus_one(scalars: Iterable[int], cap: Sequence[int]) -> tuple[int, ...]:
    """Add one to scalars."""
    items = list(scalars)
    index = 0
    while index < len(cap):
        items[index] += 1
        if items[index] > cap[index]:
            items[index] = 0
            index += 1
        else:
            return tuple(items)
    raise AssertionError("Unreachable")


def run() -> None:
    """Run program."""
    print("Took like 2 or 3 hours to run, don't use this lol.")
    print("Look into the knapsack problem, that's what this is.")
    current = (0,) * len(COINS)
    # Does not count 2 pounds mark
    ways = 1
    while current[-1] < 1:
        total = get_total(current, COINS)
        if total == 200:
            ways += 1
        ##            print(f'{current = }')
        current = plus_one(current, MAX)
    print(f"{ways = }")


if __name__ == "__main__":
    print(f"{__title__}\nProgrammed by {__author__}.\n")
    run()
