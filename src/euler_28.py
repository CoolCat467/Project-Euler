"""Project Euler - Problem 28 Prototype."""

# Programmed by CoolCat467

from __future__ import annotations

# Project Euler - Problem 28 Prototype
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

__title__ = "Project Euler - Problem 28 Prototype"
__author__ = "CoolCat467"
__license__ = "GNU General Public License Version 3"


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Generator


# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13


def yield_diagonals_old(grid_size: int) -> Generator[int, None, None]:
    """Yield spiral grid diagonal numbers from a grid_size x grid_size grid."""
    layer_dims = 0
    side = 3
    index = 0
    n = 1
    end = grid_size * grid_size
    while n <= end:
        if index == layer_dims:
            yield n
            side += 1
            index = 0
        if side == 4:
            side = 0
            index = 1
            layer_dims += 2
        else:
            index += 1
        n += 1


def yield_diagonals(grid_size: int) -> Generator[int, None, None]:
    """Yield spiral grid diagonal numbers from a grid_size x grid_size grid."""
    yield 1
    layer_dims = 2
    n = 1 + layer_dims
    end = grid_size * grid_size
    while n <= end:
        for _ in range(4):
            yield n
            n += layer_dims
        n += 2
        layer_dims += 2


def run() -> None:
    """Run program."""
    print(tuple(yield_diagonals(7)))
    print(f"{sum(yield_diagonals(1001)) = }")


if __name__ == "__main__":
    print(f"{__title__}\nProgrammed by {__author__}.\n")
    run()
