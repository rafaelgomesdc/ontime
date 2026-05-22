import flet as ft
from views import home_view

def main(page):
    view = home_view.Home_view(page)
    page.add(view.build())

    page.update()

ft.app(target=main)