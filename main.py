import uvicorn
from fastapi import FastAPI
from project_todo_list.routers import todo_list_router

app = FastAPI()

@app.get("/")
def to_do_list() -> str:
    return "My ToDo List."

app.include_router(todo_list_router.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True, log_level="info")
    # uvicorn = starts an ASGI (Asynchronous Server Gateway Interface) web server.
    # main:app = string that indicates the entry point of the FastAPI application.
    # host='0.0.0.0': defines the IP address where the server will run.
    # reload=True: automatically reloads with each change saved in the application.
    # log_level="info": displays informative messages about what happens on the server.