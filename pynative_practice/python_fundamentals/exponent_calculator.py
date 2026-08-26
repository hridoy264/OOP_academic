def exponent(a, b):
    res = 1
    for i in range(1, b+1):
        res = res * a
    return res 

print(exponent(2, 5))
