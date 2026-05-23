import os
from datetime import datetime

def Registrar_Ponto(page, ft):
    ui_ultima_marcação = ft.Text(
        value=datetime.now().strftime("%H:%M"),
        size=20
        )

    page.add(
        ft.Row(
            ui_ultima_marcação,
            alignment=ft.MainAxisAlignment.CENTER
        )
    )
    data_time = datetime.now().strftime("%d/%m/%Y %H:%M")

    with open(os.path.abspath("log/log.txt"), "a") as log:
        log.write(data_time + "\n")