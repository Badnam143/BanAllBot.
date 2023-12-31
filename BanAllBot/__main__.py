from BanAllBot import app,START_IMG,BOT_USERNAME,BOT_NAME,LOG
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup , CallbackQuery 

START_MSG="""
ʜᴇʏ **{}** , ɪ ᴀᴍ {},
Mera naam hai badnam dushmano ki gand faar chudayi Krna hai mera kaam,
Help button pe ungli dawa or mere commands yaad krle bsdk. Baad me bolna nhi bot bekar h nhi to teri bhi ma chod dunga nikl ab.

"""
START_BUTTONS=InlineKeyboardMarkup (
      [
      [
         InlineKeyboardButton (text="➕ ᴀᴅᴅ ᴍᴇ ➕",url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
      ],
      [
         InlineKeyboardButton (text="ʜᴇʟᴘ",callback_data="help_back")
      ]
      ]
)

HELP_MSG="""
**ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ᴏɴʟʏ ʙᴇ ᴜsᴇᴅ ɪɴ ɢʀᴏᴜᴘs**

⨷ /banall : ʙᴀɴ-ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ᴀ ɢʀᴏᴜᴘ

⨷ /unbanall : ᴜɴʙᴀɴ ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ᴀ ɢʀᴏᴜᴘ

⨷ /kickall : ᴋɪᴄᴋ ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ᴀ ɢʀᴏᴜᴘ

⨷ /muteall : ᴍᴜᴛᴇ ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ᴀ ɢʀᴏᴜᴘ

⨷ /unmuteall : ᴜɴᴍᴜᴛᴇ ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ᴀ ɢʀᴏᴜᴘ(sᴛɪʟʟ ᴡɪʟʟ ᴛʜᴇ ʟɪsᴛ ɪɴ ʀᴇsᴛʀɪᴄᴛᴇᴅ ᴍᴇᴍʙᴇʀs ʙᴜᴛ ᴀʟʟ ʀᴇsᴛʀɪᴄᴛɪᴏɴs ᴡɪʟʟ ɢᴏ)

⨷/unpinall : ᴜɴᴘɪɴ ᴀʟʟ ᴍᴇssᴀɢᴇs ɪɴ ᴀ ɢʀᴏᴜᴘ.

ᴄʀᴇᴀᴛᴇᴅ ʙʏ: [🅱︎🄰🅳︎🄽🅰︎🄼乂🅻︎🄰🅳︎🄺🅰︎🚬](https://t.me/badnam_ji)
"""




@app.on_message(filters.command("start"))
async def start(_,msg):
    await msg.reply_photo(
     photo=START_IMG,
     caption=START_MSG.format(msg.from_user.mention,BOT_NAME),
     reply_markup=START_BUTTONS)

@app.on_callback_query(filters.regex("help_back"))
async def help_back(_,callback_query: CallbackQuery):
    query=callback_query.message
    await query.edit_caption(HELP_MSG)    



if __name__ == "__main__":
    LOG.info("started")
    app.run()
