import os 
import pathlib

# # Basic code 
# file = open('name.txt', 'r')
# content = file.read()
# print(content)

# file.close()

# # More smarter way
# with open('name.txt', 'r') as f:
#     content = f.read()
#     print(content)

# with open('name.txt', 'w') as f:
#     # f.write("Hello world\n")
#     # f.write("I am writting in a file\n")
#     f.write("This is for testing")

# with open('name.txt', 'a') as f:
#     f.write("\nHello world\n")
#     f.write("I am writting in a file\n")
#     f.write("This is for testing")

# lines = ['\nI love python\n', 'I am new to python\n']

# with open('name.txt', 'a') as f:
#     f.writelines(lines)

if os.path.exists('name.txt'):
    print('Fiile exists')
else:
    print('File doesn\'t exists')


file_path = pathlib.Path('name.txt')

if file_path.exists():
    print("File exists")
print(os.path.abspath('name.txt'))
print(os.path.getsize('name.txt')) # bytes

with open('name.txt', 'r') as f:
    print(f.tell())     # cursor koi thake seta output dey
    print(f.read(5))