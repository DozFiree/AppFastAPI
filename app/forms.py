from pydantic import BaseModel

class UserLoginForms(BaseModel):
    email: str
    password: str

