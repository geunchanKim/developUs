import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.BufferedWriter;


public class Cash {
  private int pay = 0;
  private Tack_trash trash;
  private String path = System.getProperty("user.dir") + "/";


  public void saveFile() {

    try {
      File file = new File(path +trash.collecter.user.getId()+".txt");
      BufferedWriter BW = new BufferedWriter((new FileWriter(file,true)));
      if (file.isFile() && file.canWrite()) {//쓰기                
        BW.write("신청 시간: " + trash.getStartTime() / 3600 + ":" + (trash.getStartTime() % 3600) / 60 + ":"
            + trash.getStartTime() % 60);//개행문자쓰기                
        BW.newLine();
        BW.write("가격 : " + pay);
        BW.newLine();
        BW.newLine();
        BW.close();
      }
    } catch (IOException e) {
      System.out.println(e);
    }
  }
  
  public void paySelection() {
    pay = trash.change_cash() * 999;
  }

  public void search() {
    
  }

}