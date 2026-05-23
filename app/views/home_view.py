import sys
import os

sys.path.append(os.path.abspath("../services"))

from app.services.ponto import Registrar_Ponto
import flet as ft

import asyncio
from datetime import datetime

class Home_view:
    def __init__(self, page: ft.Page):
        self.page = page
        #self.clock = True

    def build(self):
        #Retorna o conteúdo da tela para ser carregado pela main
        self.ui_titulo = ft.Text(
            value="OnTime",
            size=40
        )

        self.ui_relogio = ft.Text(
            value="00:00:00",
            size=40
        )

        self.bt_marcar_ponto = ft.ElevatedButton(
            "Marcar Ponto", 
            on_click=self.Marcar_ponto
        )

        self.ui_txt_ultima_marcacao = ft.Text(
            value="Última marcação hoje:",
            size=20
        )

        self.page.run_task(self.relogio)

        self.row_titulo = ft.Row(
            self.ui_titulo,
            alignment=ft.MainAxisAlignment.START
        )
        self.row_content = ft.Row(
            ft.Column(
                [
                    self.ui_relogio,
                    self.bt_marcar_ponto,
                    self.ui_txt_ultima_marcacao
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            alignment=ft.MainAxisAlignment.CENTER
        )

        return ft.Column(
            [
                self.row_titulo,
                self.row_content
            ]
        )

    async def Marcar_ponto(self):
        #Ação do botão "marcar ponto"
        Registrar_Ponto(self.page, ft)
        self.page.update()

    async def relogio(self):
        #Atualiza o relógio em tempo real
        while True:
            self.ui_relogio.value = datetime.now().strftime("%H:%M:%S")
            self.ui_relogio.update()

            await asyncio.sleep(1)