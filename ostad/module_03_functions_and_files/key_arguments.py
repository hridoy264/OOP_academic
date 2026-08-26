# def my_func(f_name, l_name, age):
#     print(f"My name is {f_name} {l_name}. I am {age} years old.")

# my_func("Rahim", "Khan", 25)
# my_func(age = 25, f_name="Rahim", l_name="Khan")

# Arbitrary number of key word arguments
def my_func(**kwargs):      # **data dileo kaj korbe
    print(kwargs)
    print(f"My name is {kwargs['f_name']} {kwargs['l_name']}. I am {kwargs['age']} years old. ")
    print(kwargs['marks'])
    # print(f"My name is {f_name} {l_name}. I am {age} years old.")

# my_func("Rahim", "Khan", 25)
my_func(age = 25, f_name="Rahim", marks = 95, l_name="Khan")