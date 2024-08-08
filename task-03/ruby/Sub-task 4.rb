print "Enter a number: "
num = gets.to_i
File.open('input.txt', 'w') do |file|
  file.write(num.to_s)
end
content = File.read('input.txt')
nnum = content.to_i

File.open('output.txt', 'w') do |output|
  for i in 0...nnum
    for j in 0...(nnum - i - 1)
      output.write(" ")
    end
    for j in 0..i
      output.write("* ")
    end
    output.write("\n")
  end

  for i in 0...(nnum - 1)
    for j in 0..i
      output.write(" ")
    end
    for j in 0...(nnum - i - 1)
      output.write("* ")
    end
    output.write("\n")
  end
end

patt = File.read('output.txt')
puts patt
