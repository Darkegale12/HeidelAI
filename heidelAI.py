from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from db import SessionLocal
from models import UserModel

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class User(BaseModel):
    id: int
    name: str
    age: int

class UpdateUser(BaseModel):
    name: str
    age: int


@app.post("/users")
def create_user(user: User, db: Session = Depends(get_db)):
    db_user = UserModel(id=user.id, name=user.name, age=user.age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message": "User created successfully", "user": user}

@app.get("/users")
def get_all_users(db: Session = Depends(get_db)):
    return db.query(UserModel).all()

@app.get("/users/name/{name}")
def get_user_by_name(name: str, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.name == name).first()
    if not user:
        return {"error": "User not found"}
    return user

@app.get("/users/id/{user_id}")
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        return {"error": "User not found"}
    return user

@app.put("/users/{user_id}")
def update_user(user_id: int, updated_user: UpdateUser, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        return {"error": "User not found"}

    user.name = updated_user.name
    user.age = updated_user.age
    db.commit()
    return {"message": "User updated successfully", "user": user}

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        return {"error": "User not found"}

    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}

