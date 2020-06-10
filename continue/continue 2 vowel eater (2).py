userWord = input("Enter a word: ")
userWord = userWord.upper()

for letter in userWord:
    if letter in ("aeiouAEIOU"):
        continue
    print(letter)
