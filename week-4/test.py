from crypt import methods
from email import message
from this import d
from flask import Flask
from flask import request
from flask import render_template
from flask import session
from flask import redirect
from flask import url_for

app=Flask(__name__,static_folder="public",static_url_path="/")
app.secret_key="member"

@app.route("/",methods=["get","post"])
def index():
    if request.method == 'POST':
        result=request.form["number"]
        return redirect(url_for("square",number=result))
    return render_template("index.html")


@app.route("/signin",methods=["post"])
def signin():
    name=request.form["name"]
    password=request.form["password"]
    
    if name=="test" and password=="test":
       session["username"]=name
       return redirect("/member")
    if not name or not password:
        
        return redirect("/error?message=123")
    if name!="test" or password!="test":
        
        return redirect("/error?message=456")       

@app.route("/member")
def member():
    if "username" in session: 
        return render_template("member.html")
    else:
        return render_template("index.html")


@app.route("/error")
def error():
    data=request.args.get("message")
    if data=="123": 
        return render_template("error.html",text="請輸入帳號,密碼")
    if data=="456":
        return render_template("error.html",text="帳號或密碼輸入錯誤")    

@app.route("/signout")
def signout():
    session.pop("username",None)
    return redirect("/")



@app.route("/square/<number>" ,methods=["get","post"])
def square(number):
        return render_template("num.html",answer=int(number)*int(number))
   


app.run(port=3000)