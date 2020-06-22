
-- 1.查询选修1 号课程的学生学号与姓名
SELECT S.Sno,Sname FROM  SC,S WHERE S.Sno=SC.Sno AND SC.Cno='1';


-- 2.查询选修课程名为数据结构的学生学号与姓名
SELECT S.Sno,Sname FROM  SC,S,C  WHERE S.Sno=SC.Sno AND SC.Cno=C.Cno AND C.Cname='数据结构';

-- 3.查询不选1 号课程的学生学号与姓名
SELECT S.Sno,S.Sname FROM  S  WHERE NOT EXISTS (SELECT * FROM SC WHERE SC.Sno=S.Sno AND SC.Cno='1');

-- 4.查询学习全部课程学生姓名
SELECT S.Sname FROM S WHERE NOT EXISTS 
	(SELECT *FROM C WHERE NOT EXISTS 
		(SELECT * FROM SC WHERE SC.Cno=C.Cno AND SC.Sno=S.Sno));



-- 5.查询所有学生除了选修1 号课程外所有成绩均及格的学生的学号和平均成绩，其结果按平均成绩的降序排列
SELECT SCX.Sno,AVG(SCX.Grade) FROM SC SCX GROUP BY SCX.Sno HAVING SCX.Sno IN
(SELECT S.Sno FROM S  WHERE NOT EXISTS
	(SELECT * FROM SC SCY WHERE SCY.Sno=S.Sno AND SCY.Cno!=1 AND SCY.Grade<60))  ORDER BY AVG(SCX.Grade) DESC;


--6.查询选修数据库原理成绩第2 名的学生姓名
SELECT S.Sname 
FROM   S,SC,C 
WHERE  S.Sno=SC.Sno AND C.Cno=SC.Cno AND C.Cname='数据库' ORDER BY SC.Grade DESC LIMIT 1,1;

SELECT S.Sname FROM SC,S,C WHERE SC.Sno=S.Sno AND SC.Cno=C.Cno AND  C.Cname='数据库' AND SC.Grade=
	(Select MAX(SC.Grade) FROM SC,C WHERE   SC.Cno=C.Cno AND  C.Cname='数据库' AND S.Sno=SC.Sno  AND   SC.Grade < 
		(SELECT MAX(SC.Grade) FROM SC,C WHERE SC.Cno=C.Cno AND  C.Cname='数据库'));


-- 7.查询所有3 个学分课程中有3 门以上（含3 门）课程获80 分以上（含80 分）的学生的姓名
SELECT S.Sname FROM  S WHERE  S.Sno IN 
	(SELECT SC.Sno FROM  SC,C WHERE SC.Cno=C.Cno AND C.Ccredit=3 AND SC.Grade>=80 GROUP BY SC.Sno HAVING  COUNT(*)>=3);
    
-- 8.查询选课门数唯一的学生的学号

SELECT Sno FROM SC X GROUP BY Sno 
	HAVING COUNT(*) NOT IN 
		(SELECT COUNT(*) FROM SC Y GROUP BY Y.Sno HAVING Y.Sno<>X.Sno);


--9.其余的一些操作
SELECT * FROM S WHERE S.Sname Like '李%';
SELECT * FROM S WHERE S.Sname Like '李_';
SELECT * FROM S WHERE S.Sname Like '李\_';

-- 并操作
SELECT * FROM S WHERE S.Sdept='IS' UNION  SELECT * FROM S WHERE S.Sage=19



