#!/usr/bin/python3
"""
fecth
"""

if __name__ == "__main__":
    from sys import argv as av
    from model_city import City
    from model_state import State, Base
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                             av[1], av[2], av[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    data = session.query(State, City).filter(State.id == City.state_id).all()
    for city, state in data:
        print("{}: ({}) {}".format(city.name, city.id, state.name))
