from fastapi import FastAPI  # Here we import FastAPI class from \.venv\Lib\site-package\fastapi SOLVED
from models import User, Gender, Role
from typing import List
from uuid import UUID, uuid4

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


@app.get("/api/v1/users")  # Q: In which part of get users implements.. 
async def users():  # Q: Read about async https://fastapi.tiangolo.com/async/
    return db


# Q: Take a close look..
@app.post("/api/v1/users")
async def registrate_user(user: User):
    db.append(user)
    return {"id": user.id}
