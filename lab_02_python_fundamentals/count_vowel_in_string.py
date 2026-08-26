word = input("Enter a string: ")
vowel_count = 0
print(len(word))
for i in range(0, len(word)):
    if(word[i] == 'a' or word[i] == 'e' or word[i] == 'i' or word[i] == 'o' or word[i] == 'u'):
        vowel_count += 1

print(f"Total vowel in your string is {vowel_count}")

