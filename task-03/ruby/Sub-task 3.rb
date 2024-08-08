print "Enter the number of rows: "
rows = gets.to_i

for i in 0...(rows) do
  for j in 0...(rows-i-1)
    print " "
  end
  for j in 0..i
    print "* "
  end
  puts
end

for i in 0...(rows-1) do
  for j in 0..i
    print " "
  end
  for j in 0...(rows-i-1)
    print "* "
  end
  puts
end
