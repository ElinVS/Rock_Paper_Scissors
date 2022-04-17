
import random

#mvp##################################################################

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


#extension############################################################

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

