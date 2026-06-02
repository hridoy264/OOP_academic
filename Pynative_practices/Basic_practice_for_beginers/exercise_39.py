with open("external_file_counter.txt", "w") as file:
    file.write("Coding is the language of the future world")

with open("external_file_counter.txt", "r") as file:
    content = file.read()
    words = content.split()
    count = 0
for word in words:
     count+=1
print(count)