from sqlalchemy import Column, Integer, String
from shared.database import Base

class ToDoListClient(Base):
    __tablename__ = "ToDo_Client"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
