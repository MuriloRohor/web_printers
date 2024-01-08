import time
from models.RegistroImpressaoModel import RegistroImpressao
from util.extract_data import extrair_info

async def registar_log_impressao(serial):
    data = extrair_info(serial)
    
    last_row_log = data.iloc[-1]["Id"]
    last_row_database = RegistroImpressao.contar_registros_por_serial(serial)
    
    if last_row_database < last_row_log:
        handler = last_row_database + 1
        for row in data.iloc[handler:-1]:
            RegistroImpressao.inserir(
                user = row["user"],
                date = row["date"],
                time = row["time"],
                serial = serial,
                print_pages = row["print_pages"]
            )
    else:
        print("Não a mais registros novos para incluir no banco!")
            
            
def tempo_registro():
    while True:
        registar_log_impressao()
        time.sleep(300)