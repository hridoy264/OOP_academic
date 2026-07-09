password = "mar123@"

lowercase = 0
uppercase = 0
digit = 0
special = 0

for i in password:
    if i>='A' and i<'Z':
        uppercase = 1
    elif i>='a' and i<'z':
        lowercase = 1
    elif i>='0' and i<='9':
        digit = 1
    elif i == '@' or i == '#' or i == '$' or i == '_':
        special = 1

if uppercase == 0: print("Uppercase missing!")
if lowercase == 0: print("Lowercase missing!")
if digit == 0: print("Digit missing!")
if special == 0: print("Special character is missing")
if uppercase == 1 and lowercase == 1 and digit == 1 and special == 1: print('OK')