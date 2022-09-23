import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class LogIn {
    public static void main(String args[]) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in)); // 회원가입 및 로그인 입력을 위한 입력문 선언
        String ID = ""; // 아이디
        String PW = ""; // 비밀번호
        while(true){
            System.out.print("1.Sign Up\n2.Sign in\n3.Exit\nCh : ");
            String Ch = bf.readLine();

            if("1".equals(Ch)){
                System.out.print("ID :");
                String ID_Ch = bf.readLine(); // [회원가입] 아이디 입력

                System.out.print("PW :");
                String PW_Ch = bf.readLine(); // [회원가입] 비밀번호 입력

                ID = ID_Ch; //입력한 아이디 저장
                PW = PW_Ch; // 입력한 비빌번호 저장

            }else if("2".equals(Ch)){
                System.out.print("ID :");
                String ID_Ch = bf.readLine(); // [회원가입] 아이디 입력

                System.out.print("PW :");
                String PW_Ch = bf.readLine(); // [회원가입] 비밀번호 입력

                if(ID.equals(ID_Ch) && PW.equals(PW_Ch)){ // 아이디와 비밀번호가 같으면 성공
                    System.out.println("login Success!");
                }else{
                    System.out.println("Fall.."); // 하나라도 다르면 실패
                }

            }else if("3".equals(Ch)){
                return; // 종료
            }else{
                System.out.println("RE");
            }

        }
    }
}
