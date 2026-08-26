# part1: Writting the file
with open("notes.txt", "w") as file:
    file.write("Hello, this is my first python note.\n")
    file.write("Python file handling is easy.\n")
    file.write("End of file.\n")

with open("notes.txt", "r") as file:
    content = file.read()
    print(content)