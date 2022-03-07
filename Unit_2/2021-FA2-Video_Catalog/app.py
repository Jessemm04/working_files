from flask import Flask, render_template, request, redirect, flash, session, url_for
from datetime import datetime, date
from flask_wtf import FlaskForm
import sqlite3
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, SelectMultipleField, SelectField, RadioField, widgets
from wtforms.fields.html5 import \
DateField  # see https://stackoverflow.com/questions/26057710/datepickerwidget-with-flask-flask-admin-and-wtforms
from wtforms.validators import DataRequired, URL, Optional, InputRequired

import random

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ddksididkdkdl'

# connect to database
con = sqlite3.connect('videos.db', check_same_thread=False)
con.row_factory = sqlite3.Row
cur = con.cursor()


### Form models ####

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class MultiCheckBoxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class VideoSubmitForm(FlaskForm):
    title = TextAreaField('Title', validators=[DataRequired()])
    link = StringField('URL', validators=[DataRequired(message='You must submit a URL'), URL(message='Not a valid URL')])
    topics = MultiCheckBoxField('Topics', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Submit URL')


########## routes ##########



@app.route('/index', methods=['POST', 'GET'])
def index():
    if session['username']:
        if session['staff_code']:
            sc = session['staff_code']

            sql = """
            select *
            from video_details
            where status = 'A';
            """

            cur.execute(sql,)
            result = cur.fetchall()
            if True:
                session['title'] = result[0][1]
                session['link'] = result[0][2]
                session['date_rg'] = result[0][4]

            sql = """
            select title, video_link, date_submitted
            from video_details
            where video_id in (
                select video_id
                from videos
                where topic_id in (
                    select topic_id
                    from subject_topic
                    where subject_code in (
                        select s.subject_code
                        from staff_classes s, classes c
                        where s.subject_code = c.subject_code
                        and s.staff_code = c.staff_code
                        and s.staff_code = ? )));
            """
            cur.execute(sql,(session['staff_code'],))
            videos = cur.fetchall()
            print(result)


            sql = """
            select *
            from staff_classes
            where staff_code = ?;
            """
            cur.execute(sql, (sc,))
            classsub = cur.fetchall()
            print(classsub)

            return render_template('index.html', title='Index', subclass=classsub, result=video, videos=videos)

        return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            un = form.username.data
            pw = form.password.data

            sql = """
            select *
            from users
            where username = ?
            and password = ?;
            """
            cur.execute(sql, (un, pw))
            result = cur.fetchall()

            if len(result) == 1:
                session['username'] = result[0][0]
                session['password'] = result[0][1]
                session['firstname'] = result[0][2]
                session['lastname'] = result[0][3]
                session['teacher'] = result[0][4]
                if session['teacher']:
                    session['staff_code'] = result[0][5]
                return redirect(url_for('index'))
            else:
                flash('Username or password is incorrect, try again')
        else:
            flash('Something missing... :/')
    return render_template('login.html', title='Login', form=form)


@app.route('/video')
def video():
    if session['username']:
        form = VideoSubmitForm()
        mytopics = []

        sql = """
        select t.topic_id, subject_code, topic_name
        from subject_topic st, topics t
        where t.topic_id = st.to pic_id
        and subject_code in (
            select c.subject_code
            from users u, enrolements e, classes c
            where u.username = e.student_id
            and e.class_id = c.class_id 
            and u.username = ?);
        """

        cur.execute(sql,(session['username'],))
        result = cur.fetchall()
 
        for row in result:
            mytopics.append((row['topic_id'], row['subject_code'] + ' _ ' + row['topic_name']))
        form.topics.choices = mytopics

        #deal with post data
        if request.method == 'POST':
            if form.validate_on_submit():
                print('got data')
                for k,v in form.data.items():
                    print(k,v)

                #deal with data
                title = form.title.data
                link = form.link.data
                date_rg = datetime.datetime.now()
                topics = []

                title = session['title']
                link = session['link']
                date_rg = session['date_rg']
                for v in form.topics.data:
                    form.topics.append(int(v)) # not nessecary

                sql_video = """
                insert
                into video_details (title, link, date_submitted)
                values (?,?,?);
                """

                cur.execute(sql_video, (title, link, date_rg,))
                con.commit()

                video_video_id = cur.lastrowid
                print(video_video_id)

                sql_topics = """
                insert
                into videos(video_id, topic_id)
                values (?,?);
                """
                for topic in video:
                    cur.execute(sql_topics,(video_video_id, topic,))
                con.commit()

        return render_template('video.html', title='video_submit', form=form)

@app.route('/topics', methods=['POST', 'GET'])
def topics():

    return render_template('topics.html', title='topic_videos',)


@app.route('/logout')
def logout():
    if session['username']:
        # clear out the session
        session['username'] = None
        session['firstname'] = None
        session['lastname'] = None
        session['teacher'] = None
        session['staff_code'] = None

        flash("You have successfully logged out")
    return redirect(url_for('index'))

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 8080
    app.run(host, port, debug=True)