import logging
import os
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import config
from config import BOT_USERNAME
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant, UsernameNotOccupied, ChatAdminRequired, PeerIdInvalid
UPDATES_CHANNEL = C.UPDATES_CHANNEL


@Client.on_message(filters.incoming & filters.command(['start', 'start@VCPvtBot']))
def _start(client, message):
    update_channel = UPDATES_CHANNEL
    if update_channel:
        try:
            user = client.get_chat_member(update_channel, message.chat.id)
            if user.status == "kicked":
               client.send_message(
                   chat_id=message.chat.id,
                   text="Sorry Sir, You are Banned to use me. Contact my [Support Group](https://t.me/AwesomeSupportt).",
                   parse_mode="markdown",
                   disable_web_page_preview=True
               )
               return
        except UserNotParticipant:
            client.send_message(
                chat_id=message.chat.id,
                text="**Please Join My Updates Channel to use this Bot!**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Join Updates Channel", url=f"https://t.me/{update_channel}")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            client.send_message(message.chat.id,
                text=tr.START_MSG.format(message.from_user.first_name, message.from_user.id),
	        reply_markup=InlineKeyboardMarkup(
                    [
                        [
                           InlineKeyboardButton("Join Updates Channel", url="https://t.me/LaylaList"),
                           InlineKeyboardButton("Support Group", url="https://t.me/AwesomeSupport")
                      ],
                     [
                           InlineKeyboardButton("🧑‍💻Devloper🧑‍💻", url="https://t.me/HEROGAMERS1")
                     ],
                     [
                           InlineKeyboardButton("📚 Commands", callback_data="cbcmds")
                     ]
                 ]
             ),
        parse_mode="markdown",
        reply_to_message_id=message.message_id
        )
            return
    client.send_message(message.chat.id,
        text="**Hey [{}](tg://user?id={})**\n__I **Can Play Music In Voice Chats of Telegram Groups**.format(message.from_user.first_name, message.from_user.id),
	reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Join Updates Channel", url="https://t.me/LaylaList"),
                    InlineKeyboardButton("Support Group", url="https://t.me/AwesomeSupport")
                ],
                [
                    InlineKeyboardButton("🧑‍💻Devloper🧑‍💻", url="https://t.me/HEROGAMERS1")
                ],
                [
                     InlineKeyboardButton("📚 Commands", callback_data="cbcmds")
                ]
            ]
        ),
        parse_mode="markdown",
        reply_to_message_id=message.message_id
        )

@Client.on_message(filters.command(["start", f"start@{BOT_USERNAME}"]) & filters.group & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        text="**Music Bot Is Online ✅**",
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton(text="🎙️ Support Group 🎙️", url="https://t.me/AwesomeSupport"),
            InlineKeyboardButton(text="📣 Channel", url=f"https://t.me/LaylaList")
            ],
            [
            
            ]]
        )
    )


@Client.on_message(filters.command(["help", f"help@{BOT_USERNAME}"]) & filters.private & ~filters.channel)
async def cmdlist(_, message: Message):
    await message.reply_text(
        text=f"""<b>✨ **Welcome user, i'm {query.message.from_user.mention}** \n

__× First Add Me To Your Group..
× Promote Me As Admin In Your Group With All Permission..__

**🏷 Common Commands.**

• `/play` - Song Name : __Plays Via Youtube__
• `/dplay` - Song Name : __Play Via Deezer__
• `/splay` - Song Name : __Play Via Jio Saavn__
• `/playlist` - __Show now playing list__
• `/current` - __Show now playing__

• `/song` - Song Name : __Get The Song From YouTube__
• `/vid` - Video Name : __Get The Video From YouTube__
• `/deezer` - song name : __download songs you want quickly via deezer__
• `/saavn` - song name : __download songs you want quickly via saavn__
• `/search` - YouTube Title : __(Get YouTube Search Query)__

**🏷 Group Admin Commands.**

• `/skip` : __Skips Music__
• `/pause` : __Pause Playing Music__
• `/resume` : __Resume Playing Music__
• `/end` : __Stops playing Music__
• `/reload` : __Reloads Admin List__
• `/userbotjoin` : __Assistant Joins The Group__
• `/userbotleave` : __Assistant Leaves From The Group.__
</b>""",
        reply_markup=InlineKeyboardMarkup(
              [[
              InlineKeyboardButton(text="🎙️ Support Group 🎙️", url="https://t.me/AwesomeSupport"),
              InlineKeyboardButton(text="📣 Channel", url=f"https://t.me/LaylaList")
              ],[
              InlineKeyboardButton("🏡 BACK TO HOME", callback_data="cbstart")
              ]]
          )
      )
