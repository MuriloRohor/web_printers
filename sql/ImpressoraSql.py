SQL_CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS impressora (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  cod INTEGER NOT NULL,
  nome TEXT NOT NULL,
  ip_andress TEXT NOT NULL,
  serial TEXT NOT NULL,
  filial_id INTEGER NOT NULL,
  setor_id INTEGER NOT NULL,
  nivel_toner INTEGER NOT NULL,
  status TEXT NOT NULL,
  FOREIGN KEY (filial_id) REFERENCES filial(id),
  FOREIGN KEY (setor_id) REFERENCES setor(id)
)
"""

SQL_INSERIR = """
INSERT INTO impressora (cod, nome, ip_andress, serial, filial_id, setor_id)
VALUES (?, ?, ?, ?, ?, ?)
"""

SQL_EXCLUIR = """
DELETE FROM impressora
WHERE id = ?
"""

SQL_OBTER_POR_ID = """
SELECT (cod , nome, ip_andress, serial, filial_id, setor_id, nivel_toner, status)
FROM impressora
WHERE id = ?
"""