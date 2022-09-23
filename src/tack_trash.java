import java.lang.reflect.Method;
import java.time.LocalDateTime;
import java.time.LocalTime;

public class tack_trash {
  private int planned_time_sec = 0;//도착 예정 시간, 초단위
  private int time_sec = 0;//현재 시간, 초단위 
  private int left_time_sec = 0;//남은 시간, 초단위
  private int trash_weit_gram = 0;//쓰레기 무게g단위
  public LocalDateTime now = LocalDateTime.now(); 

  tack_trash(int hour,int min,int sec) {
    setPlanndTime(hour, min, sec);//도착시간 세팅
    setTimeSec();//현재시간 세팅
    setLeftTime();//남은시간 만들기
  }

  public void setTimeSec() {//현재시간 초로 변환해서 구하기
    int hour = now.getHour();
    int minute = now.getMinute();
    int second = now.getSecond();

    second = second + (hour * 3600) + (minute * 60);
    System.out.println("second = " + second);
    time_sec = second;    
  }
  
  public void setTrashweit(int num) {//쓰레기 무게 세팅
    trash_weit_gram = num;
  }

  public int getTrashweit() {//쓰레기 무게 조회
    return trash_weit_gram;
  }

  public void setPlanndTime(int hour,int min,int sec) {//시간, 분, 초로 넣으면 자동으로 초로 변환 도착 예정시간 세팅
    planned_time_sec = (hour * 3600) + (min * 60) + (sec);
  }

  public String getPlannedTime() {//남은시간 조회
    String a = (planned_time_sec/3600)+":"+((planned_time_sec%3600)/60)+":"+(planned_time_sec%60);
    System.out.println(a);
    return a;
  }
  public int setLeftTime() {//남은시간 생성
    System.out.println(planned_time_sec - time_sec);
    left_time_sec = planned_time_sec - time_sec;
    return left_time_sec;
  }
  
  public int change_cash() {//가중치 변환
    int weighting;
    weighting = trash_weit_gram / 500 + 1;
    
    if (weighting>10){
      weighting = 10;
    }
    return weighting;
  }


}
