"""
Создайте модели базы данных с отношением 1 ко многим.
Читатель содержит столбцы : id,имя, список книг
Книга содержит столбцы: id,Название, автор.
1 читатель может иметь много книг.
Напишите функцию вывода всех книг для вводимого с клавиатуры читателя.
"""
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import Session, relationship
from sqlalchemy.ext.declarative import declarative_base

# Создание подключения к базе данных SQLite
engine = create_engine('sqlite:///library.db')
Base = declarative_base()

# Определение моделей таблиц
class Reader(Base):
    __tablename__ = 'readers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    books = relationship("Book", back_populates="reader")

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    reader_id = Column(Integer, ForeignKey('readers.id'))
    reader = relationship("Reader", back_populates="books")

Base.metadata.create_all(engine)


# Функция для вывода всех книг для заданного читателя
def print_books_for_reader(reader_name):
	with Session(autoflush=False, bind=engine) as db:
    	reader = db.query(Reader).filter_by(name=reader_name).first()
    if reader:
        print(f"Книги для читателя {reader.name}:")
        for book in reader.books:
            print(f"- {book.title} by {book.author}")
    else:
        print(f"Читатель {reader_name} не найден.")

# Пример использования функции
reader_name = input("Введите имя читателя: ")
print_books_for_reader(reader_name)


