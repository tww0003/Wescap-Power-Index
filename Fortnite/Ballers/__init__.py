from flask import Flask, render_template, g, request
from flask_bootstrap import Bootstrap
import pymysql.cursors
import json
import os

app = Flask(__name__)
Bootstrap(app)

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


@app.route('/', methods=('GET', 'POST'))
def index():
    return render_template('index.html', json=get_better_data())


@app.route('/squad', methods=('GET', 'POST'))
def a_team():
    return render_template('ATeam.html', json=get_better_data())


@app.route('/formula', methods=('GET', 'POST'))
def formula():
    return render_template('Formula.html')


@app.route('/watch', methods=('GET', 'POST'))
def watch():
    return render_template('watch.html')


@app.route('/results', methods=('GET', 'POST'))
def results():
    return render_template('season4.html', json=get_season4())


@app.route('/user', methods=('GET', 'POST'))
def user():
    username = request.args.get('username')
    params = []
    json = get_better_data()
    for item in json:
        if item['name'] == username:
            params.append(item)
    return render_template('user.html', json=params)


@app.route('/store', methods=['GET'])
def store():
    return render_template('store.html')


def get_season4():
    new_result = None
    data = get_config()
    host = data['host']
    db_user = data['user']
    passwd = data['password']
    db = data['db']
    try:
        connection = pymysql.connect(host=host,
                                     user=db_user,
                                     password=passwd,
                                     db=db,
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `*` FROM `stats` where `season` = %s order by id desc limit 11"
            season = 4
            cursor.execute(sql, season)
            result = cursor.fetchall()

    finally:
        print('Resutls fetched')

    try:
        new_result = []
        for item in result:
            user_id = item['user_id']
            with connection.cursor() as cursor:
                temp_dict = item
                # Read a single record
                sql = "SELECT `*` FROM `user` where `user_id` = %s"
                cursor.execute(sql, (user_id,))
                temp = cursor.fetchone()
                temp_dict['name'] = temp['name']
                temp_dict['gamer_tag'] = temp['gamertag']
                solo_wins = temp_dict['solo_wins']
                duo_wins = temp_dict['duo_wins']
                squad_wins = temp_dict['squad_wins']
                temp_dict['total_wins'] = int(solo_wins) + int(duo_wins) + int(squad_wins)
                solo_matches = temp_dict['solo_matches']
                duo_matches = temp_dict['duo_matches']
                squad_matches = temp_dict['squad_matches']
                temp_dict['matches'] = int(solo_matches) + int(duo_matches) + int(squad_matches)
                new_result.append(temp_dict)
    finally:
        connection.close()
        return sorted(new_result, key=lambda k: k['wcpi_score'])[::-1]


def get_better_data():
    the_results = None
    data = get_config()
    host = data['host']
    db_user = data['user']
    passwd = data['password']
    db = data['db']

    try:
        connection = pymysql.connect(host=host,
                                     user=db_user,
                                     password=passwd,
                                     db=db,
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `*` FROM `user`"
            cursor.execute(sql, )
            result = cursor.fetchall()
            the_results = []
            for item in result:
                sql = 'select * from stats where user_id = ' + str(item['user_id']) + ' order by id desc limit 1'
                cursor.execute(sql, )
                meh = cursor.fetchall()
                meh[0]['name'] = item['name']
                meh[0]['gamer_tag'] = item['gamertag']
                meh[0]['matches'] = int(meh[0]['solo_matches']) + int(meh[0]['duo_matches']) + int(meh[0]['squad_matches'])
                meh[0]['total_wins'] = int(meh[0]['solo_wins']) + int(meh[0]['duo_wins']) + int(meh[0]['squad_wins'])
                the_results.append(meh[0])
    finally:
        connection.close()
        return sorted(the_results, key=lambda k: k['wcpi_score'])[::-1]


def get_config():
    with open(os.path.join(__location__, 'config.json')) as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    app.run(debug=False)
