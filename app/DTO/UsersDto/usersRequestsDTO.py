from pydantic import BaseModel, Field

class LoginUserBody(BaseModel):
    email: str = "kareem@gmail.com"
    password : str = "123456"