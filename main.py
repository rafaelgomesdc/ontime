import flet as ft
from routes.route import Route
from core.database import Database

db = Database()
db.Criar()

async def main(page):
    page.on_route_change = lambda e: Route(page)
    await page.push_route("/home")

ft.app(target=main)