from pyrogram import filters

from pyrogram.errors import YouBlockedUser

from pyrogram.raw.functions.messages import DeleteHistory

from EmikoRobot import telethn as tbot
from EmikoRobot.events import register
from EmikoRobot import ubot2 as ubot
from asyncio.exceptions import TimeoutError


@Client.on_message(filters.user(OWNER._ID) & filters.command("sg", "/"))

@Client.on_message(filters.me & filters.command("sg", PERFIX))
async def_(client, message):
    steal.pattern_match.group(1)
    puki = await steal.reply("```SEDANG MENCARI HISTORY NAMA PENGGUNA..```")
    if steal.fwd_from:
        return
    if not steal.reply_to_msg_id:
        await puki.edit("```REPLY PENGGUNA```")
        return
    message = await steal.get_reply_message()
    chat = "@SangMata_beta_bot"
    user_id = message.sender.id
    id = f"/search_id {user_id}"
    if message.sender.bot:
        await puki.edit("```Reply To Real User's Message.```")
        return
    await puki.edit("```MEMPROSES...```")
    try:
        async with ubot.conversation(chat) as conv:
            try:
                msg = await conv.send_message(id)
                r = await conv.get_response()
                response = await conv.get_response()
            except YouBlockedUserError:
                await steal.reply(
                    "```Error, report to @kenbotsupport```"
                )
                return
            if r.text.startswith("Name"):
                respond = await conv.get_response()
                await puki.edit(f"`{r.message}`")
                await ubot.delete_messages(
                    conv.chat_id, [msg.id, r.id, response.id, respond.id]
                ) 
                return
            if response.text.startswith("No records") or r.text.startswith(
                "No records"
            ):
                await puki.edit("```I Can't Find This User's Information, This User Has Never Changed His Name Before.```")
                await ubot.delete_messages(
                    conv.chat_id, [msg.id, r.id, response.id]
                )
                return
            else:
                respond = await conv.get_response()
                await puki.edit(f"```{response.message}```")
            await ubot.delete_messages(
                conv.chat_id, [msg.id, r.id, response.id, respond.id]
            )
    except TimeoutError:
        return await puki.edit("`I'm Sick Sorry...`")
