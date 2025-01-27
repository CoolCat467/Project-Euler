"""Project Euler - Problem 15 Prototype."""

# Programmed by CoolCat467

from __future__ import annotations

# Project Euler - Problem 15 Prototype
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

__title__ = "Project Euler - Problem 15 Prototype"
__author__ = "CoolCat467"
__license__ = "GNU General Public License Version 3"


import math
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Generator, Iterable


def yield_decompose_big_endian(
    n: int,
    bits: int,
) -> Generator[int, None, None]:
    """Yield big endian decomposition of n with given number of bits."""
    for _ in range(bits):
        yield n & 1
        n >>= 1


def yield_decompose_little_endian(
    n: int,
    bits: int,
) -> Generator[int, None, None]:
    """Yield little endian decomposition of n with given number of bits."""
    yield from reversed(tuple(yield_decompose_big_endian(n, bits)))


def decompose(n: int) -> tuple[int, ...]:
    """Decompose n into bits."""
    bits = n.bit_length()
    return tuple(yield_decompose_little_endian(n, bits))


def compose(bits: Iterable[int]) -> int:
    """Recompose an iterable of bits back into a number."""
    n = 0
    for bit in bits:
        n <<= 1
        n |= bit
    return n


##def find_routes(n: int) -> tuple[int, ...]:
##    if n == 1:
##        return (


# If we say that we have a 3x3 lattice, we have a grid of 4x4 points
# . . . .
# . . . .
# . . . .
# . . . .
#
# and if we start at (0, 0) and say at each point
# we have the operations of go right (0) and go down (1),
# full set of possible paths is the following:
#
# 000111
# 001011
# 001101
# 001110
# 010011
# 010101
# 010110
# 011001
# 011010
# 011100
# 100011
# 100101
# 100110
# 101001
# 101010
# 101100
# 110001
# 110010
# 110100
# 111000
#
# And all lattices follow this pattern, where number of bits per path is
# 2 * n, starting with first half being rights and 2nd half being downs.
# Number of rights and down are maintained, so it's just a matter of
# finding how many combinations of n#2 rights and n#2 downs there are,
# which can be found by calculating (2*n) choose n, aka the binomial
# coefficient.


def find_all_routes(n: int) -> int:
    """Return the number of possible paths through an n by n lattice."""
    ### right = False
    ### down = True
    ##for x in range(size):
    ##    for y in range(size):
    ##
    ##print(f'{n = }')
    ##choices = 2 * n
    ##print(f'{choices = }')
    ##
    ##half_choices = (n)# - 1)
    ##bits = (0,) * half_choices + (1,) * half_choices
    ##final_bits = (1,) * half_choices + (0,) * half_choices
    ##print(f'{bits = }')
    ##
    ##return math.comb(choices, half_choices)
    return math.comb(2 * n, n)


def run() -> None:
    """Run program."""
    print(f"{find_all_routes(2) = }")
    print(f"{find_all_routes(20) = }")


if __name__ == "__main__":
    print(f"{__title__}\nProgrammed by {__author__}.\n")
    run()
