from fastapi import APIRouter, Request

from repository.SetorRepo import SetorRepo

from schemas.SetorSchema import SetorSchema

router = APIRouter()

router.post("/setor/inserir")
def inserir_setor(setor: SetorSchema):
    setor_criado = SetorRepo.inserir(setor)
    return setor_criado