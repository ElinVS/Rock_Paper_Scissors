
import random


def computers_choice():
    rps =["rock", "paper", "scissors"]
    return rps[random.choice(rps)]

def player_vs_computer(player, computer):
    winner = "computer"

    if player == "rock" and computer == "paper":
        if player == "paper" and computer == "scissors":
            if player == "scissors" and computer == "rock":
                winner = "computer"

    if player == "rock" and computer == "scissors":
        if player == "paper" and computer == "rock":
            if player == "scissors" and computer == "paper":
                winner = "player"

    if player == computer :
        winner = "It's a tie. Play again!"
    

    return winner




    




        
        












# - Write a game class that has a function that takes in the 2 players and compares their choices and returns the winning player. If it is a draw the player should be `None` type.

