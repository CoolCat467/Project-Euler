"""Project Euler - Problem 18 Prototype."""

# Programmed by CoolCat467

from __future__ import annotations

# Project Euler - Problem 18 Prototype
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

__title__ = "Project Euler - Problem 18 Prototype"
__author__ = "CoolCat467"
__license__ = "GNU General Public License Version 3"


def best_sum(structure: tuple[tuple[int, ...], ...]) -> int:
    """Return sum of best path down triangle.

    More accurately, UP the triangle.
    """
    buffer = [0] * (len(structure[-1]))
    row: tuple[int, ...]
    for row in reversed(structure[1:]):
        for col, val in enumerate(row[:-1]):
            buffer[col] = max(
                val + buffer[col],
                row[col + 1] + buffer[col + 1],
            )
        # Could delete, but constant resizing might slow down even more
        # buffer.pop()
        # print(f'{buffer = }')
    return buffer[0] + structure[0][0]


def run() -> None:
    """Run program."""
    data = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""
    ##    data = """3
    ##7 4
    ##2 4 6
    ##8 5 9 3"""

    structure = tuple(
        tuple(map(int, line.split())) for line in data.splitlines()
    )
    print(f"{best_sum(structure) = }")


if __name__ == "__main__":
    print(f"{__title__}\nProgrammed by {__author__}.\n")
    run()
