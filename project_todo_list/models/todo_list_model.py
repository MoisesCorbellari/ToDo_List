from sqlalchemy import Column, Integer, String
from shared.database import Base
class ToDoList(Base):
    __tablename__ = "ToDo_List"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, index=True) # task title
    description = Column(String, index=True) # task description
    created_at = Column(String) # date of task created
    updated_at = Column(String) # date of task updated
    deleted_at = Column(String) # date of task deleted
    status = Column(String) # task status (True ou False)
    type = Column(String) # task private or public (PUBLIC ou PRIVATE)