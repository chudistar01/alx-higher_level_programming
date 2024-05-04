#!/usr/bin/python3
"""
class definition of a State and an instance Base
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State
from model_city import City
if __name__ == "__main__":
    user_name = sys.arg[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    State.cities = relationship("City",
                                order_by=City.id, back_populates="state")

    connection = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    eng = create_engine(connection.format(user_name, password, db_name),
                        pool_pre_ping=True)
    
    Session = sessionmaker(bind=eng)
    session = Session()
    query = session.query(State, City).\
                     filter(City.state_id == State.id).all()
    for row in query:
        print("{}: ({}) {}".format(row[0].name, row[1].id, row[1].name)
