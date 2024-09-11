from datetime import date
from fastapi import APIRouter, Depends
from pydantic import BaseModel, ConfigDict, Field
from shared.dependencies import get_db
from sqlalchemy.orm import Session
from project_todo_list.models.todo_list_model import task
from typing import List

router = APIRouter(prefix='/ToDo_List')

class ToDoListResponse(BaseModel):
    id: int
    title: str
    description: str
    created: date
    completed: bool
    tipo: str

    class Config:
        model_config = ConfigDict(
            from_attributes=True
        )

class ToDoListRequest(BaseModel):
    title: str = Field(min_length=3, max_length=30)
    description: str = Field(min_length=3, max_length=30)
    completed: bool = Field(default=True)
    tipo: str = Field(min_length=3, max_length=30)

# busca e retorna todas as tarefas do banco de dados no formato ToDoListResponse através de uma rota GET.
@router.get("", response_model=List[ToDoListResponse])
def get_todo_list(db: Session = Depends(get_db)) -> List[ToDoListResponse]:
    return db.query(task).all()

# define uma rota GET que busca uma tarefa específica no banco de dados pelo seu id_task (ID da tarefa).
@router.get("/{id_task}", response_model=ToDoListResponse)
def get_todo_list_by_id(id_task: int,
                        db: Session = Depends(get_db)) -> List[ToDoListResponse]:
    todo_list: task = db.get(task, id_task)
    return todo_list

@router.post("", response_model=ToDoListResponse, status_code=201)
def create_todo_list(task_request: ToDoListRequest,
                     db: Session = Depends(get_db)) -> ToDoListResponse:
    todo_list = task(
        **task_request.model_dump() # named parameters to pass all attributes of the object
    )
    
    db.add(todo_list)
    db.commit()
    db.refresh(todo_list)

    return todo_list