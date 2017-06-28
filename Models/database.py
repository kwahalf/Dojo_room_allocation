from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()
""" ORM for table People"""


class People(Base):
    __tablename__ = 'People'
    id = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(260))
    Role = Column(String(260))
    Room_allocated = Column(String(260), nullable=True)

""" ORM for table Rooms"""


class Rooms(Base):
    __tablename__ = 'Rooms'
    id = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(260), nullable=False)
    Purpose = Column(String(260), nullable=False)
    Occupants = Column(String(260), nullable=True)


engine = create_engine('sqlite:///dojo_database.db')
Base.metadata.create_all(engine)
