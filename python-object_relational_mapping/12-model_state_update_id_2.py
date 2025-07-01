#!/usr/bin/python3

"""This script connects to a MySQL database and updates
the name of the State object with id 2 to 'New Mexico'"""

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

    # Update a State object
    state_to_update = session.query(State).filter(State.id == 2).first()
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()
    else:
        print("State with id 2 not found")

    session.close()
