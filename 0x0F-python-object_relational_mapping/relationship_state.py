#!/usr/bin/python3
""" model file, sql alchemy """
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base(metadata=MetaData())


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
    name = Column(String(128), nullable=False)
    st = relationship('City', backref='state',
                      cascade="all, delete-orphan")
