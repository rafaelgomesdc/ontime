import sys
import sqlite3
import os

db = "../ontime.db"
comando = sys.argv[1]

def limpar_dados(tabela):
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor();
        cursor.execute(f"DELETE FROM {tabela}")
        conn.commit()

def deletar():
    if os.path.exists(db):
        os.remove(db)

if comando == "limpar":
    tabela = sys.argv[2]
    limpar_dados(tabela)
elif comando == "deletar":
    deletar()