from pyrogram import Client, idle
from pyromod import listen



bot = Client(
    "mo",
    api_id=10871792,
    api_hash="6f3f84d0b392900e09b0aed186470890",
    bot_token="5552982639:AAEcoHhXUFO_3fmyxpEUPLHO8mCZ0ZeD63o",
    plugins=dict(root="MZombie")
    )

DEVS = ["L_HLN","TR_E2S_ON_MY_MOoN","O_M_A_7"] 

bot_id = bot.bot_token.split(":")[0]

async def start_zombiebot():
    print("تم تشغيل الصانع بنجاح..💗")
    await bot.start()
    for hh in DEVS:
        try:
            await bot.send_message(hh, "**تم تشغيل الصانع بنجاح ...🥀**")
        except:
            pass
    await idle()
