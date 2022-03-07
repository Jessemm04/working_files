from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, SelectMultipleField, widgets, SelectField, HiddenField, RadioField
from wtforms.fields.html5 import DateField # see https://stackoverflow.com/questions/26057710/datepickerwidget-with-flask-flask-admin-and-wtforms
from wtforms.validators import DataRequired, URL, Optional, ValidationError, NumberRange, Length, Email, EqualTo #need to install email validator separately
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
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
    age = StringField('Age', validators=[DataRequired(), NumberRange(min=16)])
    sex = RadioField('Sex', choices=['m', 'f'], validators=[DataRequired()])
    earns = StringField('Earns', validators=[DataRequired()])
    likes = StringField('Likes', validators=[Optional()])
    dislikes = StringField('Dislikes', validators=[Optional()])
    submit = SubmitField('SUBMIT!!!!')

class LoginForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
    age = StringField('Age', validators=[DataRequired(), NumberRange(min=16)])
    submit = SubmitField('Login')


@app.route("/", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            name = form.name.data
            age = form.age.data

            sql = """
            select *
            from people
            where name = ?
            and age = ?;
            """

            try:
                cur.execute(sql, (name, age))
                results = cur.fetchone()
            except:
                flash('Error')
            if len(results) == 0:
                flash('Incorrect Email or password!')
                redirect('index')
            else:
                flash('login successful. Welcome back!')
                session['name'] = name
                session['age'] = age
                session['sex'] = sex
                session['earns'] = earns
    #return render_template("index.html", form=form)
@app.route("/logout")
def logout():
    if session['name']:
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
    if request.method == 'POST':
        if form.validate_on_submit():
            name = form.name.data
            age = form.age.data
            sex = form.sex.data
            earns = form.earns.data
            likes = form.likes.data
            dislikes = form.dislikes.data

            sql = """
            insert
            into members (name, age, sex, earns, likes, dislikes)
            values (?,?,?,?,?,?);
            """
            try:
                cur.execute(sql, (name, age, sex, earns, likes, dislikes))
                con.commit()
            except:
                flash('Oops... Something went wrong! Check the values, and try again')
            else:
                flash('Account Registered Successfully')
                session['name'] = name
                session['age'] = age
                session['sex'] = sex
                session['earns'] = earns
                return redirect(url_for('index'))

    return render_template('signup_people.html', form=form)
#########################################################################
if __name__ == '__main__':
    host = '127.0.0.1'
    port = 5000
    app.run(host, port, debug=True)