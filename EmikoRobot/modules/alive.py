from pyrogram import __version__ as pyrover
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram import __version__ as telever
from telethon import __version__ as tlhver

from EmikoRobot import BOT_NAME, BOT_USERNAME, OWNER_ID, SUPPORT_CHAT, pbot


@pbot.on_message(filters.command("alive"))
async def awake(_, message: Message):
    TEXT = f"**ʜᴇʏ {message.from_user.mention},\n\nɪ ᴀᴍ {BOT_NAME}**\n━━━━━━━━━━━━━━━━━━━\n\n"
    TEXT += f"» **DEV :** [Ge](https://t.me/Mamenkuy)\n\n"
    TEXT += f"» **Library version :** `{telever}` \n\n"
    TEXT += f"» **Telethon version :** `{tlhver}` \n\n"
    TEXT += f"» **Pyrogram version :** `{pyrover}` \n━━━━━━━━━━━━━━━━━\n\n"
    BUTTON = [
        [
            InlineKeyboardButton("ʜᴇʟᴘ", url=f"https://t.me/pusatmusic_bot?start=help"),
            InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/PCOgrup"),
        ]
    ]
    await message.reply_text(
        caption=TEXT,
        reply_markup=InlineKeyboardMarkup(BUTTON),
    )


__mod_name__ = "Aʟɪᴠᴇ"
        
