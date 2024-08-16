from sqlalchemy import Column, Integer, String, DateTime
from shared.database import Base
from datetime import datetime
class ToDoList(Base):
    __tablename__ = "todo_list"

    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = Column(DateTime, nullable=True)

    def __repr__(self):
        return f"TodoList(id={self.id}, description={self.description!r})"