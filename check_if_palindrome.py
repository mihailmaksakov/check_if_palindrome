def is_polindrome(word):
    return word == word[::-1]


word = "tenet"
print(word, is_polindrome(word.lower()))