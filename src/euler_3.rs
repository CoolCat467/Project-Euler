// Project Euler - Problem 3

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

pub fn main() {
    // Define the number for which we want to find prime factors
    // let n = 13195;
    let n = 600851475143;
    // Calculate the upper limit for the sieve
    let search = (n as f64).sqrt() as usize + 1;
    // Get the list of prime numbers
    let primes = sieve(search);

    // println!("{:?}", primes);

    // let mut factors = Vec::new();
    let mut greatest_factor = 1;

    // Check each prime number to see if it is a factor of n
    for &prime in &primes {
        if n % prime == 0 {
            // factors.push(prime);
            greatest_factor = prime;
        }
    }

    // println!("Prime factors of {}: {:?}", n, factors);
    println!("Greatest prime factor of {}: {}", n, greatest_factor);
}
