from pydantic import BaseModel, constr
from datetime import datetime

class MessageResponse(BaseModel):
    id:int
    question: str
    answer: str = None
    thumbState: str = None
    createdBy: int 
    createdAt: datetime
    updatedAt: datetime
    answeredAt : datetime | None
    class Config():
        orm_mode = True


