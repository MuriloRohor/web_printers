from pydantic import BaseModel
from typing import Optional

class FilialSchema(BaseModel):
    id: Optional[int] = None
    cod: str
    nome: str
    cidade: str
    