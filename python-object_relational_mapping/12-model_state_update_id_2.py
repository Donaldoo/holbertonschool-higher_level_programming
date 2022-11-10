#!/usr/bin/python3
"""updates a state from the database"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine(f"mysql+mysqldb://{argv[1]}:{argv[2]}\
                           @localhost/{argv[3]}")
    with Session(engine) as session:
        session.query(State).filter(State.id == 2).\
                update({State.name: "New Mexico"}, synchronize_session='fetch')
        session.commit()
