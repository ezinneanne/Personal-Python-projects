#My personal projects
#project no 4 - dice rolling simulator

from random import randint

print("Welcome to the Dice Rolling Simulator game 🎲")

count = 0

for i in range(6):
    i = randint(1,6)

    user = input("Choose (1) to roll the dice or (2) to end the game: ")
    if user == "1":
        print("loading...")
        print("rolling the dice...")
        print(i)
        print(f"You got {i}")
        count +=1
    elif user == "2":
        break
    else:
        print("You don't know how to type a number")
        break
       
print(f"You have played {count} times")