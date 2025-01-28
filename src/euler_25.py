"""Project Euler - Problem 25 Prototype."""

# Programmed by CoolCat467

from __future__ import annotations

# Project Euler - Problem 25 Prototype
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

__title__ = "Project Euler - Problem 25 Prototype"
__author__ = "CoolCat467"
__license__ = "GNU General Public License Version 3"


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Generator


def fibonacci() -> Generator[int, None, None]:
    """Yield values of the fibonacci sequence."""
    a = 1
    b = 1
    yield 1
    yield 1
    while True:
        c = a + b
        yield c
        a, b = b, c


def run() -> None:
    """Run program."""
    for idx, x in enumerate(fibonacci()):
        if len(str(x)) >= 1000:
            print(f"{idx + 1 = }")
            break


if __name__ == "__main__":
    print(f"{__title__}\nProgrammed by {__author__}.\n")
    run()
