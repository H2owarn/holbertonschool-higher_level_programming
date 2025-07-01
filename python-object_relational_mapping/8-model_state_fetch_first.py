#!/usr/bin/python3

"""This script connects to a MySQL database and retrieves
the first State object from the 'states' table, sorted by id."""

import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
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


    # Query the first State object, sorted by id
    state = session.query(State).order_by(State.id).first()

    # Print the result
    if state:
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")

    session.close()
