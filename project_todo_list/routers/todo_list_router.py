from datetime import date
from fastapi import APIRouter, Depends
from pydantic import BaseModel, ConfigDict, Field
from shared.dependencies import get_db
from sqlalchemy.orm import Session
from project_todo_list.models.todo_list_model import task
from typing import List
from shared.exceptions import NotFound
router = APIRouter(prefix='/ToDo_List')

class ToDoListResponse(BaseModel):
    id: int
    title: str
    description: str
    created: date
    completed: bool

    class Config:
        model_config = ConfigDict(
            from_attributes=True
        )

class ToDoListRequest(BaseModel):
    title: str = Field(min_length=3, max_length=30)
    description: str = Field(min_length=3, max_length=30)
    completed: bool = Field(default=False)

# busca e retorna todas as tarefas do banco de dados no formato ToDoListResponse através de uma rota GET.
@router.get("", response_model=List[ToDoListResponse])
def get_all_todo_list(db: Session = Depends(get_db)) -> List[ToDoListResponse]:
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
    
    db.add(todo_list) # adds the object to the session
    db.commit() # saves the object in the database
    db.refresh(todo_list) # updates the object in the session
    return todo_list # returns the object

@router.put("/{id_task}", response_model=ToDoListResponse, status_code=200)
def update_todo_list(id_task: int,
                     task_request: ToDoListRequest,
                     db: Session = Depends(get_db)) -> ToDoListResponse:
    todo_list = find_todo_list_by_id(id_task, db)
    todo_list.title = task_request.title
    todo_list.description = task_request.description
    todo_list.completed = task_request.completed
    
    db.add(todo_list) # adds the object to the session
    db.commit() # saves the object in the database
    db.refresh(todo_list) # updates the object in the session
    return todo_list # returns the object

@router.delete("/{id_task}", status_code=204)
def delete_todo_list(id_task: int,
                     db: Session = Depends(get_db)) -> None:
    todo_list = find_todo_list_by_id(id_task, db)

    db.delete(todo_list)
    db.commit()

def find_todo_list_by_id(id_task: int, db: Session) -> task:
    todo_list = db.get(task, id_task)
    if todo_list is None:
        raise NotFound('Task Not Found')
    
    return todo_list
