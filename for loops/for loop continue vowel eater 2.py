userWord = input("Enter a word: ")
userWord = userWord.upper()

new_char = "" 
for letter in userWord:
    if letter in ("aeiouAEIOU"):
        continue
    new_char += letter

print(new_char)
    
