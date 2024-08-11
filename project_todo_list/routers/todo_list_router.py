from fastapi import APIRouter, Depends
from pydantic import BaseModel, ConfigDict
from enum import Enum
from shared.dependencies import get_db
from sqlalchemy.orm import Session

from project_todo_list.models.todo_list_model import ToDoList

router = APIRouter(prefix='/ToDo_List')

class TodoListResponse(BaseModel):
    id: int
    name: str
    description: str
    created_at: str
    updated_at: str
    deleted_at: str

    model_config = ConfigDict(
        from_attributes=True
    )

class TodoListTipoEnum(str, Enum):
    PUBLIC = 'PUBLIC'
    PRIVATE = 'PRIVATE'

class TodoListRequest(BaseModel):
    name: str = None
    description: str = None
    tipo: TodoListTipoEnum = TodoListTipoEnum.PUBLIC

@router.get('', response_model=TodoListResponse)
def get_todo_list(db=Depends(get_db)) -> TodoListResponse:
    return db.query(TodoListResponse).all()

@router.get('/{id_todo_list}', response_model=TodoListResponse)
def get_todo_list(id_todo_list: int, 
                  db=Depends(get_db)) -> list[TodoListResponse]:
    todo_list: ToDoList = db.get(ToDoList, id_todo_list)
    return todo_list

