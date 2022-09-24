import os
from datetime import datetime
import trashPacky
from pathlib import Path

class User:#유저 클래스
    
    def __init__(self,Id,Pw):#생성자
      print("#"*10+"User"+"#"*10)
      self.userId = Id
      self.userPass = Pw
      self.path = os.getcwd()+"/"#파일 주소
      self.filcheck=Path(self.path+Id+".txt")
      # if not self.filcheck.exists:#파일 없으면,
      print("check")
      self.saveUser()
        
    def saveUser(self):#user정보 저장(user파일 만들고 첫줄 비밀번호)
      f=open(self.path+self.userId+".txt","w")
      f.write(self.userPass+"\n")

    def loadUser(self,searchId):#user첫 줄(비밀번호) 받아서 리턴
      f=open(self.path+searchId+".txt","r")
      str=f.readline()
      f.close()
      return str

class FindUser:
  
  def searchId(self,id):#
    print("#"*10+"finduser"+"#"*10)
    self.path_fi=Path(self.path+id+".txt")
    self.path = os.getcwd()+"/"


    if (self.path_fi.is_file()):
        return True
    else:
        return False
  
  def checkPw(self,id, pw):
    user=User(id,pw)
    str=self.loadUser(id)
    if str==pw:
        return True
    else:
        return False 

class Card:
  

  def __init__(self,inputid):#생성자
    print("#"*10+"card"+"#"*10)
    self.id=inputid
    self.cardNum=""
    self.due=""
    self.birth=""
    self.cvc=""
    self.code=""
    self.id=""
    self.path= os.getcwd()+"/"


  def saveCard(self,card):#카드정보 저장
    f=open(path+id+".txt","a")
    f.write("\n"+cardNum +"\n" 
            + due + "\n" + birth 
            + "\n" + cvc + "\n" 
            + code)
  
  def checkCard(self,card):#카드정보가 있는지 탐색
    f=open(path+id+".txt","r")
    str=f.readline()
    str=f.readline()
    if(str==null):
      return False
    else:
      return True
