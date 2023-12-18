#!/usr/bin/python3
"""A script that lists all State objects that contain
the letter a from hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base


if __name__ == "__main__":
    user, pwd, db = sys.argv[1], sys.argv[2], sys.argv[3]
    url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(user, pwd, db)
    engine = create_engine(url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    with Session() as session:
        states = session\
            .query(State)\
            .order_by(State.id)\
            .filter(State.name.like('%a%'))
    if states:
        for state in states:
            print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")
    engine.dispose()
