import datetime

class User:
    
    def __init__(self):
        self._uid = None
        self._id = None
        self.password = None
        self.create_at = datetime.datetime.now().isoformat()
    
    def setUid(self, uid):
        self._uid = uid
        
    def setId(self, id):
        self._id = id
        
    def setPassword(self, password):
        self.password = password
    
    def getUid(self):
        return self._uid
    
    def getId(self):
        return self._id
    
    def getPassword(self):
        return self.password
    
    def getUid(self):
        return self._uid
                                                
    def applyJson(self, data):
        
        self._id = data.get('_id')
        self.password = data.get('password')
        self.create_at = data.get('create_at')