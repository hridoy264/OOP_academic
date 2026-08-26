def generate_fibonacci(number):
    j = 0 
    k = 1 
    for i in range(1, number+1):
        print(j, end= " ")
        j, k = k, j+k

generate_fibonacci(20)