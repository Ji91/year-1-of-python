import random

keep_running = True
word_list = []
while keep_running == True:
    user_input = input("enter a name or type 0 to stop: ")
    if user_input == "0":
        keep_running = False
    else:
        word_list.append(user_input)

name_picked = random.choice(word_list)

print(name_picked)
