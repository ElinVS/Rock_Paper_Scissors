
from flask import render_template, request
from app import app
from models.game import computers_choice, play_the_game 
from models.player import Player
from models.game import player_vs_computer 


@app.route('/')      
def start():
    return render_template('startpage.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/rock')
def rock():
    return render_template('rock.html')

@app.route('/paper')
def paper():
    return render_template('paper.html')

@app.route('/scissors')
def scissors():
    return render_template('scissors.html')

@app.route('/rules')
def explain_game():
    return render_template('rules.html')

@app.route('/play')
def play_game():
    return render_template('play.html')

@app.route('/<player1_choice>/<player2_choice>')
def game(player1_choice,player2_choice):
    Batman = Player("Batman", player1_choice)
    Superman = Player("Superman", player2_choice)
    winner = play_the_game(player1_choice,player2_choice)

    return render_template('browsergame.html', winner = winner, Batman = "Batman", player1_choice = player1_choice, Superman ="Superman", player2_choice = player2_choice)


######################################################################


@app.route ('/results',methods=['POST'] )
def show_outcome():
    

    player_name = request.form["name"]
    player_choice = request.form["choice"]
    player = Player(player_name, player_choice) 
    choice = computers_choice()
    computer = Player("Computer", choice )
    
    winner = player_vs_computer(player, computer)

    return render_template('results.html',computer = computer, player = player,  winner = winner)
