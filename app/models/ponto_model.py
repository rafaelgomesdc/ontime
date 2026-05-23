import os

class Ponto_Model:
    arquivo = "log/log.txt"

    def Salvar_Ponto(self, dados):
        with open(os.path.abspath(self.arquivo), "a") as log:
            log.write(dados + "\n")

    def Carregar_Ultimo_Ponto(self):
        with open(os.path.abspath(self.arquivo), "r") as log:
            pontos_registrados = log.readlines()

        if pontos_registrados:
            return pontos_registrados[-1].strip()
        else:
            return "Não há pontos registrados."