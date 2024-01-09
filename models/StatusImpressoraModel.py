from dataclasses import dataclass
from typing import Optional

@dataclass
class StatusImpressora:
    id: Optional[int] = None
    nome: Optional[str] = None