import asyncio
from fastapi import APIRouter, HTTPException, Request

from repository.ImpressoraRepo import ImpressoraRepo

from schemas.ImpressoraSchema import ImpressoraSchema

from util.brother_printer import buscar_impressora_por_ip, buscar_serial_impressora

router = APIRouter()


@router.get("/printer/{ip}")
def get_impressora_por_ip(request: Request, ip: str):
    info = asyncio.run(buscar_impressora_por_ip(ip))
    return info

@router.post("/printer/inserir")
async def inserir_impressora(impressora: ImpressoraSchema):
    try:
        impressora_criada = ImpressoraRepo.inserir(impressora)
        return impressora_criada
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno do servidor: {e}")

@router.get("/printer/{id}")
def exibir_impressora(request: Request):
    return 
        
        
    