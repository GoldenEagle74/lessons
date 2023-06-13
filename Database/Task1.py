"""
Создайте базу данных фильмов состоящая из столбцов: id,название, год выпуска, жанр, рейтинг.
Создайте функции для добавления фильма в базу, получения всех фильмов, получение фильма по определенному году, обновления рейтинга, удаления фильма.
"""
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

# Создание соединения с базой данных
engine = create_engine('sqlite:///movies.db')

# Определение модели данных
Base = declarative_base()

class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    release_year = Column(Integer, nullable=False)
    genre = Column(String)
    rating = Column(Float)

# Создание таблицы (если не существует)
Base.metadata.create_all(engine)

# Функция для добавления фильма в базу данных
def add_movie(title, release_year, genre, rating):
		with Session(autoflush=False, bind=engine) as db:
		movie = Movie(title=title, release_year=release_year, genre=genre, rating=rating)
		db.add(movie)
		db.commit()

# Функция для получения всех фильмов
def get_all_movies():
	with Session(autoflush=False, bind=engine) as db:
		return db.query(Movie).all()

# Функция для получения фильма по определенному году
def get_movies_by_year(release_year):
	with Session(autoflush=False, bind=engine) as db:
		return db.query(Movie).filter_by(release_year=release_year).all()

# Функция для обновления рейтинга фильма
def update_movie_rating(movie_id, rating):
	with Session(autoflush=False, bind=engine) as db:
		movie = db.query(Movie).get(movie_id)
		if movie:
		    movie.rating = rating
		    db.commit()

# Функция для удаления фильма
def delete_movie(movie_id):
	with Session(autoflush=False, bind=engine) as db:
		movie = db.query(Movie).get(movie_id)
		if movie:
		    db.delete(movie)
		    db.commit()

# Пример использования функций
add_movie("The Shawshank Redemption", 1994, "Drama", 9.3)
add_movie("Pulp Fiction", 1994, "Crime", 8.9)
add_movie("Inception", 2010, "Sci-Fi", 8.8)

all_movies = get_all_movies()
print("All movies:")
for movie in all_movies:
    print(movie.title, movie.release_year, movie.genre, movie.rating)

movies_1994 = get_movies_by_year(1994)
print("Movies released in 1994:")
for movie in movies_1994:
    print(movie.title, movie.release_year, movie.genre, movie.rating)

update_movie_rating(1, 9.7)

delete_movie(2)

