from fastapi import APIRouter, Depends, HTTPException

# from sqlalchemy.orm import Session

# from src.schemas import UserCreate, Token
# from src.models.user import User
# from src.auth import create_access_token

# from src.db import get_db
# from src.utils import hash_password, verify_password

router = APIRouter(prefix="/account")


# @router.post("/register", response_model=User)
# def register_user(user: UserCreate, db: Session = Depends(get_db)):
#     db_user = db.query(User).filter(User.email == user.email).first()
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     user_obj = User(email=user.email, hashed_password=hash_password(user.password))
#     db.add(user_obj)
#     db.commit()
#     db.refresh(user_obj)
#     return user_obj


# @router.post("/login", response_model=Token)
# def login_user(user: UserCreate, db: Session = Depends(get_db)):
#     db_user = db.query(User).filter(User.email == user.email).first()
#     if not db_user or not verify_password(user.password, db_user.hashed_password):
#         raise HTTPException(status_code=400, detail="Invalid credentials")
#     access_token = create_access_token(data={"sub": db_user.id})
#     return {"access_token": access_token, "token_type": "bearer"}
