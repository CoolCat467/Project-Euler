"""Project Euler - Problem 26 Prototype."""

# Programmed by CoolCat467

from __future__ import annotations

# Project Euler - Problem 26 Prototype
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

__title__ = "Project Euler - Problem 26 Prototype"
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


def decompose(value: int, base: int = 10) -> tuple[int, ...]:
    """Return decomposition values of value by base in little endian order."""
    return tuple(decompose_big_endian(value, base))[-1::-1]


def long_division(
    numerator: int,
    denominator: int,
    base: int = 10,
) -> Generator[int | None, None, None]:
    """Yield digits from the long division of numerator by denominator, with None indicating a decimal point."""
    if not denominator:
        raise ZeroDivisionError("division by zero")
    num = list(decompose(numerator, base))
    current = 0
    given_decimal = False

    while num or current:
        current *= base
        if num:
            current += num.pop(0)
        elif not given_decimal:
            given_decimal = True
            yield None
        if current < denominator and current:
            continue
        div, current = divmod(current, denominator)
        yield div


def long_division_cycle(
    numerator: int,
    denominator: int,
    base: int = 10,
) -> int:
    """Return number of cyclical digits in long division."""
    num = list(decompose(numerator, base))
    current = 0

    remainder_pos_table: dict[int, int] = {}

    digit_place = 0

    while num or current:
        current *= base
        digit_place += 1
        if num:
            current += num.pop(0)
        if current < denominator and current:
            continue
        div, current = divmod(current, denominator)
        if remainder_pos_table.get(current) is not None:
            return digit_place - remainder_pos_table[current]
        remainder_pos_table[current] = digit_place
    return 0


def run() -> None:
    """Run program."""
    print(f"{long_division_cycle(1, 7) = }")

    longest_d = 1
    best_cycle_length = 0
    for d in range(2, 1000):
        cycle_len = long_division_cycle(1, d)
        if cycle_len > best_cycle_length:
            best_cycle_length = cycle_len
            longest_d = d
    print(f"{best_cycle_length = } {longest_d = }")


if __name__ == "__main__":
    print(f"{__title__}\nProgrammed by {__author__}.\n")
    run()
