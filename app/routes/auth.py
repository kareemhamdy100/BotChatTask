
from fastapi import APIRouter, HTTPException, status
from app.authentication import create_access_token

from app.config.db import users
from app.DTO.UsersDto.usersRequestsDTO import LoginUserBody
from app.DTO.UsersDto.usersResponseDTO import LoginUserResponse

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/login" , response_model= LoginUserResponse)
def login(body : LoginUserBody):
    for user in users:
        email = user["email"]
        hashed_password = user["hashed_password"]
        if body.email == email and body.password == hashed_password:
            return {
                "token" : create_access_token(user)
            }
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

   