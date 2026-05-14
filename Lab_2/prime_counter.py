import math
num_list = [int(x) for x in input("Enter some random numbers: ").split()]
prime_count = 0
print(len(num_list))
for i in range(0, len(num_list)):
    flag = 0
    for j in range(2,int(math.sqrt(num_list[i]))):
        if(num_list[i]%j == 0):
            flag = 1
if(flag == 0):
        prime_count += 1
print(f"There are {prime_count} prime numbers")
