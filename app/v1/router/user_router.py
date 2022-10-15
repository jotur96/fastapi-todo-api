from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Body

from app.v1.model import user_model
from app.v1.service import user_service

from app.v1.utils.db import get_db


router = APIRouter(prefix="/app/v1")


@router.post(
    "/user/",
    tags=["users"],
    status_code=status.HTTP_201_CREATED,
    response_model=user_model.User,
    dependencies=[Depends(get_db)],
    summary="Create a new user"
)
def create_user(user: user_model.UserRegister = Body(...)):
    """
    # Create a new user in the app

    ### Args
    The app can recive next fields into a JSON
    - email: A valid email
    - username: Unique username
    - password: Strong password for autentication

    ### Returns
    - user: User info
    """

    return user_service.create_user(user)
