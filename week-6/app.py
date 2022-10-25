from crypt import methods
from email import message
from this import d
from flask import Flask ,request,render_template,session,redirect,url_for,make_response
import mysql.connector
from mysql.connector import Error

app=Flask(__name__,static_folder="public",static_url_path="/")
app.secret_key="member"

connection = mysql.connector.connect(
host="localhost",
database="website",
user="root",
password="0000"
)

# ---------------首頁--------------------
@app.route("/",methods=["get","post"])
def index():
    return render_template("index.html")

# --------------註冊網址-----------------
@app.route("/signup",methods=["post"])
def signup():
    name=request.form["name"]
    username=request.form["username"]
    password=request.form["password"]
    cursor=connection.cursor()   
    sql=f'''select username from member where username="{username}"'''
    cursor.execute(sql)
    result=cursor.fetchone()  
    if result:
        return redirect("/error?message=456")
    else:
        new_sql="insert into member(name,username,password) VALUES (%s, %s, %s);"
        new_data=(name,username,password)           
        cursor.execute(new_sql,new_data)
        connection.commit()
        return redirect("/")  

# --------------登入網址-----------------
@app.route("/signin",methods=["post"])
def signin():
    
    username=request.form["username"]
    password=request.form["password"]
    cursor = connection.cursor()

    sql=f'''select username,password from member where username="{username}" and password="{password}"'''

    cursor.execute(sql)
    result=cursor.fetchone()
    if result:
            session["id"]=result[0]
            session["name"]=result[1]
            return redirect("/member")
        
    else :
        return  redirect("/error?message=123")  

# --------------會員頁面網址---------------

@app.route("/member")
def member():
   cursor = connection.cursor()
   sql='''select member.name, message.content from member inner join message on member.id=message.member_id;'''
   cursor.execute(sql)
   result=cursor.fetchall()
   
   if "id" and "name" in session:       
        return render_template("member.html",name=session["name"],result=result)
   else:
        return render_template("index.html") 
    
 
# --------------錯誤頁面-------------------
@app.route("/error")
def error():
    data=request.args.get("message")
    if data=="123": 
        return render_template("error.html",text="帳號或密碼輸入錯誤")

    if data=="456":
        return render_template("error.html",text="帳號已經被註冊") 

# --------------登出頁面-------------------
@app.route("/signout")
def signout():
    session.pop("id",None)
    session.pop("name",None)
    return redirect("/")   
    
# --------------留言系統----------------------
@app.route("/message" ,methods=["get","post"])
def message():
    content=request.form["content"]
    id=session["id"]
    cursor = connection.cursor()
    sql= f''' insert into message(member_id,content) values("{id}","{content}")'''
    cursor.execute(sql)
    connection.commit()  
    return redirect("/member")
        

app.run(port=3000)