#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa.
Safe from SQL injection and sorted by cities.id.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get arguments from command line
    username, password, db_name, state_name = sys.argv[1:5]

    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cur = db.cursor()

    # Parameterized query to avoid SQL injection
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC;
    """

    cur.execute(query, (state_name,))
    rows = cur.fetchall()

    # Print the results
    print(", ".join([row[0] for row in rows]))

    cur.close()
    db.close()

