from dataclasses import dataclass
from typing import Optional

@dataclass
class Setor:
    id: Optional[int] = None
    nome: Optional[str] = None