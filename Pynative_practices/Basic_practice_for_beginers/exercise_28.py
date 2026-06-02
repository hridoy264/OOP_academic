list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd = []
even = []
list_len = len(list)

for i in range(list_len):
    if list[i]%2==0:
        even.append(list[i])
    else:
        odd.append(list[i])

print(odd)
print(even)

