from typing import Annotated
from fastapi import Depends
from sqlmodel import SQLModel, Session, create_engine

from src.config import cfg


# connection string
CONNECTION = cfg["timescaledb"]["connection"]

# sql engine
engine = create_engine(CONNECTION)


def create_orders_table():
    SQLModel.metadata.create_all(engine)


def drop_orders_table():
    SQLModel.metadata.drop_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
