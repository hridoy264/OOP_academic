a = [1, 10, 23, 24, 26, 90]
# only even gula nibo
result = []

# Normal way

for i in a:
    if i%2==0:
        result.append(i)

print(result)

# List comprehension
new_result = [i for i in a if i%2==0]
print(new_result)

b = [1, 2, 3, 4, 5]     # --> [1, 4, 3, 16, 5]
b_new = [i**2 if i%2 ==0 else i for i in b]

