SQL_CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS impressora (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  cod INTEGER NOT NULL,
  nome TEXT NOT NULL,
  ip_andress TEXT NOT NULL,
  serial TEXT NULL,
  nivel_toner INTEGER NOT NULL,
  status_id INTEGER NOT NULL,
  filial_id INTEGER NOT NULL,
  setor_id INTEGER NOT NULL,
  FOREIGN KEY (filial_id) REFERENCES filial(id),
  FOREIGN KEY (setor_id) REFERENCES setor(id),
  FOREIGN KEY (status_id) REFERENCES status_impressora(id)
)
"""

SQL_INSERIR = """
INSERT INTO impressora (cod, nome, ip_andress, serial, status_id, filial_id, setor_id) 
VALUES (?, ?, ?, ?, ?, ?, ?)
"""

SQL_EXCLUIR = """
DELETE FROM impressora
WHERE id = ?
"""

SQL_OBTER_POR_ID = """
SELECT (cod , nome, ip_andress, serial, status_id, filial_id, setor_id, nivel_toner)
FROM impressora
WHERE id = ?
"""

SQL_OBTER_ID_SEM_SERIAL = """
SELECT (id)
FROM impressora
WHERE serial is NULL
"""