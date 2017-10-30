use kitep_db;
drop procedure if exists doWhile;
DELIMITER //  
CREATE PROCEDURE doWhile()   
BEGIN
DECLARE begining INT DEFAULT 1990;
DECLARE ending INT DEFAULT 2017;
WHILE begining <= ending DO
    INSERT INTO `books_years`(year) values (begining);
    SET begining = begining+1;
END WHILE;
END;
//  

CALL doWhile(); 