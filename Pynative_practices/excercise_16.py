# Numerical Palindrome Check


def palindrome_checker(n):
    n = str(n)
    rev = n[::-1]
    if n == rev:
        print("This is palindrome")
    else: 
        print("This is not palindrome")

palindrome_checker(212)
palindrome_checker(123)