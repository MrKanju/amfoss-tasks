use std::fs::File;
use std::io::{self, Read, Write};

fn main() {
    let mut input_file = File::create("input.txt").unwrap(); 
    input_file.write_all(b"5").unwrap(); 
    let mut input_file = File::open("input.txt").unwrap(); 
    let mut input = String::new();
    input_file.read_to_string(&mut input).unwrap(); 
    let rows: usize = input.trim().parse().unwrap(); 
    let mut result = String::new();
    for i in 0..rows {
        for _ in 0..(rows - i - 1) {
            result.push(' ');
        }
        for _ in 0..(i + 1) {
            result.push_str("* ");
        }
        result.push('\n');
    }
    for i in 0..(rows - 1) {
        for _ in 0..(i + 1) {
            result.push(' ');
        }
        for _ in 0..(rows - i - 1) {
            result.push_str("* ");
        }
        result.push('\n');
    }

    let mut output_file = File::create("output.txt").unwrap(); 
    output_file.write_all(result.as_bytes()).unwrap(); /
}
