# printing alternate prime number

import math
n=20
count = 0
for i in range(2, n+1):
    flag = 0
    for j in range(2, int(math.sqrt(i))+1):
        if i%j==0:
            flag=1
    if flag == 0:
        count +=1
        if count%2==1:
            print(i, end=" ")


# primes = []

# for num in range(2, 21):
#     # Check if number is prime
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             break
#     else:
#         primes.append(num)

# # Print alternate primes
# alternate_primes = primes[::2]
# print(alternate_primes)