import sqlite3
from typing import Optional

from models.FilialModel import Filial
from sql.FilialSql import *
from util.database import criar_conexao

class FilialRepo:
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
    def inserir(cls, filial: Filial) -> Optional[Filial]:
        try:
            with criar_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(SQL_INSERIR,
                               filial.cod,
                               filial.nome,
                               filial.cidade
                               )
                return True
        except sqlite3.Error as e:
            print(e)
            return False