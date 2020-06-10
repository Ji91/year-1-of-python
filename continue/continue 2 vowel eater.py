userWord = input("Enter a word: ")
userWord = userWord.upper()
counter = 0

for letter in userWord:
    if letter in ("aeiouAEIOU"):
        continue
    
    counter += 1
    print(letter)
    
userWord = input("Enter a word: ")
for letter in userWord:
    if letter in ("aeiouAEIOU"):
        continue
    print(letter)

