from sqlalchemy import Column, Integer, String
from shared.database import Base

class ToDoList(Base):
    __tablename__ = "todo_list"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    description = Column(String(255))
    created_at = Column(String(255))
    updated_at = Column(String(255))
    deleted_at = Column(String(255))