import sqlite3
import os

# Cria a pasta "database" automaticamente se ela não existir
PASTA_DADOS = "database"
if not os.path.exists(PASTA_DADOS):
    os.makedirs(PASTA_DADOS)

# Define o caminho do arquivo do banco dentro dessa pasta
CAMINHO_BANCO = os.path.join(PASTA_DADOS, "astrologia.db")

def conectar():
    return sqlite3.connect(CAMINHO_BANCO)

def criar_tabelas():
    with conectar() as con:
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS pessoas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                data_nascimento TEXT NOT NULL,
                signo TEXT NOT NULL,
                data_hora_cadastro TEXT NOT NULL
            )
        """)
        con.commit()

# Executa a criação da tabela assim que o sistema for iniciado
criar_tabelas()