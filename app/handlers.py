from fastapi import APIRouter, Depends
from forms import UserLoginForm, UserLogin
from models import connect_db

route = APIRouter()

@route.get("/")
def index():
    return {"message": "Hello World"}

@route.post("/login")
def login(user: UserLoginForm = Depends(UserLogin), db: connect_db = Depends(connect_db)):
    return {"status": "success"}
