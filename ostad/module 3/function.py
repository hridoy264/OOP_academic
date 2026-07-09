# 2 types

#1. User defined function --> Programmer nijer moto kore ekta function banabe

# 2. Built in function --> already banano ache

# Print(), input(), sum()

# print("Hello")  # ---> box er moddher juice (nije ar kichu poriborton korte parbona)
#  user_name = input("Enter your name: ") # glass er juice, return kore
# print(f"Hello {user_name*2}")


mx = max([1, 2, 3, 4])
print(f"max value {mx}. {mx*3}")

# User defined function

# 1. No input, No return 

def my_first_function():   # function definition
    a = 10 
    b = 12
    print(a+b)

my_first_function()     # function call kora

# 2. Input, no return 

def add_two_number(a, b):       #argument
    print(a+b)

add_two_number(12, 23)  #parameters


# 3. input, return 

def multiply_two_nums(a, b):
    return a*b
result = multiply_two_nums(12, 2)
print(result)

# 4. No input, return 

def hello():
    return "Hello"
greetings = hello()
print(greetings)
