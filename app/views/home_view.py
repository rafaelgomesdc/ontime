import flet as ft
import sys
import os
import asyncio
from datetime import datetime

sys.path.append(os.path.abspath("../services"))

from app.services.ponto import Ponto
from utils.utils import relogio
from utils.utils import cronometro

class Home_view:
    ponto_controller = Ponto()
    is_running = False #Cronômetro de tempo trabalhado

    def __init__(self, page: ft.Page):
        self.page = page

    def build(self):
        #Retorna o conteúdo da tela para ser carregado pela main
        self.ui_titulo = ft.Text(
            value="OnTime",
            size=40
        )

        self.ui_relogio = ft.Text( #Relógio
            value="00:00:00",
            size=20
        )

        #Cronômetro
        self.ui_ttl_work_timer = ft.Text( #Título do cronômetro 
            value="Tempo de trabalho",
            size=20
        )
        self.ui_work_timer = ft.Text( #Cronômetro de tempo trabalhado
            value="00:00:00",
            size=40
        )

        #Marcação de ponto
        self.bt_marcar_ponto = ft.ElevatedButton( #Marcar ponto
            "Marcar Ponto",
            on_click=self.Marcar_ponto
        )

        self.ui_txt_ultima_marcacao = ft.Text( #Título p/ histórico de marcação
            value="Última marcação:",
            size=20
        )

        self.page.run_task(relogio, self) #Inicia o funcionamento do relógio
        self.page.run_task(cronometro, self) #Inicia o funcionamento do cronômetro

        self.row_titulo = ft.Row(
            self.ui_titulo,
            alignment=ft.MainAxisAlignment.START
        )
        self.row_content = ft.Row(
            ft.Column(
                [
                    self.ui_relogio,
                    self.ui_ttl_work_timer,
                    self.ui_work_timer,
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
        self.ponto_controller.Registrar_Ponto(self.page, ft)
        if self.is_running:
            self.is_running = False
        else:
            self.is_running = True
        self.page.update()