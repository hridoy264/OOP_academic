num_list = [int(x) for x in input("Enter three numbers here for see maximum one: ").split()]
max = 1
for i in range(0, 3):
    if(num_list[i]>max):
        max = num_list[i]

print(max)