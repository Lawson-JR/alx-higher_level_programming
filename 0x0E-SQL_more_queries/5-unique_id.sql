-- Script to create the table unique_id in the specified MySQL database

CREATE TABLE IF NOT EXISTS unique_id (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(256),
  PRIMARY KEY (id)
);
