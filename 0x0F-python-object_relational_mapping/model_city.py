#!/usr/bin/python3
"""
    A python file that contains the class definition of
    a State and an instance Base = declarative_base()

"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base
from sqlalchemy import ForeignKey


class City(Base):
    """Cities ORM Class """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
