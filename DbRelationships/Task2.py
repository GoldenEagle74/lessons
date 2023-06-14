"""
Создайте модели базы данных работников it-компании
Таблица Работники содержит следующие столбцы: id,имя,стаж, должности
Таблица Должности содержит следующие столбцы: id, название, работники.
Напишите функции вывода всех должностей запрашиваемого работника, всех работников по должности, всех работников определенной должности со стажем больше 5.
"""
from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, DeclarativeBase

# Создание подключения к базе данных SQLite
engine = create_engine('sqlite:///employees.db')
Session = sessionmaker(bind=engine)

class Base (DeclarativeBase):
    pass

# Создание таблицы для связи между "Работниками" и "Должностями"
employee_position_association = Table('employee_position_association', Base.metadata,
    Column('employee_id', Integer, ForeignKey('employees.id')),
    Column('position_id', Integer, ForeignKey('positions.id'))
)

# Определение модели таблицы "Работники"
class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    experience = Column(Integer)
    positions = relationship("Position", secondary=employee_position_association, back_populates="employees")

# Определение модели таблицы "Должности"
class Position(Base):
    __tablename__ = 'positions'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    employees = relationship("Employee", secondary=employee_position_association, back_populates="positions")

# Создание таблиц в базе данных
Base.metadata.create_all(engine)

# Создание и добавление данных в таблицы
with Session(autoflush=False, bind=engine) as db:
    position1 = Position(name='Developer')
    position2 = Position(name='Manager')
    position3 = Position(name='Designer')
    position4 = Position(name='QA')

    employee1 = Employee(name='John', experience=7)
    employee2 = Employee(name='Alice', experience=3)
    employee3 = Employee(name='Bob', experience=9)
    employee4 = Employee(name='Eve', experience=5)

    employee1.positions.extend([position1, position2])
    employee2.positions.append(position1)
    employee3.positions.extend([position2, position3])
    employee4.positions.append(position4)

    db.add_all([position1, position2, position3, position4, employee1, employee2, employee3, employee4])
    db.commit()

# Функции для выполнения запросов

def get_employee_positions(employee_name):
    with Session(autoflush=False, bind=engine) as db:
        employee = db.query(Employee).filter_by(name=employee_name).first()
        if employee:
            positions = [position.name for position in employee.positions]
            return positions
        else:
            return []

def get_employees_by_position(position_name):
    with Session(autoflush=False, bind=engine) as db:
        position = db.query(Position).filter_by(name=position_name).first()
        if position:
            employees = [employee.name for employee in position.employees]
            return employees
        else:
            return []

def get_employees_by_position_experience(position_name):
    with Session(autoflush=False, bind=engine) as db:
        employees = db.query(Employee).join(employee_position_association).join(Position).filter(
            Position.name == position_name,
            Employee.experience > 5
        ).all()
        if employees:
            employees_list = [employee.name for employee in employees]
            return employees_list
        else:
            return []

# Пример использования функций

john_positions = get_employee_positions("John")
print(f"Должности работника John: {john_positions}")

developers = get_employees_by_position("Developer")
print(f"Работники по должности Developer: {developers}")

experienced_managers = get_employees_by_position_experience("Manager")
print(f"Работники по должности Manager со стажем больше 5: {experienced_managers}")
