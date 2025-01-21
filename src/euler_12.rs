// Project Euler - Problem 12

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

fn divisor_count(n: usize) -> usize {
    //! Returns the number of divisors of an integer based on its prime factorization.
    if n == 0 {
        return 0; // Handle edge case for 0
    }

    let search = (n as f64).sqrt() as usize + 1;
    let primes = sieve(search);
    let mut total_divisors = 1;
    let mut temp = n;

    for &prime in &primes {
        if prime >= search || prime * prime > temp {
            break; // No need to check beyond the square root of n
        }

        let mut count = 0;
        while temp % prime == 0 {
            temp /= prime;
            count += 1;
        }

        if count > 0 {
            total_divisors *= count + 1;
        }
    }

    // If there's any prime factor greater than sqrt(n), it can only be one and is temp itself
    if temp > 1 {
        total_divisors *= 2; // temp is prime
    }

    total_divisors
}

pub fn main() {
    let mut n = 1;

    loop {
        let triangle_number = n * (n + 1) / 2;
        let divisors;

        // Count divisors of T_n = n(n + 1) / 2
        if n % 2 == 0 {
            // n is even
            divisors = divisor_count(n / 2) * divisor_count(n + 1);
        } else {
            // n is odd
            divisors = divisor_count(n) * divisor_count((n + 1) / 2);
        }

        if divisors > 500 {
            println!(
                "The first triangle number with over 500 divisors is: {}",
                triangle_number,
            );
            break;
        }

        n += 1;
    }
}
