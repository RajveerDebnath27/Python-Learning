text = "Hello World"

def count_vowels(word):
    word = word.lower()
    if not word:
        return 0
    vowels = "aeiou"
    if word[0] in vowels:
        return 1 + count_vowels(word[1:])
    else:
        return 0 + count_vowels(word[1:])


print(count_vowels(text))