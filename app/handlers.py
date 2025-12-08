from fastapi import APIRouter, HTTPException
from fastapi import Depends

from AppFastAPI.app.forms import UserLoginForm
from AppFastAPI.app.model import connect_db, User
from AppFastAPI.app.util import get_password_hash

router = APIRouter()

@router.get('/')
def root():
    return {"message": "Hello World"}

@router.post('/login')
def login(user_form: UserLoginForm, datadase=Depends(connect_db)):
    user = datadase.query(User).filter_by(User.email==user_form.email).one_or_none()
    if not user or get_password_hash(user_form.password) != user.password:
        return {"message": "Login NOT Successfully"}
    return {"message": user.password}


@router.post('/user', name='create_user')
def create_user(user_form: UserLoginForm, datadase=Depends(connect_db)):
    exist_user = datadase.query(User.id).filter_by(email=user_form.email).one_or_none()
    if exist_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = User(
        email=user_form.email,
        password=get_password_hash(user_form.password),
        first_name=user_form.first_name,
        last_name=user_form.last_name,
        nick_name=user_form.nickname
    )
    datadase.add(new_user)
    datadase.commit()
    return {'new user id':new_user.id}
