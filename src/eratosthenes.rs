// Sieve of Eratosthenes

// Programmed by CoolCat467

// Copyright (C) 2025  CoolCat467
//
//     This program is free software: you can redistribute it and/or modify
//     it under the terms of the GNU General Public License as published by
//     the Free Software Foundation, either version 3 of the License, or
//     (at your option) any later version.
//
//     This program is distributed in the hope that it will be useful,
//     but WITHOUT ANY WARRANTY; without even the implied warranty of
//     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//     GNU General Public License for more details.
//
//     You should have received a copy of the GNU General Public License
//     along with this program.  If not, see <https://www.gnu.org/licenses/>.

pub fn sieve(n: usize) -> Vec<usize> {
    //! Return prime numbers up to n using Sieve of Eratosthenes.
    //!
    //! Based on https://stackoverflow.com/a/49936915/18995127.

    // Create a vector of boolean flags initialized to true
    let mut flags = vec![true; n + 1];
    flags[0] = false; // 0 is not a prime number
    flags[1] = false; // 1 is not a prime number

    // Iterate from 2 to the square root of n
    let limit = (n as f64).sqrt() as usize + 1;
    for i in 2..=limit {
        if flags[i] {
            // Mark multiples of i as false
            let mut multiple = i * i;
            while multiple <= n {
                flags[multiple] = false;
                multiple += i;
            }
        }
    }

    // Collect the indices of the true flags, which represent prime numbers
    flags
        .iter()
        .enumerate()
        .filter_map(|(index, &is_prime)| if is_prime { Some(index) } else { None })
        .collect()
}
