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
        # If you haven't seen it before, divmod is a more efficient way
        # to calculate (x//y, x%y), ie (true divisions, remainder), similar
        # to the way the actual asm instruction for division works.
        value, div = divmod(value, base)
        yield div


def decompose(value: int, base: int = 10) -> tuple[int, ...]:
    """Return decomposition values of value by base in little endian order."""
    # Just reverse the order, but that does mean it can't be a generator
    # anymore.
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

    # While we still have something in accumulator (current) or digits to pop
    # from decomposition,
    while num or current:
        # Change accumulator value to next digit place up
        # Ie if accumulator was always base 2, this would be equivalent:
        # current <<= 1
        current *= base
        # If we have numbers in decomposition yet, add them
        # Again if was base 2, equivalent would be:
        # current |= num.pop(0)
        if num:
            current += num.pop(0)
        elif not given_decimal:
            # If no numbers to pop and we haven't marked decimal place yet,
            # do so.
            given_decimal = True
            yield None
        # If can't do full division and nonzero current value, don't yield
        # full division, need more digits. If is zero, do yield, because
        # need more decimal places for following digits.
        if current < denominator and current:
            continue
        div, current = divmod(current, denominator)
        yield div


def long_division_cycle(
    numerator: int,
    denominator: int,
    base: int = 10,
) -> int:
    """Return number of cyclical digits in long division of numerator by denominator."""
    if not denominator:
        raise ZeroDivisionError("division by zero")
    num = list(decompose(numerator, base))
    current = 0

    # Keep track of mapping between remainders and digit places
    remainder_pos_table: dict[int, int] = {}

    # Because not actually yielding division return value,
    # need to keep track of which digit of answer we are currently on
    digit_place = 0

    while num or current:
        # See long_division for more information
        current *= base
        digit_place += 1
        if num:
            current += num.pop(0)
        if current < denominator and current:
            continue
        div, current = divmod(current, denominator)

        # If we have seen this remainder value before,
        if remainder_pos_table.get(current) is not None:
            # we are in a cycle, so cycle length is difference between
            # current digit place and when we first saw this remainder
            return digit_place - remainder_pos_table[current]
        # Have not seen this remainder before, remember place for the
        # future for if we see this remainder again to calculate cycle
        # length.
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
