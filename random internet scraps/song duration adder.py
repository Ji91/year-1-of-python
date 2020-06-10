songs = []
total = 0

minutes = input("Input minutes: ") * 60
seconds = input("Input seconds: ")
time = minutes + seconds
songs.append(time)

for x in range(10):
    minutes = input("Input minutes: ") * 60
    seconds = input("Input seconds: ")
    time = minutes + seconds
    songs.append(time)
print(songs)
total += x
   # if x == "stop":
        #print(songs)
        #for i in songs:
        #    total += songs[i]
        #print(total)
