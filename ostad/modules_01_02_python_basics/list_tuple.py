a = [1, 2, 3, 'Naim', 'Fahim', 3.0, 3.2]
# list mutable

a[0] = 100
print(a)
print(a[-1])
print(len(a))

s = "Hello"
print(list(s))

a.append([1, 2, 3])
print(a)
a.reverse()
print(a)

# tuple() --> immutable
t = (1, 2, 3)
# t[0] = 100
t_r = tuple(reversed(t))
print(t)
print(t_r)