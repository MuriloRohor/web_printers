import sqlite3
from typing import Optional

from models.ImpressoraModel import Impressora
from sql.ImpressoraSql import *
from util.database import criar_conexao

class ImpressoraRepo:
    
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
    def inserir(cls, impressora: Impressora) -> Optional[Impressora]:
        try:
            with criar_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(SQL_INSERIR,
                               (
                                impressora.cod,
                                impressora.nome,
                                impressora.ip_andress,
                                "",
                                impressora.filial_id,
                                impressora.setor_id
                               ))
                return impressora
        except sqlite3.Error as e:
            print(e)
            return None
        
    @classmethod
    def obter_por_id(cls, id: int) -> Optional[Impressora]:
        try:
            with criar_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(SQL_OBTER_POR_ID, (id,)).fetchone()
                return Impressora(*Impressora)
            
        except sqlite3.Error as e:
            print(e)
            return None
                
        