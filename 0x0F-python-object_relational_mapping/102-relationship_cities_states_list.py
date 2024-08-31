#!/usr/bin/python3
"""
    Write a script that lists all State objects
    from the database hbtn_0e_6_usa if its exists
"""
if __name__ == "__main__":

    import sys
    from relationship_city import City
    from relationship_state import State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    arg = sys.argv

    engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost/{}'
                .format(arg[1], arg[2], arg[3]),
                pool_pre_ping=True
            )
    Session = sessionmaker(bind=engine)
    session = Session()

    res = session.query(City).order_by(City.id).all()

    for city in res:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()
