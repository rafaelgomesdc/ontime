import sys
import os

sys.path.append(os.path.abspath("../services"))

from services.ponto import Registrar_Ponto
import flet as ft

class Home_view:
    def __init__(self, page: ft.Page):
        self.page = page

    def build(self):
        self.ui_titulo = ft.Text(value="OnTime", size=40)
        self.bt_marcar_ponto = ft.ElevatedButton("Marcar Ponto", on_click=self.Marcar_ponto)

        return ft.Column(
            [
                self.ui_titulo,
                self.bt_marcar_ponto
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

    async def Marcar_ponto(self):
        Registrar_Ponto()