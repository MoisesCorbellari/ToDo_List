from datetime import date
from fastapi import APIRouter, Depends
from pydantic import BaseModel, ConfigDict, Field
from enum import Enum
from shared.dependencies import get_db
from sqlalchemy.orm import Session
from project_todo_list.models.todo_list_model import task
from typing import List

router = APIRouter(prefix='/ToDo_List')

class TodoListResponse(BaseModel):
    id: int
    title: str
    description: str
    created: date
    completed: bool

    class Config:
        model_config = ConfigDict(
            from_attributes=True
        )

class ToDoListTipoEnum(str, Enum):
    PUBLIC = 'PUBLIC' # Implement the creation of public tasks
    PRIVATE = 'PRIVATE' # Implement private task creation

class TodoListRequest(BaseModel):
    title: str = Field(min_length=3, max_length=30)
    description: str = Field(min_length=3, max_length=30)
    completed: bool = Field(default=True)
    tipo: ToDoListTipoEnum = Field(default=ToDoListTipoEnum.PRIVATE)


@router.get('', response_model=TodoListResponse)
def get_todo_list(db: Session = Depends(get_db)) -> List[TodoListResponse]:
    return db.query(task).all()

@router.get('/{id_todo_list}', response_model=TodoListResponse)
def get_todo_list_by_id(id_todo_list: int, 
                  db: Session = Depends(get_db)) -> List[TodoListResponse]:
    todo_list: task = db.get(task, id_todo_list)
    return todo_list

@router.post('', response_model=TodoListResponse, status_code=201)
def create_todo_list(todo_list_request: TodoListRequest,
                    db: Session = Depends(get_db)) -> TodoListResponse:
    
    todo_list = task(
        **todo_list_request.model_dump() # named parameters to pass all attributes of the object
        )
    
    db.add(todo_list)
    db.commit()
    db.refresh(todo_list)

    return todo_list
