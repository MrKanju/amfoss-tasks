{:ok, file} = File.read("input.txt")
File.write!("output.txt", file)
IO.puts(File.read!("output.txt"))
