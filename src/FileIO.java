import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;

class User{
    private String userId;
    private String userPass;
    private String path = System.getProperty("user.dir") + "/";

    User(){}
    User(String Id, String Pw) {
        userId = Id;
        userPass = Pw;
    }
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
    public void saveUser() throws IOException{
        OutputStream output = new FileOutputStream(path+userId+".txt");
        byte[] by = userPass.getBytes();
        output.write(by);
        output.close();
    }
    public String loadUser(String searchId){
        String str = null;
        try{
            String filePath = path+searchId+".txt";
            FileInputStream fileStream = null;
            fileStream = new FileInputStream( filePath );// 파일 스트림 생성
	        //버퍼 선언
	        byte[ ] readBuffer = new byte[fileStream.available()];
	        while (fileStream.read( readBuffer ) != -1){}
	        str = new String(readBuffer); //출력

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
}

