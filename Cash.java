import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.BufferedWriter;


public class Cash {
  private int Cash = 0;
  private Tack_trash trash;
  private String path = System.getProperty("user.dir") + "/";

  Cash(int hour, int min, int sec) {
    trash = new Tack_trash(hour, min, sec);    
  }
  public void saveFile() {

    try {
      File file = new File(path + "save_file.txt");
      BufferedWriter BW = new BufferedWriter((new FileWriter(file)));
      if (file.isFile() && file.canWrite()) {//쓰기                
        BW.write("신청 시간: " + trash.getStartTime() / 3600 + ":" + (trash.getStartTime() % 3600) / 60 + ":"+trash.getStartTime()%60);//개행문자쓰기                
        BW.newLine();
        if (trash.getEndTime() != 0) {
          BW.write("도착 시간: " + trash.getEndTime() / 3600 + ":" + (trash.getEndTime() % 3600) / 60 + ":"
              + trash.getEndTime() % 60);
        }
        BW.newLine();
        BW.close();
      }
    } catch (IOException e) {
      System.out.println(e);
    }
    

  }
  public static void main(String args[]){
    Cash cash = new Cash(12, 30, 34);
    cash.saveFile();
}
}