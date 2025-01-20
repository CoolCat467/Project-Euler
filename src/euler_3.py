"""Project Euler - Problem 3 Prototype."""

# Programmed by CoolCat467

from __future__ import annotations

# Project Euler - Problem 3 Prototype
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

__title__ = "Project Euler - Problem 3 Prototype"
__author__ = "CoolCat467"
__license__ = "GNU General Public License Version 3"


import math
from typing import TYPE_CHECKING

import numpy as np

if TYPE_CHECKING:
    from numpy.typing import NDArray


def sieve(n: int) -> NDArray[np.int64]:
    """Return prime numbers up to n using Sieve of Eratosthenes.

    Based on https://stackoverflow.com/a/49936915/18995127.
    """
    flags = np.ones(n, dtype=np.bool)
    flags[0:1] = False
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if flags[i]:
            flags[i * i :: i] = False
    return np.flatnonzero(flags)


def run() -> None:
    """Run program."""
    ##n = 13195
    n = 600851475143
    search = math.floor(math.sqrt(n)) + 1
    primes = sieve(search)

    factors = []
    for prime in primes[1:]:
        if n % prime == 0:
            factors.append(int(prime))
    print(f"Prime factors of {n}: {factors}")


if __name__ == "__main__":
    print(f"{__title__}\nProgrammed by {__author__}.\n")
    run()
