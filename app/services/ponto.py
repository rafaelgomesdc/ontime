import os

from datetime import datetime

def Registrar_Ponto():
    data_time = datetime.now().strftime("%d/%m/%Y %H:%M")

    with open(os.path.abspath("../log/log.txt"), "a") as log:
        log.write(data_time + "\n")