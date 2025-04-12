from model.models import User
from database.jsonDAO import Database 

class UserManager:
    def __init__(self, db: Database):
        self.db = db
        self.data = self.db.load()

    def register_user(self, username):
        self.data = self.db.load()
        if username.lower() not in self.data["users"]:
            user = User(username)
            self.data["users"][username] = user.__dict__
            self.db.save(self.data)
            return "Success"
        else:
            return "Error - user already existing"