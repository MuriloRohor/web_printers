from dataclasses import dataclass
from typing import Optional

@dataclass
class Impressora:
    id: Optional[int] = None
    cod: Optional[str] = None
    nome: Optional[str] = None
    ip_andress: Optional[str] = None
    serial: Optional[str] = None
    filial_id: Optional[int] = None
    setor_id: Optional[int] = None
    
    