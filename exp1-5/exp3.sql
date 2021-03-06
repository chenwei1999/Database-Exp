
-- 1.把1号课程的非空成绩提高10％
UPDATE  SC SET SC.Grade=SC.Grade*1.1 WHERE SC.Cno='1' AND SC.Grade IS NOT NULL;

-- 2.在SC 表中删除课程名为数据结构的成绩的元组
DELETE FROM SC WHERE SC.Cno IN (SELECT C.Cno FROM C WHERE C.Cname='数据结构');

-- 3.在S 和SC 表中删除学号为201215122 的所有数据
DELETE FROM SC WHERE SC.Sno='201215122';
DELETE FROM S WHERE S.Sno='201215122';