number = int(input("Enter a number to get the summation of all numbers before it: "))
sum = 0
for i in range(1, number+1):
    sum += i

print(sum)