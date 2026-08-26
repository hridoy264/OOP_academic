

user_input = input("What is your name?")

a = "Good Morning, {}. How are you?".format(user_input)
print(user_input)
print(a)

age = 25
f_name = "Shahnewaj"
l_name = "Hridoy"

txt = "I am {f_name} {l_name}. I am {age} years old.".format(l_name=l_name, f_name=f_name, age = age)
print(txt)
txt2 = f"I am {f_name} {l_name}. I am {age} years old."
print(txt2)