// Project Euler - Problem 6

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
    let n = 100;

    let sum_of_n = (1..=n).sum::<u64>();
    let sum_of_squares = (1..=n).map(|x| x * x).sum::<u64>();

    let value = sum_of_n.pow(2) - sum_of_squares;

    println!("value = {}", value);
}
