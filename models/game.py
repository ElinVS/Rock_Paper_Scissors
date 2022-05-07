
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
    winner = computer.name

    if player.choice == computer.choice:
        winner = "No one"
    if player.choice == "rock" and computer.choice == "scissors":
        winner = player.name
    if player.choice == "scissors" and computer.choice == "paper":
        winner = player.name
    if player.choice == "paper" and computer.choice == "rock":
        winner = player.name

    return winner





