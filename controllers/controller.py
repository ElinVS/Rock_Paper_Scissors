from flask import render_template, request
from app import app
from models.player import Player
import random
#from models.game import 


@app.route('/',)      
def start():
    return render_template('startpage.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/rules')
def explain_game():
    return render_template('rules.html')

@app.route('/play')
def play_game():
    return render_template('play.html')

# player1 = Player("Nadja", "Rock")
# player2 = Player("Aston", "Paper")

# @app.route('')
# def game_played():







    #rock beats scissors
    #paper beats rock
    #scissors beats paper