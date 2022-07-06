import os
import re
import random
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from MukeshRobot.events import register
from MukeshRobot import telethn as tbot


PHOTO = [
    "https://telegra.ph/file/0a8c86f34a2e46c4832f3.jpg",
    "https://telegra.ph/file/e55ac47f2ff51aaaf62b8.jpg",
]


@register(pattern=("/alive"))
async def awake(event):
    TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ ᴍᴜᴋʜᴜsʜɪ ✘ ʀᴏʙᴏᴛ​**\n━━━━━━━━━━━━━━━━━━━\n\n"
    TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [ᴍᴜᴋᴇsʜ](https://t.me/itz_mst_boi)** \n\n"
    TEXT += f"» **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{telever}` \n\n"
    TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tlhver}` \n\n"
    TEXT += f"» **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyrover}` \n━━━━━━━━━━━━━━━━━\n\n"
    BUTTON = [
        [
            Button.url("ʜᴇʟᴘ​", "https://t.me/groupcontrollertgbot?start=help"),
            Button.url("sᴜᴘᴘᴏʀᴛ​", "https://t.me/worldwide_friend_zone"),
        ]
    ]
    ran = random.choice(PHOTO)
    await tbot.send_file(event.chat_id, ran, caption=TEXT, buttons=BUTTON)


## Alive mod
