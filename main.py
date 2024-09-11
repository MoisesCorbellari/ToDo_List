import uvicorn
from fastapi import FastAPI
from project_todo_list.routers import todo_list_router

app = FastAPI()

@app.get("/")
def to_do_list() -> str:
    return "My ToDo List"

app.include_router(todo_list_router.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0',port=8000, log_level="info", reload=True)
    # reload=True: recarrega automaticamente a cada alteração salva na aplicação.
    # log_level="info": exibe mensagens informativas sobre o que acontece no servidor.