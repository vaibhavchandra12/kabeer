from config import PREFIX
from kabeer import LOGGER, app
from kabeer import app, CMD_HELP, StartTime
import asyncio
from collections import deque
from pyrogram import Client, filters
from pyrogram.types import Message


CMD_HELP.update(
    {
        "Animation": """
**Animation:**
  `istar` -> run and try
  `ping` -> For Pinging Pyrogram
"""
    }
)

@app.on_message(filters.command("istar", PREFIX) & filters.me)
async def kabeerstar(_, message: Message):
    animation_interval = 2
    animation_ttl = range(0, 11)
    await message.edit("I am A Star")
    animation_chars = [
        "I Party like a rockstar",
        "I Look like a movie star",
        "I Play like an all star",
        "I Fuck like a pornstar",
        "Baby I'm a superstar",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        
        await message.edit(animation_chars[i % 11])
    
