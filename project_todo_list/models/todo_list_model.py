from sqlalchemy import Column, DateTime, Integer, String, Boolean
from shared.database import Base
from datetime import date

# task model
class task(Base):
    __tablename__ = "ToDo_List"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    description = Column(String(255)) 
    created = Column(DateTime, nullable=False, default=date.today)
    completed = Column(Boolean, nullable=False, default=False)