# {}
# Key value pair
# indexing er shujog nai
# key gula obossoi immutable

a = {'rahim':12, 'karim': 14, 'fahim': 78, 1: [1, 2, 3, 4], 2: {3, 4, 5}}

print(a)
print(type(a))
for i in a:
    print(i)

for i in a.values():
    print(i)

print(a.keys(), a.values())
for k, v in a.items():
    print(f"Key Name : {k}, Values: {v}")

a = [1, 2, 3]
b = ["mango", "banana", "apple"]

# {1: mango, 2: 'banana', 3: 'apple'}
print(list(zip(a,b)))
c = dict(zip(b, a))

print(c["mango"])