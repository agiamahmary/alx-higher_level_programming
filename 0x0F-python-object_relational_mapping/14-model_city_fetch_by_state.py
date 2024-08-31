#!/usr/bin/python3
"""
    Write a script that lists all State objects
    from the database hbtn_0e_6_usa if its exists
"""
if __name__ == "__main__":

    import sys
    from model_city import City
    from model_state import Base, State
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

    res = (
            session.query(State, City)
            .filter(State.id == City.state_id).order_by(City.id).all()
        )

    for state, city in res:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
