// Project Euler - Problem 21

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

fn sum_of_proper_divisors(n: usize) -> usize {
    //! Return the sum of proper divisors of n
    if n == 0 {
        return 0;
    }

    let mut sum = 0;

    // Iterate through all possible divisors from 1 to n/2
    for i in 1..=n / 2 {
        if n % i == 0 {
            sum += i;
        }
    }

    sum
}

pub fn main() {
    let mut sum = 0;

    for a in 1..10_000 {
        let b = sum_of_proper_divisors(a);
        if a == b {
            continue;
        }
        let match_a = sum_of_proper_divisors(b);
        if a == match_a {
            sum += a; // b will be found later
        }
    }
    println!("Sum amicable numbers = {}", sum);
}
