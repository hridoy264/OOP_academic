string = input("Enter a random string: ")
flag = False
for i in string:
    if i.isdigit():
        flag = True
        break
print(flag)
    
