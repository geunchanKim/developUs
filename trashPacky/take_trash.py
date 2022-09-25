import os
import trashPacky
from datetime import datetime

class take_trash:
  

  def __init__(self,hour,min,sec,id,pw,weit):
    print("#"*10+"take trash"+"#"*10)
    self.planned_time_sec=0#도착 예정 시간, 초단위
    self.time_sec=0#현재시간
    self.time_string=""
    self.start_time=0#신청 시간
    self.left_time_sec=0#남은 시간
    self.path=os.getcwd()+"/"
    self.now=datetime.now()
    self.setPlanndTime(hour,min,sec)
    self.setTimeSec()
    self.setLeftTime()
    self.collecter = trashPacky.Collecter(id,pw,weit)
    self.start_time = self.time_sec
   

  def setTimeSec(self):#현재 시간 생성
    str_time = self.now.strftime("%m월 %d일 %H시%M분")

    hour = int(self.now.strftime("%H"))
    minute = int(self.now.strftime("%M"))
    second =  int(self.now.strftime("%S"))
    second = second + (hour * 3600) + (minute * 60)
    self.time_sec=second
    self.time_string=str_time
    
  def setPlanndTime(self,hour,min,sec):#도착 예정시간 입력되는 값으로 넣어줌
    self.planned_time_sec = (hour * 3600) + (min * 60) + (sec)

  def getLeftTime(self):#남은 시간 조회
    self.setLeftTime()
    a=str((int(self.left_time_sec/3600)))+":"+str((int((self.left_time_sec%3600)/60)))+":"+str((int(self.left_time_sec%60)))
    print(a)
    return a

  def getPlannedTime(self):#도착 예정 시간 조회
    a=str(int(self.planned_time_sec/3600))+":"+str(int((self.planned_time_sec%3600)/60))+":"+str(int(self.planned_time_sec%60))
    print(a)
    return a

  def setLeftTime(self):#조회 할 때마다 조회할 떄의 시간 필요
    now=datetime.now()
    hour = int(now.strftime("%H"))
    minute = int(now.strftime("%M"))
    second =  int(now.strftime("%S"))
    second = second + (hour * 3600) + (minute * 60)
    self.left_time_sec = self.planned_time_sec - second
    return self.left_time_sec

  def change_cash(self):
    weighting = self.collecter.trash_weit_gram

    if weighting<4:
      weighting=5
    elif weighting<7:
      weighting=7
    elif weighting<10:
      weighting=6
    else:
      weighting=10
    return weighting