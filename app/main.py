from fastapi import FastAPI
from app.models import Base
from app.database import engine
from app.routes import tasks,users



app = FastAPI()

# db setup
Base.metadata.create_all(bind=engine)

# routers
app.include_router(users.router) 
app.include_router(tasks.router)



