import sqlite3
import os

class Database:
    database = "database/ontime.db"

    def Criar(self):
        os.makedirs("database", exist_ok=True)

        if not os.path.exists(self.database):
            conn = sqlite3.connect(self.database)
            cursor = conn.cursor()

            cursor.execute("""
                CREATE TABLE pontos(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    data TEXT,
                    horario TEXT,
                    motivo TEXT
                )
            """)

            conn.commit()
            conn.close()