from pydantic import BaseModel
from typing import Optional

class SetorSchema(BaseModel):
    id: Optional[int] = None
    nome: str