myList = [(number1 = int(input()),number2 = int(input()),number3 = int(input()),number4 = int(input()),number5 = int(input()),number6 = int(input()),number7 = int(input()),number8 = int(input()),number11 = int(input()),number111 = int(input()),number1111 = int(input()),number234 = int(input()),number6234 = int(input()),number2334 = int(input()),number1234 = int(input()),number555 = int(input())] # list to sort
swapped = True # it's a little fake - we need it to enter the while loop

while swapped:
    swapped = False # no swaps so far
    for i in range(len(myList) - 1):
        if myList[i] > myList[i + 1]:
            swapped = True # swap occured!
            myList[i], myList[i + 1] = myList[i + 1], myList[i]

print(myList)
