from fastapi import APIRouter, HTTPException, Response, status
from sqlmodel import select

from src.models import Order
from src.db import SessionDep

router = APIRouter(prefix="/order")


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_order(session: SessionDep, order: Order):
    try:
        session.add(order)
        session.commit()
        session.refresh(order)

        return Response(
            content="Order created successfully", status_code=status.HTTP_201_CREATED
        )
    except Exception as e:
        print(e)
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to create order"
        )


@router.get("/", response_model=Order)
async def get_order(session: SessionDep, id: int) -> Order:
    order = session.get(Order, id)
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Order not found"
        )
    return order


@router.get("/orders", response_model=list[Order])
async def get_orders(session: SessionDep, limit: int = 10):
    try:
        statement = select(Order).limit(limit)
        orders = session.exec(statement=statement).all()
        return orders
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


@router.put("/", status_code=status.HTTP_200_OK)
async def update_order(session: SessionDep, id: int, order: Order):
    order = session.get(Order, id)
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Order not found"
        )

    try:
        session.add(order)
        session.commit()
        session.refresh(order)

        return Response(
            status_code=status.HTTP_200_OK, content="Order updated successfully"
        )
    except Exception as e:
        print(e)
        session.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


@router.delete("/", status_code=status.HTTP_200_OK)
async def delete_orders(session: SessionDep, id: int):
    order = session.get(Order, id)
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Order not found"
        )

    try:
        session.delete(order)
        return Response(
            status_code=status.HTTP_200_OK, content="Order deleted successfully"
        )
    except Exception as e:
        print(e)
        session.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
