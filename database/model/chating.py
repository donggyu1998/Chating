import datetime

class Chating:
    
    def __init__(self):
        self._id = None
        self.msg = None
        self.create_at = datetime.datetime.now().isoformat()
    
    def setId(self, id):
        self._id = id
    
    def setMsg(self, msg):
        self.msg = msg
        
    def getId(self):
        return self._id
    
    def getMsg(self):
        return self.msg