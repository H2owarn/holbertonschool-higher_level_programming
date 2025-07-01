#!/usr/bin/python3

"""This script connects to a MySQL database and deletes
all State objects with names containing the letter 'a'."""

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

    # Delete all State objects with the name 'a'
    states_to_delete = (
        session.query(State)
        .filter(State.name.like('%a%'))
        .all()
    )

    for state in states_to_delete:
        session.delete(state)

    session.commit()

    session.close()
