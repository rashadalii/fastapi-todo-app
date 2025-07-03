from fastapi import FastAPI
from app.routes import auths, users, tasks
from app.database import Base, engine

app = FastAPI(title="Andersen TODO List", version="0.1.0")

Base.metadata.create_all(bind=engine)

# Register routers
app.include_router(auths.router)
app.include_router(users.router)
app.include_router(tasks.router)
