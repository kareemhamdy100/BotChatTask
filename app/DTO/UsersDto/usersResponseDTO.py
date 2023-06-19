from pydantic import BaseModel

class LoginUserResponse(BaseModel):
    token: str