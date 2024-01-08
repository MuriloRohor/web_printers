from fastapi import APIRouter, Request

from repository.FilialRepo import FilialRepo

from schemas.FilialSchema import FilialSchema

router = APIRouter()

@router.post("/filial/inserir")
def inserir_filial(filial: FilialSchema):
    filial_criada = FilialRepo.inserir(filial)
    return filial_criada