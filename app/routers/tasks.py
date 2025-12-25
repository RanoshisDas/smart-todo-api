from fastapi import APIRouter, HTTPException, status, Depends, Query
from typing import List, Optional
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse
from app.models.task import Task
from app.models.user import User
from app.utils.auth import get_current_user
from beanie.operators import In

router = APIRouter()

@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def create_task(
    task: TaskCreate,
    current_user: User = Depends(get_current_user)
):
    new_task = Task(
        **task.dict(),
        user_id=str(current_user.id)
    )
    await new_task.insert()
    return TaskResponse(**new_task.dict())

@router.get("/", response_model=List[TaskResponse])
async def get_tasks(
    status: Optional[str] = Query(None, regex="^(pending|in_progress|completed)$"),
    priority: Optional[str] = Query(None, regex="^(low|medium|high)$"),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    current_user: User = Depends(get_current_user)
):
    query = {"user_id": str(current_user.id)}
    
    if status:
        query["status"] = status
    if priority:
        query["priority"] = priority
    
    tasks = await Task.find(query).skip(skip).limit(limit).to_list()
    return [TaskResponse(**task.dict()) for task in tasks]

@router.get("/{task_id}", response_model=TaskResponse)
async def get_task(
    task_id: str,
    current_user: User = Depends(get_current_user)
):
    task = await Task.get(task_id)
    
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    
    if task.user_id != str(current_user.id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to access this task"
        )
    
    return TaskResponse(**task.dict())

@router.put("/{task_id}", response_model=TaskResponse)
async def update_task(
    task_id: str,
    task_update: TaskUpdate,
    current_user: User = Depends(get_current_user)
):
    task = await Task.get(task_id)
    
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    
    if task.user_id != str(current_user.id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to update this task"
        )
    
    update_data = task_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(task, field, value)
    
    await task.save()
    return TaskResponse(**task.dict())

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
    task_id: str,
    current_user: User = Depends(get_current_user)
):
    task = await Task.get(task_id)
    
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    
    if task.user_id != str(current_user.id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to delete this task"
        )
    
    await task.delete()
    return None