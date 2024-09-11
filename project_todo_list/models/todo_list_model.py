from sqlalchemy import Column, DateTime, Integer, String, Boolean
from shared.database import Base
from datetime import date
class task(Base):
    __tablename__ = "ToDo_List"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False) # task title
    description = Column(String(255)) # task description
    created = Column(DateTime, nullable=False, default=date.today) # date of task created
    completed = Column(Boolean, nullable=False, default=False) # task completed or not
    tipo = Column(String(255), nullable=False)