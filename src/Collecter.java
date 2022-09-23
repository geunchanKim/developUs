//도착 시간 정보 전송
//무게정보 전송
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.BufferedWriter;
import java.util.Scanner;
import java.lang.reflect.Method;
import java.time.LocalDateTime;
import java.time.LocalTime;

public class Collecter {
  private int trash_weit_gram = 0;//쓰레기 무게g단위
  private int end_time = 0;//실제 도착 시간
  private String path = System.getProperty("user.dir") + "/";
  public User user;
  public LocalDateTime now = LocalDateTime.now();
  boolean end = false;
  Collecter() {
    user = new User();
  }

  public void setTimeSec() {//현재시간 초로 변환해서 구하기
    int hour = now.getHour();
    int minute = now.getMinute();
    int second = now.getSecond();
    if (end) {
      setEndTime(hour, minute, second);
    }
  }
  
  public void setEndTime(int hour,int min,int sec) {
    end_time = (hour * 3600) + (min * 60) + (sec);
  }

  public int getEndTime() {
    return end_time;
  }

   public void setTrashweit(int num) {//쓰레기 무게 세팅
    trash_weit_gram = num;
  }

  public int getTrashweit() {//쓰레기 무게 조회
    return trash_weit_gram;
  }

  public void searchUserFile(String User) {//유저 파일(로그) 열람
    Scanner readFile;
    String[] user_name = new String[100];
    int count = 0;
    try {
      readFile = new Scanner(new File(path + "User_list.txt"));

      while (readFile.hasNext()) {
        user_name[count] = readFile.next();
        count++;
      }

    } catch (IOException e) {
      System.out.println(e);
    }
    System.out.println("User file : " + user_name);
  }
  
public void searchUserFileList() {//유저 이름 열람, user_name에 저장
    Scanner readFile;
    String[] user_name = new String[100];
    int count=0;
    try {
      readFile = new Scanner(new File(path + "User_list.txt"));
        
      while (readFile.hasNext()){
        user_name[count]=readFile.next();
        count++;
      }
      
    } catch (IOException e) {
      System.out.println(e);
    }
    System.out.println("User name list : "+user_name);
  }

  public void makeUserList(String UserName) {//유저 이름만 파일에 추가 
    try {
      File file = new File(path + "User_list.txt");
      BufferedWriter BW = new BufferedWriter((new FileWriter(file, true)));
      if (file.isFile() && file.canWrite()) {//쓰기                
        BW.write(UserName);//개행문자쓰기                
        BW.newLine();
        BW.close();
      }
    } catch (IOException e) {
      System.out.println(e);
    }
  }
  

}
