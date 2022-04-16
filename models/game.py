
import random


def computers_choice():
    rps =["rock", "paper", "scissors"]
    return rps[random.randrange(0,3)]

def player_vs_computer(player, computer):
    
    if player == computer :
        winner = "tie"
        

    elif player == "rock" and computer == "paper":
        if player == "paper" and computer == "scissors":
            if player == "scissors" and computer == "rock":
                winner = "computer"

    elif player == "rock" and computer == "scissors":
        if player == "paper" and computer == "rock":
            if player == "scissors" and computer == "paper":
                winner = "player"

    
        return winner




    




        
        












# - Write a game class that has a function that takes in the 2 players and compares their choices and returns the winning player. If it is a draw the player should be `None` type.

