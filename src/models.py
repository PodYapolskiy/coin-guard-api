import datetime
from sqlmodel import SQLModel, Field


class Order(SQLModel, table=True):
    __tablename__ = "orders"

    id: int | None = Field(default=None, primary_key=True)
    address: str = Field(default=None, nullable=False)
    timestamp: datetime.datetime = Field(default=None, nullable=False)
    price: float = Field(default=None, nullable=False)
    amount: float = Field(default=None, nullable=False)
    order_type: str = Field(default=None, nullable=False)
    status: str = Field(default=None, nullable=False)
