from pyrogram.errors import YouBlockedUser
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
    
     if message.sender.bot:
        await lol.edit(bot, f"{user.id}")

    except YouBlockedUser:

        await client.unblock_user(bot)

        await client.send_message(bot, f"{user.id}")

    await txt.delete()
    await asyncio.sleep(5)
    await lol.delete()

    
async for stalk in client.search_messages(bot, query="History", limit=1):
     if not stalk
            NotFound = await client.send_message(client.me.id, "Tidak ada komentar")

            await NotFound.delete()

        elif stalk:

            await message.reply(stalk.text)

    user_info = await client.resolve_peer(bot)
    
    

    
        
         
        
        

        

            

    

    

        
