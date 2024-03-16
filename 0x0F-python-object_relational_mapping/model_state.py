#!/usr/bin/python3
""" model file, sql alchemy """

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ definition of a State  class """
    __tablename__ = 'states'

    id = Column(
        Integer,
        nullable=False,
        primary_key=True,
        autoincrement=True,
        unique=True
    )
    name = Column(String(128), nullable=False, )
