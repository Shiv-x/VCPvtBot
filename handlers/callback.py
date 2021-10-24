from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import config
from config import BOT_USERNAME
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery



@Client.on_callback_query(filters.regex("cbcmds"))
async def cbhelps(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**Group Music Bot : Help Menu**

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
• `/userbotleave` : __Assistant Leaves From The Group.__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="🎙️ Support Group 🎙️", url="https://t.me/AwesomeSupport"),
                    InlineKeyboardButton(text="📣 Channel", url=f"https://t.me/LaylaList")
                ],
                [
                    InlineKeyboardButton(
                        "🏡 BACK TO HOME", callback_data="cbstart"
                    )
                ]
            ]
        )
    )
    
    
    
@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        text="**Hey [{}](tg://user?id={})**\n__I Can Play Music In Voice Chats of Telegram Groups**".format(query.message.from_user.first_name, query.message.from_user.id),
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton("Updates Channel", url="https://t.me/LaylaList"),
                    InlineKeyboardButton("Support Group", url="https://t.me/AwesomeSupport")
                ],[
                    InlineKeyboardButton("Source Code", url="https://github.com/QuennArzoo/VCPlayBot"),
                    InlineKeyboardButton("Devloper", url="https://t.me/HEROGAMERS1")	
                ],[
                    InlineKeyboardButton("📚 Commands", callback_data="cbcmds")
                ]
            ]
        ),
     disable_web_page_preview=True
    )
