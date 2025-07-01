#!/usr/bin/python3

"""This script connects to a MySQL database and inserts
a new State object into the 'states' table with the name 'Louisiana'"""

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

    # Create a new State object
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()


    # Print the result
    for state in session.query(State).filter(State.name == "Louisiana").all():
        print(f"{state.id}")

    session.close()
