from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, SelectMultipleField, widgets, SelectField, HiddenField, RadioField
from wtforms.fields.html5 import DateField # see https://stackoverflow.com/questions/26057710/datepickerwidget-with-flask-flask-admin-and-wtforms
from wtforms.validators import DataRequired, URL, Optional, ValidationError, Length, Email, EqualTo #need to install email validator separately
import random  # needed for random number generation
import sqlite3
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = "myverysecretkey"

#connect to the database
con = sqlite3.connect("signup.db", check_same_thread=False)
con.row_factory = sqlite3.Row

#create a cursor/pointer to navigate the database
cur = con.cursor()

#create the forms for use
class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=16)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    year_level = SelectField('Year Level', validators=[DataRequired()])
    house = RadioField('House', choices=['Mitre', 'Scudo', 'Boek', 'Taja', 'Gladius'], validators=[DataRequired()])
    submit = SubmitField('SUBMIT!!!!')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')



@app.route("/", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            email = form.email.data
            password = form.password.data

            sql = """
            select *
            from users
            where email = ?
            and password = ?;
            """

            try:
                cur.execute(sql, (email, password))
                results = cur.fetchone()
            except:
                flash('Error')
            if len(results) == 0:
                flash('Incorrect Email or password!')
                redirect('index')
            else:
                flash('login successful. Welcome back!')
                session['username'] = username
                session['email'] = email
                session['year'] = year
                session['house'] = house
    #return render_template("index.html", form=form)
@app.route("/logout")
def logout():
    if session['username']:
        for key, value in session.items():
            if key != 'csrf_token':
                session[key] = None
        flash('You have been logged out')
    else:
        flash('You must be looged in first')
    return redirect(url_for("index"))

#create the routes
@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    yearlevels = []
    for x in range(7, 13):
        option = (x, 'year' + str(x))
        yearlevels.append(option)

    form.year_level.choices = yearlevels
    if request.method == 'POST':
        if form.validate_on_submit():
            uname = form.username.data
            email = form.email.data
            passwd = form.password.data
            year = form.year_level.data
            house = form.house.data
            date_rg = datetime.datetime.now()

            sql = """
            insert
            into users (username, email, password, year, house, date_registered)
            values (?,?,?,?,?,?);
            """
            try:
                cur.execute(sql,(uname, email, passwd, year, house, date_rg))
                con.commit()
            except:
                flash('Oops... Something went wrong! Check the values, and try again')
            else:
                flash('Account Registered Successfully')
                session['username'] = uname
                session['email'] = email
                session['year'] = year
                session['house'] = house
                return redirect(url_for('index'))

    return render_template('signup.html', form=form)
#########################################################################
if __name__ == '__main__':
    host = '127.0.0.1'
    port = 5000
    app.run(host, port, debug=True)