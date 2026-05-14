n = 5
for i in range(n+1, 0, -1):
    for j in range(1, i):
        print(i-j, end = " ")
    print()