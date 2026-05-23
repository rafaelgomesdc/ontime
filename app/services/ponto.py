import os
from datetime import datetime
from app.models.ponto_model import Ponto_Model

class Ponto:
    ponto_model = Ponto_Model()

    def __init__(self):
        pass

    def Registrar_Ponto(self, page, ft):
        dados = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.ponto_model.Salvar_Ponto(dados)

        self.Exibir_Ultimo_Ponto(page, ft)

    def Exibir_Ultimo_Ponto(self, page, ft):
        #Adiciona o último ponto marcado na tela
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
        return self.ponto_model.Carregar_Ultimo_Ponto()