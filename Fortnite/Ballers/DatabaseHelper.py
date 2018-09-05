import json
import os
import pymysql.cursors
from Fortnite.Ballers.user import User
from Fortnite.Ballers.stats import Stats

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


class DatabaseHelper:

    def __init__(self):
        data = get_config()
        self.host = data['host']
        self.db_user = data['user']
        self.passwd = data['password']
        self.db = data['db']
        self.connection = pymysql.connect(host=self.host,
                                          user=self.db_user,
                                          password=self.passwd,
                                          db=self.db,
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)

    def get_all_user_ids(self):
        sql = 'select user_id from user'
        ids = []
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql,)
                result = cursor.fetchall()
                for item in result:
                    ids.append(item['user_id'])
        finally:
            return ids

    def get_user(self, user_id, season=None):
        sql = 'select * from user where user_id = %s'
        my_user = None
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql, (user_id,))
                result = cursor.fetchone()
                my_user = User(user_id=result['user_id'], name=result['name'], gamertag=result['gamertag'],
                               epic_account=result['epic_account'], platform=['platform'],
                               password_hash=result['password_hash'], email=result['email'])
            if my_user is not None and season is not None:
                my_user.stats = self.get_stats(user_id=user_id, season=season)
            elif my_user is not None:
                my_user.stats = self.get_stats(user_id)
        finally:
            return my_user

    def get_stats(self, user_id=None, season=None):
        if season is not None:
            sql = 'SELECT `*` FROM `stats` where `user_id` = %s AND `season` = %s order by id desc limit 1'
        else:
            sql = 'select * from stats where user_id = %s order by id desc limit 1'
        my_stats = None
        try:
            with self.connection.cursor() as cursor:
                if season is not None:
                    cursor.execute(sql, (user_id, season))
                else:
                    cursor.execute(sql, (user_id,))
                result = cursor.fetchone()
                my_stats = Stats(stat_id=result['id'], solo_kpg=result['solo_kpg'], duo_kpg=result['duo_kpg'],
                                 squad_kpg=result['squad_kpg'], solo_matches=result['solo_matches'],
                                 duo_matches=result['duo_matches'], squad_matches=result['squad_matches'],
                                 solo_wins=result['solo_wins'], duo_wins=result['duo_wins'],
                                 squad_wins=result['squad_wins'], solo_win_percentage=result['solo_win_percentage'],
                                 duo_win_percentage=result['duo_win_percentage'],
                                 squad_win_percentage=result['squad_win_percentage'],
                                 wcpi_score=result['wcpi_score'], user_id=user_id, date=result['date'],
                                 season=result['season'])
        finally:
            return my_stats

    def __del__(self):
        self.connection.close()


def get_config():
    with open(os.path.join(__location__, 'config.json')) as f:
        data = json.load(f)
    return data
