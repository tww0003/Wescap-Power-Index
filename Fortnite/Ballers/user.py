
class User:

    # Queries database for user id and returns user object if the user exists
    def __init__(self, user_id=None, name=None, gamertag=None,
                 epic_account=None, platform=None, password_hash=None, email=None, stats=None):
        self.user_id = user_id
        self.name = name
        self.gamertag = gamertag
        self.epic_account = epic_account
        self.platform = platform
        self.password_hash = password_hash
        self.email = email
        self.stats = stats

    def __repr__(self):
        return '<User {}>'.format(self.gamertag)

    # def add_user(self):
    #     db = DatabaseHelper.DatabaseHelper()
    #     sql = "INSERT INTO `user` (`name`, `gamertag`, `epic_account`, `platform`, `password_hash`, `email1) VALUES " \
    #           "(%s, %s, %s, %s, %s, %s)"
    #     results = db.call_command(sql,
    #                               (self.name, self.gamertag, self.epic_account,
    #                                self.platform, self.password_hash, self.email))[0]

