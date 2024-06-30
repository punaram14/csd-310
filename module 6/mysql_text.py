import mysql.connector

# Replace 'hostname', 'user', 'password', and 'database' with your details
config = {
    'user': 'root',
    'password': 'root',
    'host': '127.0.0.1',
    'database': 'movies',
    'raise_on_warnings': True
}

try:
    # Establish a database connection
    conn = mysql.connector.connect(**config)
    print("Connection established")

    # Create a cursor object
    cursor = conn.cursor()

    # Execute a query
    cursor.execute("SELECT * FROM your_table_name")

    # Fetch and print the results
    for row in cursor.fetchall():
        print(row)

except mysql.connector.Error as err:
    print("Error: ", err)
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("Connection closed")
