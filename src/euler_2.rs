// Project Euler - Problem 2

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

pub fn main() {
    let mut sum: u32 = 0;

    let mut a = 1;
    let mut b = 0;
    'fib: loop {
        if a >= 4_000_000 {
            break 'fib;
        }
        if a % 2 == 0 {
            sum += a;
        }
        (a, b) = (a + b, a);
    }

    println!("Sum: {}", sum)
}
