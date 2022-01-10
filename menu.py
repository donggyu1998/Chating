import os
from database.dbmanager import DBManager
from database.model.chating import Chating

def menuPageLogin():
    print ("************ MENU Login ************")
    print ("1) Login")
    print ("2) Register")
    print ("************************************")
    selected = int(input("Select : "))
    
    if selected == 1:
        return menuLogin()

    elif selected == 2:
        return menuRegister()
    
def menuLogin():
    dbmanager = DBManager.getInstance()
        
    id = input("ID : ")
    pw = input("PW : ")
    
    ret = dbmanager.login(id, pw)
    
    if ret is None:
        input ("Error : Pls Check ID/PW... ( If you want to retry, press enter. )")

    return ret

def menuRegister():
    dbmanager = DBManager.getInstance()
    
    id = input("ID : ")
    pw = input("PW : ")
    
    ret = dbmanager.register(id, pw)
    
    if ret is False:
        
        input ("Error : Pls Check ID/PW... ( If you want to retry, press enter. )")
        
    return ret

def menuPageChating(user):
    
    print ("< UserInfo : {} >".format(user._id))
    print ("*********** Chating List ***********")
    loadChatingRoom(user)
    print ("9) logout")
    print ("************************************")
    selected = input("Select : ")
    
    ret = True
    
    if selected == 'chat':
    
        print("Info : Pls input opponent id... ")
        user_id = input("ID : ")
        createChatingRoom(user, user_id)
        
    if selected == 9:
         user = None
         return logout()
     
    else:
        print ("Error : Pls select valid item...")
    
    return ret

def loadChatingRoom(user):
    
    if len(user.chating) <= 0:
        print ("Info : Chating room not exist.")
        print ("Info : If you want to create chating room, input 'chat'")
            
    else:
        users = list(user.chating.keys())
        print("If you want to create chating room, input 'chat'")
        
        for i in range(len(users)):
            user = users[i]
            print("{}) userName : {}".format(i, user))
            
            #selected = int(input("select : "))
            
            #if selected < len(users):
            #    pass
            
            #else:
            #    print ("Error : Index out of range exception. ")
    
def createChatingRoom(user, user_id):
    
    dbmanager = DBManager.getInstance()
    ret = dbmanager.findUser(user_id)
    
    if ret is not None:
        items = list(ret)
        user_id = items[0].get('_id')
        chating = Chating()
        os.system('cls')
        print("Info : Pls send msg or 'exit'")
        while True:
            input_text = input("input : ")
            print ("exit) chating exit")
            chating.setId(user_id)
            chating.setMsg(input_text)
            user.setChating(user_id, chating)
            
            if input_text == "exit":
                return None
        
    return ret

def logout():
    print ("LOGOUT ... ")
    
    ret = False
    return ret

"""
1. 
    
"""