
--	建立教学数据库的三个基本表
CREATE TABLE S
(
    Sno     char(9)  PRIMARY KEY,
    Sname   char(20) UNIQUE,
    Ssex    char(2),
    Sage    smallint,
    Sdept   char(20),
    CONSTRAINT C1 CHECK(Ssex IN('男','女'))
);

CREATE TABLE C
(
    Cno     char(4)  PRIMARY KEY,
    Cname   char(40) NOT NULL,
    Cpno    char(4),
    Ccredit smallint,
    FOREIGN KEY (Cpno) REFERENCES C(Cno)
);

CREATE TABLE SC
(
   Sno   char(9),
   Cno   char(4),
   Grade smallint,
   PRIMARY KEY(Sno,Cno),
   FOREIGN KEY (Sno) REFERENCES S(Sno),
   FOREIGN KEY (Cno) REFERENCES C(Cno)
);


--	创建和删除索引

CREATE UNIQUE INDEX Stusno ON S(Sno);
CREATE UNIQUE INDEX Coucno ON C(Cno);
CREATE UNIQUE INDEX SCno On SC(Sno ASC,Cno DESC);

DROP   INDEX Coucno ON C;



-- 表的创建、修改、删除

CREATE TABLE Test
(
   Sno   char(9) PRIMARY KEY,
   Cno   char(4)
);

ALTER TABLE Test CHANGE COLUMN Cno  Cno INT ;

DROP TABLE Test;




--	数据插入操作

INSERT INTO S VALUES('201215121','李勇','男',20,'CS');
INSERT INTO S VALUES('201215122','刘晨','女',19,'CS');
INSERT INTO S VALUES('201215123','王敏','女',18,'MA');
INSERT INTO S VALUES('201215124','张立','男',19,'IS');


INSERT INTO C(Cno,Cname,Cpno,Ccredit) VALUES('2','数学',NULL,2);
INSERT INTO C(Cno,Cname,Cpno,Ccredit) VALUES('6','数据处理',NULL,2);
INSERT INTO C(Cno,Cname,Cpno,Ccredit) VALUES('4','操作系统','6',3);
INSERT INTO C(Cno,Cname,Cpno,Ccredit) VALUES('7','PASCAL语言','6',4);
INSERT INTO C(Cno,Cname,Cpno,Ccredit) VALUES('5','数据结构','7',4);
INSERT INTO C(Cno,Cname,Cpno,Ccredit) VALUES('1','数据库','5',4);
INSERT INTO C(Cno,Cname,Cpno,Ccredit) VALUES('3','信息系统','1',4);


INSERT INTO SC VALUES('201215121','1',92);
INSERT INTO SC VALUES('201215121','2',85);
INSERT INTO SC VALUES('201215121','3',88);
INSERT INTO SC VALUES('201215122','2',90);
INSERT INTO SC VALUES('201215122','3',80);