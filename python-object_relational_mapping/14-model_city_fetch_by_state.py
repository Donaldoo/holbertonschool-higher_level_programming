#!/usr/bin/python3
"""lists all State objects from database hbtn_0e_6_usa"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine(f"mysql+mysqldb://{argv[1]}:{argv[2]}\
                           @localhost/{argv[3]}")
    with Session(engine) as session:
        statements = session.query(State, City).\
                   filter(State.id == City.state_id).order_by(City.id)
        for state, city in statements:
            print(f"{state.name}: ({city.id}) {city.name}")
