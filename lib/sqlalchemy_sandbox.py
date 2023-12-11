#!/usr/bin/env python3

# imports
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase): # declarative base / A parent object 
    pass


# This type of class is called a data model
class Student(Base): # Needs to inherit from base object
    
    # table name as a class attribute
    __tablename__ = 'students'

    # Columns as class attributes with one as a PK
    id = Column(Integer(), primary_key=True)
    name = Column(String())

if __name__ == '__main__': # nice trick, so this executes only when the script is run directly
    
    engine = create_engine('sqlite:///students.db') # the engine point to local sqlite url file where db will be created
    Base.metadata.create_all(engine) # Tells engine that any models were created using base as parent 