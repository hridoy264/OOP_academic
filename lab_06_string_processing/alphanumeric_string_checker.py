something = '123ssdf'
flag = []

for i in something:
    if i>='a' and i<='z':
        flag.append(0)
    elif i>='A' and i<='Z':
        flag.append(0)
    elif i>='1' and i<='9':
        flag.append(1)
    
seet = set(flag)

if len(seet)==2:
    print("MIXED")
elif len(seet)==1:
    if flag[0] == 0:
        print("WORD")
    else:
        print("NUMBER")
else:
    print("INVALID INPUT!")
