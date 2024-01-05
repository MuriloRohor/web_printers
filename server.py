import asyncio
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

from util.brother_printer import BuscarImpressoraPorIP

templates = Jinja2Templates(directory="templates")

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def main(request: Request):
    
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/printer/{ip}")
def main(request: Request, ip: str):
    info = asyncio.run(BuscarImpressoraPorIP(ip))
    return info



if __name__ == "__main__":
    uvicorn.run(app="server:app",host="localhost", reload=True, port=8000)