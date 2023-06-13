"""
Создайте базу данных пользователя состояющую из следующих столбцов: id,username,password(В виде хэша).
Создайте программу которая предлагает пользователю зарегистрироваться или авторизироваться.
При регистрации программа запрашивает логин и пароль и добавляет в базу данных нового пользователя.
При авторизации программа запрашивает логин и пароль и выводит сообщение об успешной/неуспешной авторизации.
"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import hashlib

# Создание соединения с базой данных
engine = create_engine('sqlite:///users.db')
Session = sessionmaker(bind=engine)
session = Session()

# Определение модели данных
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)

    def set_password(self, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.password = hashed_password

    def check_password(self, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return self.password == hashed_password

# Создание таблицы (если не существует)
Base.metadata.create_all(engine)

# Функция для регистрации нового пользователя
def register():
    username = input("Введите логин: ")
    password = input("Введите пароль: ")

    user = session.query(User).filter_by(username=username).first()
    if user:
        print("Пользователь с таким логином уже существует.")
    else:
        new_user = User(username=username)
        new_user.set_password(password)
        session.add(new_user)
        session.commit()
        print("Регистрация успешно завершена.")

# Функция для авторизации пользователя
def login():
    username = input("Введите логин: ")
    password = input("Введите пароль: ")

    user = session.query(User).filter_by(username=username).first()
    if user and user.check_password(password):
        print("Авторизация успешна.")
    else:
        print("Неверный логин или пароль.")

# Главная функция программы
def main():
    while True:
        print("1. Зарегистрироваться")
        print("2. Авторизоваться")
        print("3. Выйти")
        choice = input("Выберите действие: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")

    session.close()

# Запуск программы
if __name__ == "__main__":
    main()

