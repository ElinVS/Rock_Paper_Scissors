
import random


def play_the_game(player1,player2):
    
    if player1 == player2:
        return "no one"

    if player1 == "rock" and player2 == "paper":
        return "Superman"

    if player1 == "paper" and player2 == "scissors":
        return "Superman"

    if player1 == "scissors" and player2 == "rock":
        return "Superman"

    if player1 == "rock" and player2 == "scissors":
        return "Batman"
    
    if player1 == "paper" and player2 == "rock":
        return "Batman"
    
    if player1 == "scissors" and player2 == "paper":
        return "Batman"




def computers_choice():
    rps =["rock", "paper", "scissors"]
    return rps[random.randint(0,2)]


def player_vs_computer(player, computer):
    winner = "computer"

    if player == computer:
        winner = "draw"
    if player == "rock" and computer == "scissors":
        winner = "player"
    if player == "scissors" and computer == "paper":
        winner = "player"
    if player == "paper" and computer == "rock":
        winner = "player"

    return winner





















    
    # if player == computer :
    #     winner = "tie"
        
    # if player == "rock" and computer == "paper":
    #     if player == "paper" and computer == "scissors":
    #         if player == "scissors" and computer == "rock":
    #             winner = "computer"

    # if player == "rock" and computer == "scissors":
    #     if player == "paper" and computer == "rock":
    #         if player == "scissors" and computer == "paper":
    #             winner = "player"

    #     return winner




    




        
        












# - Write a game class that has a function that takes in the 2 players and compares their choices and returns the winning player. If it is a draw the player should be `None` type.

