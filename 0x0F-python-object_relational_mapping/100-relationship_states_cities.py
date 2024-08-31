#!/usr/bin/python3
"""
    Write a script that lists all State objects
    from the database hbtn_0e_6_usa if its exists
"""
if __name__ == "__main__":

    import sys
    from relationship_city import City
    from relationship_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    arg = sys.argv

    engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost/{}'
                .format(arg[1], arg[2], arg[3]),
                pool_pre_ping=True
            )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    n_state = City(name='San Francisco', state=State(name='California'))
    session.add(n_state)

    session.commit()
    session.close()
