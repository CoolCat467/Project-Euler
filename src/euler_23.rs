// Project Euler - Problem 23

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

fn sums_of_proper_divisors(limit: usize) -> Vec<u32> {
    //! Calculate the sum of proper divisors for each number up to limit
    let mut sums = vec![0; limit + 1];

    for n in 2..=limit / 2 {
        for i in (2 * n..=limit).step_by(n) {
            sums[i] += n as u32;
        }
    }

    sums
}

pub fn main() {
    let limit = 28_123;
    let sums = sums_of_proper_divisors(limit);

    let mut abundant = Vec::new();

    // Collect abundant numbers
    for n in 12..=limit {
        if sums[n] > n as u32 {
            abundant.push(n);
        }
    }

    let mut can_be_written_as_abundant_sum = vec![false; limit + 1];

    // Mark sums of two abundant numbers
    for &a in &abundant {
        for &b in &abundant {
            let sum_abundant = a + b;
            if sum_abundant > limit {
                // No need to continue if sum exceeds the limit
                break;
            }
            can_be_written_as_abundant_sum[sum_abundant] = true;
        }
    }

    let total_sum: usize = (1..=limit)
        .filter(|&n| !can_be_written_as_abundant_sum[n])
        .sum();

    println!("total_sum = {}", total_sum);
}
