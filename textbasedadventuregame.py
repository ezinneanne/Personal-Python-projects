#My Personal Projects
#project no 3 - text based adventure game


import time


def play_again():
    
    while True:
        
        user_play = input("Do you want to play again: ")
        user_play = user_play.lower()
        if user_play == "yes":
            start()
        elif user_play == "no":
            return False
        else:
            print("OMG, you're so pathetic")
            return False
            
              

def game_over():
    print("You lose!!!")
    print("GAME OVER!!!")
    
    play_again()



def diamond_room():
    print()
    print("loading....")
    time.sleep(2)
    print("Welcome to the diamond room ! ")
    time.sleep(2)
    
    print("You have two options, choose wisely!")
    time.sleep(5)
    
    user_diamondrm = input("Choose (1) if  you want to pick the diamonds or (2) if you want to go outside: ")
    if user_diamondrm == "1":
        print("You win! Congratulations!!!")
        play_again()
    elif user_diamondrm == "2":
        print("You have fallen into a very deep pit")
        print("Now you are eaten by snakes and scorpions!!!")
        game_over()
    else:
        print("Guess you were not properly schooled on how to type in a number")
        game_over()



def bear_room():
    print()
    print("loading.....")
    time.sleep(2)
    
    print("You have entered the bear room !")
    time.sleep(3)
    
    print("The bear has gone hunting, lucky you! ")
    time.sleep(3)
    
    print("There are pieces of diamonds in front of you")
    time.sleep(4)
    
    user_bearoom = input("Choose (1) if you want to pick pieces of diamonds or (2) if you want to go and search for the whole bag of diamonds: ")
    
    if user_bearoom == "1":
        print("Now, the bear has eaten you up")
        game_over()
    elif user_bearoom == "2":
        print("Goodluck on your search for the diamonds")
        diamond_room()
        
    else:
        print("You don't know how to type a number! Really?! ")
        game_over()


def monster_room():
    print()
    print("loading....")
    time.sleep(2)
    
    print("You have entered the monster room")
    
    time.sleep(1)
    print("The monster is sleeping, if you want to live, then do not disturb the monster")
    time.sleep(4)
    
    print("There are two doors, one leads to outside and it's already open but the other door leads you to the diamond room")
    time.sleep(5)
    
    user_monsteroom = input("Choose (1) if you want to use the outside door or (2) if you want to use the diamond room: ")
        
    if user_monsteroom == "1":
        print("Hurray! you made it to the diamond room")
        diamond_room()
    elif user_monsteroom == "2":
        print("You woke up the monster with the door noise and now you have been eaten")
        game_over()
    else:
        print("You don't know how to type again?: ")
        game_over()


def start():
    print("You started to play the adventure game")
    time.sleep(1)
    print("In this game, you are expected to make some options that will lead you to winning the price, which is the diamonds")
    time.sleep(4)
    print("Goodluck to you!")
    time.sleep(1)
    user = input("Do you want to go right or left ?: ")
    user = user.lower()
    if user == "right":
        monster_room()
    elif user == "left":
        bear_room()
    else:
        print("Please type in either 'right' or 'left': ")
        game_over()
        
        
        
start()

        
        