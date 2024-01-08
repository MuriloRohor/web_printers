import sqlite3
from typing import Optional

from models.RegistroImpressaoModel import RegistroImpressao
from sql.RegistroImpressaoSql import *
from util.database import criar_conexao

class RegistroImpressaoRepo:
    
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
    def inserir(cls , registro: RegistroImpressao) -> Optional[RegistroImpressao]:
        try:
            with criar_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(
                    SQL_INSERIR, 
                    registro.user,
                    registro.date,
                    registro.time,
                    registro.serial,
                    registro.print_pages
                    )
                if cursor.rowcount > 0:
                    registro.id = cursor.lastrowid
                    return registro
        except sqlite3.Error as e:
            print(e)
            return None
        
    @classmethod
    def contar_registros_por_serial(cls, serial: str) -> Optional[int]:
        try:
            with criar_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(SQL_CONTAR_LINHAS, serial)
                total_rows = cursor.fetchone()[0]
                return total_rows
        except sqlite3.Error as e:
            print(e)
            return None