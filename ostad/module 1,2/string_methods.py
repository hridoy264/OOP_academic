a = "shahnewaj"
# python immutable, so amader jor kore change korte hbe

print(a.title())
print(a)
# ami main string er konorokom change kortesina. Hazaro method ami er upor apply korte pari kintu main jinish same
a = a.title()
print(a)
print(a.upper())
print(a.lower())
# replace("konta ke change korbo", "oitar jaygay ki bosabo")
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)
print(txt.count("a"))
print(len(txt))