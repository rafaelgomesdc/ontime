import os

class Ponto_Model:
    def Salvar_Ponto(dados):
        with open(os.path.abspath("log/log.txt"), "a") as log:
            log.write(dados + "\n")