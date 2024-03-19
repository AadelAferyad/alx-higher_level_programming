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
    Session = sessionmaker(bind=engine)
    session = Session()
    data = (session.query(City, State).
            join(State, City.state_id == State.id).order_by(City.id).all())
    for city, state in data:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
