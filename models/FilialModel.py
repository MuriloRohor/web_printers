from dataclasses import dataclass
from typing import Optional

@dataclass
class Filial:
    id: Optional[int] = None
    cod: Optional[int] = None
    nome: Optional[str] = None
    cidade: Optional[str] = None
