from pyrogram import filters as  Filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from ..config import Config
from ..chatbot import chatbot


@chatbot.on_message(Filters.private & Filters.command("start"))
async def start(c, m):

    await m.reply_text(
        text=f"Hi {m.from_user.mention}.\n\n I am Aronica.\n A Chatbot based on a crappy AI learning machine.I learn as you talk to me and I react as you react to me 🙂🙂.\n\n\n\n**NOTE:**\n __please don't be angry or sad at my responses because I'm just a little machine__🙃🙃",
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('Creator', url='t.me/lolboyisback')
                ],
                [
                    InlineKeyboardButton('Maintainer', url='https://t.me/jayantkageri')
                ]
            ]
        )
    )
