#!/usr/bin/python3
"""This script connects to a MySQL database and retrieves
all State objects from the 'states' table that match a given name."""


import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL using SQLAlchemy engine
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{dbname}',
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)

    # Create a session to interact with the DB
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State with the name passed as argument
    states = (
        session.query(State)
        .filter(State.name == state_name)
        .order_by(State.id)
        .all()
    )

    # Print the result
    if states:
        for state in states:
            print(f"{state.id}")
    else:
        print("Not found")

    session.close()
