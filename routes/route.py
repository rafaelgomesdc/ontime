import flet as ft
from app.views import home_view
from app.services import ponto


def Route(page):
    match page.route:
        case "/home":
            page.controls.clear()
            view = home_view.Home_view(page)
            page.add(view.build())
            view.ponto_controller.Exibir_Ultimo_Ponto(page, ft)

    page.update()