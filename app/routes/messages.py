
from typing import List
from fastapi import APIRouter, HTTPException, BackgroundTasks, status, Depends

import time
from datetime import datetime
from app.authentication import get_current_user

from app.config.db import messages
from app.models.messages import MessageModel
from app.DTO.MessagesDto.messagesRequestsDTO import QuestionMessageBody , ThumbsStateChangeBody
from app.DTO.MessagesDto.messagesResponsesDTO import MessageResponse

router = APIRouter(
    prefix="/messages",
    tags=["Messages"]
)


def ask_LLM_for_answer(message_id : int):
    # Simulate a task that takes 3 seconds
    time.sleep(3)
    print("Background task completed", message_id)
    messages[message_id].answer = f"answer for message {message_id}"
    messages[message_id].answeredAt = datetime.now()




@router.get("/listing", response_model=List[MessageResponse])
def get_all_messages_for_user(user = Depends(get_current_user)):
    current_user_messages =  list(filter(lambda message: message.createdBy == user.get('id'), messages))
    return current_user_messages
    
@router.get("/{message_id}", response_model= MessageResponse)
def get_message_by_id( message_id : int ,user = Depends(get_current_user)):
    try :
        message:MessageModel = messages[message_id]
        if(message.createdBy != user.get('id')):
            raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED, detail= "this not your message")
        
        return message
    except IndexError:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="message not found")
    
@router.post("/", status_code= status.HTTP_201_CREATED, response_model= MessageResponse)
def post_message(background_tasks: BackgroundTasks ,body : QuestionMessageBody, user = Depends(get_current_user)):
    new_message = MessageModel(createdBy= user.get('id'), question= body.question)
    messages.append(new_message)
    new_message.id = len(messages) -1
  
    background_tasks.add_task(ask_LLM_for_answer, message_id = new_message.id)

    return new_message



@router.post("/{message_id}/change-thumbs", status_code=status.HTTP_202_ACCEPTED, response_model= MessageResponse)
def change_thumb_state(body : ThumbsStateChangeBody, message_id : int ,user = Depends(get_current_user)):
    try :
        message:MessageModel = messages[message_id]
        if(message.createdBy != user.get('id')):
            raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED, detail= "this not your message")
        if(not message.answer):
             raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail= "the message not answered yet")
        message.thumbState = body.thumbState
        
        return message
    except IndexError:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="message not found")

