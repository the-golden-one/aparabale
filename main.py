#In The Name Of God
from balethon import Client
from balethon.conditions import private
from balethon.objects import InlineKeyboard
import sqlite3
from pathlib import Path
import os


#Database Setup:
db_name = "users.db"
db_path = os.path.abspath(db_name)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    whereis TEXT,
    baleid TEXT,
    aparid TEXT,
    aparpass TEXT,
    chansubj TEXT,
    chanlink TEXT
)
""")
print(db_path)
conn.commit()
conn.close()

#-----------------------------------#
bot = Client("180320511:serDAOFxWsW8Gwncu18rHy8BXUsrf7NQjO258EnB")



#Internal Texts:

welcome = '''به ربات آپلودر از بله - به آپارات *آپاربله* خوش آمدید.
این ربات مخصوص محتوا داران بله است که مایلند علاوه بر کانال بله، در آپارات نیز کانال داشته باشند.
'''
#------------------------------------#
helper= '''برای استفاده از این ربات، شما باید مالک کانالی باشید که مایل هستید محتوا از آن کانال به آپارات آپلود شود.
سپس، در بخش تنظیم کانال، شما ابتدا آیدی کانال بله خود را وارد می کنید.
*⚠️توجه کنید که ربات باید در کانال عضو و ادمین باشد. _تضمین می شود که توسط ربات پیامی در کانال ارسال نخواهد شد_*

سپس یوزرنیم کانال آپارات خود، و سپس پسورد آن را وارد می کنید.
*⚡حریم شخصی شما را نقض نخواهیم کرد و این موارد توسط فردی استفاده نخواهند شد.*

در نهایت، موضوع کانال خود را انتخاب می کنید.
'''
#------------------------------------#
welcome_inline = InlineKeyboard(
                        [("تنظیم کانال","setc")],
                        [("تنظیمات بارگذاری", "settings")],
                        [("راهنما","help")])
#---------------------------------------#
setchannel= ''' نام کانال خود را وارد کنید. این ربات باید حتما در کانال مورد نظر ادمین باشد.
'''


#Handlers::

@bot.on_command(private,name="start")
async def start(* , message):
    await message.reply(welcome, welcome_inline)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
                   INSERT INTO users (baleid)
                   VALUES (?)
                   """, (message.author.id,))

    conn.commit()
    conn.close()

@bot.on_callback_query()
async def comhelp(callback_query):
    if callback_query.data == "help":
        await bot.edit_message_text(callback_query.message.chat.id, callback_query.message.id,helper,
                                    InlineKeyboard([("بازگشت به خانه","home")]))
    if callback_query.data == "home":
        await bot.edit_message_text(callback_query.message.chat.id, callback_query.message.id,welcome,welcome_inline)


    if callback_query.data == "setc":
        await bot.edit_message_text(callback_query.message.chat.id, callback_query.message.id,setchannel)

bot.run()