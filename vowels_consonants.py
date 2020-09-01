word = list(input().lower())
vowel = ['a', 'e', 'i', 'o', 'u']

for i, _ in enumerate(word):
    if word[i] in vowel:
        print("vowel")
    elif word[i].isalpha() and word[i] not in vowel:
        print("consonant")
    else:
        exit()

