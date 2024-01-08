SQL_CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS impressora (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  cod INTEGER NOT NULL,
  nome TEXT NOT NULL,
  ip_andress TEXT NOT NULL,
  serial TEXT NOT NULL,
  filial_id INTEGER NOT NULL,
  setor_id INTEGER NOT NULL,
  FOREING KEY (filial_id) REFERENCES filial(id)
  FOREING KEY (setor_id) REFERENCES setor(id)
)
"""

SQL_INSERIR = """
INSERT INTO (cod, nome, ip_andress, serial, filial_id, setor_id)
VALUES (?, ?, ?, ?, ?, ?)
"""

SQL_EXCLUIR = """
DELETE FROM impressora
WHERE id = ?
"""