"""Project Euler - Problem 22 Prototype."""

# Programmed by CoolCat467

from __future__ import annotations

# Project Euler - Problem 22 Prototype
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

__title__ = "Project Euler - Problem 22 Prototype"
__author__ = "CoolCat467"
__license__ = "GNU General Public License Version 3"


def name_value(name: str) -> int:
    """Return name value for given name."""
    value = 0
    for char in name:
        value += ord(char) - 64
    return value


def run() -> None:
    """Run program."""
    with open("0022_names.txt", encoding="utf-8") as file:
        sorted_names = sorted(file.read().strip()[1:-1].split('","'))
    total_score = 0
    for index, name in enumerate(sorted_names):
        total_score += (index + 1) * name_value(name)
    print(f"{total_score = }")


if __name__ == "__main__":
    print(f"{__title__}\nProgrammed by {__author__}.\n")
    run()
