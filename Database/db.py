from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, Session


engine = create_engine("postgresql://postgres:postgres@localhost:38746/postgres")

class Base(DeclarativeBase): pass

# class Person(Base):
#     __tablename__ = "people"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     age = Column(Integer)

# Base.metadata.create_all(bind=engine)

# with Session(autoflush=False, bind=engine) as db:
#     tom = Person(name="Tom", age=38)
#     db.add(tom)
#     db.commit()

# with Session(autoflush=False, bind=engine) as db:
#     tom = db.query(Person).filter(Person.id==1).first(1)
#     if (tom != None):
#         print(f"{tom.id}.{tom.name} ({tom.age})")

#         tom.name = "Tomas"
#         tom.age = 22

#         db.commit()

class order(Base):
    __tablename__ = 'supply'

    supply_id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    amount = Column(Integer)

def show():
    with Session(autoflush=False, bind=engine) as db:
        films = db.query(order)
        for film in films: print(film.amount) 

show()