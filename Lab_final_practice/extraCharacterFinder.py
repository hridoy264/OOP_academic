word1 = input("Enter a word: ")
word2 = input("Enter another word with an extra character: ")

for i in range(len(word2)):
    extra = 0
    for j in range(len(word1)):
        if word2[i] == word1[j]:
            extra = 1
    if extra == 0:
        print(word2[i])
