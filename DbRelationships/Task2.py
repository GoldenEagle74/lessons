"""
Создайте модели базы данных работников it-компании
Таблица Работники содержит следующие столбцы: id,имя,стаж, должности
Таблица Должности содержит следующие столбцы: id, название, работники.
Напишите функции вывода всех должностей запрашиваемого работника, всех работников по должности, всех работников определенной должности со стажем больше 5.
"""
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# Создание подключения к базе данных SQLite
engine = create_engine('sqlite:///company.db')
Base = declarative_base()

# Определение моделей таблиц
class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    experience = Column(Integer)
    position_id = Column(Integer, ForeignKey('positions.id'))
    position = relationship("Position", back_populates="employees")

class Position(Base):
    __tablename__ = 'positions'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    employees = relationship("Employee", back_populates="position")

Base.metadata.create_all(engine)

# Функция для вывода всех должностей заданного работника
def print_employee_positions(employee_name):
	with Session(autoflush=False, bind=engine) as db:
    	employee = session.query(Employee).filter_by(name=employee_name).first()
    if employee:
        print(f"Должности для работника {employee.name}:")
        for position in employee.position:
            print(f"- {position.name}")
    else:
        print(f"Работник {employee_name} не найден.")

# Функция для вывода всех работников по должности
def print_employees_by_position(position_name):
    with Session(autoflush=False, bind=engine) as db:
    	position = session.query(Position).filter_by(name=position_name).first()
    if position:
        print(f"Работники на должности {position.name}:")
        for employee in position.employees:
            print(f"- {employee.name}")
    else:
        print(f"Должность {position_name} не найдена.")

# Функция для вывода всех работников определенной должности со стажем больше 5
def print_employees_by_position_and_experience(position_name):
    with Session(autoflush=False, bind=engine) as db:
    	employees = session.query(Employee).join(Position).filter(Position.name == position_name, Employee.experience > 5).all()
    if employees:
        print(f"Работники на должности {position_name} со стажем больше 5:")
        for employee in employees:
            print(f"- {employee.name}")
    else:
        print(f"Нет работников на должности {position_name} со стажем больше 5.")

# Пример использования функций
employee_name = input("Введите имя работника: ")
print_employee_positions(employee_name)

position_name = input("Введите название должности: ")
print_employees_by_position(position_name)

position_name = input("Введите название должности: ")
print_employees_by_position_and_experience(position_name)

