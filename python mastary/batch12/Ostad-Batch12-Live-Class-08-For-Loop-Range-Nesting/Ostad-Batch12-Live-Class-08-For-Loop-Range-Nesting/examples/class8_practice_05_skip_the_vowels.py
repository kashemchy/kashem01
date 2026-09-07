word = "Bangladesh"
vowels = "aeiouAEIOU"

for letter in word:
    if letter in vowels:
        continue
    print(letter, end=" ")
print()
