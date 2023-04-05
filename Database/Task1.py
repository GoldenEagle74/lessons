"""
Создайте базу данных фильмов состоящая из столбцов: id,название, год выпуска, жанр, рейтинг.
Создайте функции для добавления фильма в базу, получения всех фильмов, получение фильма по определенному году, обновления рейтинга, удаления фильма.
"""
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float
from sqlalchemy.orm import DeclarativeBase, Session

engine = create_engine("sqlite:///sqlite.db")

class Base(DeclarativeBase): pass

class Movies(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    date = Column(DateTime)
    genre = Column(String)
    rate = Column(Float)

def create(f_name, f_date, f_genre, f_rate):
    with Session(autoflush=False, bind=engine) as db:
        film = Movies(name=f_name, date=f_date, genre=f_genre, rate=f_rate)
        db.add(film)
        db.commit()

def show():
    with Session(autoflush=False, bind=engine) as db:
        films = db.query(Movies)
        for film in films: print(film.name) 

def show_date():
