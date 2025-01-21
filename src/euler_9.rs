// Project Euler - Problem 9

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

// pub fn main() {
//     let mut b: u32 = 2;
//     loop {
//         let b_2 = b * b;
//         for a in 1..b {
//             let left: u32 = b_2 + a * a;
//             let c = ((left as f64).sqrt()).ceil() as u32;
//             let right = c * c;
//             if left == right {
//                 if a + b + c == 1000 {
//                     println!("a * b * c = {}", a * b * c);
//                     return;
//                 }
//             }
//         }
//         b += 1;
//     }
// }

pub fn main() {
    for b in 2..=500 {
        for a in 1..b {
            let c = 1000 - a - b;
            // Check the Pythagorean condition
            if c > 0 && a * a + b * b == c * c {
                println!("a * b * c = {}", a * b * c);
                return;
            }
        }
    }
}
