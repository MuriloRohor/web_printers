from typing import Optional
from brother import Brother, SnmpError, UnsupportedModelError
from fastapi import HTTPException

async def buscar_impressora_por_ip(printer_ip: str) -> Optional[Brother]:
    try:
        brother = await Brother.create(printer_ip, printer_type='laser')
        data = await brother.async_update() # Coleta os dados da impressora.
        
    except (ConnectionError, SnmpError, UnsupportedModelError) as error:
        raise HTTPException(status_code=400, detail=f"Erro ao conectar com a impressora: {error}")
    
    finally:
        brother.shutdown()
        
    return data
