from fastapi import APIRouter, Depends
from pydantic import BaseModel, ConfigDict, Field
from enum import Enum
from shared.dependencies import get_db
from sqlalchemy.orm import Session
from project_todo_list.models.todo_list_model import ToDoList
from typing import List

router = APIRouter(prefix='/ToDo_List')

class TodoListResponse(BaseModel):
    id: int
    title: str
    description: str
    created_at: str
    updated_at: str
    deleted_at: str
    status: str
    type: str

    model_config = ConfigDict(
        from_attributes=True
    )

class ToDoListTipoEnum(str, Enum):
    PUBLIC = 'PUBLIC' # ToDo - Implementar a criação de tarefas publicas
    PRIVATE = 'PRIVATE' # ToDo - Implementar a criação de tarefas privadas  

class TodoListRequest(BaseModel):
    name: str = Field(min_length=3, max_length=30)
    description: str = Field(min_length=3, max_length=30)
    tipo: ToDoListTipoEnum

@router.get('', response_model=TodoListResponse)
def get_todo_list(db: Session = Depends(get_db)) -> List[TodoListResponse]:
    return db.query(ToDoList).all()

@router.get('/{id_todo_list}', response_model=TodoListResponse)
def get_todo_list_by_id(id_todo_list: int, 
                  db: Session = Depends(get_db)) -> List[TodoListResponse]:
    todo_list: ToDoList = db.get(ToDoList, id_todo_list)
    return todo_list

@router.post('', response_model=TodoListResponse, status_code=201)
def create_todo_list(todo_list_request: TodoListRequest,
                    db: Session = Depends(get_db)) -> TodoListResponse:
    
    todo_list = ToDoList(
        **todo_list_request.model_dump() # parametros nomeados para passar todos os atibutos do objeto
        )
    
    db.add(todo_list)
    db.commit()
    db.refresh(todo_list)

    return todo_list
