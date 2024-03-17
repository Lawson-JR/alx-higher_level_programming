#!/usr/bin/python3
""" Module for listing states from a MySQL database """
import MySQLdb
import sys

def list_states(username, password, database)
    # Connect to MySQl server
    db = MySQLdb.connect(host= 'localhost', port=3300, user=username, passwd=password, db=database)
    cursor = db.cursor()

    # Execute SQL query to fetch all states
    c.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows from the query result
    rows = cursor.fetchall()
    
    # Print the results
    for row in rows:
        print(row)

    # Close the database connection
    db.close()

# Example
if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
