// Project Euler - Problem 14

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

fn collatz(mut n: u64) -> u32 {
    let mut count = 0;
    while n != 1 {
        if n % 2 == 0 {
            n /= 2;
        } else {
            n = 3 * n + 1;
        }
        count += 1;
    }
    return count;
}

pub fn main() {
    let cap = 1_000_000;
    let mut best = 1;
    let mut count = 1;
    for n in 2..=cap {
        let cur_count = collatz(n);
        if cur_count > count {
            count = cur_count;
            best = n;
        }
    }
    println!("n = {} count = {}", best, count);
}
