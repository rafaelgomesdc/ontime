import os
import sqlite3


class Ponto_Model:
    #arquivo = "log/log.txt"
    database = "database/ontime.db"

    def Salvar_Ponto(self, dados):
        #with open(os.path.abspath(self.arquivo), "a") as log:
        #    log.write(dados["data"] + dados["horario"] + dados["motivo"] + "\n")

        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()

            cursor.execute(
                "INSERT INTO pontos (data, horario, motivo) VALUES (?, ?, ?)",
                (dados["data"], dados["horario"], dados["motivo"],)
            )
            conn.commit()

    def Carregar_Ultimo_Ponto(self):
        #with open(os.path.abspath(self.arquivo), "r") as log:
        #    pontos_registrados = log.readlines()
        
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM pontos ORDER BY id DESC LIMIT 1")
            ponto = cursor.fetchone()

        if ponto:
            ponto_formatado = f"{ponto[1]} | {ponto[2]}"
            return ponto_formatado
        else:
            return "Não há pontos registrados."
        
    def Carregar_Pontos_Dia(self, dia):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()

            cursor.execute(
                "SELECT data FROM pontos WHERE data = (?)",
                (dia,)
            )
            pontos = cursor.fetchall()