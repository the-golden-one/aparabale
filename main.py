#In The Name Of God
from balethon import Client
from balethon.conditions import private
from balethon.objects import InlineKeyboard

bot = Client("180320511:serDAOFxWsW8Gwncu18rHy8BXUsrf7NQjO258EnB")



#Internal Texts:
welcome = '''به ربات آپلودر از بله - به آپارات *آپاربله* خوش آمدید.
این ربات مخصوص محتوا داران بله است که مایلند علاوه بر کانال بله، در آپارات نیز کانال داشته باشند.
'''


@bot.on_command(private,name="start")
async def start(* , message):
    await message.reply(welcome,
                    InlineKeyboard(
                        [("تنظیم کانال","setc")],
                        [("تنظیمات بارگذاری", "settings")],
                        [("راهنما","help")]

    ))


bot.run()