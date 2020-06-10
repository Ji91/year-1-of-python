beatles = []

member1 = input("Enter a member of The Beatles: ")

while member1 != "John Lennon":
    print("Wrong member, Try again.")
    member1 = input("Enter another name: ")
    if member1 == "John Lennon":
        beatles.append("John Lennon")
        print(member1, "is a member of the beatles.")
        print("Members of The Beatles: ", beatles)
if member1 == "John Lennon":
    beatles.append("John Lennon")

member2 = input("Enter a second member of The Beatles: ")

while member2 != "Paul McCartney":
    print("Wrong name, Try again")
    member2 = input("Enter another name: ")
    if member2 == "Paul McCartney":
        beatles.append("Paul McCartney")
        print(member2, "is a member of the beatles.")
        print("Members of The Beatles: ", beatles)
if member2 == "Paul McCartney":
    beatles.append("Paul McCartney")
    
member3 = input("Enter a third member of The Beatles: ")

while member3 != "George Harrison":
    print("Wrong name, Try again")
    member1 = input("Enter another name: ")
    if member3 == "George Harrison":
        beatles.append("George Harrison")
        print(member3, "is a member of the beatles.")
        print("Members of The Beatles: ", beatles)
if member3 == "George Harrison":
    beatles.append("George Harrison")

for members in range(2):
    beatles.append(input("New band member: "))
print("Step 3:", beatles)
 
print("Almost all members of the beatles are here now. Which are: ", beatles)

print("However we need to delete 2 members for Step 4.")
del beatles[-1]
del beatles[-1]
print("Step 4: ", beatles)       
    

key = input("Enter the final member of The Beatles: ")

while key != "Ringo Starr":
    print("Wrong name, try again!")
    key = input("Enter the final member of The Beatles: ")
    if key == "Ringo Starr":
        beatles.insert(0, "Ringo Starr")
        print(key, "is the last member of The Beatles.")
        print(beatles)
if key == "Ringo Starr":
    beatles.insert(0, "Ringo Starr")
    
print("The remaining members are: ", beatles)


print("The remaining ones are: ", len(beatles))


