from fastapi import FastAPI

from app.routes import auth, messages , adminMessages
app = FastAPI()


app.include_router(adminMessages.router)
app.include_router(auth.router)
app.include_router(messages.router)
