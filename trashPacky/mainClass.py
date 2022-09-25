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
      # print("check")
      # self.saveUser()
    
    def saveUser(self):#user정보 저장(user파일 만들고 첫줄 비밀번호)
      f=open(self.path+self.userId+".txt","w")
      f.write(self.userPass)

    def loadUser(self,searchId):#user첫 줄(비밀번호) 받아서 리턴
      f=open(self.path+searchId+".txt","r")
      str=f.readline().rstrip('\n')
      f.close()
      return str

class FindUser:
  
  def fusearchId(id):
    print("#"*10+"finduser"+"#"*10)
    path = os.getcwd()+"/"
    path_fi=Path(path+id+".txt")

    if (path_fi.is_file()):
        return True
    else:
        return False
  
  def searchId(self,id):
    print("#"*10+"finduser"+"#"*10)
    path = os.getcwd()+"/"
    path_fi=Path(path+id+".txt")

    if (path_fi.is_file()):
        return True
    else:
        return False
  
  def checkPw(self,id, pw):
    user=User(id,pw)
    str=user.loadUser(id)
    print("loadUser값 확인하기")
    print(str)
    if str==pw:
        return True
    else:
        return False 

class Card:
  

  def __init__(self,inputid,cardnum, due, cvc, code):#생성자
    print("#"*10+"card"+"#"*10)
    self.id=inputid
    self.cardNum=cardnum
    self.due=due
    self.cvc=cvc
    self.code=code
    self.id=inputid
    self.path= os.getcwd()+"/"


  def saveCard(self):#카드정보 저장
    f=open(self.path+self.id+".txt","a")
    f.write("\n"+self.cardNum +"\n" 
            + self.due + "\n" + self.cvc + "\n" 
            + self.code)
  
  def checkCard(self):#카드정보가 있는지 탐색
    f=open(self.path+self.id+".txt","r")
    str=f.readline()
    str=f.readline()
    if(str==""):
      return False
    else:
      return True
