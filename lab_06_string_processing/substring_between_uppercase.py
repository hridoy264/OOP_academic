str = "amarSonarBangla"
upper_indices = []
for i in range(len(str)):
    if str[i].isupper():
        upper_indices.append(i)
    
first_upper_index = upper_indices[0]
second_upper_index = upper_indices[1]
print(str[first_upper_index+1:second_upper_index])
if len(upper_indices)==0:
    print("BLANK")