-- Script to create the table id_not_null in the specified MySQL database

CREATE TABLE IF NOT EXISTS id_not_null (
  id INT NOT NULL DEFAULT 1,
  name VARCHAR(256)
);
