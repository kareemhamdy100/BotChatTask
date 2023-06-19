from typing import List
from fastapi import APIRouter, Depends

from app.DTO.MessagesDto.messagesResponsesDTO import MessageResponse
from app.authentication import  get_current_admin

from app.config.db import messages

router = APIRouter(
    prefix="/admin/messages",
    tags=["Admin-Messages"]
)


@router.get("/listing", response_model=List[MessageResponse])
def get_all_messages_for_user(user_id: int = None, admin_user = Depends(get_current_admin)):
    # TODO add filters and pagination
    if(user_id):
        user_messages =  list(filter(lambda message: message.createdBy == user_id, messages))
        return user_messages
    return messages