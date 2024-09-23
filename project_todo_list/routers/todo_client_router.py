from typing import List
from fastapi import APIRouter, Depends
from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy.orm import Session
from project_todo_list.models.todo_client_model import ToDoListClient
from shared.dependencies import get_db
from shared.exception import NotFound

router = APIRouter(prefix='/ToDo_Client')

class ToDoListClientResponse(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(
        from_attributes=True
    )

class ToDoListClientRequest(BaseModel):
    name: str = Field(min_length=3, max_length=255)

@router.get("/", response_model=List[ToDoListClientResponse])
def get_all_todo_client(db: Session = Depends(get_db)) -> List[ToDoListClientResponse]:
    return db.query(ToDoListClient).all()

@router.get("/{id_task_client}", response_model=ToDoListClientResponse)
def get_todo_client_by_id(id_task_client: int,
                                   db: Session = Depends(get_db)) -> List[ToDoListClientResponse]:
    return find_todo_client_by_id(id_task_client, db)

@router.post("/",response_model=ToDoListClientResponse, status_code=201)
def create_todo_client(task_client_request: ToDoListClientRequest,
                                  db: Session = Depends(get_db)) -> ToDoListClientResponse:
    todo_list_client = ToDoListClient(
        **task_client_request.model_dump()
    )
    
    db.add(todo_list_client)
    db.commit()
    db.refresh(todo_list_client)
    
    return todo_list_client

@router.put("/{id_task_client}", response_model=ToDoListClientResponse, status_code=200)
def update_todo_client_by_id(id_task_client: int,
                                  task_client_request: ToDoListClientRequest,
                                  db: Session = Depends(get_db)) -> ToDoListClientResponse:
    todo_list_client = find_todo_client_by_id(id_task_client, db)
    todo_list_client.title = task_client_request.title

    db.add(todo_list_client)
    db.commit()
    db.refresh(todo_list_client)

    return todo_list_client

@router.delete("/{id_task_client}", status_code=204)
def delete_todo_client_by_id(id_task_client: int,
                                  db: Session  = Depends(get_db)) -> None:
    todo_list_client = find_todo_client_by_id(id_task_client, db)
    
    db.delete(todo_list_client)
    db.commit()

def find_todo_client_by_id(id_task_client: int, db: Session) -> ToDoListClient:
    todo_list_client = db.get(ToDoListClient, id_task_client)

    if todo_list_client is None:
        raise NotFound(name="")
    
    return todo_list_client