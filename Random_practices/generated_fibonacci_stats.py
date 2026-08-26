def generate_fibonacci_stats(n):
    fibonacci_list = []
    for i in range(n):
        if i == 0:
            fibonacci_list.append(1)
        elif i == 1:
            fibonacci_list.append(1)
        else:
            fibonacci_list.append(fibonacci_list[-1]+fibonacci_list[-2])

    fib_tuple = tuple(fibonacci_list)
    fib_sum = sum(fib_tuple)

    print(f"fibonacci tuple: {fib_tuple}")
    print(f"Total value sum: {fib_sum}")

generate_fibonacci_stats(10)