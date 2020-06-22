# -*- coding:utf-8 -*-
from flask import *
import pymysql
import json
from flask_cors import CORS  # 导入模块
import time
from datetime import datetime
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')   
app = Flask(__name__)
CORS(app)

db = pymysql.connect(
    host='xxxxxxxx',
    port=3306,
    user='xxxxxx',
    passwd='xxxxxxx',
    db='xxxxxxxxxxxxxx',
    charset='utf8'
)

@app.route('/')
def index():
    data={"code":20000,"data":{"roles":["admin"],"introduction":"I am a super administrator","avatar":"https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif","name":"超级管理员","id":"xxxxxxxx"}}
    return json.dumps(data,ensure_ascii=False)
 
@app.route('/register',methods=['POST'])
def register():
    data=request.get_data()
    data=json.loads(data)
    userid=data['userid']
    username = data['username']
    password = data['password']
    phone = data['phone']
    age = data['age']
    sex = data['sex']
    cursor = db.cursor()
    sql="SELECT * FROM user  WHERE userid='"+str(userid)+"'"
    cursor.execute(sql)
    results = cursor.fetchall()
    db.commit()
    if len(results)>0:
            abort(404)
    else:
            cursor = db.cursor()
            sql="INSERT INTO user VALUES (%s,%s,%s,%s,%s,%s,%s)"
        
            var=(str(userid),str(password),str(phone),str(username),str(sex),str(age),"editor")
            
            cursor.execute(sql,var)
            db.commit()
            return "1"
            
    
        
@app.route('/gettoken',methods=['POST'])
def gettoken():
    data=request.get_data()
    data=json.loads(data)
    username = data['username']
    password = data['password']
    cursor = db.cursor()
    sql="SELECT * FROM user  WHERE userid='"+str(username)+"' AND password='"+str(password)+"'"
    cursor.execute(sql)
    results = cursor.fetchall()
    db.commit()
    res=dict()
    if len(results)>0:
        res['code']=20000
        data=dict()
        data['token']=username
        res['data']=data
    else:
        res['code']=404
        res['message']="账号或密码错误"
    return json.dumps(res,ensure_ascii=False)


@app.route('/getuserinfo')
def getuserinfo():
    uid=request.args.get('token')
    cursor = db.cursor()
    sql="SELECT username,roles FROM user  WHERE userid="+str(uid)
    cursor.execute(sql)
    result= cursor.fetchone()
    db.commit()
    res=dict()
    res['code']=20000
    data=dict()
    data['name']=result[0]
    roles=[]
    roles.append(result[1])
    data['roles']=roles
    data['avatar']="https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif"
    res['data']=data
    return json.dumps(res,ensure_ascii=False)



@app.route('/addlecture',methods=['POST'])
def addlecture():
    data=request.get_data()
    data=json.loads(data)
    date1 = data['date1']
    date2 = data['date2']
    name  = data['name']
    reporter = data['reporter']
    location = data['location']
    date1=date1.split(' ', 1 )[0]
    date2=date2.split(' ', 1 )[1]
    date=date1+' '+date2
    dt = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    try:
        cursor = db.cursor()
        sql="INSERT INTO lecture (lecturename,reporter,location,ltime) VALUES (%s,%s,%s,%s)"
        var=(str(name),str(reporter),str(location),str(dt))
        cursor.execute(sql,var)
        db.commit()
        return  "0"
    except:
        return  "0"

@app.route('/dellecture',methods=['GET'])
def dellecture():
    lid=request.args.get('id')
    try:
        cursor = db.cursor()
        sql="DELETE FROM lecture WHERE lectureid="+str(lid)
        cursor.execute(sql)
        db.commit()
        sql="DELETE FROM signup WHERE lectureid="+str(lid)
        cursor.execute(sql)
        db.commit()
        return "0"
    except:
        return "0"


@app.route('/alterlecture',methods=['POST'])
def alterlecture():
    data=request.get_data()
    data=json.loads(data)
    lid=data['lid']
    date1 = data['date1']
    date2 = data['date2']
    name  = data['name']
    reporter = data['reporter']
    location = data['location']
    date1=date1.split(' ', 1 )[0]
    date2=date2.split(' ', 1 )[1]
    date=date1+' '+date2
    dt = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    try:
        cursor = db.cursor()
        sql="UPDATE lecture SET lecturename='"+str(name)+"',reporter='"+str(reporter)+"',location='"+str(location)+"' WHERE lectureid="+str(lid)
        cursor.execute(sql)
        db.commit()
        return  "0"
    except:
        return  "0"

@app.route('/searchlecture1',methods=['POST'])
def searchlecture1():
    data=request.get_data()
    data=json.loads(data)
    currentpage= (int(data['page'])-1)*15
    reporter = data['option']['reporter']
    name  = data['option']['name']
    try:
       cursor = db.cursor()
       base="SELECT * FROM lecture"
       sql=""
       if name!='null':
        sql=sql+" WHERE lecturename like '%"+str(name)+"%' "
        if reporter!='null':
            sql=sql+" AND reporter like '%"+str(reporter)+"%' "
        else:
            pass
       else:
        if reporter!='null':
            sql=sql+" WHERE reporter like '%"+str(reporter)+"%' "
        else:
            pass
       tsql=base+sql+" ORDER BY ltime DESC LIMIT 15 OFFSET "+str(currentpage)
       cursor.execute(tsql)
       results = cursor.fetchall()
       db.commit()
       res=dict()
       List=[]
       if len(results)>0:
           for i in results:
              resi=dict()
              resi['lid']=i[0]
              resi['name']=i[1]
              resi['reporter']=i[2]
              resi['time']=i[4].strftime('%Y-%m-%d %H:%M')
              resi['location']=i[3]
              List.append(resi)
       res['list']=List   
       sql="SELECT COUNT(*) FROM lecture"+sql
       cursor.execute(sql)
       count= cursor.fetchone()
       db.commit()
       if len(count)>0:
            res['count']=count[0]
       else:
            res['count']=0
       return json.dumps(res,ensure_ascii=False)
    except:
       return "0"
       
@app.route('/delsignup',methods=['GET'])
def delsignup():
    uid=request.args.get('uid')
    lid=request.args.get('lid')
    cursor = db.cursor()
    sql="DELETE FROM signup WHERE userid="+str(uid)+" AND lectureid="+str(lid)
    cursor.execute(sql)
    db.commit()
    
    return "0"

@app.route('/signup',methods=['POST'])
def signup():
    data=request.get_data()
    data=json.loads(data)
    uid = data['uid']
    lid = data['lid']
    signuptime=datetime.now()
    try:
        cursor = db.cursor()
        sql="INSERT INTO signup  VALUES (%s,%s,%s)"
        var=(str(uid),str(lid),str(signuptime))
        cursor.execute(sql,var)
        db.commit()
        return "0"
    except :
        abort(404)
    
@app.route('/getsignup',methods=['GET'])
def getsignup():
    uid=request.args.get('uid')
    cursor = db.cursor()
    sql="SELECT lecturename,reporter,location,ltime,signuptime,signup.lectureid FROM user,lecture,signup WHERE user.userid=signup.userid  AND signup.lectureid=lecture.lectureid   AND user.userid="+str(uid)+" ORDER BY signuptime DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    db.commit()
    if len(results)>0:
        List=[]
        for i in results:
           resi=dict()
           resi['lecturename']=i[0]
           resi['reporter']=i[1]
           resi['location']=i[2]
           resi['lecturetime']=i[3].strftime('%Y-%m-%d %H:%M')
           resi['signuptime']=i[4].strftime('%Y-%m-%d %H:%M')
           resi['lid']=i[5]
           List.append(resi)
    else:
        List=[]
    return json.dumps(List,ensure_ascii=False)
    

@app.route('/searchsignup',methods=['POST'])
def searchsignup():
    data=request.get_data()
    data=json.loads(data)
    currentpage= (int(data['page'])-1)*15
    userid = data['option']['userid']
    username  = data['option']['username']
    lecturename  = data['option']['lecturename']
    try:
       cursor = db.cursor()
       base="SELECT user.userid,user.username,lecture.lecturename,ltime,signuptime,lecture.lectureid FROM user,lecture,signup WHERE  user.userid=signup.userid AND lecture.lectureid=signup.lectureid  "
       sql=""
       if userid!='null':
           sql=sql+" AND user.userid = "+str(userid)
       if username!='null':
           sql=sql+" AND user.username like '%"+str(username)+"%' "
       if lecturename!='null':
           sql=sql+" AND lecture.lecturename like '%"+str(lecturename)+"%' "
       tsql=base+sql+" ORDER BY signuptime DESC LIMIT 15 OFFSET "+str(currentpage)
       cursor.execute(tsql)
       results = cursor.fetchall()
       db.commit()
       res=dict()
       List=[]
       if len(results)>0:
           for i in results:
              resi=dict()
              resi['userid']=i[0]
              resi['username']=i[1]
              resi['lecturename']=i[2]
              resi['lecturetime']=i[3].strftime('%Y-%m-%d %H:%M')
              resi['signuptime']=i[4].strftime('%Y-%m-%d %H:%M')
              resi['lid']=i[5]
              List.append(resi)
       res['list']=List
       sql="SELECT COUNT(*) FROM user,lecture,signup WHERE  user.userid=signup.userid AND lecture.lectureid=signup.lectureid  "+sql
       cursor.execute(sql)
       count= cursor.fetchone()
       db.commit()
       if len(count)>0:
            res['count']=count[0]
       else:
            res['count']=0
       
       return json.dumps(res,ensure_ascii=False)
    except:
       return "0"

@app.route('/searchstudent',methods=['POST'])
def searchstudent():
    data=request.get_data()
    data=json.loads(data)
    currentpage= (int(data['page'])-1)*15
    userid = data['option']['userid']
    name  = data['option']['name']
    sex  = data['option']['sex']
    try:
       cursor = db.cursor()
       base="SELECT * FROM user WHERE  roles!='admin' "
       sql=""
       if userid!='null':
           sql=sql+" AND userid = "+str(userid)
       if name!='null':
           sql=sql+" AND username like '%"+str(name)+"%' "
       if sex!='null':
           sql=sql+" AND sex = '"+str(sex)+"' "
       tsql=base+sql+"  LIMIT 15 OFFSET "+str(currentpage)
       cursor.execute(tsql)
       results = cursor.fetchall()
       db.commit()
       res=dict()
       List=[]
       if len(results)>0:
           for i in results:
              resi=dict()
              resi['userid']=i[0]
              resi['name']=i[3]
              resi['tel']=i[2]
              resi['sex']=i[4]
              resi['age']=i[5]
              List.append(resi)
       res['list']=List
       sql="SELECT COUNT(*) FROM user WHERE  roles!='admin' "+sql
       cursor.execute(sql)
       count= cursor.fetchone()
       db.commit()
       if len(count)>0:
            res['count']=count[0]
       else:
            res['count']=0
       
       return json.dumps(res,ensure_ascii=False)
    except:
       return "0"


@app.route('/delstudent',methods=['GET'])
def delstudent():
    uid=request.args.get('id')
    try:
        cursor = db.cursor()
        sql="DELETE FROM signup WHERE userid="+str(uid)
        cursor.execute(sql)
        db.commit()
        sql="DELETE FROM user WHERE userid="+str(uid)
        cursor.execute(sql)
        db.commit()
        return "0"
    except:
        return "0"












@app.route('/getalterinfo',methods=['GET'])
def getalterinfo():
    uid=request.args.get('id')
    try:
        cursor = db.cursor()
        sql="SELECT * FROM user WHERE userid="+str(uid)
        cursor.execute(sql)
        result=cursor.fetchone()
        db.commit()
        res=dict()
        res['id']=result[0]
        res['name']=result[3]
        res['phone']=result[2]
        res['age']=result[5]
        res['sex']=result[4]
        return json.dumps(res,ensure_ascii=False)
    except:
        return "0"


@app.route('/alteruser',methods=['POST',"GET"])
def alteruser():
    data=request.get_data()
    data=json.loads(data)
    uid = data['id']
    age = data['age']
    name  = data['name']
    phone = data['phone']
    sex = data['sex']
    try:
        cursor = db.cursor()
        sql="UPDATE user SET age='"+str(age)+"' , username='"+str(name)+"' , phone='"+str(phone)+"' , sex='"+str(sex)+ "' WHERE userid="+str(uid)
        cursor.execute(sql)
        db.commit()
        return  "0"
    except:
        return  "0"
    

@app.route('/alterpasswd',methods=["POST","GET"])
def alterpasswd():
    uid = request.form.get('id')
    pwd = request.form.get('pwd')
    try:
        cursor = db.cursor()
        sql="UPDATE user SET password="+str(pwd)+" WHERE userid="+str(uid)
        cursor.execute(sql)
        db.commit()
        return  "0"
    except:
        return  "0"
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001,debug=True)
