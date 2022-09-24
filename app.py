from flask import Flask, render_template, request, redirect
import trashPacky

app = Flask(__name__)

@app.route("/")
def waruru():
    return render_template('main.html')

@app.route("/sign-in", methods=['GET', 'POST'])
def signin():
    if request.method == 'GET':
        
        return render_template('sign-in.html')
        
    else:
        return render_template('main_mypage.html')

@app.route("/sign-up")
def signup():
    return render_template('sign-up.html')

@app.route("/saving")
def savedata():#회원가입 하는 부분
    id = request.args.get('userid')
    pw = request.args.get('userpw')
    pwc = request.args.get('checkpw')
    name = request.args.get('username')
    cphone = request.args.get('phonenumber')
    email = request.args.get('email')
    print(id, pw, pwc, name, cphone, email)
    
    if pw!=pwc:
        
        print("비밀번호 재확인")
        return redirect("/")
    else:
        user=trashPacky.User(id,pw)
        print("회원가입이 완료되었습니다")
        return redirect("/")

@app.route("/payment")
def payment():
    return render_template('paymentinfo.html')

@app.route("/pickup")
def pickup():
    return render_template('pickupinfo.html')

@app.route("/live")
def live():
    return render_template('livereporting.html')

@app.route("/mypage")
def mypage():
    return render_template('mypage.html')

@app.route("/checkid")#로그인 시도 시 Id, passwd 확인하는 장소
def check():
    userid = request.args.get('userid')
    passwd = request.args.get('userpw')
    print(userid)
    print(passwd)
    if userid == "shinsion" and passwd == "dr0907":
        return redirect("main_mypage")
    else:
        return redirect("/")

@app.route("/main_mypage")
def main_mypage():
    return render_template('main_mypage.html')

if __name__ == "__main__":
    app.run()