from crypt import methods
from email import message
from this import d
from urllib import response
from flask import Flask ,request,render_template,session,redirect,url_for,make_response,json,Response
from flask import jsonify
import json 
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
    print(username)
    password=request.form["password"]
    cursor=connection.cursor()   
    sql='''select username from member where username=%s'''
    val=(username,)
    cursor.execute(sql,val)
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

    sql='''select username,password,id,name  from member where username=%s and password=%s'''
    val=(username,password) 
    cursor.execute(sql,val)
    result=cursor.fetchone()
 
    if result:
            session["id"]=result[2]
            session["name"]=result[3]
            return redirect("/member")
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
   return redirect("/")
    
 
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
    try:
        if "id" and "name" in session:  
            cursor = connection.cursor()
            sql= ''' insert into message(member_id,content) values(%s,%s);'''
            val=(id,content)
            cursor.execute(sql,val)
            connection.commit()  
            return redirect("/member")
        else:    
            return redirect("/")
    except:
        print("Unexpected Error")
    finally:
        cursor.close()   


#---------------查詢會員api-------------------
@app.route("/api/member",methods=["get"])
def api():

    username=request.args.get("username")
    try:
        cursor = connection.cursor()
        sql='''select id,name,username  from member where username=%s '''
        val=(username,)
        cursor.execute(sql,val)
        result=cursor.fetchone()
        content={}
        if result:
                content["data"]={"id":result[0],"name":result[1],"username":result[2]}
        else:       
            content["data"]="null"
    except:
        print("Unexpected Error")
    finally:
        cursor.close()
                   
    app.config['JSON_AS_ASCII'] = False
    json_string=jsonify(content)
    res=make_response(json_string,200)
    return res

#---------------修改姓名api-------------------
@app.route("/api/member",methods=["patch"])
def patch():
    app.config['JSON_AS_ASCII'] = False
    new_data=request.json
    new_name=new_data["name"]
    message={}
    try:
        if "id" and "name" in session:
            cursor = connection.cursor()
            sql='''update member set name=%s where id=%s '''
            val=(new_name,session["id"])
            cursor.execute(sql,val)
            connection.commit()
            message={"ok":True}
            session["name"]=new_name
        else:    
            message={"error":True}    
    except:
        message={"error":True}
    finally:
        cursor.close()          
    
    json_string=jsonify(message)
    res=make_response(json_string,200)
    return res

app.run(port=3000)
