import random

def createlist(n):
    mylist = []
    for i in range(n):
        mylist.append(input("enter a name:"))
    return mylist

createlist(int(input("Enter a name: ")
               
def randompicker():
    names = createlist(n)
    idx = random.choice(names)
    return print("Picked name: ", mylist[idx])

