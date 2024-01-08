import pandas as pd

from repository.RegistroImpressaoRepo import RegistroImpressao

FILE_PATH = './logs/printers/'

def extrair_info(serial: str):
    file = FILE_PATH + serial + ".csv"
    data = pd.read_csv(file, encoding='ISO-8859-1')
    return data
            