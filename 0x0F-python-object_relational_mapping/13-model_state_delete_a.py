#!/usr/bin/python3
"""
fecth data using sql alchemy
deletes
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
    for ins in session.query(State).filter(State.name.like('%a%')):
        session.delete(ins)
        session.commit()
