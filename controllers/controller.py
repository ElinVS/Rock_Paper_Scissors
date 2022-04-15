from flask import render_template 
from app import app
from models.player import Player
#from models.game import 


@app.route('/',)      
def home():
    return render_template('startpage.html')

@app.route('/home')
def welcome():
    return render_template('home.html')

@app.route('/rules')
def explain_game():
    return render_template('rules.html')

@app.route('/play')
def play_game():
    return render_template('play.html')

# player1 = Player("Nadja", "Rock")
# player2 = Player("Aston", "Paper")

# @app.route('/<player1_choice>/<player2_choice>')
# def 






    #rock beats scissors
    #paper beats rock
    #scissors beats paper