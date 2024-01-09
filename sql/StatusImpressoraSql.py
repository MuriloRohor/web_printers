SQL_CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS status_impressora (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE,
)
"""

SQL_INSERIR_STATUS_PADRAO = """
INSERT OR IGNORE INTO status_impressora (nome)
VALUES ("Conectada"))

INSERT OR IGNORE INTO status_impressora (nome)
VALUES ("Inativa"))
"""