from database.firebase.database import Database

class DBManager:
    
    __instance = None
    
    @classmethod
    def getInstance(cls):
        
        if cls.__instance == None:
            cls.__instance = DBManager()
            
        return cls.__instance
    
    def __init__(self):
        self._db = Database()
        self._db.connect()
        
    def insert(self):
        self._db.insert()
    
    def delete():
        pass
    
    def findUser(self, user_id):
        ret = self._db.findUser(user_id)
        return ret
    
    def update():
        pass
    
    def login(self, id, pw):
        ret = self._db.login(id, pw)
        return ret
    
    def register(self, id, pw):
        ret = self._db.register(id, pw)
        return ret