import asyncio
from pyrogram import filters
from pyrogram.types import (InlineKeyboardButton,                         InlineKeyboardMarkup, InputMediaPhoto, Message)


from MukeshRobot import pbot as bot

Mukesh = "https://telegra.ph/file/141146027deaaefbf7f5a.jpg"

@bot.on_message(filters.command(["noob", "owner", "mukesh"]))
async def repo(client, message):
await message.reply_photo(
photo=Mukesh,
caption=f"""**ʜᴇʏ {message.from_user.mention()},\n\nɪ ᴀᴍ [「 ᴍᴜᴋʜᴜsʜɪ ʀᴏʙᴏᴛ 」](t.me/groupcontrollertgbot)**
""",        
            reply_markup=InlineKeyboardMarkup(   
                  [          
                        [          
                              InlineKeyboardButton("• ᴏᴡɴᴇʀ •", url="https://t.me/Itz_mst_boi"),        
                              
                        ]     
                  ]      
            ),     
      )
