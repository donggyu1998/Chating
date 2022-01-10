from database.dbmanager import DBManager

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
    for number in range(1, 4):
        print ("{}) room ({})".format(number, number))
    print ("9) logout")
    print ("************************************")
    selected = int(input("Select : "))
    
    ret = True
    
    if selected == 1:
        user.chating_room

# 유저가 채팅방 접속 시 이 채팅방 기록을 가지고 있는지 체크 ? 
#   

    if selected == 9:
         user = None
         return logout()
     
    else:
        print ("Pls select valid item...")
    
    return ret

def logout():
    print ("LOGOUT ... ")
    
    ret = False
    return ret