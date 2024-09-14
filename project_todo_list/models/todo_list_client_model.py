from sqlalchemy import Column, Integer, String
from shared.database import Base

class ToDoListClient(Base):
    __tablename__ = "ToDo_List_Client"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255))
    