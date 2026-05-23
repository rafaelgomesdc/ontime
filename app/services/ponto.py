import os
from datetime import datetime
from app.models.ponto_model import Ponto_Model

class Ponto:
    def __init__(self):
        pass

    def Registrar_Ponto(self, page, ft):
        dados = datetime.now().strftime("%d/%m/%Y %H:%M")
        Ponto_Model.Salvar_Ponto(dados)

        self.Exibir_Ultimo_Ponto(page, ft)

    def Exibir_Ultimo_Ponto(self, page, ft):
        ultimo_ponto = self.Consultar_Ultimo_Ponto()

        ui_ultima_marcação = ft.Text(
            value=ultimo_ponto,
            size=20
            )

        page.add(
            ft.Row(
                ui_ultima_marcação,
                alignment=ft.MainAxisAlignment.CENTER
            )
        )

    def Consultar_Ultimo_Ponto(self):
        with open(os.path.abspath("log/log.txt"), "r") as log:
            pontos_registrados = log.readlines()

        if pontos_registrados:
            return pontos_registrados[-1].strip()
        else:
            return "Não há pontos registrados."