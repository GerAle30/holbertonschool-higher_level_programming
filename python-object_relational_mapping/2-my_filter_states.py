#!/usr/bin/python3
"""
This module contains a script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument using
MySQLdb.

The script connects to a MySQL database and executes a SELECT query with user
input using string formatting to filter states by exact name match.
Note: This approach is vulnerable to SQL injection attacks.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Get command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create cursor object
    cursor = db.cursor()

    # Execute SQL query with user input using format
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"
    cursor.execute(query.format(state_name))

    # Fetch all results
    results = cursor.fetchall()

    # Print results
    for row in results:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
