CREATE or replace TABLE lecture
(lecture_id VARCHAR(10) NOT NULL	PRIMARY KEY ,
lecture_name CHAR(15),expirence INT);
INSERT INTO lecture 
VALUES  ('br301','phanikumar',10),
('br302','srinivas',6),
('br303','bhanukumar',3),
('br304','stella',5),
('br305','srinidhi',1),
('br306','nazma',7);
INSERT INTO lecture(lecture_id) VALUES('br307')
SELECT * FROM lecture;

CREATE OR replace TABLE branch_details
(branch_id CHAR(10) PRIMARY KEY ,branch_name VARCHAR(15));
INSERT INTO branch_details
VALUES ('cse123','computers'),('ece123','electronics'),
('eee123','electical'),('it123','it'),('mech123','mechanical');
SELECT * FROM branch_details

CREATE or replace TABLE lecturebranch 
(lecture_id VARCHAR(10) , branch_id CHAR(10),teaching_hours INT ,
FOREIGN KEY (lecture_id)  REFERENCES  lecture(lecture_id),
FOREIGN KEY (branch_id) REFERENCES branch_details(branch_id));
INSERT INTO lecturebranch(lecture_id,branch_id,teaching_hours)
VALUES 
('br303','cse123',10),
('br302','eee123',5),
('br301','cse123',7),
('br303','ece123',3);

SELECT * FROM branch_details;
SELECT * FROM lecture;
SELECT * FROM lecturebranch;

SELECT lecture_id,teaching_hours FROM lecturebranch;
SELECT lecture_id,teaching_hours FROM lecturebranch WHERE teaching_hours>=5 ;

CREATE or replace TABLE lecture_detail(salary INT , teaching_branch VARCHAR(20) NOT NULL , phone_no INT,
lecture_id CHAR(10), FOREIGN KEY(lecture_id) REFERENCES lecture(lecture_id));
INSERT INTO lecture_detail(salary,teaching_branch,phone_no,lecture_id)
VALUES
(20000,'ece',073254,'br301'),
(17000,'cse',073259,'br302'),
(25000,'ece',073257,'br303'),
(27000,'ece',073252,'br304'),
(16000,'cse',073251,'br305'),
(29000,'cse',073253,'br306');

CREATE or replace TABLE teaching_details(salary INT , teaching_branch VARCHAR(20) NOT null, phone_no INT,
lecture_id CHAR(10), FOREIGN KEY(lecture_id) REFERENCES lecture(lecture_id));
INSERT INTO teaching_details(salary,teaching_branch,phone_no,lecture_id)
VALUES
(20000,'ece',073254,'br301'),
(17000,'cse',073259,'br301'),
(25000,'eee',073257,'br301'),
(27000,'ece',073252,'br302'),
(16000,'cse',073251,'br302'),
(29000,'cse',073253,'br303');

SELECT * FROM teaching_details;
SELECT * FROM lecture_detail;
SELECT * FROM lecture;
SELECT * FROM lecturebranch;
SELECT * FROM branch_details;

/*inner_join*/

SELECT lecture_name,salary,teaching_branch,expirence FROM lecture l,lecture_detail ld WHERE l.lecture_id=ld.lecture_id;

/*outer_joins*/
   /*left_join*/

SELECT lecture_id,branch_name,teaching_hours FROM lecturebranch lb LEFT JOIN  branch_details bd  ON  lb.branch_id=bd.branch_id;

SELECT lecture_name,expirence,branch_id,teaching_hours FROM lecture l LEFT JOIN lecturebranch lb ON lb.lecture_id=l.lecture_id;

/*right join*/
SELECT lecture_name,expirence,branch_id,teaching_hours FROM lecturebranch lb RIGHT  JOIN lecture l ON lb.lecture_id=l.lecture_id;

/*full join PENDING */
SELECT * FROM lecture l FULL OUTER JOIN lecture_detail ld ON l.lecture_id=ld.lecture_id;

/*like & where */
SELECT * FROM lecture WHERE  lecture_name LIKE '%r';
SELECT * FROM lecture;
SELECT * FROM lecture WHERE  lecture_name LIKE 's%';
SELECT * FROM lecture WHERE  lecture_name LIKE '_r_%';
SELECT * FROM lecture WHERE  lecture_name LIKE '%';
SELECT * FROM lecture WHERE  lecture_name='srinivas';

/*groupby*/
SELECT * FROM teaching_details;
SELECT teaching_branch,COUNT(*) FROM teaching_details GROUP BY lecture_id;
SELECT lecture_id,SUM(salary) FROM teaching_details GROUP BY lecture_id;

/*max_ min average */
SELECT lecture_id,phone_no,MAX(salary) FROM teaching_details ;
SELECT lecture_id,phone_no,MIN(salary) FROM teaching_details ;
SELECT AVG(salary) FROM teaching_details ;

/*in,and or not between  operator*/
SELECT * FROM teaching_details WHERE teaching_branch IN('cse');
SELECT * FROM teaching_details WHERE salary BETWEEN 20000 AND  29000;
SELECT * FROM teaching_details WHERE salary>=20000 AND teaching_branch='ece';
SELECT * FROM teaching_details WHERE salary>=20000 OR  teaching_branch='ece';
SELECT * FROM teaching_details WHERE salary!=20000 AND teaching_branch!='ece';

UPDATE teaching_details SET phone_no=405880625 WHERE salary=17000 AND teaching_branch='cse';


/*one-one*/

SELECT * FROM lecture JOIN lecture_detail;
SELECT * FROM lecture;
SELECT * FROM lecture_detail;
SELECT * FROM lecture natural JOIN lecture_detail;

SELECT * FROM lecture JOIN lecture_detail WHERE lecture.lecture_id=lecture_detail.lecture_id;

SELECT * FROM lecture JOIN lecture_detail WHERE lecture_detail.salary>17000;
SELECT * FROM lecture JOIN lecture_detail WHERE lecture_detail.salary<17000;
SELECT * FROM lecture JOIN lecture_detail WHERE lecture.lecture_name='srinivas' AND lecture_detail.teaching_branch='cse';

SELECT * FROM lecture l JOIN lecture_detail ld WHERE l.lecture_id=ld.lecture_id AND ld.salary<=20000 ;
SELECT lecture_name,salary,teaching_branch FROM lecture l JOIN lecture_detail ld WHERE l.lecture_id=ld.lecture_id AND ld.salary<=20000 ;

SELECT * FROM lecture JOIN lecture_detail USING(lecture_id) WHERE lecture.expirence>5;

/*one to many*/
SELECT * FROM lecture natural JOIN teaching_details;
SELECT * FROM lecture;
SELECT * FROM teaching_details;

/*mant to many*/
SELECT * FROM lecture INNER JOIN lecturebranch INNER JOIN teaching_details ;
SELECT * FROM lecture INNER JOIN lecturebranch INNER JOIN teaching_details GROUP BY teaching_branch='cse';
SELECT teaching_branch,COUNT(*) FROM lecture INNER JOIN lecturebranch INNER JOIN teaching_details GROUP BY teaching_branch;
SELECT teaching_branch,COUNT(*) FROM lecture INNER JOIN lecturebranch INNER JOIN teaching_details GROUP BY teaching_branch='cse';
SELECT teaching_branch,COUNT(*) FROM lecture INNER JOIN lecturebranch INNER JOIN teaching_details 
GROUP BY teaching_branch ORDER BY teaching_branch ASC  ;