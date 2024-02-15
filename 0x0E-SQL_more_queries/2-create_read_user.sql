-- This script creates the database hbtn_0d_2 and the user user_0d_2

SET @db_exists = (SELECT COUNT(*) FROM information_schema.SCHEMATA WHERE SCHEMA_NAME = 'hbtn_0d_2');

IF @db_exists = 0 THEN
    CREATE DATABASE hbtn_0d_2;
    SELECT 'Database hbtn_0d_2 created successfully!';
ELSE
    SELECT 'Database hbtn_0d_2 already exists!';
END IF;

SET @user_exists = (SELECT COUNT(*) FROM mysql.user WHERE user = 'user_0d_2');

IF @user_exists = 0 THEN
    CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
    GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
    FLUSH PRIVILEGES;
    SELECT 'User user_0d_2 created successfully!';
ELSE
    SELECT 'User user_0d_2 already exists!';
END IF;
