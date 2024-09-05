from sqlalchemy import Column, DateTime, Integer, String, Boolean
from shared.database import Base
import datetime
class task(Base):
    __tablename__ = "ToDo_List"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False) # task title
    description = Column(String) # task description
    created = Column(DateTime, nullable=False, default=datetime.date) # date of task created
    completed = Column(Boolean, nullable=False, default=True) # date of task completed
    
    def __repr__(self):
        return f"<Task(id={self.id}, title={self.title}, created_at={self.created_at}, completed={self.completed})>" # representação do objeto como string