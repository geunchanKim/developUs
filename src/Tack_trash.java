import java.lang.reflect.Method;
import java.time.LocalDateTime;
import java.time.LocalTime;

public class Tack_trash {
  private int planned_time_sec = 0;//도착 예정 시간, 초단위
  public Collecter collecter;
  private int time_sec = 0;//현재 시간, 초단위
  private int start_time = 0; //신청시간
  private int left_time_sec = 0;//남은 시간, 초단위
  private String path = System.getProperty("user.dir") + "/";
  private int log_num = 0;


  public LocalDateTime now = LocalDateTime.now(); 

  Tack_trash(int hour,int min,int sec) {
    setPlanndTime(hour, min, sec);//도착 예정 시간 세팅
    setTimeSec();//현재시간 세팅
    //collecter = new Collecter();//콜렉터 접근
    start_time = time_sec;//start시간 저장
    setLeftTime();//남은시간 만들기
  }

  public int getStartTime() {
    return start_time;
  }
  public void setTimeSec() {//현재시간 초로 변환해서 구하기
    int hour = now.getHour();
    int minute = now.getMinute();
    int second = now.getSecond();

    second = second + (hour * 3600) + (minute * 60);
    System.out.println("second = " + second);
    time_sec = second;    
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
    weighting = collecter.getTrashweit() / 500 + 1;
    
    if (weighting>10){
      weighting = 10;
    }
    return weighting;
  }

 

}
