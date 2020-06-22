-- 1.建立男学生的视图，属性包括学号、姓名、选修课程名和成绩
CREATE VIEW MaleStudent(Sno,Sname,Cname,Grade) AS 
	SELECT  S.Sno,S.Sname,C.Cname,SC.Grade
    FROM   SC,S,C 
    WHERE  SC.Sno=S.Sno AND SC.Cno=C.Cno AND S.Ssex='男';
	

-- 2.在男学生视图中查询平均成绩大于80 分的学生学号与姓名
SELECT MaleStudent.Sno,MaleStudent.Sname FROM MaleStudent GROUP BY MaleStudent.Sno HAVING AVG(MaleStudent.Grade)>80;