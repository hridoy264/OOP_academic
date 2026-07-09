# Basic code 
file = open('name.txt', 'r')
content = file.read()
print(content)

file.close()

# More smarter way
with open('name.txt', 'r') as f:
    content = f.read()
    print(content)

with open('name.txt', 'w') as f:
    # f.write("Hello world\n")
    # f.write("I am writting in a file\n")
    f.write("This is for testing")

with open('name.txt', 'a') as f:
    f.write("\nHello world\n")
    f.write("I am writting in a file\n")
    f.write("This is for testing")

lines = ['\nI love python\n', 'I am new to python\n']

with open('name.txt', 'a') as f:
    f.writelines(lines)