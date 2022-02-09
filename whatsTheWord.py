#PersonalPythonProjects No 14
#What's the word'

import random

list = ["Ezinne","loves","coding","but","she","is","laptopless"]

guess_limit = 5
out_of_guesses = False

guesses = random.choice(list)

while guess_limit > 0:
    user = input("Guess the word: ")
    if user in guesses:
        print(guesses)
        print(list.index(guesses))
        print(user)
        guess_limit -=1
    elif user not in guesses and user in list:
        print("Wrong guess, but it is in the list")
        print(guesses)
        print("Try again")
        guess_limit -=1
    else:
        print("Wrong guess, it is not in the list either")
        print(guesses)
        print(list.index(guesses))
        guess_limit -=1
        
out_of_guesses = True

