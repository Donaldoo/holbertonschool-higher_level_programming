#!/usr/bin/python3
"""lists all State objecs from database hbtn_0e_6_usa"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine(f"mysql+mysqldb://{argv[1]}:{argv[2]}\
                           @localhost/{argv[3]}")
    with Session(engine) as session:
        statement = session.query(State).first()
        if statement:
            print(f"{statement.id}: {statement.name}")
        else:
            print("Nothing")
