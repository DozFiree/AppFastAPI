from pydantic import BaseModel
from typing import Optional

class UserLoginForm(BaseModel):
    email: str
    password: str

class UserCreteForm(BaseModel):
    email: str
    password: str
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    nick_name: Optional[str] = None
