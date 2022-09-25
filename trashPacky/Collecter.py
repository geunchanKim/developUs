
from datetime import datetime
import trashPacky

import os
class Collecter:
  

  def __init__(self,id,pw,trash_weit):
    print("#"*10+"Collecter"+"#"*10)
    self.trash_weit_gram = trash_weit#쓰레기 무게 G단위
    self.end_time=0#실제 도착 시간
    self.path = os.getcwd()+"/"
    self.now=datetime.now()
    self.user = trashPacky.User(id,pw)
    self.setTimeSec()

  def selectMenu(self):
    menu=int(input("사용하실 기능을 선택 하세요\n1. 유저 파일 열람 2. 유저 이름 열람 3.종료"))
    if menu==1:
      userName=input("열람할 유저 이름 입력")
      searchUserFile(userName)
  
  def setTimeSec(self):#현재 시간 만들어서 도착시간에 넣기
    hour = int(self.now.strftime("%H"))
    minute = int(self.now.strftime("%M"))
    second = int(self.now.strftime("%S"))
    self.setEndTime(hour,minute,second)

  def setEndTime(self,hour,min,sec):#도착시간 초단위 세팅
    end_time = ((hour * 3600) 
    + (min * 60) + (sec))
  
  def searchUserFile(self,User):#유저 파일 열람
    user_name=[]
    f=open(path+User+".txt")
    user_name=f.readlines()




