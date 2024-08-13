IO.puts("Enter the number of rows:")
rows = IO.gets("") |> String.trim() |> String.to_integer()
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
