import secrets
from random import randint

from flask import Flask, render_template, url_for, session, redirect

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)


@app.route('/')
def base():
    return render_template('base.html')


@app.route('/start')
def start():
    session.pop('sticks', None)
    session['sticks'] = 21
    return render_template('start.html')


@app.route('/take/<int:stick_number>/')
def take(stick_number):
    if stick_number in range(1, 4):

        sticks_from_prev_turn = session['sticks']
        session['sticks'] = session.get('sticks') - stick_number
        sticks_after_human = session['sticks']
        if sticks_after_human == 0:
            return render_template('win.html', win='Computer')
        # Ход компьютера
        comp_stick = randint(1, 3)
        if session['sticks'] == 2 and comp_stick > 2:
            comp_stick = randint(1, 2)
        if session['sticks'] == 1:
            comp_stick = 1
        session['sticks'] = session.get('sticks') - comp_stick
        sticks_after_cpu = session['sticks']
        if sticks_after_cpu == 0:
            return render_template('win.html', win='Player')
        ###
        else:
            return render_template('take_x.html', stics_on_table=sticks_from_prev_turn,
                                   sticks_after_h=sticks_after_human,
                                   stick_number=stick_number, comp_stick=comp_stick, sticks_after_cpu=sticks_after_cpu)
    else:
        session.pop('sticks', None)
        return redirect(url_for('error'))


@app.route('/error')
def error():
    return render_template('error.html')
