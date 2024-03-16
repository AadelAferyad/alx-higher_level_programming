#!/usr/bin/python3
"""
fetch data using sqlalchemy
print only the first state
"""

if __name__ == "__main__":
    from sys import argv as av
    from model_state import State, Base
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                             av[1], av[2], av[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    count = session.query(State).count()
    message = ""
    if (count):
        first_state = session.query(State).first()
        message += str(first_state.id) + ": " + first_state.name
    else:
        message = "Nothing"
    print(message)
