from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum

# SOLVED
# Q: How class works in Python
# A: Class it`s a blueprint of object (class instance) which contains properties (data) and methods (functions)  
class Gender(str, Enum): # Q Why do we inharitate str and Enum
    male = "male"
    female = "female" 


class Role(str, Enum):  # Q: Why do we inharitate str and Enum
    admin = "admin"
    user = "user"
    student = "student"


class User(BaseModel):
    # Q: How syntax for next fieds works
    id: Optional[UUID] = uuid4() # Q: Read about Union type
    first_name: str
    last_name: str
    middle_name: Optional[str]  # Q: How does optional works? A: Optional is class in lib/typing
    gender: Gender  # Why does Gender is not a list here?
    roles: List[Role]  # Why does Role is a list?

class UserFieldsForUpdate(BaseModel):
    first_name: str
    last_name: str
    middle_name: Optional[str]
    gender: Gender
    roles: List[Role]