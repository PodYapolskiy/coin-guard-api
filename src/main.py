from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.routers import routers
from src.db import create_orders_table, drop_orders_table


@asynccontextmanager
async def on_startup(app: FastAPI):
    drop_orders_table()
    create_orders_table()
    # print("On startup")
    yield
    # print("On shutdown")


app = FastAPI(lifespan=on_startup)


@app.get("/")
async def index():
    return {"message": "Welcome to the Crypto Exchange API"}


for router in routers:
    app.include_router(router)
