#!/usr/bin/python3
"""Start link class to table in database."""
from sqlalchemy import Column, Integer, String, orm
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """A class representation of a state."""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    cities = orm.relationship(
        "City",
        backref="state",
        cascade="all, delete-orphan",
    )
