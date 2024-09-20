import uvicorn
from fastapi import FastAPI
from project_todo_list.routers import todo_client_router, todo_list_router
from shared.exception import NotFound
from shared.exceptions_handler import not_found_exception_handler

app = FastAPI()

@app.get("/")
def to_do_list() -> str:
    return "Development ToDo List."

app.include_router(todo_list_router.router)
app.include_router(todo_client_router.router)
app.add_exception_handler(NotFound, not_found_exception_handler)

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
