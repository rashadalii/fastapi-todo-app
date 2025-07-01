from app import models



def create_task(db, task_data, user_id):
    task = models.Task(**task_data.dict(), user_id=user_id)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def get_all_tasks(db):
    return db.query(models.Task).all()

def get_user_tasks(db, user_id):
    return db.query(models.Task).filter(models.Task.user_id == user_id).all()

def get_task_by_id(db, task_id):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

def update_task(db, task_id, user_id, data):
    task = get_task_by_id(db, task_id)
    if task and task.user_id == user_id:
        for key, value in data.dict().items():
            setattr(task, key, value)
        db.commit()
        db.refresh(task)
        return task
    return None

def delete_task(db, task_id, user_id):
    task = get_task_by_id(db, task_id)
    if task and task.user_id == user_id:
        db.delete(task)
        db.commit()
        return True
    return False
