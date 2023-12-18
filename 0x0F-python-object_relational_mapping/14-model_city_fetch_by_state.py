#!/usr/bin/python3
"""a script 14-model_city_fetch_by_state.py that prints
all City objects from the database hbtn_0e_14_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from model_city import City


if __name__ == "__main__":
    user, pwd, db = \
        sys.argv[1], sys.argv[2], sys.argv[3]
    url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    url = url.format(user, pwd, db)
    engine = create_engine(url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    with Session() as session:
        query = session.query(State, City)\
            .filter(State.id == City.state_id)\
            .order_by(City.id)\
            .all()
        for state, city in query:
            print("{}: ({}) {}".format(state.name, city.id, city.name))

    engine.dispose()
