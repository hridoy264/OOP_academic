a = [1, 2, 3, 4, 'a', 5, 6, 7]

for i in a:
    if type(i) == type('b'):
        break # loop thamiye dibo
    else:
        print(i)

for i in a:
    if type(i) == type('b'):
        continue # ignore korbo
    else:
        print(i)