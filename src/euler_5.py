"""Project Euler - Problem 5 Prototype."""

# Programmed by CoolCat467

from __future__ import annotations

# Project Euler - Problem 5 Prototype
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

__title__ = "Project Euler - Problem 5 Prototype"
__author__ = "CoolCat467"
__license__ = "GNU General Public License Version 3"


import math


def run() -> None:
    """Run program."""
    print(f"{math.lcm(*range(1, 10+1)) = }")
    print(f"{math.lcm(*range(1, 20+1)) = }")


if __name__ == "__main__":
    print(f"{__title__}\nProgrammed by {__author__}.\n")
    run()
