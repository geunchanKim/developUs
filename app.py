from audioop import add
from flask import Flask, render_template, request, redirect, flash
import trashPacky

app = Flask(__name__)
app.secret_key = "My_Key"
id = ""
outputdate =""
date = []
price = []

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
def savedata():#회원가입 하는 장소
    global id
    id = request.args.get('userid')
    pw = request.args.get('userpw')
    pwc = request.args.get('checkpw')
    name = request.args.get('username')
    cphone = request.args.get('phonenumber')
    email = request.args.get('email')
    print(id, pw, pwc, name, cphone, email)

    fu=trashPacky.FindUser
    if fu.fusearchId(id):
        flash("동일한 ID가 이미 존재합니다")
        return redirect("/sign-up")

    if pw!=pwc:

        flash("비밀번호를 확인하십시오")
        return redirect("/sign-up")
    else:
        user=trashPacky.User(id,pw)
        user.saveUser()#회원 데이터 txt생성
        print("회원가입이 완료되었습니다")
        flash("회원가입이 완료되었습니다")
        return redirect("/payment")

@app.route("/payment")
def payment():
    return render_template('paymentinfo.html')

@app.route("/paymentsaving")
def paymentsaving():
    global id
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')
    num3 = request.args.get('num3')
    num4 = request.args.get('num4')
    num=str(num1)+str(num2)+str(num3)+str(num4)
    month = request.args.get('month')
    year = request.args.get('year')
    due = str(month)+str(year)
    cvc = request.args.get('cvc')
    code = request.args.get('code')
    print(num, due, cvc, code)

    card = trashPacky.Card(id, num, due, cvc, code)
    card.saveCard()
    print("카드정보 저장됨")
    flash("카드정보 저장됨")
    return redirect("sign-in")

@app.route("/pickupinfo")
def pickup():
    return render_template('pickupinfo.html')

@app.route("/savingpickupinfo")
def savingpickupinfo():
    global id
    global outputdate
    phonenumber = request.args.get('phonenumber')
    postalcode = request.args.get('postalcode')
    address = request.args.get('address')
    detailedaddress = request.args.get('detailedaddress')
    date = request.args.get('date')
    time = request.args.get('time')
    if date == "" or time == "":
        flash("올바른 입력이 아닙니다")
        return redirect("/pickupinfo")
    spdate=date.split('-')
    outputdate=str(int(spdate[1]))+"월 "+str(int(spdate[2]))+"일 "+time+" 수거 예정"
    print(type(phonenumber), type(postalcode), type(address), type(detailedaddress), type(date), type(time))
    print(outputdate)
    #timeselc=time.split(":")
    #weit=1
    #cash = trashPacky.Cash(int(timeselc[0]),int(timeselc[1]),0,id,weit)
    return redirect("/live")


@app.route("/live")
def live():
    global outputdate
    value = outputdate
    return render_template('livereporting.html', value = value)

@app.route("/mypage")
def mypage():
    global id
    return render_template('mypage.html', value = id)

@app.route("/checkid")#로그인 시도 시 Id, passwd 확인하는 장소
def check():
    global id
    userid = request.args.get('userid')
    passwd = request.args.get('userpw')
    print(userid)
    print(passwd)
    findU = trashPacky.FindUser()
    if findU.searchId(userid) == True:
        if findU.checkPw(userid, passwd) == True:
            flash("로그인 되었습니다")
            print("올바른 회원정보")
            print("로그인 되었습니다")
            id = userid
            return redirect("main_mypage")
        else:
            flash("비밀번호가 틀림")
            print("비밀번호가 틀림")
            return redirect("sign-in")
    else:
        flash("올바르지 않은 회원정보")
        print("올바르지 않은 회원정보")
        return redirect("sign-in")

@app.route("/main_mypage")
def main_mypage():
    return render_template('main_mypage.html')

if __name__ == "__main__":
    app.run()