import sqlite3

conn = sqlite3.connect("cinema.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS reviews")
cur.execute("DROP TABLE IF EXISTS users")
cur.execute("DROP TABLE IF EXISTS movies")

cur.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
)
""")

cur.execute("""
CREATE TABLE movies (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    genre TEXT NOT NULL
)
""")

cur.execute("""
CREATE TABLE reviews (
    id INTEGER PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    movie_id INTEGER REFERENCES movies(id),
    rating INTEGER CHECK (rating >= 1 AND rating <= 10)
)
""")

users = [('Altan',), ('Aijan',), ('Bek',), ('Dana',), ('Ermek',)]
cur.executemany("INSERT INTO users (name) VALUES (?)", users)

movies = [
    ('Interstellar', 'Sci-Fi'),
    ('Dune', 'Sci-Fi'),
    ('Joker', 'Drama'),
    ('Home Alone', 'Comedy'),
    ('Avatar', 'Fantasy'),
]
cur.executemany("INSERT INTO movies (title, genre) VALUES (?, ?)", movies)

reviews = [
    (1, 1, 10),
    (1, 2, 9),
    (2, 1, 8),
    (2, 3, 7),
    (3, 2, 10),
    (3, 4, 6),
    (4, 3, 9),
    (4, 5, 8),
    (5, 1, 9),
    (5, 4, 7),
    (1, 5, 10),
    (2, 4, 8),
]
cur.executemany("INSERT INTO reviews (user_id, movie_id, rating) VALUES (?, ?, ?)", reviews)
conn.commit()

print("--- 1. Пользователь + Фильм + Оценка ---")
for row in cur.execute("""
    SELECT users.name, movies.title, reviews.rating
    FROM reviews
    JOIN users ON reviews.user_id = users.id
    JOIN movies ON reviews.movie_id = movies.id
"""):
    print(row)

print("\n--- 2. ВСЕ фильмы ---")
for row in cur.execute("""
    SELECT movies.title, reviews.rating
    FROM movies
    LEFT JOIN reviews ON movies.id = reviews.movie_id
"""):
    print(row)

print("\n--- 3. Средняя / Макс / Мин ---")
for row in cur.execute("""
    SELECT AVG(rating) AS avg_rating,
           MAX(rating) AS max_rating,
           MIN(rating) AS min_rating
    FROM reviews
"""):
    print(f"Средняя: {row[0]:.2f}, Макс: {row[1]}, Мин: {row[2]}")

conn.close()
print("\nГотово! База cinema.db создана")
