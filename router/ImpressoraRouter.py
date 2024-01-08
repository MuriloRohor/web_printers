import asyncio
from fastapi import APIRouter, Request
from repository.ImpressoraRepo import ImpressoraRepo

from schemas.ImpressoraSchema import ImpressoraSchema

from util.brother_printer import buscar_impressora_por_ip

router = APIRouter()


@router.get("/printer/{ip}")
def get_impressora_por_ip(request: Request, ip: str):
    info = asyncio.run(buscar_impressora_por_ip(ip))
    return info

@router.post("/printers/inserir")
def inserir_impressora(impressora: ImpressoraSchema):
    info = asyncio.run(buscar_impressora_por_ip(impressora.ip_andress))
    impressora.serial = info.serial
    impressora_criada = ImpressoraRepo.inserir(impressora)
    return impressora_criada