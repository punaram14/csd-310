import mysql.connector


# name: Puna Poudel
# Assignment: module 7.2
# professor: Chandra Bobba
# due date: 07/07/2024


# Database connection
config = {
    'user': 'root',
    'password': 'root',
    'host': '127.0.0.1',
    'database': 'movies',
    'raise_on_warnings': True
}

def display_results(title, cursor):
    print(f"-- {title} --")
    for record in cursor:
        if title == "DISPLAYING Studio RECORDS":
            print(f"Studio ID: {record[0]}\nStudio Name: {record[1]}")
        elif title == "DISPLAYING Genre RECORDS":
            print(f"Genre ID: {record[0]}\nGenre Name: {record[1]}")
        elif title == "DISPLAYING Short Film RECORDS":
            print(f"Film Name: {record[0]}\nRuntime: {record[1]}")
        elif title == "DISPLAYING Director RECORDS in Order":
            print(f"Film Name: {record[0]}\nDirector: {record[1]}")
        print("")

try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    # Query 1: Select all fields from the studios table
    cursor.execute("SELECT studio_id, studio_name FROM studios")
    display_results("DISPLAYING Studio RECORDS", cursor)

    # Query 2: Select all fields from the genres table
    cursor.execute("SELECT genre_id, genre_name FROM genres")
    display_results("DISPLAYING Genre RECORDS", cursor)

    # Query 3: Select movie names with runtime less than two hours
    cursor.execute("SELECT film_name, film_runtime FROM films WHERE film_runtime < 120")
    display_results("DISPLAYING Short Film RECORDS", cursor)

    # Query 4: List of film names and directors, sorted by director
    cursor.execute("SELECT film_name, film_director FROM films ORDER BY film_director")
    display_results("DISPLAYING Director RECORDS in Order", cursor)

except mysql.connector.Error as err:
    print("Error:", err)
finally:
    if db.is_connected():
        cursor.close()
        db.close()
