from flask import Flask, render_template, request, session, flash

import random

app = Flask(__name__)

app.config['SECRET_KEY'] = 'key'

def check_win(player):
    result = False
    r = 0
    p = 1
    s = 2
    sp = 3
    l = 4
    player_choice = session['pb'][r][p][s][l][sp]
    computer_choice = random.choice(player_choice)
    a = player_choice
    b = computer_choice
    d = (5 + a - b) % 5
    if d == 1 or d == 3:
        result = True
    if d == 2 or d == 4:
        result = False
    if d == 0:
        result = 0
    return result

@app.route("/")
def index():
    player_score = 0
    computer_score = 0
    session['board'] = [[' '], [' ', ' ', ' ', ' ', ' ']]
    if request.args.get('r') and request.args.get('p') and request.args.get('s') and request.args.get('l') and request.args.get('sp'):
        r = int(request.args.get('r'))
        p = int(request.args.get('p'))
        s = int(request.args.get('s'))
        l = int(request.args.get('l'))
        sp = int(request.args.get('sp'))

        session['pb'][r][p][s][l][sp] = ' '
        comp_choice = random.choice(session['board'][r][p][s][l][sp])
        #check if won
        #make it out of 3 rounds
        for i in range(3):
            r = check_win('pb')
            # if won
            if r is True:
                player_score += 1
                computer_score -= 1
                flash('Congrats you won!!')
                session['gameon'] = False
            if r is False:
                player_score -= 1
                computer_score += 1
                flash('You lost. Computer won')
                session['gameon'] = False
            if r is 0:
                player_score += 0
                computer_score += 0
                flash('You tied!')
                session['gameon'] = False
            print(player_score)
            print(computer_score)
            session['pb'][r][p][s][l][sp] = ' '


    # otherwise start new game
    else:
        score = 0
        session.pop('board')
        session['board'] = [[' '], [' ', ' ', ' ', ' ', ' ']]
        session['gameon'] = True
        flash('New game started!')
    session['board'] = session['board']
    return render_template('rpsls.html', board=session['board'], gameon=session['gameon'])


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 5000
    app.run(host, port, debug=True)