import asyncio
from datetime import datetime

async def relogio(home):
    #Atualiza o relógio em tempo real
    while True:
        home.ui_relogio.value = datetime.now().strftime("%H:%M:%S")
        home.ui_relogio.update()

        await asyncio.sleep(1)

async def cronometro(home):
    #time = 0

    s = 0
    m = 0
    h = 0

    s_text = "00"
    m_text = "00"
    h_text = "00"

    while True:
        if home.is_running:
            #Contagem
            if s < 59:
                s += 1
            elif s == 59:
                m += 1
                s = 0

            if m > 59:
                h += 1
                m = 0

            #Formatação
            if s < 10:
                s_text = f"0{s}"
            else:
                s_text = f"{s}"

            if m < 10:
                m_text = f"0{m}"
            else:
                m_text = f"{m}"
            if h < 10:
                h_text = f"0{h}"
            else:
                h_text = f"{h}"

            home.ui_work_timer.value = (f"{h_text}:{m_text}:{s_text}")
            home.ui_work_timer.update()

        await asyncio.sleep(1)

    