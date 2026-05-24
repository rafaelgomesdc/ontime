import sys
import sqlite3

db = "../ontime.db"
comando = sys.argv[1]
tabela = sys.argv[2]

def limpar_dados(tabela):
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor();
        cursor.execute(f"DELETE FROM {tabela}")
        conn.commit()

if comando == "limpar":
    limpar_dados(tabela)