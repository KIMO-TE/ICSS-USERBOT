alv = (
"""
**©icss - @rruuurr
  - Plugin Alive** 
  - **Commend:** `.السورس`
  - **Function:** لعرض معلومات السورس
"""
)

import time
from platform import python_version
from telethon import version
from resources.strings import *

from . import ALIVE_NAME, StartTime, get_readable_time, icsv, mention
from . import reply_id as rd

DEFAULTUSER = ALIVE_NAME or "ICSS"
ICSS_IMG = Config.ALIVE_PIC or "https://telegra.ph/file/fab43e60e6256874e1849.jpg"
ICSS_TEXT = Config.CUSTOM_ALIVE_TEXT or "⇝ ＴＥＬＥＴＨＯＮ ＡＲＡＢＳ ⇜"


@icssbot.on(admin_cmd(outgoing=True, pattern="السورس$"))
@icssbot.on(sudo_cmd(pattern="السورس$", allow_sudo=True))
async def ica(icss):
    if icss.fwd_from:
        return
    ics_id = await rd(icss)
    icsupt = await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    if ICSS_IMG:
        ics_c = f"**{ICSS_TEXT}**\n"
        ics_c += f"**┓قاعدة البيانات -** {check_sgnirts} 𓄂\n"
        ics_c += f"**┫اصدار التليثون -** {version.__version__} 𓄂\n"
        ics_c += f"**┫اصدار السورس -** {icsv} 𓄂\n"
        ics_c += f"**┫اصدار البايثون -** {python_version()} 𓄂\n"
        ics_c += f"**┛مطور السورس -** [اضغط هنا](t.me/rruuurr) 𓄂\n"
        await icss.client.send_file(
            icss.chat_id, ICSS_IMG, caption=ics_c, reply_to=ics_id
        )
        await icss.delete()


def check_data_base_heal_th():
    is_database_working = False
    output = "لم يتم تعيين قاعدة بيانات"
    if not Config.DB_URI:
        return is_database_working, output
    from userbot.plugins.sql_helper import SESSION

    try:
        SESSION.execute("SELECT 1")
    except Exception as e:
        output = f"❌ {str(e)}"
        is_database_working = False
    else:
        output = "تعمل بنجاح"
        is_database_working = True
    return is_database_working, output


CMD_HELP.update({"alive": f"{alv}"})
