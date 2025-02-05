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
    from collections.abc import Generator, Iterable


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
    num = list(decompose(numerator, base))
    current = 0
    given_decimal = False
    last_through = True
    while num or current:
        if num:
            current *= base
            current += num.pop(0)
        elif current < denominator:
            current *= base
            if not given_decimal:
                given_decimal = True
                last_through = False
                # Indicate decimal point
                yield None
            elif last_through:
                last_through = False
            else:
                yield 0

            continue
        if current == 0:
            yield 0
            continue
        if current >= denominator:
            div, current = divmod(current, denominator)
            yield div
            last_through = True


def find_cycle(
    sequence: Iterable[int],
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """Return non-repeating digits and repeating sequence from digit sequence."""
    digits = []
    gen = iter(sequence)
    last = next(gen)
    digits.append(last)

    graph: dict[int, list[tuple[int, int]]] = {}

    current_potential_chain: list[int] = [last]
    chains: list[tuple[int, ...]] = []

    for digit in gen:
        digits.append(digit)

        graph.setdefault(last, [])
        reached_prior = graph[last]
        for index, (number, count) in enumerate(reached_prior):
            if number != digit:
                continue
            reached_prior[index] = (digit, count + 1)
            if current_potential_chain and current_potential_chain[0] == digit:
                ##                print(f'{current_potential_chain = }')
                new_chain = (
                    current_potential_chain[-1],
                    *tuple(current_potential_chain[:-1]),
                )
                if new_chain in chains:
                    print(f"{graph = }")
                    assert next(gen) == new_chain[0]
                    return (
                        tuple(digits[: -(len(new_chain) * 3 + 2)]),
                        new_chain,
                    )
                chains.append(new_chain)
                current_potential_chain.clear()
            current_potential_chain.append(digit)
            break
        else:
            reached_prior.append((digit, 1))
            current_potential_chain.clear()

        last = digit
    ##    print(f'{graph = }')
    ##    print(f'{chains = }')
    return tuple(digits), ()


def long_division_cycle(
    numerator: int,
    denominator: int,
    base: int = 10,
) -> tuple[tuple[int | None, ...], tuple[int, ...]]:
    """Return digits before cycle and cyclical digit sequence."""
    start = []
    gen = long_division(numerator, denominator, base)
    for digit in gen:
        start.append(digit)
        if digit is None:
            break
    digits, cycle = find_cycle(int(x) for x in gen if x is not None)
    return (tuple(start) + digits), cycle


def run() -> None:
    """Run program."""
    ##    value = ''
    ##    post_decimal = False
    ##    digits = []
    ##    limit = 47*3
    ##    for digit in long_division(1, 326):
    ##        limit -= 1
    ##        if limit <= 0:
    ##            break
    ##        if digit is None:
    ##            value += "."
    ##            post_decimal = True
    ##            continue
    ##        if post_decimal:
    ##            digits.append(digit)
    ##        value += f'{digit}'
    ##    print(value)
    ##    print(f'{digits = }')
    ##    print(f'{find_cycle(digits) = }')
    print(f"{long_division_cycle(1, 326) = }")


##    longest_d = 1
##    best_cycle_length = 0
##    for d in range(2, 1000):
####        print(f'{d = }')
##        _equal, cycle = long_division_cycle(1, d)
##        cycle_len = len(cycle)
##        if cycle_len > best_cycle_length:
##            best_cycle_length = cycle_len
##            longest_d = d
##    print(f'{best_cycle_length = } {longest_d = }')


if __name__ == "__main__":
    print(f"{__title__}\nProgrammed by {__author__}.\n")
    run()
