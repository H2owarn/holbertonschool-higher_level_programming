#!/usr/bin/python3

"""This script connects to a MySQL database and retrieves
all cities from the 'cities' table along with their states."""

import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_city import City
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    # Connect to MySQL using SQLAlchemy engine
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{dbname}',
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)

    # Create a session to interact with the DB
    Session = sessionmaker(bind=engine)
    session = Session()

    # Delete all State objects with the name 'a'
    cities = (
        session.query(State.name, City.id, City.name)
        .join(State, City.state_id == State.id)
        .all()
    )

    for city in cities:
        print(f"{city[0]}: ({city[1]}) {city[2]}")



    session.close()
