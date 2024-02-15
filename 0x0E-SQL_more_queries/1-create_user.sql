-- This script creates the MySQL server user user_0d_1

SET @user_exists = (SELECT COUNT(*) FROM mysql.user WHERE user = 'user_0d_1');

-- Create the user if it doesn't exist
IF @user_exists = 0 THEN
    CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
    GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
    FLUSH PRIVILEGES;
    SELECT 'User user_0d_1 created successfully!';
ELSE
    SELECT 'User user_0d_1 already exists!';
END IF;
