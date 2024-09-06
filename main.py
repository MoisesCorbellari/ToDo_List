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
def to_do_list() -> str:
    return "My ToDo List"

app.include_router(todo_list_router.router)

if __name__ == "__main__":
    try:
        uvicorn.run("main:app", host='0.0.0.0',port=5000, log_level="info", reload=True) # 
    except Exception as e:
        print(f'Erro ao iniciar o servidor: {e}')
    # reload=True: recarrega automaticamente a cada alteração salva na aplicação.
    # log_level="info": exibe mensagens informativas sobre o que acontece no servidor.