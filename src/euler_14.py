"""Project Euler - Problem 14 Prototype."""

# Programmed by CoolCat467

from __future__ import annotations

# Project Euler - Problem 14 Prototype
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
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

__title__ = "Project Euler - Problem 14 Prototype"
__author__ = "CoolCat467"
__license__ = "GNU General Public License Version 3"


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Generator


def follow_chain(n: int) -> Generator[int, None, None]:
    """Yield collatz conjecture chain numbers."""
    while True:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        yield n


def run() -> None:
    """Run program."""
    size = 1_000_000

    best_count = 0
    best_n = 0

    for n in range(2, size):
        count = 0
        for count, value in enumerate(follow_chain(n)):  # noqa: B007
            if value == 1:
                break
        if count > best_count:
            best_count = count
            best_n = n
    print(f"{best_n = } {best_count = }")


if __name__ == "__main__":
    print(f"{__title__}\nProgrammed by {__author__}.\n")
    run()
