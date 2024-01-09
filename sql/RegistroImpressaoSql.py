SQL_CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS registro_impressao (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user TEXT NOT NULL,
  date TEXT NOT NULL,
  time TEXT NOT NULL,
  serial TEXT NOT NULL,
  print_pages INTEGER NOT NULL,
  FOREING KEY (serial) REFERENCES impressora(serial)
)
"""

SQL_INSERIR = """"
INSERT INTO registro_impressao 
(user, date, time, serial, print_pages)
VALUES (?, ?, ?, ?, ?)
"""

SQL_CONTAR_LINHAS = """
SELECT COUNT (*)
FROM registro_impressao
WHERE serial = ?
"""

SQL_FILTRO_POR_DIA = """
SELECT COUNT (*)
FROM registro_impressao
WHERE serial = ? and date = ?
"""