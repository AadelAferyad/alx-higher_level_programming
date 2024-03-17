#!/usr/bin/python3
"""
fetch data using sql alchemy
adds the State object “Louisiana” to the database hbtn_0e_6_usa
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
    state = State(name="Louisiana")
    session.add(state)
    session.commit()
    print(state.id)
