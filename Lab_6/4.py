str = "AmaarEDG"
upper_counter = 0
lower_counter = 0

for i in str:
    if i.isupper():
        upper_counter+=1
    else:
        lower_counter+=1

if upper_counter>lower_counter:
    print(str.upper())
else:
    print(str.lower())
