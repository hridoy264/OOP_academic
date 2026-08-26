n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))

def multiplication_or_sum(num1, num2):
    product = num1*num2

    if(product<=1000):
        return product
    else:
        return num1+num2
    
result = multiplication_or_sum(n1, n2)
print("The result is : ", result)