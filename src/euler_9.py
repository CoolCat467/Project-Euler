"""Project Euler - Problem 9 Prototype."""

# Programmed by CoolCat467

from __future__ import annotations

# Project Euler - Problem 9 Prototype
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
# You should have received b copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

__title__ = "Project Euler - Problem 9 Prototype"
__author__ = "CoolCat467"
__license__ = "GNU General Public License Version 3"


import math
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Generator


def yield_pythagorean_triplets() -> (
    Generator[tuple[int, int, int], None, None]
):
    """Yield Pythagorean Triplets.

    a < b < c && a**2 + b**2 = c**2
    """
    b = 2
    while True:
        b_2 = b * b
        for a in range(1, b):
            left = b_2 + a * a
            c = math.ceil(math.sqrt(left))
            if left == c * c:
                yield a, b, c
        b += 1


def run() -> None:
    """Run program."""
    for v in yield_pythagorean_triplets():
        if sum(v) == 1000:
            print(f"{v = }")
            print(f"{math.prod(v) = }")
            break


if __name__ == "__main__":
    print(f"{__title__}\nProgrammed by {__author__}.\n")
    run()
