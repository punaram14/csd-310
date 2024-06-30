-- Drop existing user if it exists
DROP USER IF EXISTS 'username'@'localhost';

-- Create new user with specified password
CREATE USER 'username'@'localhost' IDENTIFIED BY 'your_password';

-- Grant all privileges on all databases to the new user
GRANT ALL PRIVILEGES ON *.* TO 'username'@'localhost';
FLUSH PRIVILEGES;

-- Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS movies;
USE movies;

-- Drop existing tables if they exist
DROP TABLE IF EXISTS films, studios, genres;

-- Create Studios Table
CREATE TABLE studios (
    studio_id INT AUTO_INCREMENT PRIMARY KEY,
    studio_name VARCHAR(75) NOT NULL
);

-- Create Genres Table
CREATE TABLE genres (
    genre_id INT AUTO_INCREMENT PRIMARY KEY,
    genre_name VARCHAR(75) NOT NULL
);

-- Create Films Table
CREATE TABLE films (
    film_id INT AUTO_INCREMENT PRIMARY KEY,
    film_name VARCHAR(100) NOT NULL,
    film_releaseDate DATE,
    film_runtime INT,
    film_director VARCHAR(100),
    studio_id INT,
    genre_id INT,
    FOREIGN KEY (studio_id) REFERENCES studios(studio_id),
    FOREIGN KEY (genre_id) REFERENCES genres(genre_id)
);

-- Insert sample data into Studios
INSERT INTO studios (studio_name) VALUES ('Universal'), ('Warner Bros');

-- Insert sample data into Genres
INSERT INTO genres (genre_name) VALUES ('Action'), ('Drama');

-- Insert sample data into Films
INSERT INTO films (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) 
VALUES ('Film A', '2021-06-01', 120, 'Director A', 1, 1),
       ('Film B', '2021-06-15', 150, 'Director B', 2, 2);

-- Display the data to verify insertion
SELECT * FROM studios;
SELECT * FROM genres;
SELECT * FROM films;
