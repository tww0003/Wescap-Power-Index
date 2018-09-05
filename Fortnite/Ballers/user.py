class User:

    # Queries database for user id and returns user object if the user exists
    def __init__(self, user_id):
        print(user_id)
        # query database for user
        pass

    # Initializer for user class with all information
    def __init__(self, user_id, name, gamertag, epic_account, platform, password_hash, email):
        self.user_id = user_id
        self.name = name
        self.gamertag = gamertag
        self.epic_account = epic_account
        self.platform = platform
        self.password_hash = password_hash
        self.email = email

    @staticmethod
    def create_user(user_id, name, gamertag, epic_account, platform, password_hash, email):
        # check if user exists
        # validate all data is there
        # update user table
        # return user object
        return User(user_id, name, gamertag, epic_account, platform, password_hash, email)

    @staticmethod
    def get_user(user_id):
        return User(user_id)

