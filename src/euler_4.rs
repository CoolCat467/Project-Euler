// Project Euler - Problem 4

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

fn get_left_right<'nsa>(s: &'nsa str) -> (&'nsa str, &'nsa str) {
    //! Return left and right side after splitting in half, omitting center if odd length.
    let midpoint = s.len() / 2;

    // If the string length is odd, the right part will start from midpoint + 1
    if s.len() % 2 == 0 {
        (&s[..midpoint], &s[midpoint..])
    } else {
        (&s[..midpoint], &s[midpoint + 1..])
    }
}

fn reverse_string(s: &str) -> String {
    //! Return reversed string
    s.chars().rev().collect()
}

pub fn main() {
    let mut candidate: u64 = 0;
    for num_1 in (100..999).rev() {
        for num_2 in (100..999).rev() {
            let num = num_1 * num_2;
            let num_str = format!("{}", num);
            let (left, right) = get_left_right(&num_str);
            if left == reverse_string(right) && num > candidate {
                candidate = num;
            }
        }
    }
    println!("Palendrome number: {}", candidate);
}
