--  creates the database hbtn_0d_2 and the user user_0d_2


CREATE USER IF NOT EXISITS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
GRANT SELECT, On hbtn_0d_2.* TO 'user_0d_2'@'localhost';