from flask import Flask, render_template, g, request, flash, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
import json
import os
from Fortnite.Ballers.user import User
from Fortnite.Ballers.DatabaseHelper import DatabaseHelper

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
Bootstrap(app)

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


@app.route('/', methods=('GET', 'POST'))
def index():
    return render_template('index.html', users=get_current_data())


@app.route('/squad', methods=('GET', 'POST'))
def a_team():
    return render_template('ATeam.html', users=get_current_data())


@app.route('/formula', methods=('GET', 'POST'))
def formula():
    return render_template('Formula.html')


@app.route('/watch', methods=('GET', 'POST'))
def watch():
    return render_template('watch.html')


@app.route('/results', methods=('GET', 'POST'))
def results():
    return render_template('season4.html', users=get_season_four_data())


@app.route('/user', methods=('GET', 'POST'))
def user():
    username = request.args.get('username')
    params = []
    users = get_current_data()
    for item in users:
        if item.name == username:
            params.append(item)
    return render_template('user.html', users=params)


@app.route('/store', methods=['GET'])
def store():
    return render_template('store.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/')
    return render_template('signin.html', title='Sign In', form=form)


def get_config():
    with open(os.path.join(__location__, 'config.json')) as f:
        data = json.load(f)
    return data


def get_current_data():
    dbh = DatabaseHelper()
    user_ids = dbh.get_all_user_ids()
    users = []
    for user_id in user_ids:
        my_user = dbh.get_user(user_id)
        users.append(my_user)
    return sorted(users, key=lambda k: k.stats.wcpi_score)[::-1]


def get_season_four_data():
    dbh = DatabaseHelper()
    users = []
    temp = dbh.get_season_four()
    for my_user in temp:
        if my_user.stats is not None:
            users.append(my_user)
    return sorted(users, key=lambda k: k.stats.wcpi_score)[::-1]


# Login form
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


if __name__ == '__main__':
    app.run(debug=False)
