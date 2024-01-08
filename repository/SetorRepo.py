import sqlite3
from typing import Optional

from models.SetorModel import Setor
from sql.SetorSql import *
from util.database import criar_conexao

class SetorRepo:
    
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
    def inserir(cls, setor: Setor) -> Optional[Setor]:
        try:
            with criar_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(SQL_INSERIR, (setor.nome))
                if cursor.rowcount > 0:
                    setor.id = cursor.lastrowid
                    return setor
        except sqlite3.Error as e:
            print(e)
            return None
            