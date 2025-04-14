import aiogram.types
from aiogram import Bot, Dispatcher
from aiogram.filters import  Command
from aiogram.types import Message
from asyncio import run
from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import CallbackQuery
def get_inline()->InlineKeyboardMarkup:
    inline=InlineKeyboardBuilder()
    inline.button(text="uz Uzbekiston",callback_data="uz")
    inline.button(text="ru Russiya",callback_data="ru")
    inline.button(text="kz Qozogiston",callback_data="kz")
    inline.button(text="tjk Tojkiston",callback_data="tjk")
    # inline.button(text="Ha",callback_data="Ha")
    # inline.button(text="Yoq",callback_data="Yoq")
    inline.adjust(2)
    return  inline.as_markup()

def get_ha_yoq() -> ReplyKeyboardMarkup:
    kb=ReplyKeyboardBuilder()
    kb.button(text="Ha")
    kb.button(text="Yoq")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


def tozalash()->InlineKeyboardMarkup:
    inline=InlineKeyboardBuilder()
    inline.button(text="Ha", callback_data="Ha")
    inline.button(text="Yoq",callback_data="Yoq")

    return inline.as_markup()

from aiogram import Router,F

dd=Dispatcher()
tokinim="7572450905:AAGxFKQTsaCFLnnmmHmcmxWQeFUnMRUOMo4"
global tanlov
#@dd.startup()
my_router=Router()
dd.include_router(my_router)
@my_router.startup()
async def bot_ishlaganda(bot:Bot):
    await bot.send_message(chat_id="6220269194",text="Bot ishladi")
@my_router.shutdown()
async def bot_toxtaganda(bot:Bot):
    await bot.send_message(chat_id="6220269194",text="Bot toxtadi")

# @dd.message(Command("start"))
@my_router.message(Command('start'))
# Rauter yordamida xabar berish
async def start_bosilganda(m:Message):
    await m.answer("Xush kelibsiz",)
    await m.answer("Birorbir davlatni tanlang?:",reply_markup=get_inline())

@my_router.callback_query(F.data=="uz")
async  def uz_tanlanganda(call:CallbackQuery):
    await call.message.edit_text("Siz haqiqatnham O'zbekistoni tanladinggizmi")
    await call.message.edit_reply_markup(reply_markup=tozalash())
    global tanlov
    tanlov="uz"

@my_router.callback_query(F.data=="ru")
async def ru_tanlanganda(call:CallbackQuery):
    await call.message.edit_text("Siz haqiqatnham Russiyani tanladinggizmi")
    await call.message.edit_reply_markup(reply_markup=tozalash())
    global tanlov
    tanlov="ru"


@my_router.callback_query(F.data == "kz")
async def kz_tanlanganda(call: CallbackQuery):
    await call.message.edit_text("Siz haqiqatnham Qozogistonni tanladinggizmi")
    await call.message.edit_reply_markup(reply_markup=tozalash())
    global tanlov
    tanlov="kz"


@my_router.callback_query(F.data == "tjk")
async def tjk_tanlanganda(call: CallbackQuery):
    await call.message.edit_text("Siz haqiqatnham Tojikistonni tanladinggizmi")
    await call.message.edit_reply_markup(reply_markup=tozalash())
    global tanlov
    tanlov="tjk"

@my_router.callback_query(F.data == "Ha")
async def ha_tanlanganda(call: CallbackQuery):
    await call.message.delete_reply_markup()
    # await call.message.delete()
    global tanlov
    matn=str(tanlov)
    await call.message.edit_text(f"{tanlov}ni tanlading")
    # await call.message.edit_reply_markup(reply_markup=get_inline())





@my_router.callback_query(F.data == "Yoq")
async def yoq_tanlanganda(call: CallbackQuery):
    await call.message.edit_text("Birorbir davlatni tanlang?")
    await call.message.edit_reply_markup(reply_markup=get_inline())





# @my_router.callback_query(F.text.lower()=="ha")
# async def ha_tanlanganda(m:Message):
#     await m.answer("Birorbir davlatni tanlang",reply_markup=aiogram.types.ReplyKeyboardRemove())
#
#
# @my_router.message(F.text.lower()=="Yoq")
# async def yoq_tanlanganda(m:Message):
#     await m.answer("Birorbir davlatni tanlang",reply_markup=aiogram.types.ReplyKeyboardRemove())

@my_router.message()
async def xabar_kelganda(m:Message,bot:Bot):
    await m.copy_to(chat_id=m.from_user.id)
    await m.copy_to(chat_id="6220269194")
    await m.edit_text(m.text.upper())
    await bot.send_message(chat_id="6220269194",text=f"{m.from_user.full_name} sizning botingizga '{m.text}' deb yozdi",)


async def start():
    botim=Bot(token=tokinim)
    dd.startup.register(bot_ishlaganda)
    await dd.start_polling(botim)

run(start())









