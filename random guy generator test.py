import random
import sys

first = []

while True:
    answer = input('Enter a name:')
    if answer.lower().startswith("y"):
        first.append(answer)
        print("ok go on...")
    elif answer.lower().startswith("n"):
        print("ok, sayonnara")
        first1 = random.choice(first)
        print(first1)
        print(first)
        break 
