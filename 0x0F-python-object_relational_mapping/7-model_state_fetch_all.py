#!/usr/bin/python3
"""A script that lists all State objects from the database hbtn_0e_6_usa."""
import sys
from sqlalchemy import create_engine, text
from model_state import State, Base


if __name__ == "__main__":
    user, pwd, db = sys.argv[1], sys.argv[2], sys.argv[3]
    url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(user, pwd, db)
    engine = create_engine(url, pool_pre_ping=True)
    with engine.connect() as connection:
        query = text("SELECT * FROM states ORDER BY id ASC")
        states = connection.execute(query)
    if states:
        for state in states:
            print("{}: {}".format(state[0], state[1]))
    else:
        exit(1)
