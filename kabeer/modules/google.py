from pyrogram import Client, filters
from pyrogram.types import Message
from config import PREFIX
from kabeer import app, CMD_HELP

@app.on_message(filters.command(['google', 'g'], PREFIX) & filters.me)
async def webshot(client: Client, message: Message):
    user_request = ' '.join(message.command[1:])

    if user_request == '':
        if message.reply_to_message:
            reply_user_request = message.reply_to_message.text
            request = reply_user_request.replace(' ', '+')
            full_request = f'https://lmgtfy.app/?s=g&iie=1&q={request}'
            await message.edit(f'<a href={full_request}>{reply_user_request}</a>', disable_web_page_preview=True)

    else:
        request = user_request.replace(' ', '+')
        full_request = f'https://lmgtfy.app/?s=g&iie=1&q={request}'
        await message.edit(f'<a href={full_request}>{user_request}</a>', disable_web_page_preview=True)


CMD_HELP.update(
    {
        "google": """
**google**
  `google` -> Google
"""
    }
)
