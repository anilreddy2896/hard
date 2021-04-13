SELECT * FROM teaching_details;

/*creating procedure*/
DELIMITER $$
CREATE or replace PROCEDURE  avg_sal()
BEGIN 
SELECT AVG(salary) AS average_salary FROM teaching_details;
END $$
DELIMITER;

/*calling procedure*/
CALL avg_sal();

/*deleting procedure*/
DROP PROCEDURE avg_sal;

DROP PROCEDURE  if EXISTS avg_sal; 



SELECT * FROM lecturebranch; 
SELECT * FROM lecture;
/*with parameters*/

delimiter $$
CREATE PROCEDURE working_hours(IN a VARCHAR , OUT b INT )
BEGIN 
SELECT teaching_hours INTO b FROM lecturebranch WHERE lecturebranch.lecture_id=a;
END $$
delimiter ;
