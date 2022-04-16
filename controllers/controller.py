from flask import render_template, request
from app import app
from models.game import computers_choice
from models.player import Player
import random
from models.game import player_vs_computer 


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

@app.route ('/results', methods=['POST'])
def show_outcome():
    print(request.form)
    player_name = request.form["name"]
    player_choice = request.form["choice"]
    new_player = Player(player_name, player_choice)
    computer = computers_choice()

    player_vs_computer(new_player,computer) 

    return render_template('results.html')
