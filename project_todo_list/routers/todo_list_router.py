from fastapi import APIRouter, Depends
from pydantic import BaseModel, ConfigDict

controller = APIRouter(prefix='/todo_list')

class TodoList(BaseModel):
    id: int
    name: str
    description: str
    created_at: str
    updated_at: str
    deleted_at: str

    model_config = ConfigDict(
        orm_mode = True
    )