import os
from datetime import datetime
import trashPacky



class Cash:
  
  def __init__(self,hour,min,sec,id,pw,weit):#생성자
    print("#"*10+"Cash"+"#"*10)
    self.pay=0#지불 금액
    self.path=os.getcwd()+"/"#주소
    self.trash = trashPacky.take_trash(hour,min,sec,id,pw,weit)#trash생성
    self.saveFile()

  def saveFile(self):#파일 저장(신청시간, 가격)
    f=open(self.path+self.trash.collecter.user.userId+".txt","a")
    f.write("신청 시간"+str(int(self.trash.start_time/ 3600)) 
    + ":" + str(int((self.trash.start_time % 3600) / 60)) + ":"
            + str(int(self.trash.start_time % 60))+"\n")
    self.paySelection()
    f.write("가격 :"+str(self.pay)+"\n")
  
  def paySelection(self):
    self.pay = self.trash.change_cash()*999

