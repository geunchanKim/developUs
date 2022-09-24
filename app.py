from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def waruru():
    return render_template('main.html')

@app.route("/sign-in")
def signin():
    return render_template('sign-in.html')

@app.route("/sign-up")
def signup():
    return render_template('sign-up.html')

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

@app.route("/main_mypage")
def main_mypage():
    return render_template('main_mypage.html')

if __name__ == "__main__":
    app.run()