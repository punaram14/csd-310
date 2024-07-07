import mysql.connector

# name: Puna Poudel
# Assignment: module 8.2
# professor: Chandra Bobba
# due date: 07/07/2024


def show_films(cursor, title):
    print(f"-- {title} --")
    query = """
    SELECT film_name AS 'Film Name', film_director AS 'Director', genre.genre_name AS 'Genre Name', studio.studio_name AS 'Studio Name'
    FROM film 
    INNER JOIN genre ON film.genre_id = genre.genre_id 
    INNER JOIN studio ON film.studio_id = studio.studio_id;
    """
    cursor.execute(query)
    results = cursor.fetchall()
    for film in results:
        print(f"Film Name: {film[0]}\nDirector: {film[1]}\nGenre Name: {film[2]}\nStudio Name: {film[3]}\n")

# Database connection
config = {
    'user': 'root',
    'password': 'root',
    'host': '127.0.0.1',
    'database': 'movies',
    'raise_on_warnings': True
}

try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    # Display initial films
    show_films(cursor, "DISPLAYING FILMS")

    # Insert a new film with proper date format
    insert_query = """
    INSERT INTO film (film_name, film_director, film_releaseDate, film_runtime, genre_id, studio_id) 
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(insert_query, ('Inception', 'Christopher Nolan', '2010-07-16', 148, 1, 1))
    db.commit()
    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

    # Update film genre
    update_query = "UPDATE film SET genre_id = (SELECT genre_id FROM genre WHERE genre_name = 'Horror') WHERE film_name = 'Alien'"
    cursor.execute(update_query)
    db.commit()
    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE - Changed Genre to Horror")

    # Delete a film
    delete_query = "DELETE FROM film WHERE film_name = 'Gladiator'"
    cursor.execute(delete_query)
    db.commit()
    show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

except mysql.connector.Error as err:
    print("Error:", err)
finally:
    if db.is_connected():
        cursor.close()
        db.close()
