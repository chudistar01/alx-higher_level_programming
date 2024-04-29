#!/usr/bin/python3
"""
class definition of a State and an instance Base
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
             'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                         sys.argv[2],
                                                         sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_instance = session.query(State).filter_by(id=2).first()
    new_instance.name = 'New Mexico'
    session.commit()
