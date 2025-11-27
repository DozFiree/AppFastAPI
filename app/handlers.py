from fastapi import APIRouter, Depends
from forms import UserLoginForm
from models import connect_db

route = APIRouter()

@route.get("/")
def index():
    return {"message": "Hello World"}

@route.post("/login")
def login(user_forms: UserLoginForm, db: connect_db = Depends(connect_db)):
    return {
        "status": "success",
        "form": user_forms.emal,
        "database": database,
    }
