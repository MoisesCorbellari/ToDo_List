from sqlalchemy import Column, Date, ForeignKey, Integer, String, Boolean, Text
from shared.database import Base
from datetime import date
from sqlalchemy.orm import relationship

class Task(Base):
    __tablename__ = "ToDo_List"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False) 
    description = Column(Text, nullable=False) 
    created = Column(Date, nullable=False, default=date.today)
    completed = Column(Boolean, nullable=False, default=False)

    task_client_id = Column(Integer, ForeignKey('ToDo_Client.id'), nullable=True) # parent table
    todo = relationship("ToDoListClient") # child table