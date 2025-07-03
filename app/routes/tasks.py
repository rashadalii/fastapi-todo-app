from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas
from app.database import get_db
from app.dependencies import get_current_user  
from app.models import User

router = APIRouter(prefix="/api/v1/tasks", tags=["task"])

@router.get("/", response_model=List[schemas.TaskOut])
def list_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return crud.get_all_tasks(db, skip=skip, limit=limit)


@router.get("/task_id", response_model=schemas.TaskOut)
def get_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user) ):
    task = crud.get_task_by_id(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


