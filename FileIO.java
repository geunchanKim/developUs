import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.OutputStream;
import java.lang.management.BufferPoolMXBean;

class User{ //유저 클래스, 사용자 ID와 PW 전부 저장 및 관리
    private String userId;
    private String userPass;
    private String path = System.getProperty("user.dir") + "/"; //텍스트파일들이 저장되는 위치

    public void setId(String inputId){//id설정
        userId = inputId;
    }
    public String getId(){
        return userId;
    }
    public void setPass(String inputPass){
        userPass = inputPass;
    }
    public String getPass(){
        return userPass;
    }
    public void saveUser() throws IOException{  //getter로 얻은 ID와 PW를 텍스트파일로 저장
        OutputStream output = new FileOutputStream(path+userId+".txt");
        byte[] by = userPass.getBytes();
        output.write(by);
        output.close();
    }
    public String loadUser(String searchId){    //저장된 텍스트파일을 불러와 첫번째 줄(PW)을 읽어줌
        String str = null;
        try{
            String filePath = path+searchId+".txt";
            BufferedReader br = new BufferedReader(new FileReader(filePath));
            str = br.readLine();
            FileInputStream fileStream = null;
            fileStream = new FileInputStream( filePath );// 파일 스트림 생성
	        //버퍼 선언
	        byte[] readBuffer = new byte[fileStream.available()];
	        while (fileStream.read( readBuffer ) != -1){}
	        //str = new String(readBuffer); //출력
            br.close();
	        fileStream.close(); //스트림 닫기
        }
        catch (FileNotFoundException e){
            e.getStackTrace();
        }
        catch(IOException e){
            e.getStackTrace();
        }
        return str;
    }
}

class FindUser{
    private String path = System.getProperty("user.dir")+"/";
    
    public boolean searchId(String id){//id가 이미 생성된 것인지 체크
        File file = new File(path+id+".txt");
        if(file.exists()){//파일 존재 시
            return true;
        }
        else{             //파일 존재하지 않을 시
            return false;
        }
    }
    public boolean checkPw(String id, String pw){   //텍스트파일 첫째줄(pw)을 읽고 입력받은 패스워드가 옳은지 검사함
        User user = new User();
        String str = user.loadUser(id);
        if(str.equals(pw)){
            return true;
        }
        else{
            return false;
        }
    }
}

class Card{ //카드정보 클래스
    private String cardNum;    //카드번호 16자리
    private String due;        //유효기간 MMYYYY
    private String birth;      //생년월일 YYMMDD
    private String cvc;        //cvc번호 3자리
    private String code;       //비밀번호 앞 2자리
    private String id;
    private String path = System.getProperty("user.dir")+"/";

    public Card(String id){ //사용자 아이디 넘겨주기
        this.id = id;
    }
    
    public void setcardNum(String num){
//      String cd = Integer.toString(num1)+Integer.toString(num2)+Integer.toString(num3)+Integer.toString(num4);
        cardNum = num;
    }

    public String getcardNum(){
        return cardNum;
    }

    public void setdue(String num){
 //     String cd = Integer.toString(mm)+Integer.toString(yyyy);
 //     due = Integer.parseInt(cd);
        due = num;
    }

    public String getdue(){
        return due; 
    }

    public void setbirth(String yy, String mm, String dd){
//       String cd = Integer.toString(yy)+Integer.toString(mm)+Integer.toString(dd);
//       birth = Integer.parseInt(cd);
        String cd = yy + mm + dd;
        birth = cd;
    }

    public String getbirth(){
        return birth;
    }

    public void setcvc(String num){
        cvc = num;
    }

    public String getcvc(){
        return cvc;
    }

    public void setcode(String num){
        code = num;
    }

    public String getcode(){
        return code;
    }

    public void saveCard(Card card){    //getter로 얻은 카드정보를 텍스트 파일에 추가함. 카드정보는 사용자의 텍스트파일에 비밀번호 밑줄부터 저장됨
        try {
            File file = new File(path+id+".txt");
            BufferedWriter bw = new BufferedWriter(new FileWriter(file, true));
            if(file.isFile()&& file.canWrite()){
                bw.newLine();
                bw.write(card.getcardNum() +"\n" + card.getdue() + "\n" + card.getbirth() + "\n" +  card.getcvc() + "\n" + card.getcode());
            }
            bw.close();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }

    public boolean checkCard(Card card) throws IOException{    //저장된 사용자 텍스트파일을 읽어 사용자의 카드정보가 추가되었는지 확인함
        File file = new File(path+id+".txt");
        String str = null;
            BufferedReader br = new BufferedReader(new FileReader(file));
                str = br.readLine();
                str = br.readLine();                
                br.close();
                if(str==null){
                    return false;
                }
                else{
                    return true;
                }

    }

}

public class FileIO{
    public static void main(String args[]) throws IOException{
        User user = new User();
        FindUser fu = new FindUser();
        String id = "abcdef";
        String pw = "12345";
        user.setId(id);
        user.setPass(pw);
        user.saveUser();
        System.out.println(user.loadUser(id));
    }
}