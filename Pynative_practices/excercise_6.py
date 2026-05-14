#Finding factorial using loop

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = i*fact
    return fact

fact = factorial(00)
print(fact)