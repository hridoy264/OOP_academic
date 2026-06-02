#Vowel Frequency Counter
a = 0
e = 0 
ai = 0
o = 0
u = 0
text = "My name is Shahnewaj Hridoy"

for i in range(0, len(text)):
    if text[i] == 'a':
        a += 1
    elif text[i] =='e':
        e += 1
    elif text[i] == 'i':
        ai += 1
    elif text[i] == 'o':
        o += 1
    elif text[i] == 'u':
        u += 1
    else:
        continue
print(f"a: {a}, e: {e}, i: {ai}, o: {o}, u: {u}")