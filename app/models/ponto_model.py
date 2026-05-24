import os
import sqlite3


class Ponto_Model:
    arquivo = "log/log.txt"
    database = "ontime.db"

    def Salvar_Ponto(self, dados):
        with open(os.path.abspath(self.arquivo), "a") as log:
            log.write(dados["data"] + dados["horario"] + dados["motivo"] + "\n")

        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()

            cursor.execute(
                "INSERT INTO pontos (data, horario, motivo) VALUES (?, ?, ?)",
                (dados["data"], dados["horario"], dados["motivo"],)
            )
            conn.commit()

    def Carregar_Ultimo_Ponto(self):
        with open(os.path.abspath(self.arquivo), "r") as log:
            pontos_registrados = log.readlines()

        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM pontos ORDER BY id DESC LIMIT 1")
            ponto = cursor.fetchone()

        if ponto:
            #return pontos_registrados[-1].strip()
            return ponto
        else:
            return "Não há pontos registrados."