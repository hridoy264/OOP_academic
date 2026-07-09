# scope --> area or region, where a variable is accessible
x = 10      # global variable

print(x)
def func():
    y = 19  # local variable
    x = 200

    print(x)
func()
# print(y)
print(x)

#   LEGB rule
# L - Local 
# E - Enclosing
# G - Global 
# B - Builtin scope     (print, sum, max, input)

n = "global"     # Global variable

def outer():
    n = "enclosing"          # Enclosing variable
    def inner():
        # global n         # global --> just global variable ke update kore
        nonlocal n         # nonlocal --> enclosing ke change korte pare, not global  
        n = "local"      # Local variable
        print(n)
    inner()
    print(n)
outer()
print(n)