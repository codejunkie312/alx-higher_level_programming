#!/usr/bin/python3
"""tart link class to cities table in database."""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import State, Base


class City(Base):
    """A class representation of a city."""

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
