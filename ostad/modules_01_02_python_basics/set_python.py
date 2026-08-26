# {} carly bracket diye thake
# unordered --> indexing kore value pawa jabe na
# immutable --> no update  
# No duplicates
# set()

a = [1, 2, 2, 3, 4, 4, 4, 5]
s = set(a)
# s[0] = 100.   immutable
print(s)
# print(s[0])   not subcriptable

# Union, INtersection
a = {1, 2, 3}
b = {2, 3, 4}

c = b.intersection(a)
d = a.union(b)
print(c)
print(d)