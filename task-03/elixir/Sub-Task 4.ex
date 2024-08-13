IO.puts("Enter a number: ")
num = IO.gets("") |> String.trim() |> String.to_integer()
File.write!("input.txt", Integer.to_string(num))
{:ok, content} = File.read('input.txt')
rows = String.trim(content) |> String.to_integer()
pattern =
  for i <- 0..(rows - 2) do
    for _ <- 0..(rows - i - 1) do
      IO.write(" ")
    end
    for _ <- 0..i do
      IO.write("* ")
    end
    IO.puts("")
  end

  for i <- 0..(rows - 1) do
    # Print leading spaces
    for _ <- 0..i do
      IO.write(" ")
    end

    # Print asterisks
    for _ <- 0..(rows - i - 1) do
      IO.write("* ")
    end

    IO.puts("")
  end
File.write!("output.txt", pattern)

{:ok, new} = File.read("output.txt")
 IO.puts(new)
