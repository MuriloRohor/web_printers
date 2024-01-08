from pydantic import BaseModel
from typing import Optional

class ImpressoraSchema(BaseModel):
    id: Optional[int] = None
    cod: str
    nome: str
    ip_andress: str
    serial: Optional[str] = None
    filial_id: int
    setor_id: int
    
    
    
    
