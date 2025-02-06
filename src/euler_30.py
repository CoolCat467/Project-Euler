"""Project Euler - Problem 30 Prototype."""

# Programmed by CoolCat467

from __future__ import annotations

# Project Euler - Problem 30 Prototype
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

__title__ = "Project Euler - Problem 30 Prototype"
__author__ = "CoolCat467"
__license__ = "GNU General Public License Version 3"


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Generator


def decompose_big_endian(
    value: int,
    base: int = 10,
) -> Generator[int, None, None]:
    """Yield decomposition values of value by base in big endian order."""
    while value > 0:
        value, div = divmod(value, base)
        yield div


def run() -> None:
    """Run program."""
    power = 5
    digits = tuple(x**power for x in range(10))
    min_ = 2  # 10 ** (power - 1)
    max_ = (10 ** (power + 1)) - 1  # (10 ** power) - 1

    matches = 0

    print(f"{(min_, max_) = }")

    for n in range(min_, max_):
        sum_ = 0
        for digit in decompose_big_endian(n, 10):
            sum_ += digits[digit]
            if sum_ > n:
                break
        else:  # did not break
            if n != sum_:
                continue
            print(f"{n = }")
            matches += n
    print(f"{matches = }")


if __name__ == "__main__":
    print(f"{__title__}\nProgrammed by {__author__}.\n")
    run()
