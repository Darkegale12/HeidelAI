from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
    id: int
    name: str
    age: int

class UpdateUser(BaseModel):
    name: str
    age: int

@app.post("/users")
def create_user(user: User):
    users.append(user)
    return {"message": "User created successfully", "user": user}

@app.get("/users")
def get_all_users():
    return users

@app.get("/users/{user_id}")
def get_user_by_id(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    return {"error": "User not found"}

@app.put("/users/{user_id}")
def update_user(user_id: int, updated_user: UpdateUser):
    for user in users:
        if user.id == user_id:
            user.name = updated_user.name
            user.age = updated_user.age
            return {"message": "User updated successfully", "user": user}
    return {"error": "User not found"}

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return {"message": "User deleted successfully"}
    return {"error": "User not found"}
