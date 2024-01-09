import sqlite3
from typing import Optional

from models.StatusImpressoraModel import StatusImpressora
from sql.StatusImpressoraSql import *
from util.database import criar_conexao

class StatusImpressoraRepo:
    
    @classmethod
    def criar_tabela(cls) -> bool:
        try:
            with criar_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(SQL_CRIAR_TABELA)
                return True
        except sqlite3.Error as e:
            print(e)
            return False
        
    @classmethod
    def inserir_status_padrao(cls) -> Optional[StatusImpressora]:
        try:
            with criar_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(SQL_INSERIR_STATUS_PADRAO)
                return cursor.rowcount > 0
        except sqlite3.Error as e:
            print(e)
            return None