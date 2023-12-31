import asyncio
import threading
import schedule
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn


from repository.RegistroImpressaoRepo import RegistroImpressao
from repository.ImpressoraRepo import ImpressoraRepo
from repository.SetorRepo import SetorRepo
from repository.FilialRepo import FilialRepo
from repository.StatusImpressoraRepo import StatusImpressoraRepo

from router.ImpressoraRouter import router as impressoraRouter
from router.FilialRouter import router as filialRouter
from router.SetorRouter import router as setorRouter

from schemas.ImpressoraSchema import ImpressoraSchema

from util.brother_printer import buscar_impressora_por_ip
from util.registros import tempo_registro

templates = Jinja2Templates(directory="templates")

app = FastAPI()

FilialRepo.criar_tabela()
SetorRepo.criar_tabela()
StatusImpressoraRepo.inserir_status_padrao()
ImpressoraRepo.criar_tabela()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(impressoraRouter)
app.include_router(filialRouter)
app.include_router(setorRouter)

@app.get("/")
def main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

#@app.on_event("startup")
#async def on_startup():
    #tarefa_thread = threading.Thread(target=tempo_registro)
    #tarefa_thread.start()

if __name__ == "__main__":
    uvicorn.run(app="server:app",host="localhost", reload=True, port=8000)