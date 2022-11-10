#!/usr/bin/python3
"""adds new state to the database"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine(f"mysql+mysqldb://{argv[1]}:{argv[2]}\
                           @localhost/{argv[3]}")
    with Session(engine) as session:
        new = State(name="Louisiana")
        session.add(new)
        session.commit()
        print(f"{new.id}")
