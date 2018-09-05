
class User:

    def __init__(self, user_id=None, name=None, gamertag=None,
                 epic_account=None, platform=None, password_hash=None, email=None, stats=None):
        self.user_id = float(user_id)
        self.name = str(name)
        self.gamertag = str(gamertag)
        self.epic_account = str(epic_account)
        self.platform = str(platform)
        self.password_hash = str(password_hash)
        self.email = str(email)
        self.stats = stats

    def __repr__(self):
        return '<User {}>'.format(self.gamertag)
