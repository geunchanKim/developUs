from audioop import add
from flask import Flask, render_template, request, redirect, flash
import trashPacky

app = Flask(__name__)
app.secret_key = "My_Key"
id = ""
pw=""
outputdate =""
mypageinfo =[]

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
    global id,pw
    global outputdate, mypageinfo
    ttype = ""
    phonenumber = request.args.get('phonenumber')
    postalcode = request.args.get('postalcode')
    address = request.args.get('address')
    detailedaddress = request.args.get('detailedaddress')
    date = request.args.get('date')
    time = request.args.get('time')
    trashtype = request.args.get('type')
    if date == "" or time == "":
        flash("올바른 입력이 아닙니다")
        return redirect("/pickupinfo")
    spdate=date.split('-')
    outputdate=str(int(spdate[1]))+"월 "+str(int(spdate[2]))+"일 "+time+" 수거 예정"
    print(type(phonenumber), type(postalcode), type(address), type(detailedaddress), type(date), type(time), type(trashtype))
    trashtype = int(trashtype)
    if trashtype < 7:
        ttype = "일반쓰레기"
    else:
        ttype = "음식물쓰레기"
    print(outputdate, ttype)
    timeselc=time.split(":")
    timeselc[0]=int(timeselc[0])
    timeselc[1]=int(timeselc[1])
    time_sels=timeselc

    cash = trashPacky.Cash(time_sels[0],time_sels[1],0,id,pw, trashtype)
    
    mypageinfo=cash.callFile()
    print("before mypageinfo:",mypageinfo)
    for i in range(len(mypageinfo)):
        mypageinfo[i][1]=mypageinfo[i][1][4:]
        mypageinfo[i][2]=mypageinfo[i][2][7:]
        if mypageinfo[i][0]=='0':
            mypageinfo[i][0]="일반 쓰레기 2L"
        elif mypageinfo[i][0]=='1':
            mypageinfo[i][0]=("일반 쓰레기 5L")
        elif mypageinfo[i][0]=='2':
            mypageinfo[i][0]=("일반 쓰레기 10L")
        elif mypageinfo[i][0]=='3':
            mypageinfo[i][0]=("일반 쓰레기 20L")
        elif mypageinfo[i][0]=='4':
            mypageinfo[i][0]=("일반 쓰레기 50L")
        if mypageinfo[i][0]=='5':
            mypageinfo[i][0]=("일반 쓰레기 75L")
        if mypageinfo[i][0]=='6':
            mypageinfo[i][0]=("일반 쓰레기 100L")
        if mypageinfo[i][0]=='7':
            mypageinfo[i][0]=("음식물 쓰레기 1L")
        if mypageinfo[i][0]=='8':
            mypageinfo[i][0]=("음식물 쓰레기 2L")
        if mypageinfo[i][0]=='9':
            mypageinfo[i][0]=("음식물 쓰레기 3L")
        if mypageinfo[i][0]=='10':
            mypageinfo[i][0]=("음식물 쓰레기 5L")
        if mypageinfo[i][0]=='11':
            mypageinfo[i][0]=("음식물 쓰레기 10L")
        if mypageinfo[i][0]=='12':
            mypageinfo[i][0]=("음식물 쓰레기 20L")  
    print("after mypageinfo: ",mypageinfo)
    
    #trashtype=1
    #cash = trashPacky.Cash(int(timeselc[0]),int(timeselc[1]),0,id,trashtype)
    return redirect("/live")


@app.route("/live")
def live():
    global outputdate
    value = outputdate
    return render_template('livereporting.html', value = value)

@app.route("/loadmypage")
def loadmypage():
    global mypageinfo
    print(mypageinfo)
  
    return redirect("/mypage")

@app.route("/mypage")
def mypage():
    global id
    global mypageinfo
    print(mypageinfo)
   
    
    string = []
    for i in range(len(mypageinfo)):
        for j in range(3):
            string.append(mypageinfo[i][j])
            
    
    # string = mypageinfo[0][0]
    # string2 = mypageinfo[0][1]
    # string3 = mypageinfo[0][2]

    # string4 = mypageinfo[1][0]
    # string5 = mypageinfo[1][1]
    # string6 = mypageinfo[1][2]

    # string7 = mypageinfo[2][0]
    # string8 = mypageinfo[2][1]
    # string9 = mypageinfo[2][2]

    # string10 = mypageinfo[3][0]
    # string11 = mypageinfo[3][1]
    # string12 = mypageinfo[3][2]

    return render_template('mypage.html', value = id, values = string)
    # return render_template('mypage.html', value = id, value0= string[0], value1 = string[1], value2 = string[2], value3 = string[3], value4 = string[4], 
    # value5 = string[5], value6 = string[6], value7 = string[7], value8=string[8], value9=string[9], value10=string[10], value11=string[11])

@app.route("/checkid")#로그인 시도 시 Id, passwd 확인하는 장소
def check():
    global id,pw
    userid = request.args.get('userid')
    passwd = request.args.get('userpw')
    print(userid)
    print(passwd)
    pw=passwd
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