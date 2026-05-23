import flet as ft
from app.views import home_view

def Route(page):
    match page.route:
        case "/home":
            page.controls.clear()
            view = home_view.Home_view(page)
            page.add(view.build())

    page.update()