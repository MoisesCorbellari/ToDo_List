from datetime import date
from fastapi import APIRouter, Depends
from pydantic import BaseModel, ConfigDict, Field
from project_todo_list.routers.todo_client_router import ToDoListClientResponse
from shared.dependencies import get_db
from sqlalchemy.orm import Session
from project_todo_list.models.todo_list_model import Task
from typing import List
from shared.exception import NotFound

router = APIRouter(prefix='/ToDo_List')

class ToDoListResponse(BaseModel):
    id: int
    title: str
    description: str
    created: date
    completed: bool
    todo: ToDoListClientResponse # import ToDoListClientResponse

    class Config:
        model_config = ConfigDict(
            from_attributes=True
        )

class ToDoListRequest(BaseModel):
    title: str = Field(min_length=3, max_length=30)
    description: str = Field(min_length=3, max_length=255)
    completed: bool = Field(default=False)
    task_client_id: int | None = None

@router.get("", response_model=List[ToDoListResponse])
def get_all_todo_list(db: Session = Depends(get_db)) -> List[ToDoListResponse]:
    return db.query(Task).all()

@router.get("/{id_task}", response_model=ToDoListResponse)
def get_todo_list_by_id(id_task: int,
                        db: Session = Depends(get_db)) -> List[ToDoListResponse]:
    todo_list: Task = find_todo_list_by_id(id_task, db)
    return todo_list

@router.post("", response_model=ToDoListResponse, status_code=201)
def create_todo_list(task_request: ToDoListRequest,
                     db: Session = Depends(get_db)) -> ToDoListResponse:
    todo_list = Task(
        **task_request.model_dump() 
    )
    
    db.add(todo_list) 
    db.commit() 
    db.refresh(todo_list) 
    return todo_list 

@router.put("/{id_task}", response_model=ToDoListResponse, status_code=200)
def update_todo_list_by_id(id_task: int,
                     task_request: ToDoListRequest,
                     db: Session = Depends(get_db)) -> ToDoListResponse:
    todo_list = find_todo_list_by_id(id_task, db)
    todo_list.title = task_request.title
    todo_list.description = task_request.description
    todo_list.completed = task_request.completed
    
    db.add(todo_list) 
    db.commit() 
    db.refresh(todo_list) 
    return todo_list 

@router.delete("/{id_task}", status_code=204)
def delete_todo_list_by_id(id_task: int,
                     db: Session = Depends(get_db)) -> None:
    todo_list = find_todo_list_by_id(id_task, db)

    db.delete(todo_list)
    db.commit()

def find_todo_list_by_id(id_task: int, db: Session) -> Task:
    todo_list = db.get(Task, id_task)
    if todo_list is None:
        raise NotFound(name="")
    
    return todo_list
