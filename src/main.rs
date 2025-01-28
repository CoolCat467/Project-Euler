// Project Euler

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

use std::env;
use std::time::Instant;

mod eratosthenes;
mod euler_1;
mod euler_10;
mod euler_11;
mod euler_12;
mod euler_14;
mod euler_2;
mod euler_21;
mod euler_3;
mod euler_4;
mod euler_5;
mod euler_6;
mod euler_7;
mod euler_8;
mod euler_9;

fn print_license() {
    println!("Project Euler\n");
    println!("Programmed by CoolCat467\n");
    println!("Copyright (C) 2025  CoolCat467\n");
    println!("This program is free software: you can redistribute it and/or modify");
    println!("it under the terms of the GNU General Public License as published by");
    println!("the Free Software Foundation, either version 3 of the License, or");
    println!("(at your option) any later version.\n");
    println!("This program is distributed in the hope that it will be useful,");
    println!("but WITHOUT ANY WARRANTY; without even the implied warranty of");
    println!("MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the");
    println!("GNU General Public License for more details.\n");
    println!("You should have received a copy of the GNU General Public License");
    println!("along with this program.  If not, see <https://www.gnu.org/licenses/>.");
}

fn main() {
    // Get the command-line arguments
    let args: Vec<String> = env::args().collect();

    if args.len() > 1 && (args[1] == "--license" || args[1] == "-l") {
        print_license();
        return;
    }

    // Check if an argument was provided
    if args.len() < 2 {
        eprintln!("Usage: cargo run <problem_number> or cargo run --license");
        return;
    }

    // Parse the problem number from the command-line argument
    let problem_number: u32 = match args[1].parse() {
        Ok(num) => num,
        Err(_) => {
            eprintln!("Invalid problem number: {}", args[1]);
            return;
        }
    };

    let start = Instant::now();

    // Match the problem number to the corresponding function
    match problem_number {
        1 => euler_1::main(),
        2 => euler_2::main(),
        3 => euler_3::main(),
        4 => euler_4::main(),
        5 => euler_5::main(),
        6 => euler_6::main(),
        7 => euler_7::main(),
        8 => euler_8::main(),
        9 => euler_9::main(),
        10 => euler_10::main(),
        11 => euler_11::main(),
        12 => euler_12::main(),
        14 => euler_14::main(),
        21 => euler_21::main(),
        _ => eprintln!("Problem {} not implemented.", problem_number),
    }

    println!("Took {:?}", start.elapsed());
}
