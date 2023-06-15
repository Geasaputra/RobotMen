from pyrogram.errors import YouBlockedUser
from pyrogram import filters
from pyrogram.raw.functions.messages import DeleteHistory
from EmikoRobot import OWNER_ID
from EmikoRobot import pbot
from EmikoRobot import ubot2 as ubot
from asyncio.exceptions import TimeoutError



@pbot.on_message(filters.command("sg"))
async def sg(client, message):
    response = await extract_user(message)
    lol = await eor(message, "Sedang Memproses...")
    if args:
       try:
          user = await client.get_users(args)
       except Exception as error:
           return await lol.edit(error)
        
    bot = "@SangMata_BOT"
    user_id = message.sender.id
    id =f"/search_id {user_id}"
    
      
