# from typing import Optional, List
# from uuid import UUID, uuid4
# from pydantic import BaseModel
# from enum import Enum


# SOLVED
# Q: How class works in Python
# A: Class it`s a blueprint of object (class instance) which contains properties (data) and methods (functions)  
# class Gender(str, Enum): # Q Why do we inharitate str and Enum
#     male = "male"
#     female = "female" 


# class Role(str, Enum):  # Q: Why do we inharitate str and Enum
#     admin = "admin"
#     user = "user"
#     student = "student"


# class User(BaseModel):
#     # Q: How syntax for next fieds works
#     id: Optional[UUID] = uuid4() # Q: Read about Union type
#     first_name: str
#     last_name: str
#     middle_name: Optional[str]  # Q: How does optional works? A: Optional is class in lib/typing
#     gender: Gender  # Why does Gender is not a list here?
#     roles: List[Role]  # Why does Role is a list?

# class UserFieldsForUpdate(BaseModel):
#     first_name: str
#     last_name: str
#     middle_name: Optional[str]
#     gender: Gender
#     roles: List[Role]


from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base  # Why do we use ".database" and not just "database"  


class User(Base):
    __tablename__ = "users"  # Q: __tablename__ - how is this works?
    # A: __tablename__ attribute tells SQLAlchemy the name of the table to use in the database for each of these models.
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(Boolean, default=True)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")


