from pydantic import BaseModel, constr

from enum import Enum



class ThumbStateEnum(str, Enum):
    THUMBS_UP = "THUMBS_UP"
    THUMBS_DOWN = "THUMBS_DOWN"

class QuestionMessageBody(BaseModel):
    question: constr(min_length=4, max_length=1000)


class ThumbsStateChangeBody(BaseModel):
     thumbState : ThumbStateEnum