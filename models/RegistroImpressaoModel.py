from dataclasses import dataclass
from typing import Optional

@dataclass
class RegistroImpressao:
    id: Optional[int] = None
    user: Optional[str] = None
    date: Optional[str] = None
    time: Optional[str] = None
    serial: Optional[str] = None
    print_pages: Optional[int] = None