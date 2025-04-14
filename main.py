from aiogram import Bot,Dispatcher
from asyncio import run
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

t="7572450905:AAGxFKQTsaCFLnnmmHmcmxWQeFUnMRUOMo4"
dp=Dispatcher()
#Dekarat bilan Dispetcherga vazifalar yaratish
# @dp.message(CommandStart) #habar korinishida
#Javob beradigan dekarator Command ("start") Start buyrugi
async def start_bosilgand(x:Message,bot:Bot):
    await x.answer(f"Xush kelibsiz")
    await bot.send_message("6220269194","Xush kelibsiz  2")
    await bot.delete_message(chat_id="6220269194",message_id="6220269194")


async  def main():
    bot=Bot(token=t)
    dp.message.register(start_bosilgand, CommandStart)
    await dp.start_polling(bot)
run(main())
