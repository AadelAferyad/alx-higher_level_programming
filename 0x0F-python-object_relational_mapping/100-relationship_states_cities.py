#!/usr/bin/python3
"""
relationship
"""

if __name__ == "__main__":
    from sys import argv as av
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_state import State, Base
    from relationship_city import City

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                             av[1], av[2], av[3]))
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    state = State(name="California")
    city = City(name="San Francisco")
    state.st.append(city)
    session.add(state)
    session.add(city)
    session.commit()
