-- 1.计算每个学生有成绩的课程门数、平均成绩
SELECT SC.Sno,COUNT(SC.Cno),AVG(SC.Grade) FROM SC WHERE SC.Grade IS NOT NULL GROUP BY SC.Sno;

-- 2.使用GRANT 语句，把对基本表S、SC、C 的使用权限授给其它用户

CREATE USER 'test'@'%' IDENTIFIED BY 'test';
GRANT ALL PRIVILEGES ON S TO 'test'@'%';
GRANT ALL PRIVILEGES ON C TO 'test'@'%';
GRANT ALL PRIVILEGES ON SC TO 'test'@'%';

-- 3.实验完成后，撤消建立的基本表和视图
DROP VIEW MaleStudent;
DROP TABLE SC;
DROP TABLE C;
DROP TABLE S;