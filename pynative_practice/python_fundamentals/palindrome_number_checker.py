def check_palindrome(number):
    str_num = str(number)
    rev_str = str_num[::-1]

    if str_num == rev_str:
        print("This is a palindrome number")
    else:
        print("This is not a palindrome number")

check_palindrome(123)
check_palindrome(232)