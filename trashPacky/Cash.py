import os
from datetime import datetime
import trashPacky



class Cash:
  
  def __init__(self,hour,min,sec,id,pw,weit):#생성자
    print("#"*10+"Cash"+"#"*10)
    self.trashtype=weit
    self.pay=0#지불 금액
    self.path=os.getcwd()+"/"#주소
    self.trash = trashPacky.take_trash(hour,min,sec,id,pw,weit)#trash생성

    self.saveFile()
    

  def saveFile(self):#파일 저장(신청시간, 가격)
    now=datetime.now()
    f=open(self.path+self.trash.collecter.user.userId+".txt","a")
    str_time = now.strftime("%m월 %d일 %H시%M분")
    f.write("\n신청시간 : "+str_time+"\n")
    self.paySelection()
    f.write("가격 :"+str(int(self.pay))+"원\n")
    print("SELF.trashtype")
    print(str(self.trashtype))
    f.write(str(self.trashtype))
    print("Did it work?")
  
  def callFile(self):
    f=open(self.path+self.trash.collecter.user.userId+".txt","r")
    st=[]
    s=f.read().split('\n')
    print(len(s))
    sq=[]
    for i in range(len(s)-1,3,-1):
      if i<0:
        break
      sq.append(s[i])
    str_mypg=[]
    save2=[]
    for i in sq:
      save2.append(i)
      if len(save2)==3:
        str_mypg.append(save2)
        save2=[]
    print(str_mypg)
    return str_mypg

  def paySelection(self):
    self.pay = self.trash.change_cash()*1000
