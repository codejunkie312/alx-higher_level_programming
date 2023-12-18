#!/usr/bin/python3
"""a script that prints the State object with the name
passed as argumentfrom the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base


if __name__ == "__main__":
    user, pwd, db, state_name = \
        sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(user, pwd, db)
    engine = create_engine(url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    with Session() as session:
        state = session\
            .query(State)\
            .order_by(State.id)\
            .filter(State.name == state_name)\
            .first()
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")
    engine.dispose()
