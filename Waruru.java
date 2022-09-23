import java.io.IOException;
import java.util.Scanner;

public class Waruru {

    private String usrid;

    public void setusrid(String id){
        usrid = id;
    }

    public String getusrid(){
        return usrid;
    }

    private int login() throws IOException{
        Scanner sc = new Scanner(System.in);
        System.out.println("와르르와 함께 쓰레기 없는 삶을 경험하세요.");
        while(true){
            System.out.printf("\n1. 로그인\n2. 회원가입\n3. 종료\n");
            String ch = sc.next();
            System.out.println();
            if("1".equals(ch)){
                System.out.printf("Id: ");
                String id = sc.next();
                System.out.printf("Password: ");
                String pw = sc.next();
                FindUser fu = new FindUser();
                if(fu.searchId(id)){    //id가 존재할 경우
                    if(fu.checkPw(id, pw)){ //pw가 일치할 경우
                        System.out.println("로그인 되었습니다.");
                        System.out.println(id+"님 환영합니다.");
                        setusrid(id);
                        return 0;
                      //  break;
                    }
                    else{
                        System.out.println("로그인 정보가 일치하지 않습니다.");
                    }
                }
                else{
                    System.out.println("로그인 정보가 일치하지 않습니다.");
                }

            }
            else if("2".equals(ch)){
                System.out.printf("희망하는 Id: ");
                String id = sc.next();
                System.out.printf("희망하는 Password: ");
                String pw = sc.next();
                User user = new User();
                FindUser fu = new FindUser();
                if(fu.searchId(id)){
                    System.out.println("이미 존재하는 Id 입니다.");
                }
                else{
                    user.setId(id);
                    user.setPass(pw);
                    user.saveUser();
                    System.out.println(id+"님, 회원가입이 완료되었습니다.");
                }
            }
            else{
                return 1;
            }
        }

    }
    
    private int card() throws IOException{
        Card card = new Card(getusrid());
        Scanner sc = new Scanner(System.in);
        System.out.println("카드정보를 확인하세요");
        if(card.checkCard(card)){
            System.out.println("카드정보 확인됨.");
            sc.close();
            return 0;
        }
        else{
            System.out.println("카드정보가 없습니다.");
            System.out.println("카드를 등록하세요.");
            System.out.println("카드번호 16자리를 공백없이 입력하세요");
            String num = sc.next();
            card.setcardNum(num);
            System.out.println("유효기간을 입력하세요. MMYYYY");
            String due = sc.next();
            card.setdue(due);
            System.out.println("생년월일을 입력하세요. YY MM DD");
            String yy = sc.next();
            String mm = sc.next();
            String dd = sc.next();
            card.setbirth(yy, mm, dd);
            System.out.println("CVC, 보안코드 앞 두자리를 입력하세요.");
            String cvc = sc.next();
            card.setcvc(cvc);
            String code = sc.next();
            card.setcode(code);
            card.saveCard(card);
            System.out.println("카드정보가 저장되었습니다.");
            System.out.println("카드정보 확인됨.");
            sc.close();
            return 0;
        }
    }

    public void cash(){
        System.out.println("HIIII");
    }

    public static void main(String args[]) throws IOException{
        Waruru waruru = new Waruru();
        if(waruru.login()==1){
            return;
        }
        if(waruru.card() != 0){
            ;
        }
        waruru.cash();
    }
}
