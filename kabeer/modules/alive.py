# (C) 2021, Jayant Kageri

from config import PREFIX
import asyncio
import time
from datetime import datetime
from pyrogram import filters
from kabeer import app, CMD_HELP, StartTime
from sys import version_info
from pyrogram import __version__ as __pyro_version__
from pyrogram.types import Message

CMD_HELP.update(
    {
        "Alive": """
**Alive**
  `alive` -> For Checking Pyrogram Alive Status
  `ping` -> For Pinging Pyrogram
"""
    }
)

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


@app.on_message(filters.command("alive", PREFIX) & filters.me)
async def alive(_, m):
    start_time = time.time()
    await message.reply_sticker("CAACAgUAAxkBAAEGU0JhK49gLY2KvJUabs-p1A8BOUtFXgACBAMAAmA2WVUykujmd_XWISAE")
    uptime = get_readable_time((time.time() - StartTime))
    reply_msg = f"↽↽↽↽↽↽↽↽↽↽↽↽↽↽↽↽↽↽↽↽↽"
    reply_msg = f"**I am Alive\n"
    reply_msg += f"**Python Version:** `{__python_version__}`\n"
    reply_msg += f"**Pyrogram Version:** `{__pyro_version__}`\n"
    end_time = time.time()
    reply_msg += f"\nUptime: {uptime}"
    await m.delete()
    await app.send_message(m.chat.id, reply_msg, disable_web_page_preview=True)


@app.on_message(filters.command("ping", PREFIX) & filters.me)
async def pingme(_, message: Message):
    app_info = await app.get_me()
    start = datetime.now()
    end = datetime.now()
    m_s = (end - start).microseconds / 1000
    await message.edit(f"**Pong** : `{m_s} ms`", disable_web_page_preview=True)
