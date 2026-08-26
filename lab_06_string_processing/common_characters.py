str1 = "I am so good"
str2 = "I am not bad"
concat_string = ""
for j in str2:
    if j in str1:
        concat_string += j

print(concat_string)
