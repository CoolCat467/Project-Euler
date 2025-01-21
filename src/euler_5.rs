// Project Euler - Problem 5

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

fn gcd(a: u64, b: u64) -> u64 {
    if b == 0 {
        a
    } else {
        gcd(b, a % b)
    }
}

fn lcm(a: u64, b: u64) -> u64 {
    a * b / gcd(a, b)
}

fn lcm_range(n: u64) -> u64 {
    (1..=n).fold(1, |acc, x| lcm(acc, x))
}

pub fn main() {
    println!("LCM of 1 to 10: {}", lcm_range(10));
    println!("LCM of 1 to 20: {}", lcm_range(20));
}
