import time
import menu
import os

from enum import Enum 

class PageState(Enum):
    PAGE_LOGIN = 0
    PAGE_CHATING = 1

def displayMenu():
    
    global cur_page
    global user
    
    if cur_page == PageState.PAGE_LOGIN:
        ret = menu.menuPageLogin()
        
        if not ((ret is None) or # 로그인 실패했을 경우
                (ret is True) or # 회원가입 성공했을 경우 
                (ret is False)): # 회원가입 실패했을 경우

            user = ret
            cur_page = PageState.PAGE_CHATING
            
    elif cur_page == PageState.PAGE_CHATING:
        
        ret = menu.menuPageChating(user)
        
        if ret is False: # 로그아웃했을 경우
            cur_page = PageState.PAGE_LOGIN

cur_page = PageState.PAGE_LOGIN
user = None
 
def main():
    while True:
        os.system('cls')
        displayMenu()
        time.sleep(0.5)

if __name__ == "__main__":
    main()

    """
1대1 채팅도 결국 그룹톡에서는 2명이면 1대1 채팅이다. 
collection 이 그룹톡에 대한 것이 있어야하며, 지금 구조로는 이상함

1. 구조 같은 부분에서 우ㅣ
2. 기획이 잘 못된건 logout, 등 번호가 바뀌고 chat str이 들어가는게 이상함

    """