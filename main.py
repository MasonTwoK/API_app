from fastapi import FastAPI, HTTPException  # Here we import FastAPI class from \.venv\Lib\site-package\fastapi SOLVED
from models import User, Gender, Role
from typing import List
from uuid import UUID

# SOLVED
# Q: What is going on here?
# A: We create instance of class FastAPI which is named app
app = FastAPI()

# Q: Who does ':' works?
db: List[User] = [
    User(
        id="4b6c2f2a-445b-40fe-a585-a4bbb7314c8c",
        first_name="Jamila",
        last_name="Ahmed",
        gender=Gender.female,
        roles=[Role.student]
    ),
    User(
        id="7c37e10a-7f8d-48bc-b863-38577b592acb",
        first_name="Alex",
        last_name="Jones",
        gender=Gender.male,
        roles=[Role.admin, Role.student]
    )
]

# SOLVED
# Q: What is @ ?
# A: @ is decorator. Video which explains it https://youtu.be/r7Dtus7N4pI
@app.get("/")
async def root(): # Q Read about async
    return {"Hello": "World"}


@app.get("/api/v1/users")  # Q: In which part of get users implements.. ?
async def fetch_users():  # Q: Read about async https://fastapi.tiangolo.com/async/ ?
    return db


@app.get("/api/v1/users/{user_id}")
async def fetch_user_by_id(user_id: UUID):
    for user in db:
        if user.id == user_id:
            return user


@app.delete("/api/v1/users/{user_id}")
async def delete_user_by_id(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
        # Why if I put return out of if statement code block method will not return anything
        
    # Q: How does raise work?
    # Q: How can we just add 2 parameters into class with out creating instance? 
    raise HTTPException( 
        status_code=404,
        detail=f"User with id: {user_id} does not exists"
    )


# Q: Take a close look..
@app.post("/api/v1/users")
async def registrate_user(user: User):
    db.append(user)
    return {"id": user.id}  # Q: What is {} ? ..probably dictionary  


# Q: Disocver difference between PATCH and PUT 
@app.patch("/api/v1/users/{user_id}")
async def update_id_data(user_id: UUID, patched_user: User):
    for user in db:
        if  user.id == user_id:
            db.remove(user)
            db.append(patched_user)
            return  {"id": patched_user.id}