"""Project Euler - Problem 8 Prototype."""

# Programmed by CoolCat467

from __future__ import annotations

# Project Euler - Problem 8 Prototype
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

__title__ = "Project Euler - Problem 8 Prototype"
__author__ = "CoolCat467"
__license__ = "GNU General Public License Version 3"


import math
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Generator


# Stolen from my Advent of Code 2024 Day 6, 2024 Day 10, and 2024 Day 12
def get_point_edges(
    x: int,
    y: int,
) -> tuple[tuple[int, int], tuple[int, int], tuple[int, int], tuple[int, int]]:
    """Return edges of given point."""
    return (
        (x, y - 1),
        (x + 1, y),
        (x, y + 1),
        (x - 1, y),
    )


def find_number_indexes(
    matrix: list[str],
    target: int | str,
) -> Generator[tuple[int, int], None, None]:
    """Yield (row, column) positions of target character/number in matrix."""
    target_str = str(target)
    for row, line in enumerate(matrix):
        for col, char in enumerate(line):
            if char == target_str:
                yield (row, col)


def find_highest_score_chain_prod(matrix: list[str], chain_length: int) -> int:
    """Return the largest product of chains of given length in matrix."""
    height = len(matrix)
    width = len(matrix[0])
    # Keeping track of chains by chain's current product.
    # Value for in_progress_chains at point is list of chains with
    # product of that value.
    # Build initially by finding 9s in the matrix
    in_progress_chains: dict[int, list[list[tuple[int, int]]]] = {
        9: [[pos] for pos in find_number_indexes(matrix, 9)],
    }

    best = 9
    # While we have chains to process,
    while in_progress_chains:
        # Find current highest product
        cur_prod = max(in_progress_chains)
        # Get list of in-progress chains with this product
        top = in_progress_chains[cur_prod]
        # Remove entry
        del in_progress_chains[cur_prod]
        chain: list[tuple[int, int]]
        for chain in top:
            # Get head of current chain
            head = chain[-1]
            # For each adjacent cell to chain head
            for edge in get_point_edges(*head):
                # Ignore it if it's out of bounds
                row, col = edge
                if col < 0 or col >= width:
                    continue
                if row < 0 or row >= height:
                    continue
                # If it's already in the chain, ignore it.
                if edge in chain:
                    continue
                # Get value of this new adjacent cell
                value = int(matrix[row][col])
                # Calculate new product
                new_prod = cur_prod * value
                # If this new cell will make chain too long, update best product
                if len(chain) + 1 >= chain_length:
                    best = max(best, new_prod)
                    continue
                # Otherwise, add new chain to in progress chains.
                in_progress_chains.setdefault(new_prod, [])
                in_progress_chains[new_prod].append([*chain, edge])
    return best


def find_greatest_product_of_adjacent_digits(
    number: str,
    adjacent_count: int,
) -> int:
    """Return greatest project of adjacent digits."""
    max_product = 0

    # Iterate through the number, considering each group of adjacent_count digits
    for index in range(len(number) - adjacent_count + 1):
        # Get the current slice of adjacent digits
        slice_of_digits = number[index : index + adjacent_count]

        # Calculate the product of the digits in the slice
        product = math.prod(int(d) for d in slice_of_digits)
        max_product = max(max_product, product)

    return max_product


def run() -> None:
    """Run program."""
    data = (
        "73167176531330624919225119674426574742355349194934"
        "96983520312774506326239578318016984801869478851843"
        "85861560789112949495459501737958331952853208805511"
        "12540698747158523863050715693290963295227443043557"
        "66896648950445244523161731856403098711121722383113"
        "62229893423380308135336276614282806444486645238749"
        "30358907296290491560440772390713810515859307960866"
        "70172427121883998797908792274921901699720888093776"
        "65727333001053367881220235421809751254540594752243"
        "52584907711670556013604839586446706324415722155397"
        "53697817977846174064955149290862569321978468622482"
        "83972241375657056057490261407972968652414535100474"
        "82166370484403199890008895243450658541227588666881"
        "16427171479924442928230863465674813919123162824586"
        "17866458359124566529476545682848912883142607690042"
        "24219022671055626321111109370544217506941658960408"
        "07198403850962455444362981230987879927244284909188"
        "84580156166097919133875499200524063689912560717606"
        "05886116467109405077541002256983155200055935729725"
        "71636269561882670428252483600823257530420752963450"
    )

    length = 13
    # Not actually matrix
    ##matrix: list[str] = data.splitlines()
    ##result = find_highest_score_chain_prod(matrix, length)
    result = find_greatest_product_of_adjacent_digits(data, length)
    print(f"{length = } {result = }")


if __name__ == "__main__":
    print(f"{__title__}\nProgrammed by {__author__}.\n")
    run()
