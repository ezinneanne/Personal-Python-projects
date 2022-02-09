#PersonalPythonProjects No 15
#rock, paper, scissors game

import random

def play():
    user = input("Enter 'r' for rock or\n 'p' for paper or\n 's' for scissors: ")
    computer = random.choice(['r','s','p'])
    
    if user == computer:
        print("It's a tie")
        

    #To check for wins or loses           
    if is_win(user, computer):
        return "You win"
           
    return "You Lose"
    
    

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or(player == 'p' and opponent == 'r'):
        return True
        
        
print(play())