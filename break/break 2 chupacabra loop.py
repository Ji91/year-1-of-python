word = input("Enter a word: ")

while word != "chupacabra":
    print("Wrong word!!")
    word = input("Enter a word: ")
    if word == "chupacabra":
        break
print("You've successfully left the loop.")
    
