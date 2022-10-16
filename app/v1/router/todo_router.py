from fastapi import APIRouter, Depends, Body
from fastapi import status
from fastapi import Query, Path

from typing import List, Optional

from app.v1.model import todo_model
from app.v1.service import todo_service
from app.v1.utils.db import get_db
from app.v1.model.user_model import User
from app.v1.service.auth_service import get_current_user


router = APIRouter(
    prefix="/api/v1/to-do",
)


@router.post(
    "/",
    tags=["to-do"],
    status_code=status.HTTP_201_CREATED,
    response_model=todo_model.Todo,
    dependencies=[Depends(get_db)]

)
def create_task(
        todo: todo_model.TodoCreate = Body(...),
        current_user: User = Depends(get_current_user)):
    return todo_service.create_task(todo, current_user)


@router.get(
    "/",
    tags=["to-do"],
    status_code=status.HTTP_200_OK,
    response_model=List[todo_model.Todo],
    dependencies=[Depends(get_db)]
)
def get_tasks(
        is_done: Optional[bool] = Query(None),
        current_user: User = Depends(get_current_user)):
    return todo_service.get_tasks(current_user, is_done)


@router.get(
    "/{task_id}",
    tags=["to-do"],
    status_code=status.HTTP_200_OK,
    response_model=todo_model.Todo,
    dependencies=[Depends(get_db)]
)
def get_task(
        task_id: int = Path(
            ...,
            gt=0),
        current_user: User = Depends(get_current_user)):
    return todo_service.get_task(task_id, current_user)


@router.patch(
    "/{task_id}/mark_done",
    tags=["to-do"],
    status_code=status.HTTP_200_OK,
    response_model=todo_model.Todo,
    dependencies=[Depends(get_db)]
)
def mark_task_done(
        task_id: int = Path(
            ...,
            gt=0),
        current_user: User = Depends(get_current_user)):
    return todo_service.update_status_task(True, task_id, current_user)


@router.patch(
    "/{task_id}/unmark_done",
    tags=["to-do"],
    status_code=status.HTTP_200_OK,
    response_model=todo_model.Todo,
    dependencies=[Depends(get_db)]
)
def unmark_task_done(
        task_id: int = Path(
            ...,
            gt=0),
        current_user: User = Depends(get_current_user)):
    return todo_service.update_status_task(False, task_id, current_user)


@router.delete(
    "/{task_id}/",
    tags=["to-do"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)]
)
def delete_task(
        task_id: int = Path(
            ...,
            gt=0),
        current_user: User = Depends(get_current_user)):

    return {'msg': 'Task deleted successfully.'}
