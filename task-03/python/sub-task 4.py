num = int(input("Enter a number: "))
file = open('input.txt', 'w')
file.write(str(num))
file.close()

input_file = open("input.txt", 'r')
content = input_file.read()
nnum = int(content)
input_file.close()

output = open("output.txt", 'w')

for i in range(nnum):
    for j in range(nnum - i - 1):
        output.write(" ")
    for j in range(i + 1):
        output.write("* ")
    output.write("\n")

for i in range(nnum - 1):
    for j in range(i + 1):
        output.write(" ")
    for j in range(nnum - i - 1):
        output.write("* ")
    output.write("\n")

output.close()
file = open("output.txt", 'r')
patt = file.read()
file.close()
print(patt)