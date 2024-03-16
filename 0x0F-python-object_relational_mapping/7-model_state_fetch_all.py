#!/usr/bin/python3
"""
fetch all data using sqlalchemy
"""

if __name__ == "__main__":
    from sys import argv as av
    from model_state import State, Base
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (av[1], av[2], av[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(State).order_by(State.id):
        print(str(instance.id) + ": " + instance.name)
