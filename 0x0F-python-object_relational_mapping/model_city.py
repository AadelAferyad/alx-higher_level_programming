#!/usr/bin/python3
"""
new modle
"""
from model_state import Base
from sqlalchemy import Integer, Column, String, ForeignKey, MetaData
from sqlalchemy.orm import declarative_base

Base = declarative_base(metadata=MetaData())


class City(Base):
    """
    City class
    """
    __tablename__ = 'cities'

    id = Column(
        Integer,
        nullable=False,
        primary_key=True,
        autoincrement=True,
        unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(
        Integer,
        ForeignKey('states.id'),
        nullable=False)
