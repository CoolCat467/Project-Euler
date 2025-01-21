// Project Euler - Problem 7

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

fn sieve(n: usize) -> Vec<usize> {
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

fn estimate_search_size(k: usize) -> usize {
    //! Estimate the upper bound for the k-th prime number using the Prime Number Theorem
    if k < 6 {
        return 15; // A small constant for small k values
    }

    let log_k = (k as f64).ln();
    let log_log_k = log_k.ln();
    (k as f64 * (log_k + log_log_k)) as usize
}

pub fn main() {
    // Number of prime numbers we want to find
    let k = 10_001;

    // Estimate the search size
    let n = estimate_search_size(k);

    let primes = sieve(n);

    println!(
        "The {}-th prime number is: {} (searched with bound {})",
        k,
        primes[k - 1],
        n
    );
}
