import asyncio
from datetime import datetime

async def relogio(home):
    #Atualiza o relógio em tempo real
        while True:
            home.ui_relogio.value = datetime.now().strftime("%H:%M:%S")
            home.ui_relogio.update()

            await asyncio.sleep(1)

    