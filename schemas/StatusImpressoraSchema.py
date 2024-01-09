from pydantic import BaseModel
from typing import Optional

class StatusImpressoraSchema(BaseModel):
    id: Optional[int] = None
    nome: str