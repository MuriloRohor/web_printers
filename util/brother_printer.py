import asyncio
from brother import Brother, SnmpError, UnsupportedModelError

async def BuscarImpressoraPorIP(printer_ip: str):
    try:
        # Cria uma instância do Brother para a impressora no IP fornecido.
        # Substitua 'laser' por 'ink' se for uma impressora jato de tinta.
        brother = await Brother.create(printer_ip, printer_type='laser')
        
        # Coleta os dados da impressora.
        data = await brother.async_update()
    except (ConnectionError, SnmpError, UnsupportedModelError) as error:
        print(f"Erro ao conectar com a impressora: {error}")
        return
    
    brother.shutdown()
    
    if data:
        impressora = {
            "modelo": brother.model,
            "Status": data.status,
            "Serial": data.serial,
            "qtd_print": data.page_counter
            
        }
    
    return impressora

# Executa a função assíncrona.
