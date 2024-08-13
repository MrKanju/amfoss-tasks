use std::fs::File;
use std::io::{self, Read, Write};

fn main() -> io::Result<()> {
    let mut inputfile = File::open("input.txt")?; 
    let mut contents = String::new();
    input_file.read_to_string(&mut contents)?; 

    let mut output_file = File::create("output.txt")?; 
    output_file.write_all(contents.as_bytes())?; 
    Ok(())
}
