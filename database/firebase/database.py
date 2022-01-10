from datetime import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from database.model.user import User

class Database:
    cred = credentials.Certificate("database/firebase/firebase_key.json")
    projectId = 'chating-ee150'
    
    def __init__(self):
        self._client = None
        self._db = None
        self._firebase_db = None
        
    def connect(self):
        self._client = firebase_admin.initialize_app(self.cred, {'projectId':self.projectId})
        
        if (self._client is None):
            print ("Firebase : could not connect to Firebase. ")
            return False
        
        else:
            self._firebase_db = firestore.client()
            return True
        
    def insert(self):
        pass
    
    def delete():
        pass
    
    def update():
        pass
    
    def findUser(self, user_id):
        
        ret = None
        
        ref = self._firebase_db.collection(u'user')
        snapshot = ref.where(u'_id', u'==', user_id).get()
        items = list(snapshot)
        
        if len(items) <= 0:
            print("Error : find not opponent id...")
            
        else:
            ret = items
            
        return ret
       
    def login(self, id, pw):
        
        ret = None
        
        ref = self._firebase_db.collection(u'user')
        snapshot = ref.where(u'_id', u'==', id).get()
        items = list(snapshot)

        if len(items) <= 0:
            print ("Error : Account is None or exists, Try again. ")
        
        else:
            user_pw = items[0].get('password')
            
            if (pw != user_pw):
                print ("Error : The password is incorrect, Try again. ")
            
            else:
                ret = User()
                ret.applyJson(items[0])
                user_uid = items[0].id
                ret.setUid(user_uid)
                print ("Login Success. ")
        
        return ret
    
    def register(self, id, pw):
        
        ref = self._firebase_db.collection(u'user')
        id_dup_check = ref.where(u'_id', u'==', id).get()
    
        if id_dup_check:
            print ("Error : Account is exists, Try again. ")
            return False 
        
        else:
            user = User()
            user.setId(id)
            user.setPassword(pw)
            user.setUid("None")
            ref.document().set(user.__dict__)
            print ("Register Success. ")
            return True 
            