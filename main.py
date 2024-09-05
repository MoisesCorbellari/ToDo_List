'''
## Objetivos

Criar o backend ToDo LIST (Lista de tarefas), usando o FastAPI

> Definir o modelo de dados para as tarefas.
> 
- [ ]  Criar a estrutura básica do projeto.
- [ ]  Configurar a conexão com o banco de dados (utilizando uma ORM).
- [ ]  Criar a Rota GET para pegar TODAS as tarefas registradas.
- [ ]  Criar a Rota GET para pegar UMA tarefa específica pelo ID.
- [ ]  Criar a Rota POST para criar uma NOVA tarefa.
- [ ]  Criar a Rota PUT para ATUALIZAR uma tarefa existente pelo ID.
- [ ]  Criar a Rota DELETE para EXCLUIR uma tarefa existente pelo ID.
'''

import uvicorn
from fastapi import FastAPI
from project_todo_list.routers import todo_list_router

app = FastAPI()

@app.get("/")
def ToDoList() -> str:
    return "My ToDo List"

app.include_router(todo_list_router.router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
