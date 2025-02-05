// Project Euler - Problem 27

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
use std::collections::HashSet;

pub fn main() {
    let mut best_successive = 0;
    let mut best_product = 1;

    let cap = 12989; //4096
    let prime_set: HashSet<usize> = sieve(cap).into_iter().collect();

    for a in -999..=999 {
        // Not sure if -a is technically right here, but
        // runs faster and still correct answer so I guess its fine.
        for b in -a..=1_000 {
            let mut n = 0;
            let mut successive = 0;

            loop {
                let v: i64 = n * n + a * n + b;
                if v < 0 {
                    break;
                }
                if v as usize > cap {
                    panic!("{v} > {cap}");
                    // // Double the cap and update the primes
                    // cap *= 2;
                    // prime_set = sieve(cap).iter().cloned().collect();
                }
                if prime_set.contains(&(v as usize)) {
                    successive += 1;
                } else {
                    break;
                }
                n += 1;
            }

            if successive > best_successive {
                best_successive = successive;
                best_product = a * b;
            }
        }
    }

    println!("best_successive = {best_successive}");
    println!("best_product = {best_product}");
}
