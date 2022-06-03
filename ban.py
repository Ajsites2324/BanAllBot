#  Copyright (c) 2022 @TheRiZoeL - RiZoeL
# Telegram Ban All Bot 
# Creator - RiZoeL

import logging
import re
import os
import sys
import asyncio
from telethon import TelegramClient, events
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from asyncio import sleep
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins, ChatAdminRights
from telethon.tl.functions.channels import EditBannedRequest
from datetime import datetime
from var import Var


logging.basicConfig(level=logging.INFO)

print("Starting.....")

Riz = TelegramClient('Riz', Var.API_ID, Var.API_HASH).start(bot_token=Var.BOT_TOKEN)


SUDO_USERS = []
for x in Var.SUDO: 
    SUDO_USERS.append(x)

@Riz.on(events.NewMessage(pattern="^/ping"))  
async def ping(e):
    if e.sender_id in SUDO_USERS:
        start = datetime.now()
        text = "Pong!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"**I'm On 𝐀𝐉𝐄𝐄𝐓 𓆩𝗫𓆪 𝐑𝐎𝐁𝐎𝐓 ** \n\n __Pong__ !! `{ms}` ms")


@Riz.on(events.NewMessage(pattern="^/banall"))
async def testing(event):
  if event.sender_id in SUDO_USERS:
   if not event.is_group:
        Reply = f"𝐀𝐁𝐄 𝐂𝐇𝐔𝐓𝐓𝐈𝐘𝐄 !! 𝐘𝐄 𝐂𝐎𝐌𝐌𝐀𝐍𝐃 𝐆𝐑𝐎𝐔𝐏 𝐌𝐄 𝐉𝐀 𝐊𝐄 𝐔𝐒𝐄 𝐊𝐀𝐑 𝐏𝐇𝐈𝐑 𝐃𝐄𝐊𝐇𝐎 𝐊𝐌𝐀𝐀𝐋 𝐀𝐉𝐄𝐄𝐓 𝐏𝐀𝐏𝐀 𝐊𝐄 𝐁𝐎𝐓 𝐊𝐀."
        await event.reply(Reply, parse_mode=None, link_preview=None )
   else:
       await event.delete()
       RiZoeL = await event.get_chat()
       RiZoeLop = await event.client.get_me()
       admin = RiZoeL.admin_rights
       creator = RiZoeL.creator
       if not admin and not creator:
           await event.reply(" 𝐂𝐇𝐔𝐓𝐈𝐘𝐄𝐄 𝐑𝐈𝐆𝐇𝐓𝐒 𝐓𝐎 𝐃𝐈𝐋𝐀, 𝐀𝐉𝐄𝐄𝐓 𝐏𝐀𝐏𝐀 𝐊𝐀 𝐁𝐎𝐓 𝐀𝐀𝐈𝐒𝐄 𝐊𝐀𝐀𝐌 𝐍𝐀𝐇𝐈 𝐊𝐀𝐑𝐓𝐀 !!")
           return
       await event.reply("𝐇𝐄𝐇𝐄𝐄𝐄 !! 𝐌𝐀𝐈 𝐉𝐈𝐍𝐃𝐀 𝐇𝐔")
       everyone = await event.client.get_participants(event.chat_id)
       for user in everyone:
           if user.id == RiZoeLop.id:
               pass
           try:
               await event.client(EditBannedRequest(event.chat_id, int(user.id), ChatBannedRights(until_date=None,view_messages=True)))
           except Exception as e:
               await event.edit(str(e))
           await sleep(0.3)


@Riz.on(events.NewMessage(pattern="^/leave"))
async def _(e):
    if e.sender_id in SUDO_USERS:
        rizoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = rizoel[0]
            bc = int(bc)
            text = "Leaving....."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("𝐀𝐉𝐄𝐄𝐓 𝐏𝐀𝐏𝐀 𝐍𝐄 𝐂𝐇𝐎𝐃𝐃𝐃 𝐊𝐄 𝐂𝐇𝐇𝐎𝐑 𝐃𝐈𝐘𝐀")
            except Exception as e:
                await event.edit(str(e))   
        else:
            bc = e.chat_id
            text = "Leaving....."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("𝐀𝐉𝐄𝐄𝐓 𝐏𝐀𝐏𝐀 𝐍𝐄 𝐂𝐇𝐎𝐃𝐃𝐃 𝐊𝐄 𝐂𝐇𝐇𝐎𝐑 𝐃𝐈𝐘𝐀")
            except Exception as e:
                await event.edit(str(e))   
          


@Riz.on(events.NewMessage(pattern="^/restart"))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        text = "__Restarting__ !!!"
        await e.reply(text, parse_mode=None, link_preview=None )
        try:
            await Riz.disconnect()
        except Exception:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()


print("\n\n")
print("𝐀𝐉𝐄𝐄𝐓 𝐏𝐀𝐏𝐀 𝐊𝐀 𝐁𝐎𝐓 𝐒𝐔𝐑𝐔 𝐇𝐎 𝐆𝐘𝐀")

Riz.run_until_disconnected()
