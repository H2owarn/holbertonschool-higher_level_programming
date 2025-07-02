#!/usr/bin/python3

"""This module defines the City class for use with SQLAlchemy ORM."""

from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey



class City(Base):
    """City class for SQLAlchemy ORM."""
    __tablename__ = 'cities'
    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        unique=True
    )
    name = Column(String(128), nullable=False)
    state_id = Column(
        Integer,
        ForeignKey('states.id'),
        nullable=False
    )
