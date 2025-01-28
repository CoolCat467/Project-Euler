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

use crate::eratosthenes::sieve;

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
