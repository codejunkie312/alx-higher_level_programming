#!/usr/bin/python3
"""a script that creates the State “California” with
the City “San Francisco” from the database hbtn_0e_100_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City


if __name__ == "__main__":
    user, pwd, db = \
        sys.argv[1], sys.argv[2], sys.argv[3]
    url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    url = url.format(user, pwd, db)
    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    with Session() as session:
        new_state = State(name="California")
        new_city = City(name="San Francisco")
        new_state.cities.append(new_city)
        session.add(new_state)
        session.add(new_city)
        session.commit()

    engine.dispose()
