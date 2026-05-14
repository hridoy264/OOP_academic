# Integer Digit Extraction and Reversal

def reverse_seperate(n):
    while n != 0:
        print(n%10 , end = " ")
        n = n//10
    print()
reverse_seperate(123456)