from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas
from app.database import get_db
from app.dependencies import get_current_user  
from app.models import User

router = APIRouter(prefix="/api/v1/user", tags=["user"])





# Get User Tasks (with pagination)
@router.get("/tasks", response_model=List[schemas.TaskOut])
def list_user_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return crud.get_user_tasks(db, current_user.id, skip=skip, limit=limit)


#  Filter User Tasks by Status
@router.get("/tasks/filter", response_model=List[schemas.TaskOut])
def filter_tasks(status: schemas.TaskStatus, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return crud.filter_tasks_by_status(db, current_user.id, status)

# Create Task
@router.post("/task", response_model=schemas.TaskOut)
def create_task(task: schemas.TaskBase, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return crud.create_task(db, task, current_user.id)


# Update Task
@router.patch("/{task_id}", response_model=schemas.TaskOut)
def update_task(task_id: int, task_data: schemas.TaskUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    task = crud.update_task(db, task_id, current_user.id, task_data)
    if task is None:
        raise HTTPException(status_code=403, detail="Forbidden or task not found")
    return task


#  Mark Task as Completed
@router.patch("/{task_id}/complete", response_model=schemas.TaskOut)
def complete_task(task_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    task = crud.mark_task_completed(db, task_id, current_user.id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found or not yours")
    return task


# Delete Task
@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if not crud.delete_task(db, task_id, current_user.id):
        raise HTTPException(status_code=403, detail="Forbidden or task not found")
    return {"message": "Deleted"}
