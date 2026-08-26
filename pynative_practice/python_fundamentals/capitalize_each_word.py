str = input("Enter a string: ")

words = str.split()
capitalized_words = []
for word in words:
    capitalized_words.append(word.capitalize())

result = " ".join(capitalized_words)
print(result)
