from RandomData import *
import pymysql
from faker import Faker
import time
from datetime import datetime
db = pymysql.connect(
    host='xxxxxxxx',
    port=3306,
    user='xxxxxxxxx',
    passwd='xxxxxxxxx',
    db='xxxxxxxxx',
    charset='utf8'
)



def RandomUser():
    test=RandomData()
    for i in range(90000):
        try:
            cursor = db.cursor()
            sql="INSERT INTO user VALUES (%s,%s,%s,%s,%s,%s,%s)"
            var=(str(test.getRandomUserID()),str(test.getRandomPassword()),str(test.getRandomPhone()),str(test.getRandomChineseName()),str(test.getRandomSex()),str(test.getRandomAge()),"editor")
            cursor.execute(sql,var)
            db.commit()
        except:
            pass


def RandomLecture():
    f=Faker(locale='zh_CN')
    for i in range(50):
        try:
            cursor = db.cursor()
            sql="INSERT INTO lecture (lecturename,reporter,location,ltime) VALUES (%s,%s,%s,%s)"
            var=(str(f.sentence()),str(f.name()),str(f.street_address()),str(str(f.date_between(start_date='now', end_date='+120d'))+" "+f.time()))
            cursor.execute(sql,var)
            db.commit()
        except:
            pass

RandomLecture()