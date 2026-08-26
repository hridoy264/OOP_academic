string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

def return_additional_char(string1, string2):
    set1 = set(string1)
    set2 = set(string2)
    print("This is the additional letter: ", set2.difference(set1))
    
return_additional_char(string1, string2)