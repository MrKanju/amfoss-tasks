use std::io;
fn main() {
    let mut input = String::new();
    println!("Enter the number of rows: ");
    io::stdin().read_line(&mut input).expect("Failed to read line");

    let rows: usize = match input.trim().parse() {
        Ok(num) => num,
        Err(_) => {
            eprintln!("Please enter a valid number");
            return;
        }
    };
    for i in 0..rows {
        for j in 0..(rows - i - 1) {
            print!(" ");
        }
        for j in 0..(i + 1) {
            print!("* ");
        }
        println!();
    }
    for i in 0..(rows - 1) {
        for j in 0..(i + 1) {
            print!(" ");
        }
        for j in 0..(rows - i - 1) {
            print!("* ");
        }
        println!();
    }
}