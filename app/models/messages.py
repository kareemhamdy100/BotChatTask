from datetime import datetime
from enum import Enum
from typing import List, Optional


class ThumbState(Enum):
    THUMBS_UP = "THUMBS_UP"
    THUMBS_DOWN = "THUMBS_DOWN"

class MessageModel:
    def __init__(
        self,
        question: str,
        createdBy: int,
        id: Optional[int] = None,
        answer: Optional[str] = None,
        thumbState: Optional[ThumbState] = None,
        createdAt: Optional[datetime] = None,
        updatedAt: Optional[datetime] = None,
        answeredAt: Optional[datetime] = None
    ):
        self.id = id
        self.question = question
        self.answer = answer
        self.createdBy = createdBy
        self.thumbState = thumbState
        self.createdAt = createdAt or datetime.now()
        self.updatedAt = updatedAt or datetime.now()
        self.answeredAt = answeredAt

    def __str__(self):
        return (
            f"id: {self.id}\n"
            f"Question: {self.question}\n"
            f"Answer: {self.answer}\n"
            f"Created By: {self.createdBy}\n"
            f"Thumb State: {self.thumbState}\n"
            f"Created At: {self.createdAt}\n"
            f"Updated At: {self.updatedAt}\n"
            f"Answered At: {self.answeredAt}"
        )

